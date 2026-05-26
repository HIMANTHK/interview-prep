#!/usr/bin/env python3
"""Appends Section S remainder (Q355-Q370) + Sections T, U, V (Q371-Q455)."""
from pathlib import Path
OUT = Path("/Users/himanshu/Desktop/Job/Job Preparation/Interview_Prep_200_QA.md")

CONTENT = """
**355. How do you write a PL/SQL package to suppress planner notifications selectively?**
The GE solution used a custom package `XXGEA_NOTIF_CTRL_PKG` with a function `should_suppress(p_planner_id, p_vendor_id, p_change_type) RETURN BOOLEAN`. It checked a rules table `XXGEA_NOTIF_RULES` (populated by the procurement team) storing which planner–supplier–change-type combinations should be suppressed. The OAF-invoked workflow called this function before raising the standard `PONOT` notification. If the function returned TRUE, the notification activity was skipped via `WF_ENGINE.CompleteActivity` with a 'SUPPRESS' result; otherwise the standard notification fired. This gave procurement managers a UI-configurable control over notification volume without code changes.

**356. Write a PL/SQL function to return the open quantity available for ASN submission.**
```sql
FUNCTION get_asn_available_qty (p_line_location_id IN NUMBER)
RETURN NUMBER IS
  l_ordered    NUMBER;
  l_received   NUMBER;
  l_cancelled  NUMBER;
  l_in_transit NUMBER;
BEGIN
  SELECT pll.quantity,
         NVL(pll.quantity_received,0),
         NVL(pll.quantity_cancelled,0)
    INTO l_ordered, l_received, l_cancelled
    FROM po_line_locations_all pll
   WHERE pll.line_location_id = p_line_location_id;

  SELECT NVL(SUM(rsl.quantity_shipped - NVL(rsl.quantity_received,0)),0)
    INTO l_in_transit
    FROM rcv_shipment_lines rsl
    JOIN rcv_shipment_headers rsh ON rsh.shipment_header_id = rsl.shipment_header_id
   WHERE rsl.po_line_location_id       = p_line_location_id
     AND rsl.shipment_line_status_code = 'EXPECTED'
     AND rsh.receipt_source_code       = 'VENDOR';

  RETURN GREATEST(0, l_ordered - l_received - l_cancelled - l_in_transit);
EXCEPTION
  WHEN NO_DATA_FOUND THEN RETURN 0;
  WHEN OTHERS THEN RETURN -1;
END;
```
Subtracting in-transit ASN quantities prevents over-shipment when a supplier submits a second ASN before the first is received. This was the "Balance Outstanding Qty" column logic at GE.

**357. Write a PL/SQL trigger to auto-populate last_updated_by and last_update_date on a custom table.**
```sql
CREATE OR REPLACE TRIGGER xxgea_notif_rules_biu
BEFORE INSERT OR UPDATE ON xxgea_notif_rules
FOR EACH ROW
BEGIN
  IF INSERTING THEN
    :NEW.created_by      := FND_GLOBAL.USER_ID;
    :NEW.creation_date   := SYSDATE;
    :NEW.last_updated_by := FND_GLOBAL.USER_ID;
    :NEW.last_update_date:= SYSDATE;
    :NEW.last_update_login := FND_GLOBAL.LOGIN_ID;
  ELSIF UPDATING THEN
    :NEW.last_updated_by  := FND_GLOBAL.USER_ID;
    :NEW.last_update_date := SYSDATE;
    :NEW.last_update_login:= FND_GLOBAL.LOGIN_ID;
  END IF;
END;
```
Standard Oracle WHO column pattern — all custom EBS tables should include `CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`, `LAST_UPDATE_LOGIN` with this trigger. Required for EBS audit standards and for FNDLOAD/iSetup migration tools to track record ownership.

**358. How do you use DBMS_UTILITY.FORMAT_ERROR_BACKTRACE in production PL/SQL?**
`DBMS_UTILITY.FORMAT_ERROR_BACKTRACE` returns the call stack at the point where the exception was *raised* (not where it was caught) — including package name, procedure name, and line number. Combined with `DBMS_UTILITY.FORMAT_ERROR_STACK` (the full error chain including wrapped exceptions), you get complete diagnostic information without needing source code access. At GE, all custom packages logged both strings to `XXGEA_ERROR_LOG` in a `PRAGMA AUTONOMOUS_TRANSACTION` logger procedure, which allowed the team to diagnose production errors from the log table even when the OC4J logs were not accessible.

**359. How do you implement a batch Promise Date update via the standard PO API?**
```sql
DECLARE
  l_chg      PO_CHANGES_REC_TYPE;
  l_ship_chg PO_SHIPMENT_CHANGES_REC_TYPE;
  l_ret_sts  VARCHAR2(1);
  l_errors   PO_API_ERRORS_REC_TYPE;
BEGIN
  l_ship_chg := PO_SHIPMENT_CHANGES_REC_TYPE(
    po_line_location_id => :p_line_location_id,
    promised_date       => :p_new_promise_date
  );
  l_chg := PO_CHANGES_REC_TYPE(
    shipment_changes => PO_SHIPMENT_CHANGES_TABLE(l_ship_chg)
  );
  PO_DOCUMENT_UPDATE_GRP.update_document(
    p_api_version      => 1.0,
    p_init_msg_list    => FND_API.G_TRUE,
    x_return_status    => l_ret_sts,
    x_api_errors       => l_errors,
    p_changes          => l_chg,
    p_run_submission_checks => FND_API.G_TRUE,
    p_launch_approvals => FND_API.G_FALSE
  );
  IF l_ret_sts != 'S' THEN
    RAISE_APPLICATION_ERROR(-20001, l_errors.message_text(1));
  END IF;
  COMMIT;
END;
```
The GE WebADI bulk Promise Date upload called this exact API pattern per row, wrapped in a loop with per-row error handling so one bad row did not stop the whole batch.

**360. How do you write a PL/SQL package to log surrogate buyer actions for compliance audit?**
```sql
CREATE OR REPLACE PACKAGE BODY xxgea_surrogate_audit_pkg AS
  PROCEDURE log_surrogate_action (
    p_buyer_user_id  IN NUMBER,
    p_vendor_id      IN NUMBER,
    p_vendor_site_id IN NUMBER,
    p_action_type    IN VARCHAR2,  -- 'ASN_SUBMIT','PO_ACK','CHG_REQ'
    p_reference_id   IN NUMBER
  ) IS
    PRAGMA AUTONOMOUS_TRANSACTION;
  BEGIN
    INSERT INTO xxgea_surrogate_audit (
      audit_id, buyer_user_id, vendor_id, vendor_site_id,
      action_type, reference_id, action_date, session_id
    ) VALUES (
      xxgea_surr_audit_s.NEXTVAL, p_buyer_user_id,
      p_vendor_id, p_vendor_site_id,
      p_action_type, p_reference_id, SYSDATE,
      SYS_CONTEXT('USERENV','SESSIONID')
    );
    COMMIT;
  EXCEPTION
    WHEN OTHERS THEN ROLLBACK;  -- never break main transaction for audit
  END;
END xxgea_surrogate_audit_pkg;
```
Every surrogate action (buyer transacting on behalf of a supplier) was logged via this autonomous-transaction procedure, called from the OAF controller. The audit table was the compliance evidence that all surrogate activities were traceable to a specific internal buyer at GE.

**361. Write a SQL to find top 10 most frequently run concurrent programs in the last 30 days.**
```sql
SELECT fcp.user_concurrent_program_name, COUNT(*) run_count,
       AVG(fcr.actual_completion_date - fcr.actual_start_date)*24*60 avg_runtime_mins,
       SUM(CASE WHEN fcr.status_code='E' THEN 1 ELSE 0 END) error_count
  FROM fnd_concurrent_requests fcr
  JOIN fnd_concurrent_programs_tl fcp
    ON fcp.concurrent_program_id = fcr.concurrent_program_id AND fcp.language='US'
 WHERE fcr.actual_start_date >= SYSDATE - 30
GROUP BY fcp.user_concurrent_program_name
ORDER BY run_count DESC
FETCH FIRST 10 ROWS ONLY;
```

**362. Write a PL/SQL block to validate that a supplier site is active and purchasing-enabled.**
```sql
FUNCTION is_valid_supplier_site (
  p_vendor_id      IN NUMBER,
  p_vendor_site_id IN NUMBER,
  p_org_id         IN NUMBER
) RETURN BOOLEAN IS
  l_cnt NUMBER;
BEGIN
  SELECT COUNT(*) INTO l_cnt
    FROM ap_supplier_sites_all
   WHERE vendor_id          = p_vendor_id
     AND vendor_site_id     = p_vendor_site_id
     AND org_id             = p_org_id
     AND purchasing_site_flag = 'Y'
     AND (inactive_date IS NULL OR inactive_date > SYSDATE);
  RETURN l_cnt > 0;
EXCEPTION
  WHEN OTHERS THEN RETURN FALSE;
END;
```

**363. How do you implement cursor-based processing with exception isolation per row?**
Use an explicit cursor FOR loop with an inner `BEGIN..EXCEPTION..END` block. Each row's exception is caught and logged independently — the outer cursor continues. For large tables, combine with `BULK COLLECT LIMIT` for performance: fetch 500 rows, process each with inner exception handling, commit the batch, then fetch next 500. This pattern was used for the GE surrogate-account onboarding batch (67 accounts) — each account setup was attempted independently so one bad account didn't block the rest.

**364. Write a PL/SQL block using EXECUTE IMMEDIATE for a DDL operation in a deployment script.**
```sql
BEGIN
  EXECUTE IMMEDIATE 'CREATE TABLE xxgea_batch_errors (
    error_id       NUMBER,
    reference_id   NUMBER,
    error_message  VARCHAR2(4000),
    error_date     DATE,
    created_by     NUMBER
  )';
  EXECUTE IMMEDIATE 'CREATE SEQUENCE xxgea_batch_err_s START WITH 1 INCREMENT BY 1 NOCACHE';
  EXECUTE IMMEDIATE 'GRANT SELECT, INSERT ON xxgea_batch_errors TO apps';
  EXECUTE IMMEDIATE 'CREATE SYNONYM apps.xxgea_batch_errors FOR xxgea.xxgea_batch_errors';
  DBMS_OUTPUT.PUT_LINE('Objects created successfully');
EXCEPTION
  WHEN OTHERS THEN
    IF SQLCODE = -955 THEN  -- ORA-00955: name already used
      DBMS_OUTPUT.PUT_LINE('Object already exists - skipping');
    ELSE
      RAISE;
    END IF;
END;
```
DDL inside PL/SQL requires `EXECUTE IMMEDIATE` because PL/SQL does not allow DDL statements directly. The `ORA-00955` trap makes deployment scripts re-runnable — a critical practice for EBS deployment scripts that may be run in multiple environments.

**365. Write a PL/SQL function to get the current user's supplier context from ICX session.**
```sql
FUNCTION get_icx_vendor_id RETURN NUMBER IS
  l_vendor_id NUMBER;
BEGIN
  l_vendor_id := TO_NUMBER(
    ICX_SEC.GetSessionValue(
      p_session_id => ICX_SEC.getID(ICX_SEC.PV_SESSION_ID),
      p_name       => 'SUPPLIER_ID'
    )
  );
  RETURN l_vendor_id;
EXCEPTION
  WHEN OTHERS THEN
    -- fallback: derive from FND user's supplier mapping
    SELECT psu.vendor_id INTO l_vendor_id
      FROM pos_supplier_users psu
     WHERE psu.user_id = FND_GLOBAL.USER_ID
       AND ROWNUM = 1;
    RETURN l_vendor_id;
END;
```
Understanding how to resolve `vendor_id` from the ICX session is fundamental to iSupplier security — all supplier-facing VOs depend on this to enforce row-level access. The `ICX_SEC` package manages iSupplier session attributes.

**366. Write a PL/SQL procedure to handle the Promise Date bypass scenario at GE.**
```sql
PROCEDURE validate_promise_date_ack (
  p_line_location_id IN  NUMBER,
  p_promise_date     IN  DATE,
  p_na_flag          IN  VARCHAR2,  -- 'Y' = N/A bypass selected
  p_bypass_reason    IN  VARCHAR2,
  x_status           OUT VARCHAR2,
  x_message          OUT VARCHAR2
) IS
BEGIN
  x_status := 'S';
  IF p_na_flag = 'Y' THEN
    IF p_bypass_reason IS NULL THEN
      x_status  := 'E';
      x_message := 'Bypass reason is required when Promise Date is N/A.';
    END IF;
    RETURN;  -- bypass accepted with reason
  END IF;
  IF p_promise_date IS NULL THEN
    x_status  := 'E';
    x_message := 'Promise Date is required. Select N/A if date is not known.';
    RETURN;
  END IF;
  IF p_promise_date < TRUNC(SYSDATE) THEN
    x_status  := 'W';
    x_message := 'Promise Date is in the past. Please confirm.';
  END IF;
END;
```
This encapsulates the complete GE Promise Date validation: mandatory field with N/A bypass option. The `x_status = 'W'` (warning) path showed a confirmation dialog but allowed submission — hard errors (`'E'`) blocked submission entirely.

**367. Write a SQL to identify all custom packages currently invalid in the APPS schema.**
```sql
SELECT object_name, object_type, status, last_ddl_time
  FROM all_objects
 WHERE owner       = 'APPS'
   AND object_name LIKE 'XX%'  -- custom prefix
   AND status      = 'INVALID'
   AND object_type IN ('PACKAGE','PACKAGE BODY','PROCEDURE','FUNCTION','TRIGGER')
ORDER BY object_type, object_name;
```
After an EBS patch, custom objects that depend on modified Oracle objects become invalid. Run `EXEC DBMS_UTILITY.COMPILE_SCHEMA('APPS')` or `EXEC UTL_RECOMP.RECOMP_PARALLEL(4)` to recompile. At GE, this query was part of the post-patch validation checklist to verify all custom `XXGEA_*` objects compiled cleanly.

**368. Write a PL/SQL block to send email from a concurrent program using UTL_MAIL.**
```sql
BEGIN
  UTL_MAIL.SEND(
    sender      => 'noreply@ge.com',
    recipients  => :p_email_list,
    subject     => 'ASN Compliance Report - ' || TO_CHAR(SYSDATE,'DD-MON-YYYY'),
    message     => 'Please find attached the ASN compliance report.'
                || CHR(10) || 'Total ASNs this week: ' || :p_count,
    mime_type   => 'text/plain; charset=us-ascii'
  );
EXCEPTION
  WHEN OTHERS THEN
    FND_FILE.PUT_LINE(FND_FILE.LOG,'Email failed: '||SQLERRM||' - continuing');
END;
```
`UTL_MAIL` requires the `SMTP_OUT_SERVER` initialization parameter to be set. In EBS, Oracle Workflow Notification Mailer is the preferred mechanism for outbound email (it handles HTML, attachments, and delivery receipts). `UTL_MAIL` is a fallback for simple notification emails from concurrent programs where setting up a full workflow item would be disproportionate.

**369. Write a SQL to find all FND messages used in the XXGEA custom code.**
```sql
SELECT DISTINCT fm.message_name, fm.message_text, fm.type
  FROM fnd_new_messages fm
 WHERE fm.language_code = 'US'
   AND fm.message_name IN (
         SELECT REGEXP_SUBSTR(s.text,'XX[A-Z_0-9]+',1,1)
           FROM all_source s
          WHERE s.owner = 'APPS'
            AND s.name LIKE 'XXGEA%'
            AND s.text LIKE '%FND_MESSAGE%'
       )
ORDER BY fm.message_name;
```

**370. How would you write the PL/SQL fix for the Unit Price pulling from BPA vs Standard PO bug?**
The root cause was that the VO query joined `PO_LINE_LOCATIONS_ALL` to `PO_LINES_ALL` and then followed `PO_LINES_ALL.FROM_LINE_ID` (the BPA source line) to get the price, overriding the Standard PO price. Fix in the VO's Expert Mode SQL:
```sql
-- Correct: use the Standard PO line price directly
SELECT pl.unit_price,  -- Standard PO line price
       pll.price_override  -- release/shipment price override if any
  FROM po_line_locations_all pll
  JOIN po_lines_all pl ON pl.po_line_id = pll.po_line_id
  -- Do NOT join back to the from_line_id BPA line for price
```
The display price should be `NVL(pll.price_override, pl.unit_price)` — the shipment-level override if set, otherwise the PO line price. Never follow `pl.from_line_id` to the BPA for the display price on a Standard PO. This was corrected via VO extension + personalization at GE; no Oracle source was touched.

---

# Section T — Production Support & Real Bug-Fix Scenarios (Q371–Q405)

**371. Walk through the BPA price editability bug you fixed — root cause and fix.**
**Root cause:** iSupplier Change Request screen for BPA/GBPA lines had the Unit Price field rendered as an editable `messageTextInput` item — the seeded personalization did not restrict it for change requests. Suppliers could type any price and submit, which updated `PO_CHANGE_REQUESTS.NEW_PRICE`, and if a buyer approved without noticing, it revised the agreed BPA price. **Fix:** OAF personalization on the Change Request page set `ReadOnly = true` (static personalization) on the Unit Price item for both Standard PO and BPA/GBPA type POs. Added a server-side validation in the controller extension's `processFormRequest` to reject any submission where `NEW_PRICE != PLL.UNIT_PRICE` as an extra defense layer. **Verification:** tested with a surrogate buyer account against a BPA, confirmed price field locked, confirmed server validation caught any bypass attempts.

**372. How did you debug the Unit Price pulling from Blanket Agreement instead of Standard PO?**
Reproduced the issue: created a Standard PO sourced from a BPA, opened the delivery schedules screen in iSupplier, and saw the BPA line price instead of the Standard PO price. Used "About This Page" to find the VO (`RcvDeliveryScheduleVO`) and inspected its SQL via diagnostics. Found the query joined `PO_LINES_ALL.FROM_LINE_ID` → BPA `PO_LINES_ALL.UNIT_PRICE` for the displayed price, overriding the Standard PO line price. Fixed by extending the VO and overriding the price column expression to use `NVL(pll.price_override, pl.unit_price)` directly from the Standard PO line, not the BPA source line.

**373. Promise Date was defaulting to Need-by Date silently — explain the complete fix.**
**Problem:** Oracle's seeded PO acknowledgement code copied `NEED_BY_DATE` into `PROMISED_DATE` when the supplier acknowledged without entering a date, creating false OTD data. **Investigation:** queried `PO_LINE_LOCATIONS_ALL` after acknowledgement and found `promised_date = need_by_date` for all lines — not a supplier entry. Traced to a PL/SQL procedure in `PO_ACKNOWLEDGE_PO_GRP` that set `promised_date := need_by_date` when input was null. **Fix:** (1) OAF personalization made Promise Date field mandatory (cannot submit blank), preventing the null input that triggered the default. (2) Added an N/A checkbox with bypass reason as an alternative for suppliers who genuinely cannot commit. (3) A one-time data-fix script nulled out historical records where `promised_date = need_by_date` with a post-acknowledgement timestamp. (4) Renamed the column label from "Due Date" to "Promise Date" via FND message personalization.

**374. The Vendor LOT search on View ASN was not working — what was the issue?**
The "View ASN" search screen had a Vendor LOT search parameter, but it was querying the wrong column — `RCV_SHIPMENT_LINES.LOT_NUM` (the standard Oracle lot tracking column, populated via the standard serial/lot flow) instead of the custom `VENDOR_LOT_NUM` column added by the GE extension. The VO extension that added `VENDOR_LOT_NUM` was correctly applied on the ASN creation page but was not applied on the View ASN search VO. Fix: extend the View ASN search VO to include `VENDOR_LOT_NUM` and update the personalized search field to bind to the correct attribute. Validated by searching for a known Vendor LOT and confirming results appeared.

**375. The Ship-Method LOV showed "No Items Found" — investigation and resolution.**
Used "About This Page" to find the LOV VO name and SQL query. Executed the query directly in SQL Developer — it returned rows. Then checked the LOV's search criteria and found it was filtering by `view_application_id = 0` (global lookups) but the `SHIPMENT_METHOD` lookup type in that EBS instance was defined under `view_application_id = 201` (PO). The seeded LOV VO had `view_application_id` hardcoded as a different value. Fix: extended the LOV VO to override the WHERE clause to use `view_application_id = 201`, registered the substitution, bounced OC4J via CTASK. Validated by confirming ship methods appeared in the LOV.

**376. DPAS messaging was not appearing on PO acknowledgement for rated POs — what was the fix?**
DPAS (Defense Priorities and Allocations System) messaging requires `PO_HEADERS_ALL.DPAS_RATING` to be populated and a specific profile or lookup to trigger the DPAS message display. Investigation: checked `PO_HEADERS_ALL.DPAS_RATING` for the test PO — it was populated correctly with 'DO'. Then inspected the OAF acknowledgement page's controller logic — the condition rendering the DPAS message region used `IF vo.getAttribute("DpasRating") != null` but the VO attribute was named `DPAS_RATING` (Oracle convention) and the getAttribute call used `"dpasRating"` (camelCase mismatch — Java is case-sensitive). Fix: corrected the case in the controller extension's processRequest where the DPAS rendered flag was being set on the region.

**377. Planners were getting excessive notifications when suppliers updated Promise Dates — solution.**
**Problem:** Every supplier promise-date change triggered an Oracle Workflow notification to the PO's planner, flooding their worklist with low-priority updates. At 100+ suppliers across 5 sites, this was hundreds of daily notifications. **Solution:** (1) Created a custom workflow item type `XXPROMIS` with a filter function activity. (2) Built `XXGEA_NOTIF_CTRL_PKG.should_suppress()` that checked a rules table — suppress if the change was < 3 days from the original, or the supplier had a "trusted" flag, or the planner had opted out. (3) Hooked this into the iSupplier promise-date change workflow using a controller extension that called the custom package before the seeded notification fired. (4) Built a buyer-facing UI (OAF personalization) to manage the suppression rules. Result: notification volume reduced by ~80%.

**378. An ASN was submitted but no confirmation appeared and the record didn't show in Receiving.**
This is an interface processing failure. Check in order: (1) `RCV_HEADERS_INTERFACE` — is the header record there with `processing_status_code = 'PENDING'` or `'ERROR'`? (2) `RCV_TRANSACTIONS_INTERFACE` — same check for line records. (3) `PO_INTERFACE_ERRORS` — join on `header_interface_id` to get the exact error message. (4) Check if the Receiving Transaction Processor ran — look for a recent completed concurrent request. (5) If the interface records are missing entirely, the OAF page may have failed before inserting — check the OC4J log for Java exceptions. Most common causes: invalid ship-to organization, quantity exceeds tolerance, PO ack required but not done, item not enabled for receiving.

**379. A supplier says their PO is not visible in iSupplier even though it's approved — investigation.**
Systematic checklist: (1) Verify the PO `authorization_status = 'APPROVED'` and `closed_code` is not 'FINALLY CLOSED'. (2) Check `ap_supplier_sites_all.purchasing_site_flag = 'Y'` for the supplier site on the PO. (3) Verify the supplier user is correctly mapped in `pos_supplier_users` with the correct `vendor_id` and `vendor_site_id`. (4) Check `fnd_user_resp_groups_direct` — does the user have an active iSupplier responsibility? (5) Verify the responsibility's `MO: Operating Unit` profile matches the PO's `org_id`. (6) Check if the PO's `type_lookup_code` is a type displayed in iSupplier (Standard/BPA/Release — not all types show). (7) If all correct, check for a personalization hiding the PO based on a field condition that incorrectly matches this PO. At GE, the most common cause was `vendor_site_id` mismatch — the PO was raised against Site A but the user was mapped only to Site B.

**380. Why does OACore/OC4J need to be bounced after a personalization deployment?**
OAF caches the MDS (MetaData Services) page definitions in the application server's JVM memory at startup or on first access. When you import new personalizations into the MDS database tables, the running JVM still serves the cached old version. Bouncing OC4J (or OACore, which is the Oracle Application Core servlet container for OAF in R12) flushes the JVM memory cache, forcing OAF to re-read the updated page definitions from MDS on the next request. Without the bounce, users may see the old personalization or, worse, a mix of cached and new definitions causing inconsistent behavior. This is why all personalization deployments at GE were done via ServiceNow CTASKs coordinated with the DBA team for a controlled OC4J restart.

**381. A concurrent program is stuck in "Pending - Normal" — what do you check?**
(1) **Internal Concurrent Manager (ICM) running?** — Check via sysadmin: Concurrent → Manager → Administer. If ICM is down, all requests queue. (2) **Work shift active?** — Check if the Standard Manager has an active work shift covering the current time. (3) **Incompatibilities?** — Check if an incompatible program is running, blocking this one via Conflict Resolution Manager. (4) **Enough processes?** — Check the Standard Manager's `MAX_PROCESSES` vs current running count. If at max, requests queue until a slot frees. (5) **Specialization rules?** — If the manager has specialization rules restricting which programs it runs, verify this program is included. At GE, post-go-live a queue backup was caused by a long-running custom batch holding all 5 Standard Manager processes.

**382. After a PROD patch, several OAF personalizations stopped working — diagnosis.**
First, check whether the patch updated the OAF base page files (`.xml` files on the filesystem or MDS-imported base definitions). Run `JDR_UTILS.printDocument('/oracle/apps/icx/...')` to compare the page structure before/after — if Oracle added, removed, or renamed regions/items, personalizations targeting those components by ID are broken. Second, check if the patch introduced a VO substitution that conflicts with yours — two substitutions on the same VO can cause unpredictable behavior. Third, export the personalization XML and inspect for broken `refPath` values pointing to components that no longer exist. Fix by re-applying the personalization against the new page structure, adjusting region/item IDs to match the patched page.

**383. A BI Publisher report generates blank output — systematic diagnosis.**
Step 1: Run the concurrent program with output format = XML; if the XML file is empty or contains no data rows, the problem is in the query/data model (wrong parameters, `org_id` context missing, data doesn't exist for the period). Step 2: If XML has data but the PDF/Excel is blank, the RTF template has a bug — load the XML into Template Builder for Word and run locally; look for mismatched element names in `<?for-each?>` tags (case-sensitive). Step 3: Check the BIP Template Definition — is the template code exactly matching the data definition code? A mismatch means BIP applies no template. Step 4: Check the output language/territory setting — wrong locale can cause number/date formatting to fail silently. At GE, a blank Mass ASN Label report was caused by `<?for-each:G_ASN?>` in the RTF not matching the group name `G_Asn` (case mismatch) in the data template.

**384. A WebADI upload is failing for some rows but not all — debugging approach.**
WebADI writes error messages back into the spreadsheet's error column for each failed row. Download the spreadsheet after upload and read those error cells — they contain the exact `x_msg_data` from your validation API or the interface table error. Then reproduce the failing rows in SQL Developer by calling the PL/SQL validation procedure directly with those row values. Common causes: date format mismatch (the spreadsheet sends dates as strings; your procedure expects DATE — check the WebADI interface column's data type definition), null values in required fields that the layout didn't mark required, or a value that passes client-side LOV validation but fails a DB constraint. At GE, Promise Date upload failures were caused by date format differences between UK-format Excel (`DD/MM/YYYY`) and the expected Oracle format.

**385. An iSupplier user is seeing POs from the wrong supplier — data security investigation.**
This is a critical security issue. Immediate triage: (1) Check `pos_supplier_users` for the affected user — do they have multiple `vendor_id` mappings? A user accidentally mapped to two vendors would see both. (2) Check `icx_sessions` for the user's current session — what `vendor_id` is stored? If it's wrong, a session attribute was set incorrectly (possibly from a surrogate action not clearing properly). (3) Check whether the iSupplier responsibility's data security profile covers multiple suppliers. (4) Verify no personalization removed or bypassed the `vendor_id` WHERE clause filter in the PO search VO. Fix: clean the `pos_supplier_users` mapping, terminate the session (`icx_sessions.disabled_flag = 'Y'`), and have the user re-login. Document as a security incident.

**386. The ASN eligibility engine is blocking shipments that should be eligible — debugging.**
Run the `is_eligible_for_asn` function directly in SQL Developer for the specific `line_location_id` in question and check which condition is returning 'N'. Common false-negative causes: (1) `days_early_receipt_allowed` is 0 and the PO need-by date is tomorrow — mathematically eligible but the function's date arithmetic has an off-by-one (use `>=` not `>`). (2) `pll.closed_code` is `'CLOSED FOR RECEIVING'` but the query checks `NOT IN ('CLOSED','FINALLY CLOSED')` — so 'CLOSED FOR RECEIVING' passes, but check if this state should also be excluded. (3) The `in_transit` calculation double-counts partially received ASN lines. (4) Timezone issue — `SYSDATE` in the DB is UTC but need-by dates are stored in site local time. At GE, an off-by-one in the early-receipt window was blocking valid same-day shipments.

**387. After SSO enablement, some supplier users cannot log in — likely issues and resolution.**
SSO (Single Sign-On) delegates authentication to an Identity Provider. Supplier users failing after SSO enablement: (1) Their `fnd_user` accounts may not have a `GUID` populated — SSO matches users by GUID or by email/username to the IdP. Run: `SELECT user_name, user_guid FROM fnd_user WHERE user_name = :p_user`. If `user_guid` is null, the SSO provisioning did not complete for that user. Fix: populate `user_guid` via `FND_USER_PKG.UPDATEUSER`. (2) The IdP may not have the supplier's identity — they need to be provisioned in the corporate IdP (or a partner IdP). (3) JIT (Just-In-Time) provisioning may be misconfigured for external users. (4) The supplier's email domain may be excluded from SSO routing rules. At GE, 3 suppliers failed because their email domains were not in the SSO email-routing allowlist.

**388. A VO substitution deployed in DEV is not working in UAT — what was missed?**
Substitutions are MDS documents — they must be explicitly exported from DEV using `jpxexport` and imported into UAT using `jpximport`. Unlike personalizations (which are migrated via Functional Administrator), substitutions require the command-line `jpximport` tool. Check: (1) Was `jpximport` run against the UAT instance with the substitution XML? (2) Was OC4J bounced in UAT after import to flush the MDS cache? (3) Is the custom JAR file containing the extended class deployed to UAT's `$OA_HTML/WEB-INF/lib` or `$OA_CLASSPATH`? Without the JAR, the substitution references a class that doesn't exist on the classpath, causing a silent fallback to the base class. (4) Does the UAT instance have a different `APPL_TOP` structure requiring the JAR to be deployed separately per node?

**389. Promise Date mandatory validation fires even when bypass reason is provided — fix.**
The controller extension's `processFormRequest` was reading the N/A checkbox value incorrectly. The checkbox was a `messageCheckBox` item in OAF — when unchecked, `pageContext.getParameter("naFlag")` returns null (not "N"). The validation code had: `if (naFlag != "Y")` — but in Java, string comparison with `!=` compares references, not values. Fix: change to `if (!"Y".equals(naFlag))`. This is a classic Java string comparison bug. After the fix, the bypass path correctly skipped the mandatory-date validation and only required the bypass reason. Always use `.equals()` for OAF parameter string comparisons, never `==` or `!=`.

**390. The receipt interface is rejecting ASNs with "PO_PDOI_INVALID_SHIP_TO_ORG" — what does it mean?**
`PO_PDOI_INVALID_SHIP_TO_ORG` means the `SHIP_TO_ORGANIZATION_ID` (inventory org) on the ASN does not match the ship-to organization on the PO shipment, or the org is not a valid receiving organization. Check: (1) `PO_LINE_LOCATIONS_ALL.SHIP_TO_ORGANIZATION_ID` for the PO shipment. (2) The ASN header's `SHIP_TO_ORG_ID` in `RCV_HEADERS_INTERFACE` — does it match? (3) Is the `SHIP_TO_ORGANIZATION_ID` in `RCV_SHIPMENT_HEADERS` a valid inventory org in `ORG_ORGANIZATION_DEFINITIONS`? At GE, this error appeared after a new site's inventory org was added — the iSupplier ship-to location mapping table was not updated to include the new org, so ASNs for that site were rejected.

**391. A FNDLOAD upload of concurrent program definitions is failing in PROD — causes?**
Common causes: (1) The LDT file references an executable that doesn't exist in PROD — FNDLOAD is trying to update a concurrent program but the underlying executable was not migrated first. (2) Insufficient APPS password — FNDLOAD uses `apps/password@db` and a wrong password silently fails or produces a cryptic error. (3) The LCT (control file) version doesn't match the EBS version — FNDLOAD is strict about the control file version matching the target instance's release. (4) Incompatible character in program description (special characters, non-ASCII). (5) The program is locked by an active request — some FNDLOAD operations require the program to be inactive. Fix: check the FNDLOAD log file, validate the LDT against the target environment, and ensure prerequisite objects (executables, request groups) are migrated first.

**392. Describe your ServiceNow CTASK standard procedure for PROD OAF deployments.**
The GE deployment procedure: (1) **CTASK creation:** detail all steps — files to deploy, OC4J bounce sequence, rollback steps, estimated duration, maintenance window. (2) **Approval:** architecture lead and client IT approved; change manager scheduled the window. (3) **Pre-deployment backup:** DBA exported existing MDS personalizations for affected pages. (4) **Deployment sequence:** (a) deploy custom JARs/class files to `$OA_HTML/WEB-INF/lib` on each node, (b) import FNDLOAD objects (concurrent programs, profiles, messages), (c) import OAF personalizations via Functional Administrator, (d) import VO substitutions via jpximport, (e) bounce OC4J on both nodes (rolling bounce to avoid downtime), (f) smoke-test the affected pages. (5) **Closure:** log outcomes, attach screenshots of smoke-test results, close CTASK. This process was followed for every PROD change at GE.

**393. A Workflow notification email is not reaching the supplier — tracing and fix.**
(1) Check `WF_NOTIFICATIONS` — is the notification status `OPEN` or `CLOSED`? If `CLOSED` with no response, it may have timed out. (2) Check `WF_NOTIFICATION_OUT` view — is the email listed? If not, the Notification Mailer may not have processed it. (3) Check the Workflow Notification Mailer concurrent program status and logs — look for SMTP errors or connection failures. (4) Check if the recipient role (`WF_NOTIFICATIONS.RECIPIENT_ROLE`) maps to an email address — query `WF_ROLES` and verify `EMAIL_ADDRESS` is not null. (5) Check spam filters at the supplier's mail server — ask the supplier to whitelist the sender domain. (6) For iSupplier, also check the supplier contact's `email_address` in `ap_supplier_contacts` — if null, no email is sent even if the workflow notification fires.

**394. Mass ASN Label BIP report is showing wrong quantities — investigation.**
Check the report's data template SQL: the ASN label should display `RCV_SHIPMENT_LINES.QUANTITY_SHIPPED` (what the supplier said they shipped), not `QUANTITY_RECEIVED` (what was physically received — may be zero for in-transit ASNs). If the report shows zero quantities, the query is using `quantity_received` from `rcv_transactions` which is zero for EXPECTED shipments. Fix: ensure the data template joins `RCV_SHIPMENT_LINES` and uses `quantity_shipped`. For the "Child Project Quantity" breakup in the GE Collaboration History report, ensure the GROUP BY is at the project level, not aggregated at the header level.

**395. After adding 2 server nodes, some OAF sessions are dropping — what configuration is needed?**
Multi-node OAF requires sticky sessions (HTTP session affinity) at the load balancer — each user's requests must route to the same JVM to maintain their AM pool state. If sessions drop, the load balancer is routing a user to a different node on subsequent requests. Fix: configure the load balancer to route based on `JSESSIONID` cookie or `JVM_ID` cookie. In Oracle HTTP Server with `mod_oc4j`, configure `OC4JMountCopy` and sticky routing. Also verify: (1) `dbc` file is updated on both nodes to point to the correct DB. (2) `APPL_TOP` is shared via NFS or synchronized across nodes. (3) `$OA_HTML` and custom JARs are deployed on both nodes. (4) Concurrent manager is not running on both nodes simultaneously unless clustered correctly.

**396. A custom PL/SQL package compiles in DEV but not in PROD — possible causes.**
(1) **Missing object:** the package references a table, view, or synonym that exists in DEV but not PROD. Check `ALL_OBJECTS` in PROD for the referenced objects. (2) **Synonym not created:** a custom table exists in `XX` schema in PROD but the APPS synonym is missing. (3) **Grant missing:** the APPS schema doesn't have SELECT/EXECUTE privilege on the referenced object in PROD. (4) **Different Oracle version:** PROD may be on a different Oracle DB version that doesn't support a syntax feature used. (5) **Character set difference:** if the package was copied as text, special characters may have been corrupted. (6) **Dependency on a standard package** that has a different spec in PROD due to a different EBS patch level.

**397. An OAF SPEL personalization stops working after an EBS patch — why?**
SPEL expressions bind to a VO attribute name, e.g., `${oa.MyVO.MyAttribute}`. If the patch renames the VO (new substitution replaces the old VO with a different class that has a different set of attributes), or removes/renames the attribute, the SPEL expression evaluates to null at runtime and the property defaults to its base value (typically `false` for Rendered, `false` for Required). Investigate: use "About This Page" to check if the VO name and attribute name still exist in the patched page. If the attribute was renamed, update the personalization's SPEL expression. If the VO was replaced, re-apply the VO extension against the new base class.

**398. A supplier submitted a change request that is not routing for approval — workflow debug.**
(1) Check `PO_CHANGE_REQUESTS` for the record — is `request_status = 'PENDING'`? If `'BUYER_APP'`, it was already processed. (2) Check `WF_ITEMS` for the corresponding workflow item (type `POSCHNG`, item_key = change_request_id). If no item exists, the workflow was never launched. (3) Check if the iSupplier change-request submission code successfully committed the `PO_CHANGE_REQUESTS` row and launched the workflow. Look for OC4J exceptions around the submission. (4) Check the PO's buyer assignment (`agent_id`) — if the buyer's FND user has no email or no workflow role, notifications fail silently. (5) Run `WF_ENGINE.LaunchProcess` manually for the change_request_id to force the workflow to start, then monitor via Workflow Status Monitor.

**399. The iSupplier On-Time Performance screen shows incorrect percentages — what tables to check?**
The OTP screen derives data from the `RCV_TRANSACTIONS` (receipt date) vs `PO_LINE_LOCATIONS_ALL.PROMISED_DATE` comparison. Check: (1) Are `promised_date` values correct, or are they still defaulting to `need_by_date` (the GE defect)? Incorrect promises make OTP calculations meaningless. (2) Is the query filtering on `transaction_type = 'RECEIVE'` only? Including DELIVER or CORRECT transactions would inflate receipt counts. (3) Is the date comparison using `TRUNC()` on both sides? A receipt at 23:59 and a promise date at 00:00 on the same day would show as late without TRUNC. (4) Is the time period filter correct — fiscal calendar vs calendar year? (5) Check the OAF VO's SQL query (via About This Page) against the tables to verify the formula matches expectations.

**400. After a data migration, existing supplier contacts cannot log in to iSupplier — FND data fix.**
After migrating supplier data (e.g., from one instance to another), the `fnd_user.person_party_id` field may not be populated — this links the FND user to the TCA party of the supplier contact. Without this link, the iSupplier session cannot resolve the user's `vendor_id`. Fix steps: (1) Identify affected users: `SELECT user_name FROM fnd_user WHERE person_party_id IS NULL AND user_name LIKE 'SUPP%'`. (2) Match each user to their TCA party via `ap_supplier_contacts.email_address = fnd_user.email_address` → `ap_supplier_contacts.party_id`. (3) Update `fnd_user.person_party_id` using `FND_USER_PKG.UPDATEUSER(x_user_name, x_person_party_id => ...)` — never update `fnd_user` directly. (4) Verify `pos_supplier_users` has the correct `vendor_id`/`vendor_site_id` mapping for each user.

**401. A batch PL/SQL job completes but only processes a fraction of expected rows — root cause.**
Most common cause: a `WHERE` clause condition that filters more aggressively than expected. Check: (1) Is `org_id` correctly set? A MOAC context issue may restrict rows to one OU when all OUs are needed. (2) Is there a date filter using `SYSDATE` that should use a parameter? (3) Is the cursor using `ROWNUM` that limits results? (4) Is the `COMMIT` inside the cursor loop destroying the cursor state — in Oracle, committing inside a cursor loop can cause the cursor to lose rows (use bulk collect + commit per batch instead). (5) Is there a `WHEN OTHERS THEN NULL` exception block silently swallowing errors and skipping rows?

**402. The Concurrent Manager is running slowly and requests are queuing — what to check?**
(1) Check the Standard Manager's `MAX_PROCESSES` vs queue depth — if processes are at max and the queue is deep, increase processes temporarily (via Manager Administer) or add a work shift. (2) Check for long-running requests blocking pool slots — `SELECT request_id, concurrent_program_id, actual_start_date FROM fnd_concurrent_requests WHERE phase_code='R'` — kill any obviously stalled ones. (3) Check DB performance — a slow shared DB will slow all concurrent programs. Look at `V$SESSION` for blocked/waiting CM worker sessions. (4) Check the ICM log for frequent restart or errors. (5) Check if a nightly batch is running during peak hours, consuming all CM processes. At GE, a full-table-scan in a nightly BI Publisher data template was consuming all concurrent processes for 3 hours during morning peak hours.

**403. A page personalization is showing for all users instead of just one responsibility — what went wrong?**
The personalization was applied at the wrong level. OAF personalization levels: User > Responsibility > Organization > Operating Unit > Localization > Site > Function. If a personalization meant for one responsibility was exported and re-imported without the correct level document name (which includes the responsibility ID), it may have been imported at Site level — affecting all users. Check the MDS document name: responsibility-level personalizations have names like `resp<app_id>_<resp_id>`. Delete the incorrect Site-level personalization and re-import specifically at the Responsibility level. Always verify the level after import using Functional Administrator → Personalization → search for the page.

**404. An OAF controller extension is causing a ClassCastException in production — root cause.**
A `ClassCastException` in OAF usually means the wrong class is being cast — most commonly when a VO extension substitution is partially applied. Example: `(MyExtendedVO) am.findViewObject("StandardVO")` throws `ClassCastException` if the substitution is not active in PROD (so the AM returns the base class, not your extension). Check: (1) Is the substitution imported in PROD (`jpximport`)? (2) Is the JAR containing `MyExtendedVO` deployed on all nodes? (3) Was OC4J bounced on all nodes after deployment? (4) Is there a version mismatch — the controller expects a method that exists in your extended VO but not in the base VO? Another cause: casting an OAWebBean from a wrong region type (e.g., casting a `messageTextInput` as `messageChoice`).

**405. Describe a post-go-live production crisis you managed — communication and resolution.**
At GE's Day 1 post-go-live, 15 suppliers reported they could not submit ASNs. The error in the portal was generic — "Submission failed." Immediate steps: (1) Acknowledged to the client within 10 minutes with a confirmed incident-in-progress message. (2) Queried `PO_INTERFACE_ERRORS` and found `error_message = 'RCV_ORG_NOT_FOUND'` — the new Site 3 inventory org had not been added to the iSupplier ship-to location mapping table (`ICX_PO_VENDOR_SHIP_ORGS`). (3) Root cause isolated in 20 minutes. (4) DBA raised a CTASK for emergency data fix (insert missing org mapping). (5) Tested with a surrogate account, confirmed fix. (6) Communicated resolution to all 15 suppliers with clear retry instructions. (7) Post-incident: added the org mapping check to the go-live checklist for Sites 4 and 5. Total downtime: 90 minutes. Lesson: every inventory org used for receiving must be explicitly registered in iSupplier configuration tables.

---

# Section U — REST, SOAP, Spring Boot & OIC Integration (Q406–Q430)

**406. How did you architect the Spring Boot integration between EBS and third-party SCM systems at TCS?**
The architecture was a **hub-and-spoke** pattern: Spring Boot acted as the integration hub with EBS on one side and third-party systems on the other. Key components: (1) **Inbound REST controller** receiving data from third-party systems (JSON payloads), validated via Bean Validation (`@Valid`). (2) **Transformation service** mapping third-party data models to EBS interface table structures. (3) **EBS adapter layer** inserting into Oracle interface tables (`PO_HEADERS_INTERFACE`, `RCV_TRANSACTIONS_INTERFACE`) via JDBC, then calling `FND_REQUEST.SUBMIT_REQUEST` via a stored procedure to trigger the import concurrent program. (4) **Outbound SOAP client** using JAX-WS to query EBS Oracle Integration Repository (IREP) services for PO status and pushing to the third-party system. (5) **Error handling** with a custom exception hierarchy, retry queue (DB-backed), and alerts via email for persistent failures.

**407. How do you handle authentication when calling EBS SOAP web services from Spring Boot?**
EBS SOAP services via the Integration Repository (IREP/ISG) use **HTTP Basic Authentication** (username/password) passed as a SOAP header or HTTP Authorization header. In Spring Boot, configure `WebServiceTemplate` with a `HttpComponentsMessageSender` and set `UsernamePasswordCredentials`. For more secure deployments, use a service account with minimal EBS responsibilities. Example:
```java
HttpComponentsMessageSender sender = new HttpComponentsMessageSender();
sender.setCredentials(new UsernamePasswordCredentials("svc_account", "password"));
webServiceTemplate.setMessageSender(sender);
```
In production, credentials are stored in Spring Cloud Config or Vault — never hardcoded. EBS also supports WS-Security (UsernameToken profile) for SOAP which is handled via `Wss4jSecurityInterceptor` in Spring WS.

**408. What is the EBS Integration Repository (IREP) and how is it used?**
IREP (Integration Repository) is Oracle's catalog of all public EBS service interfaces — PL/SQL APIs, Java APIs, Business Events, XML Gateway transactions, and Open Interfaces. You can browse it at `http://host:port/OA_HTML/BneApplicationService?page=/oracle/apps/fnd/irep/webui/IrepHomePG`. It documents exact API signatures, parameters, and integration patterns for each EBS module. For the TCS integrations, I used IREP to find the correct `PO_HEADERS_INTERFACE` structure and the PO Import concurrent program signature, rather than reverse-engineering from the tables. Oracle also exposes some IREP APIs via the Integrated SOA Gateway (ISG) as deployable REST/SOAP services.

**409. What is Oracle Integration Cloud (OIC) and how would you use it to connect EBS to Fusion?**
OIC is Oracle's Integration Platform as a Service (iPaaS) — a cloud-hosted integration platform with pre-built adapters for Oracle SaaS, on-premises EBS (via Oracle EBS Adapter), and 200+ third-party applications. Key concepts: **Integrations** (orchestration flows connecting two endpoints), **Adapters** (EBS, Fusion ERP, REST, SOAP, FTP, DB), **Visual Mapper** (XSLT-based field mapping GUI), **Lookups** (value mapping tables), **Error Handling** (fault policies, notification). For EBS→Fusion migration: OIC can read from EBS (via DB adapter querying interface tables or via EBS adapter calling IREP APIs), transform the data, and write to Fusion (via Fusion ERP adapter calling REST APIs). My REST/SOAP background from TCS maps directly to OIC's adapter concepts.

**410. What is the difference between synchronous and asynchronous integration patterns with EBS?**
**Synchronous:** the calling system waits for the EBS response before continuing. Suitable for real-time lookups (e.g., "is this PO approved?") where the caller needs an immediate answer. Risk: if EBS is slow or down, the calling system is blocked. **Asynchronous:** the caller posts data and receives an immediate acknowledgement (correlation ID), then polls or receives a callback when EBS finishes processing. Suitable for bulk loads (ASN submissions, invoice imports) where processing may take minutes. The EBS concurrent program model is inherently asynchronous — `FND_REQUEST.SUBMIT_REQUEST` returns a request_id immediately; the caller must poll `fnd_concurrent_requests` for completion. At TCS, all high-volume integrations used async patterns with a status-tracking table; real-time inventory checks used synchronous REST calls to ISG-exposed APIs.

**411. How do you implement idempotency in a REST API that creates ASNs in EBS?**
Accept a client-supplied `idempotency_key` (e.g., the supplier's own packing slip number) in the request header. On receipt: (1) Check if this key already exists in a `XXGEA_IDEMPOTENCY_KEYS` table. (2) If found and status = 'SUCCESS', return the original response (do not reprocess). (3) If found and status = 'IN_PROGRESS', return `409 Conflict` telling the client to poll. (4) If not found, insert the key with status 'IN_PROGRESS', process the ASN, update to 'SUCCESS' with the EBS shipment_header_id, and return `201 Created`. This prevents duplicate ASNs when network timeouts cause the client to retry a request that already succeeded. The idempotency table should have a unique index on `idempotency_key` to handle concurrent duplicate submissions.

**412. How do you map EBS PO data to a REST JSON payload for a third-party system?**
```java
@Service
public class PoMappingService {
  public ThirdPartyPoDto mapFromEbs(PoHeaderDto ebsPo) {
    return ThirdPartyPoDto.builder()
      .externalPoNumber(ebsPo.getSegment1())
      .supplierCode(ebsPo.getVendorNum())
      .supplierSite(ebsPo.getVendorSiteCode())
      .currency(ebsPo.getCurrencyCode())
      .lines(ebsPo.getLines().stream()
        .map(line -> ThirdPartyLineDto.builder()
          .lineNumber(line.getLineNum())
          .itemCode(line.getItemNumber())
          .quantity(line.getQuantity())
          .unitPrice(line.getUnitPrice())
          .needByDate(line.getNeedByDate().format(DateTimeFormatter.ISO_DATE))
          .build())
        .collect(Collectors.toList()))
      .build();
  }
}
```
Map field-by-field with explicit null-safety (`Optional.ofNullable`). Date formats must match the third-party system's expectation — always use ISO 8601 (`YYYY-MM-DD`) for external APIs; never send Oracle's internal date format.

**413. What is a circuit breaker pattern and when would you use it in EBS integration?**
A circuit breaker wraps calls to a remote service and tracks failure rates. If failures exceed a threshold (e.g., 50% in 10 seconds), the circuit "opens" — subsequent calls fail immediately without attempting the remote call, giving the failing service time to recover. After a timeout, the circuit enters "half-open" state and allows one test call — if it succeeds, the circuit closes. Implement with Resilience4j in Spring Boot: `@CircuitBreaker(name = "ebs-asn-service", fallbackMethod = "asnFallback")`. Use this for EBS→third-party calls where the third-party is known to be intermittently unavailable, preventing cascade failures and timeouts across all supplier transactions.

**414. How do you design an event-driven integration where an ASN submission triggers an external notification?**
EBS Business Events can publish an event when an ASN is submitted (Oracle delivers `oracle.apps.rcv.asn.create` Business Event). Subscribe to this event via Oracle Workflow and trigger a custom PL/SQL procedure that: (1) Reads the shipment details. (2) Calls a Spring Boot webhook endpoint via `UTL_HTTP.REQUEST` (or uses the Workflow Notification Mailer for email-based notification). For a modern architecture with OIC: subscribe to the EBS Business Event in OIC using the EBS Adapter's event subscription capability, then OIC orchestrates the downstream notification (REST POST to a 3PL system, email via SendGrid, Slack webhook, etc.) without the EBS DB making outbound HTTP calls.

**415. What are the key EBS APIs you would expose via REST for a supplier portal integration?**
For a custom supplier portal (replacing or extending iSupplier): PO query API (`PO_INQUIRE_GRP`), PO acknowledgement API (`PO_ACKNOWLEDGE_PO_GRP`), ASN creation via RCV interface tables + Receiving Transaction Processor, promise date update (`PO_DOCUMENT_UPDATE_GRP`), receipt inquiry (`RCV_SHIPMENT_INQUIRY`), payment status via AP APIs. Expose these through ISG (Integrated SOA Gateway) as REST services after enabling the relevant ISG interface. For Fusion Cloud, equivalent REST APIs are available OOTB at `/fscmRestApi/resources/latest/purchaseOrders`, `/supplierPortal`, etc. — no custom development needed.

**416. How do you handle data transformation challenges when integrating EBS with a third-party system?**
Key challenges and solutions: (1) **Code mappings** — EBS uses internal lookup codes (e.g., `SHIPMENT_METHOD = 'AIR'`) while third-party uses different codes — use a transformation lookup table (`BNE_LOOKUPS` or a custom `XXGEA_CODE_MAP` table). (2) **Date/time zones** — EBS stores dates in the server timezone; third-party may use UTC — always convert explicitly. (3) **UOM differences** — EBS uses `EA` (Each) while third-party uses `PC` (Piece) — maintain a UOM cross-reference. (4) **Currency precision** — EBS rounds to 2 decimal places for some currencies; third-party may require 4. (5) **Character encoding** — EBS may use AL32UTF8 or WE8ISO8859P1; ensure Spring Boot reads/writes UTF-8 consistently for supplier names with special characters.

**417. How do you structure a Spring Boot service to handle EBS interface table inserts?**
Three-layer structure: (1) **REST Controller** — validates request, maps DTO, calls service. (2) **EBS Integration Service** — contains business logic: generate sequence values, map to interface table columns, call DAO. Annotated `@Transactional` with rollback on any failure. (3) **EBS Interface DAO** (Data Access Object) — uses `JdbcTemplate` or `NamedParameterJdbcTemplate` for direct Oracle JDBC inserts into interface tables. Example:
```java
@Repository
public class RcvInterfaceDao {
  @Autowired private NamedParameterJdbcTemplate jdbc;

  public void insertHeader(RcvHeaderInterface hdr) {
    jdbc.update(
      "INSERT INTO rcv_headers_interface (header_interface_id, vendor_id, shipment_num, ...) " +
      "VALUES (:headerId, :vendorId, :shipmentNum, ...)",
      new BeanPropertySqlParameterSource(hdr));
  }
}
```
Use `NamedParameterJdbcTemplate` (not string concatenation) for SQL injection safety. Always call `COMMIT` via the transaction boundary or explicitly after the interface inserts.

**418. What is Oracle EBS Integrated SOA Gateway (ISG) and how does it work?**
ISG (also called Oracle Application Server Integration) exposes EBS IREP-registered APIs as web services (SOAP or REST) without custom code. Configuration: (1) Grant the service from IREP. (2) Deploy the service via ISG Administration in EBS. (3) The service becomes available at a URL like `http://host:port/webservices/SOAProvider/plsql/po_document_update_grp/`. ISG handles authentication (HTTP Basic or WS-Security), translates the SOAP/REST request into an EBS PL/SQL call, and returns the response. At TCS, ISG-exposed services for PO status queries eliminated the need for a Spring Boot middleware layer for simple read operations.

**419. How do you test a REST API integration end-to-end in an EBS environment?**
(1) **Unit test:** mock the EBS JDBC call with H2 or Mockito — test transformation logic independently. (2) **Integration test:** connect to a DEV EBS instance; POST a test ASN payload and verify the row appears in `RCV_HEADERS_INTERFACE` and `RCV_TRANSACTIONS_INTERFACE`. (3) **End-to-end test:** trigger the Receiving Transaction Processor and verify the ASN appears in `RCV_SHIPMENT_HEADERS`. (4) **Negative testing:** send invalid payloads (null vendor_id, closed PO, exceeded quantity) and verify the correct error codes are returned. (5) **Performance test:** JMeter or Gatling with 50 concurrent ASN submissions to validate throughput. Use Postman collections for DEV smoke testing and share them with the team as living documentation.

**420. How do you implement retry with exponential backoff in a Spring Boot EBS integration?**
```java
@Retryable(value = {EbsConnectionException.class},
           maxAttempts = 3,
           backoff = @Backoff(delay = 2000, multiplier = 2.0))
public String submitAsn(AsnRequest request) {
  return ebsGateway.postToInterface(request);
}

@Recover
public String asnFallback(EbsConnectionException e, AsnRequest request) {
  log.error("ASN submission failed after retries: {}", request.getPackingSlip(), e);
  deadLetterService.enqueue(request);  // save for manual review
  throw new IntegrationException("EBS unavailable - ASN queued for retry", e);
}
```
Use Spring Retry (`@Retryable`). The dead-letter queue (backed by a DB table) ensures no submissions are lost — operations staff can reprocess after EBS recovery. Always log the correlation ID (packing slip, PO number) with every retry attempt.

**421. What is the difference between push and pull integration patterns with EBS?**
**Push (EBS initiates):** EBS fires a Business Event or a scheduled concurrent program that calls the external system. Latency = trigger interval (could be real-time via Business Events or batch via CP schedule). Examples: EBS sends new PO to a 3PL, EBS pushes receipt confirmation to a supplier's order management system. **Pull (external initiates):** the external system polls EBS REST/SOAP endpoints for new data. Latency = polling interval. Examples: a supplier's ERP polls EBS every 15 minutes for new POs; a 3PL pulls shipping instructions hourly. Push is more real-time but requires EBS to know the external endpoint. Pull is simpler to implement from the EBS side but less responsive. Most production integrations use a hybrid: push for critical events (PO created, invoice paid), pull for bulk data synchronization.

**422. How would you secure sensitive supplier data in a REST API payload?**
(1) **Transport security:** TLS 1.2+ mandatory for all API calls — no HTTP. (2) **Authentication:** OAuth 2.0 client credentials for machine-to-machine; API keys for simpler cases — store in Vault, not config files. (3) **Authorization:** use OAuth scopes to restrict what each client can access (`po:read`, `asn:write` — a 3PL should not see invoice data). (4) **Data minimization:** only include fields the consumer needs — never return bank account details unless explicitly required and the consumer is authorized. (5) **Field-level encryption:** for PII (email, address), encrypt fields before storage in staging tables using Oracle TDE or application-level AES-256. (6) **Audit logging:** log every API call with caller identity, timestamp, and data accessed — not the payload itself.

**423. How do you implement a WebHook for real-time ASN status updates from EBS to a third-party system?**
EBS does not natively support outbound webhooks, but you can build them: (1) Subscribe to the `oracle.apps.rcv.asn.create` Business Event in Oracle Workflow. (2) The event subscription calls a PL/SQL procedure that reads shipment details and calls `UTL_HTTP.REQUEST_PIECES` to POST a JSON payload to the external webhook URL. (3) Handle HTTP errors (timeouts, non-2xx responses) with retry logic in the PL/SQL. (4) For a more robust approach: the Business Event writes to a `XXGEA_WEBHOOK_QUEUE` table, and a Spring Boot poller reads and delivers events asynchronously with proper retry/dead-letter handling. The DB-backed queue ensures no events are lost if the external system is temporarily unavailable.

**424. What logging and monitoring strategy did you use for the TCS REST/SOAP integrations?**
Three logging levels: (1) **Request/response logging** — log every inbound request (HTTP method, URL, caller identity) and outbound call (URL, status code, duration) using Spring `HandlerInterceptor` and `ClientHttpRequestInterceptor`. Mask sensitive fields (passwords, bank numbers) before logging. (2) **Business event logging** — log the business outcome (ASN submitted successfully for PO #XXXXX, shipment_header_id = YYYYY) to a structured log (JSON) consumed by ELK or Splunk. (3) **Error logging** — every exception logged with stack trace, request payload (sanitized), and correlation ID. Metrics: request count, error rate, p95 latency tracked via Spring Boot Actuator → Prometheus → Grafana. Alert on error rate > 5% or p95 > 2 seconds.

**425. What is Spring Boot Actuator and how would you use it in an EBS integration service?**
Spring Boot Actuator exposes production-ready endpoints: `/actuator/health` (UP/DOWN with DB connectivity check), `/actuator/metrics` (JVM, HTTP, custom meters), `/actuator/info` (build version, git commit), `/actuator/env` (configuration). Secure all Actuator endpoints with Spring Security — never expose them publicly. Add a custom health indicator to check EBS connectivity: ping `fnd_concurrent_requests` with a simple `SELECT 1`. Expose custom metrics via `MeterRegistry`: count of successful/failed ASN submissions, processing latency histograms. Integrate with Prometheus and Grafana for real-time dashboards — in the GE project, this provided the operations team a live view of integration health alongside the EBS concurrent program status.

**426. What is Oracle EBS Business Event System and how did you use it?**
The Business Event System (part of Oracle Workflow) lets you publish and subscribe to named events (`oracle.apps.po.document.approve`, `oracle.apps.rcv.asn.create`, etc.) when specific EBS actions occur. Subscribe via `WF_EVENT.SUBSCRIBE` or via System Administration → Workflow → Business Events → Subscriptions. The subscription can call a PL/SQL agent procedure, a Java agent, or an Oracle Advanced Queuing (AQ) agent. At TCS, I subscribed to the PO Approval event to trigger downstream ERP synchronization — avoiding polling and providing real-time updates to the third-party system within seconds of PO approval.

**427. How do you handle the case where an EBS integration times out and the EBS processing was actually successful?**
This is the classic "at-least-once delivery" problem. Solution: implement idempotency with a status-check endpoint. When the caller times out: (1) Wait a safe interval (e.g., 30 seconds). (2) Call a GET endpoint with the `idempotency_key` to check status. (3) If status = 'SUCCESS', use the returned result without resubmitting. (4) If status = 'IN_PROGRESS', wait and retry the GET. (5) Only resubmit if the status is 'NOT_FOUND' (the original request never arrived). This approach requires the idempotency key to be persisted server-side. Combined with the idempotency check on POST, you avoid duplicate ASNs even under network failure scenarios.

**428. What is your approach to API versioning for EBS integrations?**
Use URI versioning (`/api/v1/asn`, `/api/v2/asn`) for major breaking changes. Minor/additive changes (new optional fields) don't require a version bump — all existing clients continue working. Maintain v1 alongside v2 for a transition period (communicate deprecation timeline to consumers). In practice, EBS integrations rarely need major API version changes unless the underlying EBS data model changes (e.g., migration from EBS to Fusion). Document the API with OpenAPI/Swagger (`springdoc-openapi`) and share the spec with consumers via an API portal. At TCS, we version-tagged APIs with the EBS release they were built against (`v2024.1`) for easier troubleshooting when behavior changed after a patch.

**429. How do you design a bulk REST API to update 1000 promise dates from an external system?**
Accept an array of update requests in a single POST body:
```json
{ "updates": [
  { "po_number": "PO-001", "shipment_num": 1, "new_promise_date": "2026-06-15" },
  ...
]}
```
Process in a single EBS session: (1) Validate all records first (one DB round-trip per batch, not per record). (2) Call `PO_DOCUMENT_UPDATE_GRP.update_document` in a loop, collecting errors per record. (3) Return a batch response: `{ "succeeded": 990, "failed": 10, "errors": [...] }`. Cap batch size at 500 records per call to prevent timeout. Clients with 1000+ updates split into two calls. This approach avoids 1000 HTTP round-trips and instead uses 2-3 calls, reducing latency by 99%.

**430. Describe your Spring Boot component architecture for EBS integration — layers and patterns.**
**Layer 1 — API Layer:** REST controllers, request/response DTOs, Bean Validation, Swagger docs. **Layer 2 — Service Layer:** business logic, orchestration between multiple EBS calls, transaction management (`@Transactional`), retry (`@Retryable`). **Layer 3 — EBS Adapter Layer:** EBS-specific integration (interface table DAO, IREP service clients, FND_REQUEST calls via JDBC). **Layer 4 — Infrastructure:** JDBC connection pool (HikariCP), Spring Retry, Resilience4j circuit breaker, Spring Boot Actuator health/metrics, Logback with JSON appender. **Cross-cutting:** Correlation ID propagation (MDC), security (Spring Security + OAuth2 or Basic Auth), error handling (`@ControllerAdvice` with standard error response structure). This was the architecture used for TCS supply-chain integrations — each layer independently testable, loosely coupled.

---

# Section V — Oracle Forms, Concurrent Programs & AOL Advanced (Q431–Q455)

**431. What is Oracle Forms in EBS and how does it differ from OAF?**
Oracle Forms is a client-server (then web-deployed via Forms Services) UI technology used in older EBS modules — Purchasing, Payables, General Ledger, Inventory. Forms (.fmb source, .fmx compiled) run via the Oracle Forms Servlet in a Java plugin or native Forms client. OAF (Oracle Application Framework) is the modern Java/J2EE web-based framework for self-service pages (iSupplier, iProcurement, iBenefits). Key differences: Forms uses `WHEN-*` triggers for logic; OAF uses Java controllers. Forms personalizations use the Forms Personalization engine (stored in `FND_FORM_CUSTOM_RULES`); OAF uses MDS-based personalizations. In EBS R12, procurement/purchasing transactions still use Forms (PO Entry screen) while self-service (iSupplier) uses OAF.

**432. What are the key trigger types in Oracle Forms and when does each fire?**
**WHEN-NEW-FORM-INSTANCE:** fires once when the form opens — use for initialization, setting globals, defaulting values. **WHEN-NEW-BLOCK-INSTANCE:** fires when focus moves to a block — use for block-level initialization. **WHEN-NEW-RECORD-INSTANCE:** fires for each new record — use for record-level defaults. **WHEN-NEW-ITEM-INSTANCE:** fires when an item gets focus — use for field-level behavior. **WHEN-VALIDATE-ITEM:** fires after leaving a field — use for field validation. **WHEN-VALIDATE-RECORD:** fires when the record is validated — use for cross-field validation. **ON-INSERT/ON-UPDATE/ON-DELETE:** fires on DML — use to intercept and customize database operations. **KEY-NEXT-ITEM, KEY-DUPREC, KEY-COMMIT:** fires on key press — use for keyboard customization. **PRE-INSERT/POST-INSERT:** fires before/after the actual INSERT — use for pre/post DML logic.

**433. What is the CUSTOM library in Oracle Forms and how is it used for EBS customizations?**
`CUSTOM.pll` (compiled to `CUSTOM.plx`) is Oracle's provided hook for Forms customizations in EBS — it is loaded into every form automatically. Rather than modifying Oracle's standard `.fmb` files (which would be overwritten by patches), you add your customization code to `CUSTOM.pll`'s `CUSTOM.Event` procedure. The event procedure receives the form name, block name, and event name — you add `IF form_name = 'POXPOEPO' AND event_name = 'WHEN-VALIDATE-ITEM' THEN ... END IF;` to target specific forms and triggers. This approach survives patches because you only maintain `CUSTOM.pll`, not Oracle's source files. Limitation: `CUSTOM.pll` is shared — poorly written code affects all forms.

**434. What is Forms Personalization in EBS and how does it differ from CUSTOM.pll?**
Forms Personalization (`FND_FORM_CUSTOM_RULES`) is a declarative framework — configure via Help → Customize from any form screen. You define rules with conditions (form/block/field values) and actions (set property, message, go_block, etc.) without writing PL/SQL. It is the preferred method for simple UI customizations (hiding fields, defaulting values, restricting navigation) because it is stored in the database, migrated with FNDLOAD, and does not affect patching. `CUSTOM.pll` is for complex programmatic logic that Forms Personalization cannot handle (complex calculations, calling external procedures, dynamic SQL). Both layers can coexist — Forms Personalization fires before CUSTOM triggers.

**435. How do you add a custom button to an Oracle Forms screen in EBS?**
In the form source (`.fmb` in JDeveloper Forms Builder or Oracle Forms Developer): add a button item to the desired block/canvas. In the `WHEN-BUTTON-PRESSED` trigger, add your logic (call a PL/SQL package, open a window, navigate). Compile to `.fmx` and deploy to `$PROD_TOP/forms/US/` (or the language-specific directory). Since modifying Oracle `.fmb` files directly is patching-unfriendly, use Forms Personalization to add UI changes declaratively, or use `CUSTOM.pll` to intercept `WHEN-BUTTON-PRESSED` on an existing button and augment its behavior. For a truly new button (not possible via personalization), there is no patch-safe way — it requires a copy-and-modify approach tracked as a CEMLI Modification.

**436. What are the executable method types for concurrent programs and when do you use each?**
**PL/SQL Stored Procedure:** for programs implemented as PL/SQL packages — most common for business logic. **SQL*Plus:** runs a SQL*Plus script — legacy, rarely used for new programs. **SQL*Loader:** loads flat files into interface tables — for data migration. **Host (Shell):** runs an OS script — for file manipulation, ETL, calling external tools. **Oracle Reports:** runs a `.rdf` report — for older Oracle Reports-based reports. **Java Concurrent Program:** a Java class implementing `CpContext` interface — for Java-based processing. **Spawned:** the program spawns a subprocess — used when the program forks other processes. **Request Set Stage Function:** used within request sets to determine conditional execution. At GE: PL/SQL for all business logic and data processing; Oracle Reports for legacy; Java for the Spring Boot-integrated batch jobs.

**437. How do you create a concurrent program with table-validated value set parameters?**
(1) Create the Value Set: System Admin → Application → Validation → Set. Type = `Table`, Application Table = `AP_SUPPLIERS`, Value Column = `VENDOR_NAME`, ID Column = `VENDOR_ID`, Where Clause = `enabled_flag = 'Y'`. (2) Create the Concurrent Program parameter: Application → Concurrent → Program → Parameters. Set the Value Set to your new set, data type = Character (for value) or Number (for id). The parameter will show a LOV in the Submit Request form. The concurrent program procedure receives `p_vendor_id IN VARCHAR2` — even number parameters come as VARCHAR2; cast with `TO_NUMBER(p_vendor_id)`. Set `p_vendor_id` as IN parameter #1 (after errbuf/retcode).

**438. What is the difference between a standard concurrent program and a spawned program?**
A **standard** concurrent program runs directly in the concurrent manager worker process. A **spawned** program's executable type is `Spawned` — the concurrent manager launches an OS-level child process (a separate JVM, a Perl script, a C binary). Spawned programs can use more memory and different runtime environments than the CM worker allows. They are commonly used for Java-based concurrent programs and some Oracle Reports programs. The spawned process runs independently and reports completion status back to the CM via exit codes. Standard programs are simpler but share the CM process memory limits.

**439. What are the key FNDLOAD LCT files for common EBS object types?**
`$FND_TOP/patch/115/import/afcpprog.lct` — Concurrent Programs, Executables, Request Groups. `$FND_TOP/patch/115/import/afmdmsg.lct` — FND Messages. `$FND_TOP/patch/115/import/afffload.lct` — Flexfields. `$FND_TOP/patch/115/import/afscprof.lct` — Profile Options and Values. `$FND_TOP/patch/115/import/afsload.lct` — Responsibilities, Menus, Functions. `$FND_TOP/patch/115/import/aflvmlu.lct` — Lookups. `$FND_TOP/patch/115/import/wfload.lct` — Workflow item types, processes. Usage: `FNDLOAD apps/pwd@db 0 Y DOWNLOAD $FND_TOP/patch/115/import/afcpprog.lct cp.ldt PROGRAM APPLICATION_SHORT_NAME="XX" CONCURRENT_PROGRAM_NAME="XXGEA%"`.

**440. How do you migrate a custom concurrent program from DEV to PROD using FNDLOAD?**
```bash
# In DEV - Download
FNDLOAD apps/appsdev@devdb 0 Y DOWNLOAD \
  $FND_TOP/patch/115/import/afcpprog.lct \
  XXGEA_ASN_COMPLIANCE.ldt \
  PROGRAM APPLICATION_SHORT_NAME="XX" \
  CONCURRENT_PROGRAM_NAME="XXGEA_ASN_COMPLIANCE"

# In PROD - Upload (within CTASK)
FNDLOAD apps/appsprod@proddb 0 Y UPLOAD \
  $FND_TOP/patch/115/import/afcpprog.lct \
  XXGEA_ASN_COMPLIANCE.ldt
```
The `.ldt` file is a portable ASCII file — commit it to Git for version control. Always FNDLOAD the executable first (separate `.ldt`), then the program, then add to the request group. Verify in PROD: `SELECT * FROM fnd_concurrent_programs_tl WHERE concurrent_program_name='XXGEA_ASN_COMPLIANCE'`.

**441. What is a Value Set of type "Dependent" and when do you use it?**
A Dependent value set's valid values depend on the value entered in an "Independent" value set (its parent). Example: Country (Independent) → State (Dependent — only states for the selected country appear). The dependent VS references the independent VS and the parent value filters which child values are active. Used in DFFs and concurrent program parameters where a second parameter's LOV should be filtered by the first. Limitation: the dependent relationship is one level only (no chaining of dependencies like grandchild), and both parent and child must be on the same DFF context.

**442. What is FND_MESSAGES and how do you add a custom message for OAF validation?**
`FND_NEW_MESSAGES` (the actual table; `FND_MESSAGES` is the view) stores application messages used throughout EBS for notifications, errors, and UI text. To add a custom message: Application → Messages → New. Enter Application Short Name (`XX`), Message Name (`XXGEA_PROMISE_DATE_REQUIRED`), Message Text (`Promise Date is required. Enter N/A with a reason if the date is not available.`), Type (`Error`/`Warning`/`Information`). In OAF: `throw new OAException("XX", "XXGEA_PROMISE_DATE_REQUIRED", null, OAException.ERROR, null)`. Migrate via FNDLOAD with `afmdmsg.lct`. Messages are translatable — add translations via the Messages form's Language LOV.

**443. How do you use APP_EXCEPTION and FND_MESSAGE packages in EBS PL/SQL?**
```sql
-- Set a message with token substitution
FND_MESSAGE.SET_NAME('XX', 'XXGEA_ASN_QTY_EXCEEDS');
FND_MESSAGE.SET_TOKEN('ITEM_NUM', p_item_number);
FND_MESSAGE.SET_TOKEN('MAX_QTY', TO_CHAR(p_max_qty));
APP_EXCEPTION.RAISE_EXCEPTION;  -- raises ORA-20001 with the formatted message
```
`FND_MESSAGE.SET_NAME` prepares the message; `SET_TOKEN` substitutes `&ITEM_NUM` and `&MAX_QTY` placeholders. `APP_EXCEPTION.RAISE_EXCEPTION` raises `ORA-20001` with the formatted text. In OAF AM methods, you can also use `throw new OAException(FND_MESSAGE.RETRIEVE_EXCEPTION())` after calling the PL/SQL procedure to surface the message in the UI.

**444. What is the difference between FND_PROFILE.VALUE and FND_PROFILE.GET?**
`FND_PROFILE.VALUE('PROFILE_NAME')` returns the profile value as VARCHAR2 at the highest applicable level for the current session (no session initialization needed if called within a concurrent program or form context). `FND_PROFILE.GET('PROFILE_NAME', l_variable)` is the older procedure syntax — it sets the `l_variable` OUT parameter. Both read the same data; `VALUE` is the preferred modern function form. For PL/SQL APIs that need to set the profile level explicitly: `FND_PROFILE.VALUE_SPECIFIC('PROFILE_NAME', user_id, resp_id, appl_id)` reads at a specific level. Never use `FND_PROFILE.VALUE` in a bulk loop — call once and cache the result in a local variable.

**445. How do you create a new menu function in AOL and assign it to a responsibility?**
(1) **Create Function:** System Admin → Security → Function. Name = `XXGEA_SURROGATE_SRCH`, User Function Name = `iSupplier Surrogate Search`, Type = `SSWA jsp page`, HTML Parameters = `OAFunc=XXGEA_SURROGATE_SRCH&retainAM=Y&page=/oracle/apps/xx/isupplier/webui/SurrogateSrchPG`. (2) **Add to Menu:** Security → Menu → Query the iSupplier buyer menu → Add a new entry with the new function. (3) **Assign Menu to Responsibility:** or use the existing iSupplier buyer responsibility whose menu already includes the parent menu. (4) **Test:** log in as a buyer, navigate the menu — the new function should appear.

**446. What is FNDLOAD vs AFLOAD and when do you use each?**
`FNDLOAD` is Oracle's generic loader for AOL objects using a `.lct` (control file) + `.ldt` (data file) paradigm — it handles most EBS setup objects (programs, messages, lookups, profiles, menus, responsibilities, flexfields). `AFLOAD` is an older, deprecated loader that handled some objects FNDLOAD doesn't cover in old releases — in R12 it's rarely needed. For WebADI objects, use the `BNELOAD` utility. For workflow objects, use `WFLOAD` (same syntax as FNDLOAD but with `$WF_TOP` LCT files). For OAF substitutions, use `jpximport`/`jpxexport`. Always check the specific object type's documentation for the correct loader and LCT file.

**447. What is the Apps Initialization procedure and when must you call it in PL/SQL?**
`FND_GLOBAL.APPS_INITIALIZE(user_id, resp_id, resp_appl_id)` sets up the EBS session context in a database session — it populates `FND_GLOBAL` values (user, responsibility, org_id via MOAC), initializes the FND message stack, and sets NLS parameters. Must be called: (1) In any PL/SQL that calls EBS standard APIs when the session was not initialized via the EBS application (e.g., from SQL Developer, a JDBC connection, a shell script, or a standalone Java program). (2) In concurrent programs (done automatically by the CM worker, but if your program spawns a new DB session, you must reinitialize). Without it, `FND_GLOBAL.USER_ID` returns -1, profile values return null, and standard APIs fail with unhelpful errors.

**448. How do you trace a "You have no access to this function" error for an iSupplier user?**
This is a function security check failure. Trace: (1) Identify the function name from the URL (`OAFunc=ICX_PO_ASN_CREATE` for ASN creation). (2) Check `fnd_form_functions` for the function: `SELECT * FROM fnd_form_functions WHERE function_name = 'ICX_PO_ASN_CREATE'`. (3) Check if the function is on the user's responsibility menu: `SELECT * FROM fnd_menu_entries WHERE function_id = (SELECT function_id FROM fnd_form_functions WHERE function_name = 'ICX_PO_ASN_CREATE')`. (4) Verify the menu tree up to the responsibility's root menu includes this function. (5) Check for function security exclusions: `SELECT * FROM fnd_resp_functions WHERE responsibility_id = :resp_id` — exclusions at the responsibility level can override menu assignments. Fix: add the function to the appropriate menu or remove the exclusion.

**449. What is a Request Set and how do you use it to chain concurrent programs at GE?**
A Request Set groups multiple concurrent programs to run in sequence or in parallel as a single submission unit. At GE: created a request set `XXGEA_ASN_EOD_PROCESS` with 3 stages: (1) `XXGEA_ASN_COMPLIANCE` (data validation — must succeed before stage 2). (2) `XXGEA_ASN_REPORT` (generate compliance report — runs in parallel with stage 3). (3) `XXGEA_SUPPLIER_EXPORT` (supplier data export). Define via: Application → Concurrent → Sets. Each stage has a completion status check — if stage 1 fails, subsequent stages are skipped. The request set is added to a request group and scheduled via a request set submission — users submit one item instead of 3.

**450. How do you register a custom Oracle EBS table with AOL (grants and synonyms)?**
```sql
-- In custom schema (e.g., XXGEA):
CREATE TABLE xxgea_notif_rules (...);

-- In APPS schema (run as APPS user):
GRANT SELECT, INSERT, UPDATE, DELETE ON xxgea.xxgea_notif_rules TO apps;
CREATE SYNONYM apps.xxgea_notif_rules FOR xxgea.xxgea_notif_rules;

-- Register with AD_DD for patch utilities to know the table:
EXEC AD_DD.REGISTER_TABLE('XX', 'XXGEA_NOTIF_RULES', 'T');
EXEC AD_DD.REGISTER_COLUMN('XX', 'XXGEA_NOTIF_RULES', 'RULE_ID', 1, 'NUMBER', 'N');
-- ... repeat for each column
```
`AD_DD.REGISTER_TABLE` and `AD_DD.REGISTER_COLUMN` populate `FND_TABLES` and `FND_COLUMNS` so that table-validated value sets, flexfields, and FNDLOAD can reference the table. Always create the synonym in APPS so code connecting as APPS can access `XXGEA_NOTIF_RULES` without schema prefix.

**451. What is a Descriptive Flexfield (DFF) and how do you configure one for a custom attribute?**
A DFF adds custom attributes to standard Oracle screens/tables using ATTRIBUTE1–ATTRIBUTE30 columns. Configuration: Application → Flexfield → Descriptive → Register (if custom table) or query (for standard table like `PO_HEADERS_ALL`). Define a context (global or context-sensitive). For each context, define segments mapped to ATTRIBUTE columns, with optional value sets for validation. Enable the flexfield. Freeze and compile. The DFF appears as a `[...]` button on the form. At GE, a DFF on `PO_HEADERS_ALL` captured the GE-specific "Program Code" attribute for defense contract categorization — stored in `PO_HEADERS_ALL.ATTRIBUTE1`, surfaced in PO Entry via the standard DFF mechanism.

**452. How do you define a concurrent program with a date range parameter and use it in the query?**
Define two parameters in the concurrent program: `P_DATE_FROM` (format mask `DD-MON-YYYY`, validation type=None) and `P_DATE_TO`. In the PL/SQL procedure, receive them as `VARCHAR2` and convert: `l_from := TO_DATE(p_date_from, 'DD-MON-YYYY')`. Use `FND_DATE.CANONICAL_TO_DATE` for more robust conversion that handles the NLS calendar. In the query: `WHERE ph.creation_date BETWEEN l_from AND l_to + 1 - 1/86400` (add 1 day minus 1 second to make `p_date_to` inclusive through end of day). Always validate that `p_date_from <= p_date_to` and raise `APP_EXCEPTION` if not.

**453. What is FND_REQUEST.SUBMIT_REQUEST and what are its key parameters?**
```sql
l_req_id := FND_REQUEST.SUBMIT_REQUEST(
  application  => 'XX',       -- app short name
  program      => 'XXGEA_ASN_COMPLIANCE',  -- program short name
  description  => 'ASN Compliance - GEA',  -- optional description for log
  start_time   => TO_CHAR(SYSDATE + 1/24, 'DD-MON-YYYY HH24:MI:SS'),  -- 1 hr from now
  sub_request  => FALSE,       -- TRUE if called from within another CP
  argument1    => TO_CHAR(p_org_id),
  argument2    => TO_CHAR(SYSDATE,'YYYY/MM/DD'),
  argument3    => NULL         -- up to 100 arguments
);
COMMIT;  -- mandatory to register the request
```
`sub_request = TRUE` is used when one concurrent program submits child requests — the parent waits for children. Arguments are always VARCHAR2; cast in the receiving procedure. The returned `request_id = 0` indicates failure — check `FND_MESSAGE.GET_ENCODED` for the error.

**454. How do you set up a Value Set for a concurrent program parameter that restricts to active vendors?**
Value Set type = `Table`. Application = `Payables`. Table = `AP_SUPPLIERS`. Value Column = `VENDOR_NAME`. ID Column = `VENDOR_ID`. Where Clause = `ENABLED_FLAG='Y' AND (END_DATE_ACTIVE IS NULL OR END_DATE_ACTIVE > SYSDATE)`. Order By = `VENDOR_NAME`. In the CP parameter: data type = Character, Value Set = above, Token = `VENDOR_ID` (uses ID column as the actual value passed). Result: a user running the CP gets an LOV of active vendor names, but the program receives the `VENDOR_ID` number. This was the approach for all GE report parameters that required supplier selection.

**455. How do you troubleshoot "ORA-20001: APP-FND-01564: ORACLE error 1403 in fdflvc" in a DFF?**
`ORA-1403` is `NO_DATA_FOUND`. In the DFF context: `fdflvc` is the FND flexfield validation C routine. This error means the DFF's value set table query returned no rows for the value the user entered. Steps: (1) Find the DFF and the specific segment causing the error — the `fdflvc` error context includes the flexfield code and context. (2) Query the value set's validation table directly with the same WHERE clause and the entered value — does it return a row? (3) Check `org_id` or other bind variables in the Where Clause — if the session org_id is wrong, the LOV may return nothing. (4) Check if the data was recently inactivated (the value existed before but the record was end-dated). Fix by correcting the value set WHERE clause or the data.

---
"""

with open(OUT, 'a', encoding='utf-8') as f:
    f.write(CONTENT)

print(f"Appended Section S remainder + Sections T, U, V (Q355-Q455)")
print(f"File size: {OUT.stat().st_size // 1024} KB")
