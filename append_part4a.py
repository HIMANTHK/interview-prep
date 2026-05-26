content = """

# Section W — Performance Tuning (Q456–Q480)

**456. How do you use EXPLAIN PLAN and DBMS_XPLAN to tune a slow SQL query in Oracle EBS?**
Run `EXPLAIN PLAN FOR <your_sql>`, then `SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY)`. Look for full table scans on large tables (`AP_SUPPLIER_SITES_ALL`, `PO_HEADERS_ALL`), high cardinality mismatches, or missing index usage. In EBS, always set `APPS` context with `APPS_INITIALIZE` before explaining queries that use VPD policies (like `org_id` row-level security), otherwise the plan won't reflect actual runtime conditions.

**457. A BIP report over RCV_TRANSACTIONS takes 4 minutes to run. Walk through your tuning approach.**
First pull the BIP data template SQL and run it manually in SQL Developer with AUTOTRACE on. Check: (1) Is `org_id` filter pushed early? (2) Are there joins to `MTL_SYSTEM_ITEMS_B` without `ORGANIZATION_ID`? (3) Is `RCV_TRANSACTIONS.TRANSACTION_DATE` indexed and are date range filters SARGable? Typical fix: add `/*+ LEADING(rsh) USE_NL(rt) INDEX(rt RCV_TRANSACTIONS_N5) */` hint or rewrite the driving table order. Also check if the BIP concurrent program runs under an APPS schema context that bypasses org security — use `mo_global.set_policy_context`.

**458. What causes BULK COLLECT to consume excessive PGA memory and how do you fix it?**
`BULK COLLECT` without a `LIMIT` clause fetches the entire result set into a PL/SQL collection at once. On a query returning 500K rows from `PO_LINES_ALL`, this can allocate 200–400 MB of PGA per session. Fix: use `BULK COLLECT ... LIMIT 500` inside a loop — process and clear the collection each iteration (`l_tab.DELETE`). Also watch for `FORALL` with large arrays: if the DML fails mid-batch, the rollback cost is proportional to array size.

**459. Explain hard parse vs soft parse and how bind variables reduce parse overhead in EBS.**
A hard parse compiles SQL from scratch: syntax check, semantic check, optimization, plan generation — typically 5–50 ms of CPU plus shared pool latch contention. A soft parse finds the cursor in the shared pool (matching SQL text exactly) and reuses the plan — microseconds. In EBS, dynamically built SQL like `WHERE vendor_id = 12345` causes hard parses for every vendor. Fix: use bind variables (`WHERE vendor_id = :p_vendor_id`). In PL/SQL this happens automatically with static SQL. In dynamic SQL, use `USING` clause. Profile using `V$SQL` — look for `PARSE_CALLS` close to `EXECUTIONS` indicating no plan reuse.

**460. Write a query to find the top 10 most resource-intensive SQL statements in the shared pool.**
```sql
SELECT sql_id, executions, elapsed_time/1000000 elapsed_sec,
       cpu_time/1000000 cpu_sec, buffer_gets, disk_reads,
       ROUND(elapsed_time/NULLIF(executions,0)/1000000,3) avg_elapsed_sec,
       sql_text
FROM   v$sql
WHERE  executions > 0
ORDER  BY elapsed_time DESC
FETCH  FIRST 10 ROWS ONLY;
```
Also useful: sort by `BUFFER_GETS/EXECUTIONS` for logical I/O hogs; by `DISK_READS` for physical I/O issues. In a running EBS system, cross-reference with `V$SESSION` to find active sessions running those `sql_id` values.

**461. What is the N+1 query problem in OAF and how does it manifest?**
N+1 occurs when OAF executes one query to fetch N parent rows (e.g., 50 PO headers), then for each row fires a separate child query (e.g., fetching line count per PO) — resulting in 51 database round trips. It manifests as a page taking 3–8 seconds while the individual queries are fast. Fix: redesign the VO to join or use a sub-query column (`SELECT COUNT(*) FROM po_lines_all WHERE po_header_id = :1` as an inline view). Also consider using a single VO with a GROUP BY instead of nested VOs without proper caching.

**462. How does partition pruning work and when does it help in EBS receiving tables?**
Oracle skips partitions that cannot contain qualifying rows — reducing I/O from a full table scan to just relevant partition(s). `RCV_TRANSACTIONS` in large EBS instances is often range-partitioned by `TRANSACTION_DATE`. A query with `WHERE TRANSACTION_DATE BETWEEN :start AND :end` prunes to only those date partitions. Verify pruning with EXPLAIN PLAN — look for `PARTITION RANGE ITERATOR` instead of `PARTITION RANGE ALL`. Without partition key in the WHERE clause (e.g., filtering only on `VENDOR_ID`), all partitions scan — defeating the purpose.

**463. Describe tuning a PL/SQL procedure that processes PO lines row-by-row (slow-by-slow).**
Row-by-row (`FOR rec IN cursor LOOP ... UPDATE ... END LOOP`) causes one context switch per row between PL/SQL and SQL engines. For 50K PO lines, this means 50K individual UPDATEs. Fix: (1) Replace cursor loop + UPDATE with a single `UPDATE po_lines_all SET ... WHERE po_header_id IN (SELECT ...)`. (2) If complex logic is needed, use `BULK COLLECT ... LIMIT 1000` + `FORALL`. Typical speedup: 10x–100x. Measure before/after with `DBMS_UTILITY.GET_TIME`.

**464. What does AUTOTRACE show and what do the statistics mean?**
`SET AUTOTRACE ON` in SQL*Plus/SQL Developer shows execution plan + statistics after query execution. Key stats: `db block gets` (current-mode reads, writes), `consistent gets` (read-consistent reads — main I/O metric), `physical reads` (disk I/O), `redo size` (write volume), `sorts (disk)` (spill to temp — bad). For a tuning baseline: run query, note `consistent gets`. After adding index or rewriting, if `consistent gets` drops 90%, the optimization worked. `physical reads` = 0 means data was cached — warm-cache tests may hide I/O problems; test on cold cache for realistic numbers.

**465. What is CURSOR_SHARING and when would you enable it in EBS?**
`CURSOR_SHARING = FORCE` makes Oracle replace literal values in SQL with system-generated bind variables at parse time, enabling cursor sharing for statements that differ only in literals. Use it as a temporary relief when an application generates non-bind-variable SQL you cannot change (e.g., a legacy custom report). Risks: optimizer may get poor cardinality estimates because it can't peek at literal values; can cause plan regressions. In EBS, Oracle recommends `CURSOR_SHARING = EXACT` (default) because EBS itself uses bind variables properly. Use `FORCE` only for specific problem schemas via `ALTER SESSION` in login triggers.

**466. A slow BIP report is generating wrong plans after statistics were last gathered 6 months ago. What do you do?**
First gather fresh stats: `DBMS_STATS.GATHER_TABLE_STATS('APPS', 'RCV_TRANSACTIONS', cascade=>TRUE)`. If the plan is still bad, lock the good plan using SQL Plan Baselines: `DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE` to capture the current plan, then evolve/accept the baseline. Alternatively, add an `OPT_PARAM` hint or use `DBMS_SQLTUNE` (SQL Tuning Advisor) to get an automated recommendation. In EBS production, always test stat-gathering in UAT first — stale stats are common because `GATHER_SCHEMA_STATS('APPS')` is disruptive and often deferred.

**467. How does a poorly written trigger slow down PO approval and what do you look for?**
A trigger on `PO_HEADERS_ALL` that runs a SELECT query on every UPDATE (e.g., to fetch vendor name from `AP_SUPPLIERS`) executes once per row — for batch approvals processing 1000 POs, that's 1000 extra selects. Worse if the trigger calls a package that does DML (cascading). Signs: `V$SQL` shows an unexpected SELECT from inside a trigger context (look at MODULE/ACTION columns). Fix: move logic to the calling PL/SQL procedure where you can bulk-process, or cache the lookup value in a package variable. Also watch for mutating table errors (ORA-04091) in row triggers on `PO_LINES_ALL` that also query `PO_LINES_ALL`.

**468. Explain OAF Application Module pool sizing and its performance impact.**
The AM pool holds instantiated AM objects. `jbo.doconnectionpooling=true` with `jbo.pool.maxsize` controls pool size per JVM. Too small: requests wait for a free AM, causing latency spikes (OAF "pooling timeout" errors). Too large: excess memory consumption per OC4J node. For GE's 5-site iSupplier with ~200 concurrent users, pool size was set to 50 per node (4 nodes) = 200 total AMs. Monitor: check OAF diagnostic logs for `AM pool starved` messages; use OC4J metrics in Enterprise Manager. Passivation (AM state written to DB `JBO_SESSION` table) kicks in when pool is full — adds DB I/O overhead.

**469. What are materialized views and when would you use one in an EBS reporting context?**
A materialized view stores the result of a complex query physically, refreshed on a schedule. In EBS, you cannot add MVs to standard Oracle schemas (patching would overwrite them), but you can create them in a custom schema for reporting. Use case: a dashboard showing PO-to-receipt cycle time across all sites joining `PO_HEADERS_ALL`, `PO_LINE_LOCATIONS_ALL`, `RCV_SHIPMENT_LINES` — expensive at query time. Create MV in `XXCUST` schema, refresh nightly via concurrent program. Key consideration: `REFRESH FAST` requires materialized view logs on base tables — risky on high-DML EBS tables; use `REFRESH COMPLETE` during off-hours.

**470. What is ORA-01555 (snapshot too old) and how does it occur in EBS batch processes?**
ORA-01555 means Oracle cannot reconstruct a read-consistent image of a block because the undo segment that held the before-image has been overwritten. Occurs in long-running queries or transactions: a batch job running for 2 hours reads a block, then when it needs the old version of that block, the undo is gone. In EBS, common in: (1) long-running custom reports on `PO_HEADERS_ALL` during heavy DML periods; (2) FND concurrent programs with COMMIT inside a cursor loop — COMMIT releases undo, but the cursor still needs consistent reads. Fix: increase `UNDO_RETENTION`, avoid COMMITs inside open cursors, or use `SET TRANSACTION READ ONLY`.

**471. How do you read an AWR report to diagnose a performance problem in EBS?**
Focus on: (1) **Top Timed Events** — if `db file sequential read` dominates, it's single-block I/O (index scans hitting slow disk); `db file scattered read` = full table scans; `log file sync` = COMMIT frequency issue; `library cache lock` = hard parse/DDL contention. (2) **Top SQL by Elapsed Time** — identify which SQL_IDs are burning most time. (3) **Instance Efficiency** — buffer hit ratio should be >98% for OLTP; if lower, buffer cache too small. (4) **Load Profile** — check logical reads/sec, parses/sec (hard parses >100/sec is a problem). Cross-reference with ASH (`V$ACTIVE_SESSION_HISTORY`) for session-level drill-down.

**472. WebADI uploads of 5000 rows are timing out. How do you tune this?**
WebADI upload calls `BNE_UPLOAD_MANAGER_PKG.UPLOAD_AND_VALIDATE` which processes rows one at a time via the interface engine. For 5K rows: (1) Increase FND concurrent program timeout for the upload concurrent request. (2) Check if the custom validation package (registered as a pre-upload validator) is doing row-by-row queries — bulk them. (3) Check `BNE_INTERFACE_LINES` insert performance — if the table lacks proper indexes for your interface, add them in the custom schema. (4) Consider splitting the upload into multiple Excel sheets of 500 rows each. Also check if the WebADI servlet timeout in `oc4j-connectors.xml` is smaller than the concurrent program timeout.

**473. How does connection pool exhaustion manifest and how do you resolve it in an EBS multi-node setup?**
Symptoms: users get "connection refused" or long hang on page load; OC4J logs show `No available connection in pool`; DB `V$SESSION` shows max sessions hit. Causes: (1) Long-running OAF AM queries holding DB connections. (2) Connection leak — OAF code that opens a JDBC connection without closing it (custom Java code bypassing BC4J). (3) Sudden spike in concurrent users. Resolution: (1) Increase `jdbc-connection-pool max-connections` in `data-sources.xml` (coordinate with DBA on DB `SESSIONS` parameter). (2) Enable connection validation (`test-connections-on-match`) to cull stale connections. (3) Profile AM lifecycle — ensure AMs are released after use with proper `prepareForActivation`/`passivate` calls.

**474. How do you use DBMS_PROFILER or DBMS_HPROF to find bottlenecks in a PL/SQL package?**
`DBMS_PROFILER`: install with `profload.sql`, call `DBMS_PROFILER.START_PROFILER('run1')`, execute your package, call `DBMS_PROFILER.STOP_PROFILER`. Query `PLSQL_PROFILER_DATA` joined to `PLSQL_PROFILER_UNITS` — look for lines with highest `TOTAL_TIME`. Good for line-level analysis. `DBMS_HPROF` (hierarchical profiler, 11g+): `DBMS_HPROF.START_PROFILING('PLSHPROF_DIR', 'trace.trc')`, run, `STOP_PROFILING`. Analyze with `DBMS_HPROF.ANALYZE` — shows call tree with time per function. Better for identifying which subprogram is the bottleneck when many procedures call each other (e.g., a complex approval routing package).

**475. What is latch contention and how does it affect EBS performance under high concurrency?**
Latches are lightweight serialization mechanisms protecting shared memory structures (shared pool, buffer cache). Under high concurrency: `library cache latch` contention → hard parse storm (fix: bind variables, `CURSOR_SHARING`). `cache buffers chains latch` → hot block contention — too many sessions reading the same block (e.g., a sequence or frequently-updated `AP_SUPPLIERS` row). Fix for hot blocks: reverse-key indexes, hash partitioning, sequence cache increase. Diagnose via `V$LATCH` (misses/gets ratio > 1% is concerning) and AWR latch statistics section. In EBS during period-end close with many concurrent approval workflows, `library cache: mutex X` is a common bottleneck.

**476. How do you size concurrent manager work shifts for optimal throughput in EBS?**
Work shifts define max concurrent processes per manager. Standard Manager default is often 1 — this is the most common mistake. For GE's environment with 200+ users submitting reports: (1) Standard Manager: 10–15 processes (handles most user-submitted requests). (2) Conflict Resolution Manager: 1 (don't increase). (3) Custom managers for specific programs (BIP reports, custom interfaces): 5–8 each. Profile using `FND_CONCURRENT_REQUESTS` — if `STATUS_CODE='P'` (Pending) requests queue > 5 minutes, increase work shift. Also check `MAX_PROCESSES` at the node level in `FND_NODES`. Separate work shifts for business hours vs off-peak is best practice.

**477. A query joining PO_HEADERS_ALL and AP_INVOICES_ALL runs fine in DEV but slow in PROD. Why?**
Most common reasons: (1) **Stale statistics in PROD** — PROD has 2M PO headers, DEV has 10K; optimizer chooses different plan. Fix: `DBMS_STATS.GATHER_TABLE_STATS`. (2) **Bind variable peeking** — PROD compiled the plan with an atypical bind value (e.g., `org_id = 999` with 1 row), creating a plan wrong for common org_ids. Fix: `DBMS_STATS.SET_TABLE_STATS` with histograms, or SQL Plan Baseline. (3) **VPD/MOAC policies** — PROD has MO Security Profile active, adding invisible predicates that prevent index use. Check with `DBMS_RLS.GET_POLICY`. (4) **Different indexes** — a custom index exists in DEV but wasn't migrated to PROD (check FNDLOAD/DDL deployment checklist).

**478. Explain how you would investigate and fix a slow iSupplier portal home page load.**
Step 1: Enable OAF diagnostics (`?ora_debug=y&ora_performance=query`) to see per-VO query times. Step 2: Identify the slowest VO — often `PosSupplierInfoVO` or a custom supplier summary VO. Step 3: Pull the VO SQL from OAF diagnostic output and run EXPLAIN PLAN. Step 4: Check if `POS_SUPPLIER_USERS` join to `AP_SUPPLIERS` is using index on `VENDOR_ID` — if not, check `ORG_ID` predicate. Step 5: Check MOAC context — `MO_GLOBAL.SET_POLICY_CONTEXT` must be called before VO execution. Step 6: If personalization added columns referencing related VOs, check if those added N+1 queries. Fix typically involves: adding a DB hint to the VO SQL override, or denormalizing the supplier summary into a custom materialized view refreshed on supplier update.

**479. What are the performance implications of using PRAGMA AUTONOMOUS_TRANSACTION in a frequently called function?**
`PRAGMA AUTONOMOUS_TRANSACTION` starts a new independent transaction — allocating a new undo segment entry, requiring a separate `COMMIT`/`ROLLBACK`. If called 10K times in a loop (e.g., logging function called per PO line), this creates 10K micro-transactions with 10K undo entries and 10K log flushes — severe performance impact. Best practice: batch log inserts. Use autonomous transaction only for: (1) Error logging where you need the log entry to survive even if the main transaction rolls back. (2) External audit tables. Never use it in tight loops. Profile with `V$TRANSACTION` — if you see thousands of tiny transactions, an autonomous transaction in a loop is the likely cause.

**480. How do you identify and resolve temp space (ORA-01652) issues in EBS during large reports?**
ORA-01652: `unable to extend temp segment by N in tablespace TEMP`. Causes: sort operations or hash joins that exceed PGA (`WORK_AREA_SIZE_POLICY=AUTO`, `PGA_AGGREGATE_TARGET`). Diagnosis: `SELECT username, sql_id, temp_space_allocated FROM v$tempseg_usage` during the failing query. Fix options: (1) Tune the SQL to reduce sort/hash operations — add indexes to avoid sorts, rewrite hash joins. (2) Increase `PGA_AGGREGATE_TARGET` if server memory allows. (3) Increase TEMP tablespace size (coordinate with DBA). (4) For BIP reports: reduce report data set by adding date filters, or schedule during off-peak when TEMP is less contended. In EBS, period-end BIP reports and GL journal imports are common culprits.
"""

with open("/Users/himanshu/Desktop/Job/Job Preparation/Interview_Prep_200_QA.md", "a", encoding="utf-8") as f:
    f.write(content)

print("Section W appended (Q456-Q480)")
