#!/usr/bin/env python3
"""Appends Sections P & Q (Q201-Q285) to the interview prep markdown."""
from pathlib import Path

OUT = Path("/Users/himanshu/Desktop/Job/Job Preparation/Interview_Prep_200_QA.md")

CONTENT = """

---

# Section P — SQL Deep Dive: EBS Procurement & iSupplier Queries (Q201–Q240)

**201. Write a SQL to list all open Standard POs for a supplier with shipment details.**
```sql
SELECT ph.segment1 po_number, ph.revision_num,
       pv.vendor_name, pvs.vendor_site_code,
       pl.line_num, pl.item_description, pl.unit_price,
       pll.shipment_num, pll.quantity ordered_qty,
       NVL(pll.quantity_received,0) received_qty,
       pll.quantity - NVL(pll.quantity_received,0) open_qty,
       pll.need_by_date, pll.promised_date
  FROM po_headers_all     ph
  JOIN po_lines_all        pl  ON pl.po_header_id     = ph.po_header_id
  JOIN po_line_locations_all pll ON pll.po_line_id    = pl.po_line_id
  JOIN ap_suppliers         pv  ON pv.vendor_id       = ph.vendor_id
  JOIN ap_supplier_sites_all pvs ON pvs.vendor_site_id = ph.vendor_site_id
 WHERE ph.type_lookup_code      = 'STANDARD'
   AND ph.authorization_status  = 'APPROVED'
   AND pll.closed_code NOT IN ('CLOSED','FINALLY CLOSED')
   AND pll.quantity - NVL(pll.quantity_received,0) > 0
   AND pv.vendor_id = :p_vendor_id
 ORDER BY ph.segment1, pl.line_num;
```
Always filter `closed_code NOT IN ('CLOSED','FINALLY CLOSED')` — shipments in 'FINALLY CLOSED' have completed AP matching and should not appear in open-order views. Add `pll.org_id = mo_global.get_current_org_id()` for MOAC-correct results. This query backed the GE iSupplier "Open Orders" supplier-facing screen.

**202. How do you query PO lines where Promise Date is NULL or equals Need-by Date?**
```sql
SELECT ph.segment1, pl.line_num, pll.shipment_num,
       pv.vendor_name, pll.need_by_date, pll.promised_date,
       CASE WHEN pll.promised_date IS NULL THEN 'NO PROMISE'
            ELSE 'DEFAULTED' END issue_type
  FROM po_headers_all ph
  JOIN po_lines_all pl ON pl.po_header_id = ph.po_header_id
  JOIN po_line_locations_all pll ON pll.po_line_id = pl.po_line_id
  JOIN ap_suppliers pv ON pv.vendor_id = ph.vendor_id
 WHERE ph.authorization_status = 'APPROVED'
   AND (pll.promised_date IS NULL
        OR TRUNC(pll.promised_date) = TRUNC(pll.need_by_date))
   AND pll.closed_code NOT IN ('CLOSED','FINALLY CLOSED');
```
This was the exact diagnostic query run on the GE project to quantify the Promise Date defaulting problem before the fix. A high count of `promised_date = need_by_date` after acknowledgement meant the standard code was silently copying Need-by into Promise Date, making OTD measurement meaningless.

**203. Write a SQL to get ASN header and line details for a specific shipment number.**
```sql
SELECT rsh.shipment_num, rsh.shipped_date, rsh.expected_receipt_date,
       rsh.waybill_airbill_num, rsh.packing_slip, rsh.freight_carrier_code,
       rsl.line_num, rsl.item_description, rsl.quantity_shipped,
       rsl.quantity_received, rsl.shipment_line_status_code,
       ph.segment1 po_number, pll.shipment_num po_shipment_num,
       pv.vendor_name
  FROM rcv_shipment_headers rsh
  JOIN rcv_shipment_lines rsl  ON rsl.shipment_header_id  = rsh.shipment_header_id
  JOIN po_line_locations_all pll ON pll.line_location_id  = rsl.po_line_location_id
  JOIN po_lines_all pl         ON pl.po_line_id           = pll.po_line_id
  JOIN po_headers_all ph       ON ph.po_header_id         = pl.po_header_id
  JOIN ap_suppliers pv         ON pv.vendor_id            = ph.vendor_id
 WHERE rsh.shipment_num = :p_shipment_num
   AND rsh.receipt_source_code = 'VENDOR';
```
`receipt_source_code = 'VENDOR'` isolates supplier ASNs from internal transfers. `shipment_line_status_code = 'EXPECTED'` means in-transit. The `waybill_airbill_num` and `packing_slip` in `rcv_shipment_headers` are the mandatory compliance fields enforced at GE for customs traceability.

**204. How do you join PO_HEADERS_ALL to AP_SUPPLIERS in R12?**
The join is `po_headers_all.vendor_id = ap_suppliers.vendor_id`. In R12, `PO_VENDORS` became a synonym/view over `AP_SUPPLIERS` and `PO_VENDOR_SITES_ALL` over `AP_SUPPLIER_SITES_ALL` — both work but always prefer `AP_SUPPLIERS` in new code. For sites: `po_headers_all.vendor_site_id = ap_supplier_sites_all.vendor_site_id AND ap_supplier_sites_all.org_id = :org_id`. Never join supplier sites without `org_id` — the same site code can exist across multiple Operating Units and you will get duplicates silently.

**205. Write a SQL to find suppliers who have not submitted an ASN in the last 30 days.**
```sql
SELECT pv.vendor_name, pvs.vendor_site_code, pvs.org_id
  FROM ap_suppliers pv
  JOIN ap_supplier_sites_all pvs ON pvs.vendor_id = pv.vendor_id
 WHERE pvs.purchasing_site_flag = 'Y'
   AND (pvs.inactive_date IS NULL OR pvs.inactive_date > SYSDATE)
   AND pv.vendor_id NOT IN (
         SELECT DISTINCT ph.vendor_id
           FROM rcv_shipment_headers rsh
           JOIN rcv_shipment_lines rsl ON rsl.shipment_header_id = rsh.shipment_header_id
           JOIN po_line_locations_all pll ON pll.line_location_id = rsl.po_line_location_id
           JOIN po_headers_all ph ON ph.po_header_id = pll.po_header_id
          WHERE rsh.receipt_source_code = 'VENDOR'
            AND rsh.creation_date >= SYSDATE - 30
       )
ORDER BY pv.vendor_name;
```
This hypercare query identified which suppliers were live but not transacting, so the team could proactively reach out for adoption support.

**206. What is the difference between PO_HEADERS_ALL and PO_HEADERS?**
`PO_HEADERS_ALL` is the base table holding rows for all Operating Units. `PO_HEADERS` is a view that adds `WHERE org_id = SYS_CONTEXT('multi_org','org_id')` to restrict to the current MOAC context. In custom packages and concurrent programs always use `_ALL` tables with an explicit `org_id` bind variable — relying on the view is fragile if the APPS session context is not correctly initialized. In OAF, the AM sets `mo_global` context before VO execution, so VOs can safely use either, but prefer `_ALL` plus explicit bind for clarity.

**207. Write a SQL to identify duplicate supplier sites across Operating Units.**
```sql
SELECT pv.vendor_name, pvs.vendor_site_code,
       COUNT(DISTINCT pvs.org_id) org_count,
       LISTAGG(pvs.org_id,', ') WITHIN GROUP (ORDER BY pvs.org_id) org_ids
  FROM ap_suppliers pv
  JOIN ap_supplier_sites_all pvs ON pvs.vendor_id = pv.vendor_id
 WHERE pvs.purchasing_site_flag = 'Y'
GROUP BY pv.vendor_name, pvs.vendor_site_code
HAVING COUNT(DISTINCT pvs.org_id) > 1
ORDER BY pv.vendor_name;
```
Useful during multi-site rollouts to verify which suppliers are mapped to multiple OUs. On GE's 5-site deployment this confirmed cross-site purchasing was correctly configured and no site was accidentally duplicated with conflicting settings.

**208. How do you query receiving transaction history for a specific PO line?**
```sql
SELECT rt.transaction_type, rt.transaction_date, rt.quantity,
       rt.unit_of_measure, rt.destination_type_code,
       rt.subinventory, rsh.shipment_num,
       rt.comments, rt.reason_id
  FROM rcv_transactions rt
  JOIN rcv_shipment_headers rsh ON rsh.shipment_header_id = rt.shipment_header_id
 WHERE rt.po_line_location_id = :p_line_location_id
 ORDER BY rt.transaction_date;
```
`TRANSACTION_TYPE` values: RECEIVE (dock receipt), DELIVER (to stock/destination), RETURN TO VENDOR, RETURN TO RECEIVING, CORRECT (quantity adjustment). Tracking the full sequence shows whether a shipment was received and then returned — critical for audit and supplier dispute resolution at GE.

**209. Write a SQL to calculate on-time delivery percentage per supplier.**
```sql
SELECT pv.vendor_name,
       COUNT(*)                                                              total_receipts,
       SUM(CASE WHEN TRUNC(rt.transaction_date) <= TRUNC(pll.promised_date)
                THEN 1 ELSE 0 END)                                          on_time,
       ROUND(SUM(CASE WHEN TRUNC(rt.transaction_date) <= TRUNC(pll.promised_date)
                      THEN 1 ELSE 0 END) / COUNT(*) * 100, 1)              otd_pct
  FROM rcv_transactions rt
  JOIN po_line_locations_all pll ON pll.line_location_id = rt.po_line_location_id
  JOIN po_headers_all ph         ON ph.po_header_id      = pll.po_header_id
  JOIN ap_suppliers pv           ON pv.vendor_id         = ph.vendor_id
 WHERE rt.transaction_type = 'RECEIVE'
   AND rt.transaction_date >= ADD_MONTHS(SYSDATE,-12)
   AND pll.promised_date IS NOT NULL
GROUP BY pv.vendor_name
ORDER BY otd_pct;
```
The critical filter `pll.promised_date IS NOT NULL` excludes lines where no commitment was made — measuring OTD against a blank or defaulted date is misleading, which is why making Promise Date mandatory was the key GE project change.

**210. How do you find POs in "Requires Acknowledgement" status that block ASN creation?**
```sql
SELECT ph.segment1 po_number, ph.revision_num, pv.vendor_name,
       pvs.vendor_site_code, ph.acceptance_due_date,
       NVL((SELECT 'Y' FROM po_acceptances pa
             WHERE pa.po_header_id = ph.po_header_id
               AND pa.revision_num = ph.revision_num
               AND pa.accepted_flag = 'Y'
               AND ROWNUM=1),'N') is_acknowledged
  FROM po_headers_all ph
  JOIN ap_suppliers pv ON pv.vendor_id = ph.vendor_id
  JOIN ap_supplier_sites_all pvs ON pvs.vendor_site_id = ph.vendor_site_id
 WHERE ph.authorization_status  = 'APPROVED'
   AND ph.acceptance_required_flag = 'Y'
   AND NVL((SELECT 'Y' FROM po_acceptances pa
             WHERE pa.po_header_id = ph.po_header_id
               AND pa.revision_num = ph.revision_num
               AND pa.accepted_flag = 'Y' AND ROWNUM=1),'N') = 'N'
ORDER BY ph.acceptance_due_date;
```
`PO_ACCEPTANCES` stores the supplier responses per revision. Check `revision_num` match — a new PO revision resets acknowledgement. This exact condition was used in the GE ASN eligibility engine to block ASN creation for unacknowledged POs.

**211. Write a SQL to get outstanding balance quantity per PO shipment.**
```sql
SELECT ph.segment1 po_number, pl.line_num, pll.shipment_num,
       pll.quantity                                                         ordered_qty,
       NVL(pll.quantity_received,0)                                        received_qty,
       NVL(pll.quantity_cancelled,0)                                       cancelled_qty,
       pll.quantity - NVL(pll.quantity_received,0)
                    - NVL(pll.quantity_cancelled,0)                        balance_qty,
       pll.need_by_date, pll.promised_date,
       hl.description ship_to_location
  FROM po_line_locations_all pll
  JOIN po_lines_all pl       ON pl.po_line_id         = pll.po_line_id
  JOIN po_headers_all ph     ON ph.po_header_id       = pl.po_header_id
  JOIN ap_suppliers pv       ON pv.vendor_id          = ph.vendor_id
  JOIN hr_locations_all hl   ON hl.location_id        = pll.ship_to_location_id
 WHERE ph.authorization_status = 'APPROVED'
   AND pll.closed_code NOT IN ('CLOSED','FINALLY CLOSED')
   AND pll.quantity - NVL(pll.quantity_received,0) - NVL(pll.quantity_cancelled,0) > 0
   AND ph.vendor_id = :p_vendor_id;
```
The "Balance Outstanding Qty" column added to the GE ASN creation screen was driven by exactly this formula. Suppliers needed real-time open quantity to avoid over-shipping.

**212. How do you find all BPA releases against a specific Blanket Purchase Agreement?**
```sql
SELECT ph.segment1 bpa_number, pr.release_num, pr.authorization_status,
       pr.creation_date, pr.approved_date, pr.release_type,
       pll.shipment_num, pll.quantity, pll.need_by_date, pll.ship_to_location_id
  FROM po_releases_all pr
  JOIN po_headers_all ph         ON ph.po_header_id  = pr.po_header_id
  JOIN po_line_locations_all pll ON pll.po_release_id = pr.po_release_id
  JOIN ap_suppliers pv           ON pv.vendor_id      = ph.vendor_id
 WHERE ph.segment1         = :p_bpa_number
   AND ph.type_lookup_code = 'BLANKET'
ORDER BY pr.release_num, pll.shipment_num;
```
`PO_RELEASES_ALL.po_release_id` is the key to join into `PO_LINE_LOCATIONS_ALL` for release shipments. The GE unit-price bug involved release shipments incorrectly pulling price from the BPA agreement line instead of the Standard PO, caught by comparing `pl.unit_price` vs `pll.price_override`.

**213. Write a SQL to list concurrent program requests that errored in the last 24 hours.**
```sql
SELECT fcr.request_id, fcp.user_concurrent_program_name,
       fcr.argument_text parameters,
       fcr.actual_start_date, fcr.actual_completion_date,
       fcr.phase_code, fcr.status_code,
       fu.user_name requested_by,
       fcr.logfile_name
  FROM fnd_concurrent_requests fcr
  JOIN fnd_concurrent_programs_tl fcp
    ON fcp.concurrent_program_id = fcr.concurrent_program_id
   AND fcp.language = 'US'
  JOIN fnd_user fu ON fu.user_id = fcr.requested_by
 WHERE fcr.status_code = 'E'
   AND fcr.actual_completion_date >= SYSDATE - 1
ORDER BY fcr.actual_completion_date DESC;
```
`status_code = 'E'` with `phase_code = 'C'` = Completed–Error. `logfile_name` gives the OS path under `$APPLCSF/log`. This was a standard hypercare morning-check query at GE to catch overnight batch failures before suppliers started submitting for the day.

**214. How do you query FND tables to find all OAF personalizations for an iSupplier page?**
```sql
SELECT jdr_utils.getDocumentName(d.path_docid) doc_path,
       d.name level_name,
       jdc.comp_type_name, jdc.att_name, jdc.att_value
  FROM jdr_paths d
  JOIN jdr_attributes jdc ON jdc.doc_id = d.path_docid
 WHERE jdr_utils.getDocumentName(d.path_docid) LIKE '/oracle/apps/icx/%'
   AND jdc.att_name IN ('rendered','readOnly','required','css')
ORDER BY d.path_docid, jdc.comp_seq;
```
The MDS repository tables `JDR_PATHS`, `JDR_COMPONENTS`, and `JDR_ATTRIBUTES` store personalization XML. Use `JDR_UTILS.listDocuments('/oracle/apps/icx/',TRUE)` to list all iSupplier pages with personalizations. This query was run before each DEV→UAT migration to audit which personalizations existed and needed to be exported.

**215. Write a SQL to find all suppliers registered as active iSupplier portal users.**
```sql
SELECT pv.vendor_name, pvs.vendor_site_code,
       fu.user_name, fu.email_address,
       fu.start_date user_from, fu.end_date user_to,
       frt.responsibility_name
  FROM ap_suppliers pv
  JOIN ap_supplier_sites_all pvs   ON pvs.vendor_id         = pv.vendor_id
  JOIN pos_supplier_users psu      ON psu.vendor_id         = pv.vendor_id
  JOIN fnd_user fu                 ON fu.user_id            = psu.user_id
  JOIN fnd_user_resp_groups_direct furg ON furg.user_id     = fu.user_id
  JOIN fnd_responsibility_tl frt   ON frt.responsibility_id = furg.responsibility_id
                                  AND frt.language          = 'US'
 WHERE frt.responsibility_name LIKE '%iSupplier%'
   AND (fu.end_date IS NULL OR fu.end_date > SYSDATE)
   AND (furg.end_date IS NULL OR furg.end_date > SYSDATE)
ORDER BY pv.vendor_name, fu.user_name;
```
`POS_SUPPLIER_USERS` is the iSupplier-specific bridge table linking FND users to their vendor/vendor-site. This audit query was run at each GE site go-live to confirm all 100+ supplier contacts had active accounts before cutover.

**216. How do you query workflow item activity status to debug a stuck PO approval?**
```sql
SELECT wias.item_type, wias.item_key, wias.process_name,
       wias.activity_name, wias.activity_status,
       wias.activity_result_code, wias.assigned_user,
       wias.begin_date, wias.error_name, wias.error_message
  FROM wf_item_activity_statuses wias
 WHERE wias.item_type = 'POAPPRV'
   AND wias.item_key  = TO_CHAR(:p_po_header_id)
   AND wias.activity_status IN ('ACTIVE','ERROR','NOTIFIED')
ORDER BY wias.begin_date DESC;
```
For iSupplier notification workflows use `item_type = 'PONOT'` or `'POSCHNG'`. `error_message` + `error_stack` in `WF_ITEM_ACTIVITY_STATUSES_H` (history table) gives the full Java or PL/SQL trace. When the GE planner notification workflow was stuck, this query pinpointed the activity and error in under two minutes without needing Workflow Builder.

**217. Write a SQL to identify PO receipts that exceeded over-receipt tolerance.**
```sql
SELECT ph.segment1, pl.line_num, pll.shipment_num,
       pll.quantity                                ordered_qty,
       pll.quantity_received                       received_qty,
       pll.qty_rcv_tolerance                       tolerance_pct,
       ROUND((pll.quantity_received/pll.quantity - 1)*100, 2) over_pct
  FROM po_line_locations_all pll
  JOIN po_lines_all pl ON pl.po_line_id = pll.po_line_id
  JOIN po_headers_all ph ON ph.po_header_id = pl.po_header_id
 WHERE pll.quantity_received > pll.quantity * (1 + NVL(pll.qty_rcv_tolerance,0)/100)
   AND pll.quantity_received IS NOT NULL
ORDER BY over_pct DESC;
```
`qty_rcv_tolerance` on the shipment holds the allowed over-receipt percentage (can default from item or receiving options). Used to validate the GE ASN eligibility engine — blocked ASNs for lines already at or near their receipt tolerance ceiling.

**218. How do you debug a BI Publisher report that produces blank output?**
First, run the concurrent program with output format set to XML and download the raw output file — this isolates whether the problem is data (empty XML) or template (bad RTF tags). If XML is empty, debug the underlying SQL/data template: check parameter binds, `org_id` context, and whether the query returns rows in SQL Developer with the same parameters. If XML has data but output is blank, open the RTF template in Word with the Template Builder add-in, load the XML as sample data, and preview locally — missing `for-each` tags or mismatched element names cause blank sections. Also check the template language/locale and that the template code matches the data definition code exactly.

**219. Write a SQL to get the complete P2P audit trail for an invoice.**
```sql
SELECT ai.invoice_num, ai.invoice_date, ai.invoice_amount,
       ph.segment1 po_number, pl.line_num, pll.shipment_num,
       rsh.shipment_num asn_number, rt.transaction_date receipt_date,
       rt.quantity received_qty, aid.amount dist_amount,
       gcc.concatenated_segments gl_account,
       aip.payment_date, aip.amount payment_amount
  FROM ap_invoices_all ai
  JOIN ap_invoice_distributions_all aid ON aid.invoice_id = ai.invoice_id
  JOIN po_distributions_all pd     ON pd.po_distribution_id = aid.po_distribution_id
  JOIN po_line_locations_all pll   ON pll.line_location_id  = pd.line_location_id
  JOIN po_lines_all pl             ON pl.po_line_id         = pll.po_line_id
  JOIN po_headers_all ph           ON ph.po_header_id       = pl.po_header_id
  JOIN rcv_transactions rt         ON rt.po_line_location_id= pll.line_location_id
                                  AND rt.transaction_type   = 'RECEIVE'
  JOIN rcv_shipment_headers rsh    ON rsh.shipment_header_id= rt.shipment_header_id
  JOIN gl_code_combinations_kfv gcc ON gcc.code_combination_id = aid.dist_code_combination_id
  LEFT JOIN ap_invoice_payments_all aip ON aip.invoice_id   = ai.invoice_id
 WHERE ai.invoice_num = :p_invoice_num
   AND ai.org_id = :p_org_id;
```
The `PO_DISTRIBUTIONS_ALL` → `AP_INVOICE_DISTRIBUTIONS_ALL` join via `po_distribution_id` is the 3-way match link. Missing this join means you cannot trace from invoice back to the original PO commitment.

**220. Write a SQL to find profile option values set at responsibility level for iSupplier.**
```sql
SELECT fpot.user_profile_option_name,
       frt.responsibility_name,
       fpov.profile_option_value,
       fpov.last_update_date
  FROM fnd_profile_option_values fpov
  JOIN fnd_profile_options fpo    ON fpo.profile_option_id  = fpov.profile_option_id
  JOIN fnd_profile_options_tl fpot ON fpot.profile_option_id = fpo.profile_option_id
                                  AND fpot.language = 'US'
  JOIN fnd_responsibility_tl frt  ON frt.responsibility_id  = fpov.level_value
                                  AND frt.language = 'US'
 WHERE fpov.level_id = 10003
   AND frt.responsibility_name LIKE '%iSupplier%'
ORDER BY fpot.user_profile_option_name;
```
`level_id` hierarchy: 10001=Site, 10002=Application, 10003=Responsibility, 10004=User. At GE, `MO: Operating Unit`, `FND: Personalization Region Link Enabled`, and `ICX: Session Timeout` were all set at responsibility level differently per site — this query was the audit check before each site's go-live.

**221. Write a SQL to get all supplier contacts and their portal access levels.**
```sql
SELECT pv.vendor_name, pvs.vendor_site_code,
       vc.last_name||', '||vc.first_name contact_name,
       vc.email_address, vc.phone,
       fu.user_name portal_username, fu.start_date, fu.end_date,
       frt.responsibility_name access_level
  FROM ap_suppliers pv
  JOIN ap_supplier_sites_all pvs ON pvs.vendor_id       = pv.vendor_id
  JOIN ap_supplier_contacts vc   ON vc.vendor_site_id   = pvs.vendor_site_id
  LEFT JOIN fnd_user fu          ON fu.person_party_id  = vc.party_id
  LEFT JOIN fnd_user_resp_groups_direct furg ON furg.user_id = fu.user_id
  LEFT JOIN fnd_responsibility_tl frt
         ON frt.responsibility_id = furg.responsibility_id AND frt.language = 'US'
 WHERE pvs.purchasing_site_flag = 'Y'
ORDER BY pv.vendor_name, vc.last_name;
```
`AP_SUPPLIER_CONTACTS` links to TCA `HZ_PARTIES` via `party_id`; FND users link via `person_party_id`. This join pattern was used to produce the GE supplier onboarding audit report showing which contacts had portal access and which still needed registration.

**222. Write a SQL to find POs where unit price differs between PO line and receipt.**
```sql
SELECT ph.segment1 po_number, pl.line_num,
       pl.unit_price   po_line_price,
       rt.po_unit_price receipt_price,
       ABS(pl.unit_price - NVL(rt.po_unit_price, pl.unit_price)) diff,
       pv.vendor_name, rt.transaction_date
  FROM rcv_transactions rt
  JOIN po_line_locations_all pll ON pll.line_location_id = rt.po_line_location_id
  JOIN po_lines_all pl           ON pl.po_line_id        = pll.po_line_id
  JOIN po_headers_all ph         ON ph.po_header_id      = pl.po_header_id
  JOIN ap_suppliers pv           ON pv.vendor_id         = ph.vendor_id
 WHERE rt.transaction_type = 'RECEIVE'
   AND NVL(rt.po_unit_price, pl.unit_price) <> pl.unit_price
ORDER BY diff DESC;
```
`RCV_TRANSACTIONS.po_unit_price` stores the price at time of receipt. The GE bug had `rt.po_unit_price` pulling from the BPA agreement price via an incorrect VO join — fixed by ensuring the Standard PO's `po_lines_all.unit_price` was used, not the blanket line.

**223. Write a SQL aging report for overdue PO shipments.**
```sql
SELECT pv.vendor_name, ph.segment1 po_number,
       pll.need_by_date,
       TRUNC(SYSDATE) - TRUNC(pll.need_by_date) days_overdue,
       CASE WHEN SYSDATE - pll.need_by_date BETWEEN 1  AND 7  THEN '1-7 days'
            WHEN SYSDATE - pll.need_by_date BETWEEN 8  AND 30 THEN '8-30 days'
            WHEN SYSDATE - pll.need_by_date BETWEEN 31 AND 60 THEN '31-60 days'
            ELSE '60+ days' END bucket,
       pll.quantity - NVL(pll.quantity_received,0) open_qty
  FROM po_line_locations_all pll
  JOIN po_lines_all pl   ON pl.po_line_id    = pll.po_line_id
  JOIN po_headers_all ph ON ph.po_header_id  = pl.po_header_id
  JOIN ap_suppliers pv   ON pv.vendor_id     = ph.vendor_id
 WHERE pll.need_by_date < SYSDATE
   AND pll.closed_code NOT IN ('CLOSED','FINALLY CLOSED')
   AND (pll.quantity - NVL(pll.quantity_received,0)) > 0
   AND ph.authorization_status = 'APPROVED'
ORDER BY days_overdue DESC;
```

**224. How do you identify orphaned ASN records that failed the receiving interface?**
```sql
SELECT rti.interface_transaction_id, rti.header_interface_id,
       rti.po_number, rti.quantity, rti.processing_status_code,
       pie.column_name error_column, pie.error_message
  FROM rcv_transactions_interface rti
  LEFT JOIN po_interface_errors pie
         ON pie.interface_header_id = rti.header_interface_id
        AND pie.table_name = 'RCV_TRANSACTIONS_INTERFACE'
 WHERE rti.processing_status_code IN ('ERROR','PENDING')
ORDER BY rti.creation_date DESC;
```
`PO_INTERFACE_ERRORS` is the single most valuable debugging table for ASN failures — captures the exact validation that failed (invalid ship-to org, quantity exceeds tolerance, PO ack required, etc.). At GE, improving the error messages shown to suppliers was directly informed by the top error codes from this table during hypercare.

**225. Write a SQL using analytic functions to rank suppliers by on-time delivery per quarter.**
```sql
SELECT vendor_name, qtr, total_receipts, on_time,
       ROUND(on_time / total_receipts * 100, 1) otd_pct,
       RANK() OVER (PARTITION BY qtr ORDER BY on_time/total_receipts DESC) rnk
  FROM (
    SELECT pv.vendor_name,
           TO_CHAR(rt.transaction_date,'YYYY-"Q"Q') qtr,
           COUNT(*)                                  total_receipts,
           SUM(CASE WHEN TRUNC(rt.transaction_date) <= TRUNC(pll.promised_date)
                    THEN 1 ELSE 0 END)               on_time
      FROM rcv_transactions rt
      JOIN po_line_locations_all pll ON pll.line_location_id = rt.po_line_location_id
      JOIN po_headers_all ph         ON ph.po_header_id      = pll.po_header_id
      JOIN ap_suppliers pv           ON pv.vendor_id         = ph.vendor_id
     WHERE rt.transaction_type = 'RECEIVE'
       AND pll.promised_date IS NOT NULL
    GROUP BY pv.vendor_name, TO_CHAR(rt.transaction_date,'YYYY-"Q"Q')
  )
ORDER BY qtr, rnk;
```
`RANK()` gaps for ties (1,1,3); use `DENSE_RANK()` for no gaps (1,1,2). This was the basis for the GE collaboration history report's quarterly supplier scorecard section.

**226. How do you query FND_LOOKUP_VALUES for a specific lookup type?**
```sql
SELECT flv.lookup_code, flv.meaning, flv.description,
       flv.enabled_flag, flv.start_date_active, flv.end_date_active, flv.tag
  FROM fnd_lookup_values flv
 WHERE flv.lookup_type         = :p_lookup_type  -- e.g. 'SHIPMENT_METHOD'
   AND flv.view_application_id = 201              -- 201 = PO application
   AND flv.language            = USERENV('LANG')
   AND flv.enabled_flag        = 'Y'
   AND SYSDATE BETWEEN NVL(flv.start_date_active, SYSDATE-1)
                   AND NVL(flv.end_date_active,   SYSDATE+1)
ORDER BY NVL(flv.display_sequence,9999), flv.meaning;
```
Always filter `language = USERENV('LANG')` and `view_application_id` — without the app ID you may get lookup codes from wrong modules that happen to share the same type name. The ship-method LOV "No Items Found" bug at GE was caused by a mismatched `view_application_id` in the VO query.

**227. Write a SQL to find all active concurrent programs in a specific request group.**
```sql
SELECT fcp.user_concurrent_program_name,
       fce.execution_file_name, fce.execution_method_code,
       fc.output_file_type, fc.enabled_flag
  FROM fnd_request_group_units frgu
  JOIN fnd_request_groups frg       ON frg.request_group_id    = frgu.request_group_id
  JOIN fnd_concurrent_programs fc   ON fc.concurrent_program_id = frgu.request_unit_id
  JOIN fnd_concurrent_programs_tl fcp ON fcp.concurrent_program_id = fc.concurrent_program_id
                                     AND fcp.language = 'US'
  JOIN fnd_executables fce          ON fce.executable_id        = fc.executable_id
 WHERE frg.request_group_name = :p_group_name
   AND fc.enabled_flag        = 'Y'
   AND frgu.unit_application_id = frg.application_id
ORDER BY fcp.user_concurrent_program_name;
```

**228. How do you query the error details for a specific concurrent program request?**
```sql
SELECT fcr.request_id, fcp.user_concurrent_program_name,
       fcr.phase_code, fcr.status_code,
       fcr.actual_start_date, fcr.actual_completion_date,
       fcr.logfile_name, fcr.outfile_name,
       fcr.argument_text
  FROM fnd_concurrent_requests fcr
  JOIN fnd_concurrent_programs_tl fcp
    ON fcp.concurrent_program_id = fcr.concurrent_program_id
   AND fcp.language = 'US'
 WHERE fcr.request_id = :p_request_id;
```
The actual log content lives on the OS at `$APPLCSF/log/<logfile_name>`. In R12 you can view it via View Requests → View Log. For critical batch failures during hypercare, I used `UTL_FILE` in a quick PL/SQL block to read the tail of the log file without needing server access.

**229. Write a SQL to identify PO revisions and supplier-initiated changes in the last week.**
```sql
SELECT ph.segment1 po_number, ph.revision_num,
       ph.last_update_date, ph.authorization_status,
       pv.vendor_name,
       fu.user_name updated_by,
       ph.change_requested_by  -- 'SUPPLIER' for iSupplier-originated changes
  FROM po_headers_all ph
  JOIN ap_suppliers pv ON pv.vendor_id   = ph.vendor_id
  JOIN fnd_user fu     ON fu.user_id     = ph.last_updated_by
 WHERE ph.last_update_date >= SYSDATE - 7
   AND ph.revision_num > 0
   AND ph.type_lookup_code = 'STANDARD'
ORDER BY ph.last_update_date DESC;
```
`change_requested_by = 'SUPPLIER'` identifies changes originating from iSupplier change requests. Monitoring this during hypercare showed whether suppliers were correctly using the change-request workflow vs contacting buyers directly.

**230. Write a SQL to reconcile PO quantities, ASN in-transit, and received quantities.**
```sql
SELECT ph.segment1 po_number, pl.line_num, pll.shipment_num,
       pv.vendor_name,
       pll.quantity                              ordered_qty,
       NVL(asn.asn_qty, 0)                       in_transit_qty,
       NVL(pll.quantity_received, 0)             received_qty,
       pll.quantity - NVL(pll.quantity_received,0) open_po_qty,
       NVL(pll.quantity_billed,0)                billed_qty
  FROM po_line_locations_all pll
  JOIN po_lines_all pl   ON pl.po_line_id     = pll.po_line_id
  JOIN po_headers_all ph ON ph.po_header_id   = pl.po_header_id
  JOIN ap_suppliers pv   ON pv.vendor_id      = ph.vendor_id
  LEFT JOIN (
    SELECT rsl.po_line_location_id, SUM(rsl.quantity_shipped) asn_qty
      FROM rcv_shipment_lines rsl
      JOIN rcv_shipment_headers rsh ON rsh.shipment_header_id = rsl.shipment_header_id
     WHERE rsl.shipment_line_status_code = 'EXPECTED'
       AND rsh.receipt_source_code = 'VENDOR'
    GROUP BY rsl.po_line_location_id
  ) asn ON asn.po_line_location_id = pll.line_location_id
 WHERE ph.authorization_status = 'APPROVED'
   AND pll.closed_code != 'FINALLY CLOSED'
ORDER BY ph.segment1, pl.line_num;
```
`shipment_line_status_code = 'EXPECTED'` in `RCV_SHIPMENT_LINES` identifies ASNs in transit not yet physically received. This three-way reconciliation was the foundation of the GE Supplier Export BI Publisher report.

**231. Write a SQL to find WebADI integrator and layout column definitions.**
```sql
SELECT bvi.integrator_code, bvi.integrator_user_name,
       bvl.layout_code, bvl.layout_user_name,
       bic.interface_col_name, bic.prompt_left,
       bic.required_flag, bic.display_width, bic.sequence_num
  FROM bne_integrators_vl bvi
  JOIN bne_layouts_vl bvl   ON bvl.integrator_code    = bvi.integrator_code
                           AND bvl.integrator_app_id  = bvi.integrator_app_id
  JOIN bne_layout_cols bic  ON bic.layout_code        = bvl.layout_code
                           AND bic.layout_app_id      = bvl.application_id
 WHERE bvi.integrator_code LIKE '%PROMISE%'
ORDER BY bic.sequence_num;
```
`BNE_INTEGRATORS_VL`, `BNE_LAYOUTS_VL`, and `BNE_LAYOUT_COLS` define the WebADI spreadsheet structure. `BNE_INTERFACES_VL` and `BNE_INTERFACE_COLS_VL` map columns to the API/target table. Used to audit the GE WebADI promise-date upload integrator columns before each environment migration.

**232. Write a SQL to find all value sets of validation type "Table" and their WHERE clauses.**
```sql
SELECT fvs.flex_value_set_name, fvs.validation_type,
       fvs.format_type, fvs.maximum_size,
       fvst.application_table_name, fvst.value_column_name,
       fvst.id_column_name, fvst.additional_where_clause
  FROM fnd_flex_value_sets fvs
  JOIN fnd_flex_validation_tables fvst
    ON fvst.flex_value_set_id = fvs.flex_value_set_id
 WHERE fvs.validation_type = 'F'
ORDER BY fvs.flex_value_set_name;
```
Table-validated value sets (`validation_type = 'F'`) run SQL at runtime — check `additional_where_clause` for bind variables and joins. These are performance risks if the target table is large and the WHERE clause lacks index-friendly predicates. Always test them with AUTOTRACE before deploying to production.

**233. Write a SQL to find all pending workflow notifications for iSupplier acknowledgements.**
```sql
SELECT wn.notification_id, wn.message_type, wn.message_name,
       wn.recipient_role, wn.subject,
       wn.begin_date sent_date, wn.due_date, wn.status,
       wi.item_key po_reference
  FROM wf_notifications wn
  JOIN wf_item_activity_statuses wias ON wias.notification_id = wn.notification_id
  JOIN wf_items wi ON wi.item_type = wias.item_type
                  AND wi.item_key  = wias.item_key
 WHERE wn.message_type IN ('POAPPRV','PONOT','POSCHNG')
   AND wn.status        = 'OPEN'
   AND wn.begin_date   >= SYSDATE - 7
ORDER BY wn.begin_date DESC;
```

**234. How do you query RCV_TRANSACTIONS to get all Return to Vendor (RTV) transactions?**
```sql
SELECT rt.transaction_id, rt.transaction_date, rt.quantity,
       rt.reason_id, rr.reason_name,
       rsh.shipment_num original_asn,
       ph.segment1 po_number, pl.line_num,
       pv.vendor_name
  FROM rcv_transactions rt
  JOIN rcv_shipment_headers rsh  ON rsh.shipment_header_id = rt.shipment_header_id
  JOIN po_line_locations_all pll ON pll.line_location_id   = rt.po_line_location_id
  JOIN po_lines_all pl           ON pl.po_line_id          = pll.po_line_id
  JOIN po_headers_all ph         ON ph.po_header_id        = pl.po_header_id
  JOIN ap_suppliers pv           ON pv.vendor_id           = ph.vendor_id
  LEFT JOIN rcv_reasons rr       ON rr.reason_id           = rt.reason_id
 WHERE rt.transaction_type = 'RETURN TO VENDOR'
   AND ph.vendor_id        = :p_vendor_id
ORDER BY rt.transaction_date DESC;
```
RTV transactions reduce `pll.quantity_received`. The return reason from `RCV_REASONS` is what appears in the iSupplier Returns screen. On GE, adding PO Line Number to the Returns screen used this exact join to `po_lines_all.line_num`.

**235. Write a SQL to audit FND user and responsibility access for iSupplier.**
```sql
SELECT fu.user_name, fu.email_address,
       fu.start_date user_created, fu.end_date user_expires,
       frt.responsibility_name,
       furg.start_date resp_from, furg.end_date resp_to,
       fa.application_short_name
  FROM fnd_user fu
  JOIN fnd_user_resp_groups_direct furg ON furg.user_id             = fu.user_id
  JOIN fnd_responsibility fr            ON fr.responsibility_id     = furg.responsibility_id
  JOIN fnd_responsibility_tl frt        ON frt.responsibility_id    = fr.responsibility_id
                                       AND frt.language = 'US'
  JOIN fnd_application fa               ON fa.application_id        = fr.application_id
 WHERE frt.responsibility_name LIKE '%iSupplier%'
   AND (fu.end_date   IS NULL OR fu.end_date   > SYSDATE)
   AND (furg.end_date IS NULL OR furg.end_date > SYSDATE)
ORDER BY fu.user_name;
```

**236. Write a SQL to generate a supplier performance scorecard.**
```sql
SELECT pv.vendor_name,
       COUNT(DISTINCT ph.po_header_id)                          total_pos,
       COUNT(DISTINCT rsh.shipment_header_id)                   total_shipments,
       COUNT(rt.transaction_id)                                  total_receipts,
       SUM(CASE WHEN TRUNC(rt.transaction_date)<=TRUNC(pll.promised_date) THEN 1 END) on_time,
       ROUND(SUM(CASE WHEN TRUNC(rt.transaction_date)<=TRUNC(pll.promised_date) THEN 1 END)
             /NULLIF(COUNT(rt.transaction_id),0)*100,1)          otd_pct,
       ROUND(AVG(TRUNC(rt.transaction_date)-TRUNC(pll.promised_date)),1) avg_days_delta
  FROM rcv_transactions rt
  JOIN rcv_shipment_headers rsh  ON rsh.shipment_header_id = rt.shipment_header_id
  JOIN po_line_locations_all pll ON pll.line_location_id   = rt.po_line_location_id
  JOIN po_headers_all ph         ON ph.po_header_id        = pll.po_header_id
  JOIN ap_suppliers pv           ON pv.vendor_id           = ph.vendor_id
 WHERE rt.transaction_type  = 'RECEIVE'
   AND rt.transaction_date >= ADD_MONTHS(SYSDATE,-3)
   AND pll.promised_date IS NOT NULL
GROUP BY pv.vendor_name
ORDER BY otd_pct;
```
A negative `avg_days_delta` means the supplier typically delivers early; positive means late. `NULLIF(...,0)` prevents divide-by-zero for suppliers with no receipts in the period.

**237. Write a SQL to find PO lines with no ASN and overdue need-by date.**
```sql
SELECT ph.segment1, pv.vendor_name, pll.need_by_date,
       TRUNC(SYSDATE)-TRUNC(pll.need_by_date) days_overdue,
       pll.quantity - NVL(pll.quantity_received,0) open_qty
  FROM po_line_locations_all pll
  JOIN po_lines_all pl   ON pl.po_line_id    = pll.po_line_id
  JOIN po_headers_all ph ON ph.po_header_id  = pl.po_header_id
  JOIN ap_suppliers pv   ON pv.vendor_id     = ph.vendor_id
 WHERE pll.need_by_date < SYSDATE
   AND pll.closed_code NOT IN ('CLOSED','FINALLY CLOSED')
   AND (pll.quantity - NVL(pll.quantity_received,0)) > 0
   AND ph.authorization_status = 'APPROVED'
   AND NOT EXISTS (
         SELECT 1 FROM rcv_shipment_lines rsl
          JOIN rcv_shipment_headers rsh ON rsh.shipment_header_id = rsl.shipment_header_id
         WHERE rsl.po_line_location_id = pll.line_location_id
           AND rsh.receipt_source_code = 'VENDOR'
       )
ORDER BY days_overdue DESC;
```

**238. Write a SQL to query OAF personalization levels for a specific responsibility.**
```sql
SELECT jdr_utils.getDocumentName(jp.path_docid) page_doc,
       jp.name personalization_level,
       jdc.att_name property, jdc.att_value new_value
  FROM jdr_paths jp
  JOIN jdr_attributes jdc ON jdc.doc_id = jp.path_docid
 WHERE jp.name LIKE 'resp%'
   AND TO_NUMBER(REGEXP_SUBSTR(jp.name,'[0-9]+$')) = :p_responsibility_id
ORDER BY jp.path_docid, jdc.comp_seq;
```
Responsibility-level personalizations are stored in MDS with a naming pattern like `resp<app_id>_<resp_id>`. Before migrating personalizations at GE, this query was run to get the complete list of pages personalized for each site-specific responsibility.

**239. Write a SQL to find concurrent program incompatibility rules.**
```sql
SELECT fcp1.user_concurrent_program_name running_program,
       fcp2.user_concurrent_program_name incompatible_with,
       fci.incompatibility_type
  FROM fnd_concurrent_program_incompatibilities fci
  JOIN fnd_concurrent_programs_tl fcp1
    ON fcp1.concurrent_program_id = fci.concurrent_program_id AND fcp1.language='US'
  JOIN fnd_concurrent_programs_tl fcp2
    ON fcp2.concurrent_program_id = fci.incompatible_id AND fcp2.language='US'
ORDER BY fcp1.user_concurrent_program_name;
```

**240. Write a SQL to find all supplier users who have never logged in to iSupplier.**
```sql
SELECT fu.user_name, fu.email_address, fu.creation_date,
       fu.last_logon_date, pv.vendor_name, pvs.vendor_site_code
  FROM fnd_user fu
  JOIN pos_supplier_users psu ON psu.user_id = fu.user_id
  JOIN ap_suppliers pv        ON pv.vendor_id = psu.vendor_id
  JOIN ap_supplier_sites_all pvs ON pvs.vendor_id = pv.vendor_id
 WHERE fu.last_logon_date IS NULL
   AND (fu.end_date IS NULL OR fu.end_date > SYSDATE)
ORDER BY pv.vendor_name, fu.user_name;
```
`fnd_user.last_logon_date` is NULL for accounts that have never been used. This adoption-tracking query was a key hypercare metric — at go-live we targeted 80% supplier login rate within two weeks.

---

# Section Q — OAF Technical Deep Dive (Q241–Q285)

**241. Explain the lifecycle of an OAF page request from browser to rendered response.**
The browser sends an HTTP GET/POST to the OC4J servlet container. The `OAPageBean` entry point receives the request, resolves the page document from MDS (layering base XML with personalizations and substitutions), and instantiates the AM from the pool. On GET, `processRequest` fires on each controller top-down, initializing VOs and UI state. The framework serializes the region tree to HTML and sends it back. On POST, `processFormRequest` fires, routes events to the appropriate controller, calls AM methods, and issues commit/rollback. Understanding this lifecycle is essential for knowing where to put initialization code (processRequest) vs event handling (processFormRequest).

**242. What is OADBTransaction and how do you use it in OAF?**
`OADBTransaction` is the interface to the underlying database connection and transaction for an AM. You get it via `am.getOADBTransaction()`. Key methods: `commit()`, `rollback()`, `executeQuery(String sql, Object[] binds)` for raw SQL, `getSessionValue(String)` for EBS session globals, and `writeDiagnostics(controller, message, level)` for debug logging. For calling PL/SQL, use `callProcedure(String sql, Object[] binds)`. Never call `java.sql.Connection` directly — always go through `OADBTransaction` so the framework manages the connection lifecycle and passivation correctly.

**243. What is the difference between OAApplicationModule and OADBTransaction?**
`OAApplicationModule` is the transaction container — it manages the VO lifecycle, the AM pool slot, and exposes business service methods. `OADBTransaction` is the database-level interface accessible from the AM, providing raw SQL/PL/SQL execution and session state. Think of AM as the service layer and `OADBTransaction` as the JDBC-adjacent layer. You access `OADBTransaction` from within AM methods; controllers access the AM. Never call `OADBTransaction` directly from a controller — always via an AM method for proper layering.

**244. How do you handle a scenario where a VO query needs a dynamic WHERE clause based on user role?**
In `processRequest`, after resolving the user's responsibility/role from `pageContext.getResponsibilityId()` or a profile value, call `vo.setWhereClause(null)` to clear any prior filter, then `vo.setWhereClause("column = :1")` and `vo.setWhereClauseParam(0, value)`. Always use bind variables (`:1`, `:2`) — never concatenate. If the clause structure itself changes by role (not just values), build it conditionally in the AM method and pass the fully-formed clause string as a parameter. On GE, supplier-facing VOs filtered by `vendor_id` resolved from the ICX session; buyer/surrogate VOs used a broader filter based on agent assignment.

**245. What are the OAF API classes you used most heavily on the GE iSupplier project?**
Key classes: `OAPageContext` (session, parameters, forwarding), `OAApplicationModule` and its extensions (service methods, VO access), `OAViewObject` / `OAViewObjectImpl` (query execution, where-clause, row iteration), `OARow` / `OAViewRowImpl` (attribute get/set), `OADBTransaction` (commit/rollback/PL-SQL), `OAException` (raising errors), `OAWebBeanTableLayout` and `OAMessageTextInput` (programmatic UI manipulation). `oracle.apps.icx.por.util.PorUtil` and `oracle.apps.icx.icatalog.shopping.util.IcxUtil` were iSupplier-specific utilities used for session-context resolution (vendor_id, vendor_site_id, supplier name).

**246. How do you raise a validation error from a controller and display it on the page?**
```java
throw new OAException("ICX", "MY_ERROR_MSG_NAME", null,
                      OAException.ERROR, null);
```
For inline field-level errors, use `pageContext.putDialogMessage(new OAException(...))` before the throw, or set the message on the specific item. Use message names defined in `FND_MESSAGES` so they are translatable and patchable. On the GE project, all Promise Date validation errors (null without bypass, bypass reason missing) were raised as `OAException.ERROR` with custom FND message names, displaying inline on the acknowledgement page without a full page error.

**247. What is the difference between pageContext.putTransactionValue and putSessionValue?**
`putTransactionValue(key, value)` stores data in the AM's transaction scope — it is cleared on commit or rollback, making it suitable for in-flight page data you don't want persisted. `putSessionValue(key, value)` stores data in the HTTP session scope — it survives across multiple page navigations until the session expires or is explicitly cleared. On GE, we used `putTransactionValue` to pass the selected vendor_id between the supplier search popup and the main surrogate-buyer task flow, and `putSessionValue` for the user's iSupplier responsibility context that needed to persist across page navigations.

**248. How do you create a custom paginated table region in OAF?**
Define a `table` region in JDeveloper bound to a VO with a `RangeSize` property set (e.g., 10) — OAF handles pagination automatically via `First/Previous/Next/Last` navigation links. In `processRequest`, call `vo.setRangeSize(10)` and `vo.executeQuery()`. For custom navigation, override the `NavigationBar` event in `processFormRequest`, detect the `event.getId()` equals `"navigateRows"`, and call `vo.scrollToRangePage(pageContext.getParameter("goPage"))`. Ensuring the VO has a `ORDER BY` clause that produces deterministic ordering is critical — without it, paging shows different rows on refresh.

**249. How do you implement a dependent LOV in OAF (values change based on another field)?**
The parent field (e.g., Organization) has a PPR (Partial Page Rendering) action that fires when its value changes. In `processFormRequest`, detect the PPR event for the parent field, read its new value from `pageContext.getParameter("orgId")`, then on the dependent LOV's VO call `setWhereClause` with the parent value and `executeQuery()`. Register the parent item's PPR action with `setFirePartialAction(true)` and set the dependent LOV item's `Rendered` or `QueryRequired` SPEL to force re-evaluation. On GE, the ship-to city LOV was dependent on the ship-to organization selected in the ASN header.

**250. How do you call a PL/SQL stored procedure from an OAF Application Module?**
```java
OADBTransaction txn = getOADBTransaction();
CallableStatement cs = txn.createCallableStatement(
    "BEGIN my_pkg.my_proc(:1,:2,:3); END;", 1);
cs.setString(1, inputParam);
cs.registerOutParameter(2, Types.VARCHAR);
cs.registerOutParameter(3, Types.VARCHAR);
cs.execute();
String result  = cs.getString(2);
String errMsg  = cs.getString(3);
cs.close();
```
Alternatively use `txn.callProcedure(sql, binds)` for simpler procedures. The callable statement approach is needed when you need OUT parameters. On GE, all ASN validation, surrogate-buyer mapping lookups, and promise-date update APIs were exposed as PL/SQL packages and called this way from AM methods.

**251. What is EO-based VO vs Expert Mode VO and when do you use each?**
An **EO-based VO** is backed by one or more Entity Objects — it participates in the BC4J transaction, handles DML automatically via EO, supports validation, and is suitable for pages that insert/update/delete data. An **Expert Mode VO** has a hand-written SQL query with no EO backing — it is read-only and bypass BC4J validation, suitable for complex multi-table queries used in reports, search results, or display-only pages. On GE, the ASN eligible-shipments VO used Expert Mode with a complex eligibility query (Need-by ± days, open qty, ack status), while the ASN header VO was EO-based for DML when the supplier submitted.

**252. What is SPEL and give three real examples from your GE project?**
SPEL (Simplest Possible Expression Language) binds a UI item property to a VO attribute at runtime, syntax `${oa.ViewName.AttributeName}`. Three GE examples: (1) `Rendered = ${oa.AsnHeaderVO.ShowVendorLotFlag}` — shows the Vendor LOT field only when the item requires LOT tracking; (2) `Required = ${oa.AckVO.PromiseDateRequiredFlag}` — makes Promise Date mandatory when the PO type has mandatory-acknowledgement flag set; (3) `ReadOnly = ${oa.ChangeRequestVO.PriceReadonlyFlag}` — locks the Unit Price field on BPA change requests. All three required a transient Boolean attribute in the VO populated from PL/SQL or query logic.

**253. What is static vs dynamic personalization in OAF?**
**Static** sets a property (Rendered, ReadOnly, Required) to a hard-coded True or False at personalization time — the value never changes at runtime. **Dynamic** binds the property to a SPEL expression `${oa.VOName.AttrName}` so it evaluates against live VO data on each page render. Dynamic personalizations require a VO attribute to bind to, which may need a transient attribute or VO extension to create. On GE, static personalizations hid fields irrelevant to all users; dynamic personalizations handled conditional visibility based on PO type, supplier type, and acknowledgement status.

**254. How do you migrate OAF personalizations between instances (DEV → UAT → PROD)?**
Export via **Functional Administrator** → Core Services → Personalizations → Export, selecting the page and level. This downloads an XML file (MDS document) capturing all personalizations for that page at that level. Import on the target instance via the same screen → Import. For bulk/scripted migration, use the `FNDLOAD`-equivalent `jpximport`/`jpxexport` commands or the `XDFCMD` utility for MDS documents. At GE, personalizations were bundled into release packages along with FNDLOAD scripts and CEMLI files, migrated in a single coordinated CTASK in ServiceNow to ensure atomicity.

**255. How do you add a column to an existing OAF table region without touching Oracle's code?**
Via personalization: open the page with `Personalize` link enabled, navigate to the table region, click Personalize, and add a new `messageTextInput` item (or `formValue` for non-display) with a new `View Attribute` mapped to a VO attribute you've added via VO extension. If the attribute doesn't exist in the seeded VO, first create a VO extension with the additional attribute (transient or from a SQL expression), register the substitution, then personalize to bind to it. On GE, the "Balance Outstanding Qty" and "Vendor LOT" columns were added this way — no Oracle code was modified.

**256. How do you create a VO extension and register a substitution in OAF?**
In JDeveloper, create a new VO class that extends the base Oracle VO (e.g., `oracle.apps.icx.por.rcv.server.RcvShipmentVO`). Add transient attributes or override `create()` to populate them. Export the substitution document (XML defining `<OASubstitution>` mapping old VO → new VO) using `jpxexport`, then import it into each environment with `jpximport`. Substitutions are instance-wide and affect all pages using that VO. On GE, several iSupplier VOs were extended to add computed attributes (ASN eligibility flag, balance qty, vendor LOT availability) without touching the base Oracle class.

**257. How do you debug a NullPointerException in an OAF controller in production?**
Enable diagnostics: set profile `FND: Diagnostics` to Yes, then use the "About this Page" link to inspect the page structure, AM, and VO state. Add `pageContext.writeDiagnostics(this, "value=" + var, OAFwkConstants.STATEMENT)` in the controller. Check the OC4J/WLS application log (`$LOG_HOME/oacore/oacore_default_group_1/`) for the Java stack trace — the NPE stack will show the class, method, and line number. In production without source access, the class file package name and method name from the stack trace usually points to the exact Oracle standard or custom class causing the issue.

**258. What is passivation in OAF and when does it cause problems?**
Passivation is OAF saving the AM's state (VO query state, transient attributes, pending changes) to `FND_TM_PENDING_SESSIONS` in the database so the AM can be recycled from the pool and restored for the next request. Problems occur when: (1) transient attributes contain non-serializable Java objects — AM cannot passivate and the user gets a session error; (2) large VO result sets are passivated frequently — causes DB I/O spikes; (3) passivation is triggered during a long user think-time and the session timeout fires before the AM is restored. Fix by making transient attributes use serializable types and setting `Passivation Preferred = false` on AMs that hold heavy state.

**259. How do you pass data between a parent page and a popup (detail) page in OAF?**
For a popup, use `pageContext.setForwardURL()` with `KEEP_MENU_CONTEXT` and pass parameters as URL query string parameters. On the popup page, read via `pageContext.getParameter("paramName")`. To return data from popup to parent, store the result in a `putTransactionValue()` key in the shared AM (both pages must share the same root AM), then the parent reads it in `processFormRequest` after the popup closes. Alternatively, use `OADialogPage` for simple OK/Cancel confirmations. On GE, the surrogate-supplier selection popup passed the chosen `vendor_id` and `vendor_site_id` back to the task flow via `putTransactionValue`.

**260. What is a PPR (Partial Page Rendering) event and when did you use it at GE?**
PPR allows a portion of the page to refresh without a full reload by submitting a partial form post. A UI item declares itself a PPR target (`setFirePartialAction(true)`) and lists the regions to refresh (`addPartialRootDataBoundRegion`). In `processFormRequest`, detect the PPR event by `pageContext.isFormSubmission() && "ppr".equals(event.getId())`. On GE: (1) selecting a ship-to organization triggered a PPR to refresh the ship-to city LOV; (2) checking the "Promise Date N/A" checkbox triggered a PPR to toggle the Promise Date field between required and hidden; (3) changing ASN quantity triggered a PPR to recalculate the Balance Outstanding Qty display.

**261. How do you register a new OAF page function in AOL and assign it to a menu?**
In System Administrator → Security → Function, create a new function with Type = `SSWA jsp page`, Parameters = `page=/oracle/apps/xx/module/webui/MyPagePG`, and set the Object Name. Then in Security → Menu, add this function to the appropriate menu used by the iSupplier responsibility. Grant the function to the relevant user/responsibility via Security Groups if using function-level security. Finally, ensure the page file is deployed to `$OA_HTML` and the JAR is compiled into `$OA_CLASSPATH`. On GE, the custom surrogate-supplier task flow was added as a new function under the buyer iSupplier responsibility.

**262. What are the OAF regions specific to iSupplier and how are they structured?**
iSupplier pages live under `/oracle/apps/icx/por/` (purchasing), `/oracle/apps/icx/rcv/` (receiving/ASN), and `/oracle/apps/icx/payables/` (invoice/payment). Key page groups: `icx.por.rcv.webui.RcvShipNoticeCreatePG` (ASN creation), `icx.por.webui.PoAcknowledgePG` (PO acknowledgement), `icx.por.rcv.webui.RcvShipNoticeViewPG` (View ASN). Each page follows a standard OAF structure: a root `pageLayout` region containing header (`stackLayout`), table (`table` or `tableLayout`), and action (`flowLayout`) regions. Personalizations at GE targeted specific item IDs within these regions, identified using "About this Page" diagnostics.

**263. Describe the OAF components of the surrogate-supplier task flow you built at GE.**
The surrogate task flow comprised: (1) a **search page** (`SurrogateSrchPG`) with an AM extending the standard Purchasing AM, containing a VO (`SurrogateSupplierVO`) querying `pos_supplier_users` joined to `ap_suppliers` for buyer-accessible suppliers; (2) a **confirmation page** setting `vendor_id`/`vendor_site_id` on the ICX session via `OADBTransaction.getSessionValue`; (3) a **custom controller** in `processFormRequest` calling a PL/SQL procedure to log the surrogate action and send a notification to the mapped buyer; (4) **responsibility mapping** via OAF personalization restricting the task flow function to the surrogate-buyer responsibility. The 67 surrogate accounts were each associated with a list of supplier-site pairs stored in a custom lookup table queried by the VO.

**264. How do you handle the "AM not found in pool" error in OAF production?**
This usually means AM pool exhaustion (all pool slots occupied) or a session timeout with a bad AM reference. First check the OC4J/WLS metrics for AM pool size and active sessions. If pool is full, increase `jbo.ampool.maxpoolsize` in `BC4JConfig.xml` or add application server nodes. If timeout-related, clear the user's session and have them re-login. Persistent occurrences often indicate AM instances not being returned to pool (leaked) — look for `commit()`/`rollback()` not being called in error paths, or controllers holding AM references across requests. In the GE multi-node deployment, AM affinity (sticky sessions) was required to prevent users hitting different nodes on each request.

**265. How does OAF handle multi-node deployment and what session configuration is required?**
OAF AMs are pooled per JVM, so multi-node deployments require **sticky sessions** (HTTP session affinity) at the load balancer — each user must consistently hit the same application server node. If a node goes down, the AM state is passivated to the DB (FND_TM tables) and can be restored on another node. Configure `jbo.ampool.sessionCookieName` for the AM pool cookie, and ensure the Oracle HTTP Server's `mod_oc4j` or the load balancer routes based on `JSESSIONID`. At GE, adding the 2 server nodes required updating the `opmn.xml`, the `dbc` files, and the load balancer sticky-session configuration — verified by checking `$FND_TOP/secure/*.dbc` and testing node failover.

**266. How do you implement row-level security in a VO query based on the logged-in supplier?**
In the AM's `prepareSession()` or in the VO's `executeQueryForCollection`, resolve the current user's `vendor_id` from the ICX session: `String vendorId = getOADBTransaction().getSessionValue("vendor_id")`. Then call `vo.setWhereClause("vendor_id = :vendorId")` and `vo.setWhereClauseParam(0, vendorId)` before `vo.executeQuery()`. For surrogate users, resolve the impersonated vendor_id from the surrogate mapping table instead. This was the core security mechanism for all supplier-facing iSupplier VOs at GE — a supplier can only ever see their own POs, ASNs, and receipts.

**267. What is the BC4J cache and when does it cause stale-data issues in OAF?**
BC4J maintains an in-memory entity cache within the AM scope. If multiple requests modify the same row (e.g., in a multi-user scenario), a cached EO may not reflect the latest DB state until the cache is invalidated. Stale cache shows up as: old data displayed after another user's commit, validation against outdated values. Fix by calling `am.getOADBTransaction().clearEntityCache(EO.class)` or using `refreshVO()` to re-execute the query, or by switching to Expert Mode VO (no EO cache) for display-only pages where always-fresh data is critical. On GE, the View ASN page used Expert Mode to always show the current `quantity_received` without cache staleness.

**268. How do you implement an OAF page that validates a field only when another checkbox is unchecked?**
In `processFormRequest`, after checking `pageContext.isFormSubmission()`, read both values: the checkbox value via `pageContext.getParameter("naCheckbox")` and the promise date via `pageContext.getParameter("promisedDate")`. Add conditional logic: if checkbox is not checked and promisedDate is blank, throw `OAException` with your error message. For client-side feel without a round-trip, use PPR — when the checkbox fires a PPR action, set the `Required` property of the date field in `processFormRequest` via `OAMessageDateFieldBean bean = (OAMessageDateFieldBean)webBean.findIndexedChildRecursive("PromiseDate"); bean.setRequired(...)`. This is exactly the Promise Date mandatory/bypass logic built at GE.

**269. What is the significance of "Retain AM" on an OAF navigation and when do you use it?**
`Retain AM` on a `setForwardURL` or `returnForwardURL` call means the current root AM is kept alive across the navigation rather than being released to the pool. Use it when navigating from a parent page to a detail/edit popup page that must share transaction state with the parent. Without `Retain AM`, the new page gets a fresh AM and cannot access the parent's uncommitted data. Misusing it (retaining AM unnecessarily) causes pool exhaustion in high-traffic scenarios. On GE, the ASN header → ASN line detail navigation retained the AM so line-level changes could be committed atomically with the header.

**270. How do you unit test OAF controller logic without deploying to an EBS instance?**
OAF lacks a native lightweight unit test framework. The practical approach at GE: (1) unit test PL/SQL APIs independently in SQL Developer with mock inputs; (2) test VO queries directly in SQL Developer with representative data; (3) for controller logic, use JDeveloper's local run capability connected to a DEV EBS database — run the page locally and step through controller code in the JDeveloper debugger; (4) for SPEL expressions, create a test page in DEV with the exact conditions (acknowledged/not acknowledged, PO type, etc.) and verify rendering. Full end-to-end testing still requires the DEV EBS instance; there's no way to fully mock the OAF framework.

**271. What is MDS and how are OAF page definitions stored?**
MDS (MetaData Services) is Oracle's XML-based metadata repository. In EBS, it stores OAF page definitions (`.xml` files) and personalizations in the database in `JDR_*` tables (`JDR_PATHS`, `JDR_COMPONENTS`, `JDR_ATTRIBUTES`, `JDR_ELEMENTS`). At runtime, OAF reads the base page XML from MDS, then layers personalizations and substitutions on top. Personalizations are stored as separate MDS documents that override specific properties of base page elements. Because they are in the database rather than the filesystem, personalizations survive EBS patching (unlike modifications to Oracle's code files).

**272. How do you use "About This Page" for OAF debugging?**
Enable `FND: Diagnostics = Yes` at user or responsibility level. Then a small "About this Page" link appears at the bottom of every OAF page. Clicking it shows: the page document path in MDS, all regions and items with their types and property values, the root AM class and all nested AMs, each VO's name, class, SQL query, bind variables, and current result count. This is the single most powerful OAF debugging tool — it shows the exact VO name and attribute to personalize without source code access, verifies personalizations are applied, and confirms VO queries are executing with correct bind values. On GE, nearly every personalization was designed using About This Page to find the right region ID, item ID, and VO attribute name.

**273. What is the oracle.apps.icx package and what key classes does it contain for iSupplier?**
`oracle.apps.icx` is the Internet Commerce (ICX) application package — iSupplier Portal is part of the ICX product family. Key packages: `oracle.apps.icx.por` (purchasing/PO screens), `oracle.apps.icx.rcv` (receiving/ASN screens), `oracle.apps.icx.payables` (invoice/payment screens). Within these: `IcxContext` manages the ICX session attributes (vendor_id, vendor_site_id, user context); `PorUtil` provides common utility methods for resolving purchasing entities; `RcvShipNoticeAM` is the main Application Module for ASN creation. Understanding which AM owns the ASN flow was essential for knowing where to add validation hooks at GE.

**274. How do you add a custom mandatory field to an existing OAF page via extension?**
(1) Create a VO extension adding a transient VARCHAR2 attribute (e.g., `VendorLotNum`) with a default value of null. Register the VO substitution. (2) Personalize the page: add a new `messageTextInput` item mapped to `VendorLotNum` attribute, set `Required = true` (or use SPEL for conditional). (3) In the controller extension's `processFormRequest`, read `pageContext.getParameter("VendorLotNum")` and if blank throw `OAException`. This was the exact pattern used to add the Vendor LOT field to the GE ASN creation page — VO extension for the attribute, personalization for the UI item, controller extension for the mandatory validation.

**275. How do you handle multiple operating units in a single OAF page for a multi-site iSupplier?**
Set `MO: Security Profile` at the iSupplier responsibility level to a security profile that includes all required OUs. In VO queries, do not hardcode `org_id`; instead use `mo_global.get_current_org_id()` (for single-OU context) or include `org_id IN (SELECT org_id FROM mo_glob_org_access_tmp)` for multi-OU access. In the controller, call `MoGlobal.initAccessControl(am)` to initialize the MOAC context before VO execution. At GE, the 5-site rollout used 5 Operating Units under one MOAC security profile — supplier users saw only their site's POs because the supplier's `vendor_site_id` naturally scoped the results, while buyer/surrogate users needed cross-OU visibility.

---
"""

with open(OUT, 'a', encoding='utf-8') as f:
    f.write(CONTENT)

print(f"Appended Sections P & Q (Q201–Q285) to {OUT.name}")
print(f"New file size: {OUT.stat().st_size // 1024} KB")
