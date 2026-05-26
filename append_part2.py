#!/usr/bin/env python3
"""Appends Sections R & S (Q286-Q370) to the interview prep markdown."""
from pathlib import Path

OUT = Path("/Users/himanshu/Desktop/Job/Job Preparation/Interview_Prep_200_QA.md")

CONTENT = """
---

# Section R — Supplier, PO & Receiving Module Tables: Real Queries (Q286–Q325)

**286. Describe the AP_SUPPLIERS table and its key columns.**
`AP_SUPPLIERS` (replaced `PO_VENDORS` as the base table in R12 via TCA integration) stores the master supplier record. Key columns: `VENDOR_ID` (PK), `VENDOR_NAME`, `SEGMENT1` (supplier number), `VENDOR_TYPE_LOOKUP_CODE` (EMPLOYEE, VENDOR, etc.), `ENABLED_FLAG`, `HOLD_FLAG`, `EMPLOYEE_ID` (for employee-type suppliers), `PARTY_ID` (links to `HZ_PARTIES` in TCA), `ONE_TIME_FLAG`, `PAY_GROUP_LOOKUP_CODE`, `TERMS_ID` (payment terms). `STATUS` indicates if the supplier is active. `CREATION_DATE` and `LAST_UPDATE_DATE` are standard WHO columns. Always join to `HZ_PARTIES` for additional supplier attributes like taxpayer ID in a compliant way rather than querying `AP_SUPPLIERS` directly for PII.

**287. What is the relationship between AP_SUPPLIERS and AP_SUPPLIER_SITES_ALL?**
One supplier (`AP_SUPPLIERS`) can have multiple sites (`AP_SUPPLIER_SITES_ALL`) — one per Operating Unit per physical location. Join on `vendor_id`. Key site columns: `VENDOR_SITE_ID` (PK), `VENDOR_ID`, `VENDOR_SITE_CODE`, `ORG_ID` (Operating Unit), `PURCHASING_SITE_FLAG` (`Y` = can raise POs against this site), `PAY_SITE_FLAG` (`Y` = invoices paid from this site), `ADDRESS_LINE1–4`, `CITY`, `STATE`, `ZIP`, `COUNTRY`, `PAYMENT_METHOD_LOOKUP_CODE`, `TERMS_ID`, `INACTIVE_DATE`. A supplier may have a purchasing site in OU1 and a pay site in OU2. Always join with `org_id` to avoid cross-OU duplicates.

**288. What columns in AP_SUPPLIER_SITES_ALL control purchasing and payment behavior?**
For purchasing: `PURCHASING_SITE_FLAG`, `RFQ_ONLY_SITE_FLAG`, `ATTENTION_AR_FLAG`, `SHIP_TO_LOCATION_ID`, `BILL_TO_LOCATION_ID`, `TERMS_ID` (payment terms), `INVOICE_CURRENCY_CODE`, `PAY_CURRENCY_CODE`. For payment: `PAY_SITE_FLAG`, `PAYMENT_METHOD_LOOKUP_CODE`, `BANK_ACCOUNT_NAME`, `HOLD_ALL_PAYMENTS_FLAG`, `HOLD_FUTURE_PAYMENTS_FLAG`. For ERS/self-billing: `CREATE_DEBIT_MEMO_FLAG`. For EDI: `EDI_TRANSACTION_HANDLING`, `EDI_CONNECTION_TYPE`. On the GE project, `SHIP_TO_LOCATION_ID` varied by site and drove which receiving organization defaulted on PO shipments, critical for multi-site routing.

**289. What is the difference between PO_VENDORS and AP_SUPPLIERS in R12?**
In R12, `PO_VENDORS` is a database synonym (or backward-compatible view) that maps to `AP_SUPPLIERS`. The underlying data model shifted to the TCA (Trading Community Architecture) party model where each supplier is an `HZ_PARTY`. `AP_SUPPLIERS` is the proper table; `PO_VENDORS` still works for compatibility. New code should use `AP_SUPPLIERS` and `AP_SUPPLIER_SITES_ALL`. `PO_VENDOR_CONTACTS` similarly is now `AP_SUPPLIER_CONTACTS`. If you see `PO_VENDORS` in existing code, it works but signals legacy code that predates R12 data model consolidation.

**290. How does TCA (Trading Community Architecture) relate to the supplier model in R12?**
Every supplier in R12 is an `HZ_PARTY` of type `ORGANIZATION`. `AP_SUPPLIERS.PARTY_ID` links to `HZ_PARTIES.PARTY_ID`. Supplier contacts are `HZ_PARTY` records of type `PERSON` linked via `HZ_RELATIONSHIPS`. TCA also manages addresses (`HZ_LOCATIONS`, `HZ_PARTY_SITES`). This unification means suppliers and customers share the same party registry, enabling duplicate detection and unified contact management. For iSupplier, `FND_USER.PERSON_PARTY_ID` links the EBS user to their TCA person party, which is how the portal resolves which supplier a logged-in contact belongs to.

**291. What are the key tables for supplier contacts and iSupplier user access?**
`AP_SUPPLIER_CONTACTS` stores supplier contact records (`VENDOR_CONTACT_ID`, `VENDOR_SITE_ID`, `FIRST_NAME`, `LAST_NAME`, `PHONE`, `EMAIL_ADDRESS`, `PARTY_ID`). `FND_USER` stores the EBS login (`USER_ID`, `USER_NAME`, `PERSON_PARTY_ID`). `POS_SUPPLIER_USERS` (or `ICX_PO_SUPPLIER_USERS` in older releases) bridges: (`USER_ID`, `VENDOR_ID`, `VENDOR_SITE_ID`). `FND_USER_RESP_GROUPS_DIRECT` maps users to responsibilities. The chain: `POS_SUPPLIER_USERS.USER_ID = FND_USER.USER_ID = FND_USER_RESP_GROUPS_DIRECT.USER_ID` confirms which supplier users have active iSupplier responsibilities — the key audit join for the GE 100+ supplier access verification.

**292. Describe PO_HEADERS_ALL and its key columns.**
`PO_HEADERS_ALL` stores the PO document header. Key columns: `PO_HEADER_ID` (PK), `SEGMENT1` (PO number), `TYPE_LOOKUP_CODE` (`STANDARD`, `BLANKET`, `PLANNED`, `CONTRACT`), `AUTHORIZATION_STATUS` (`INCOMPLETE`, `IN PROCESS`, `APPROVED`, `REJECTED`, `REQUIRES REAPPROVAL`), `REVISION_NUM`, `VENDOR_ID`, `VENDOR_SITE_ID`, `AGENT_ID` (buyer), `SHIP_TO_LOCATION_ID`, `BILL_TO_LOCATION_ID`, `CURRENCY_CODE`, `ACCEPTANCE_REQUIRED_FLAG`, `ACCEPTANCE_DUE_DATE`, `CLOSED_CODE` (`OPEN`, `CLOSED`, `FINALLY CLOSED`), `CHANGE_REQUESTED_BY` (`SUPPLIER` for iSupplier changes), `ORG_ID`. The `ACCEPTANCE_REQUIRED_FLAG = 'Y'` column drives the iSupplier PO acknowledgement flow.

**293. What does AUTHORIZATION_STATUS in PO_HEADERS_ALL hold and what are its values?**
`AUTHORIZATION_STATUS` tracks the PO approval lifecycle: `INCOMPLETE` (draft, not submitted), `IN PROCESS` (submitted for approval, workflow active), `APPROVED` (fully approved, available for transacting), `REJECTED` (approval rejected by approver), `REQUIRES REAPPROVAL` (approved but subsequently changed, needs re-approval), `PRE-APPROVED` (approved by first approver in chain). Only `APPROVED` POs appear in iSupplier for supplier action. The `CLOSED_CODE` column separately tracks the financial closure: `OPEN`, `CLOSED FOR INVOICING`, `CLOSED FOR RECEIVING`, `CLOSED`, `FINALLY CLOSED`.

**294. What is the difference between PO_LINES_ALL and PO_LINE_LOCATIONS_ALL?**
`PO_LINES_ALL` (PO Line) defines what is being purchased: `PO_LINE_ID`, `LINE_NUM`, `ITEM_ID`, `ITEM_DESCRIPTION`, `UNIT_MEAS_LOOKUP_CODE`, `UNIT_PRICE`, `QUANTITY` (for fixed-price lines), `CATEGORY_ID`, `LINE_TYPE_ID`. One PO header has many lines. `PO_LINE_LOCATIONS_ALL` (PO Shipment) defines where and when it ships: `LINE_LOCATION_ID`, `PO_LINE_ID`, `SHIPMENT_NUM`, `QUANTITY`, `QUANTITY_RECEIVED`, `QUANTITY_BILLED`, `NEED_BY_DATE`, `PROMISED_DATE`, `SHIP_TO_LOCATION_ID`, `ORG_ID`, `CLOSED_CODE`, `QTY_RCV_TOLERANCE`. One line can have multiple shipments (different delivery dates/locations). The GE ASN eligibility engine operated at the shipment level — checking `promised_date`, `quantity_received`, and `closed_code` on `PO_LINE_LOCATIONS_ALL`.

**295. What does SHIPMENT_TYPE in PO_LINE_LOCATIONS_ALL represent?**
`SHIPMENT_TYPE` distinguishes the shipment's origin: `STANDARD` (from a Standard PO), `BLANKET` (a blanket release shipment — joined to `PO_RELEASES_ALL` via `PO_RELEASE_ID`), `SCHEDULED` (from a Planned PO release), `PRICE BREAK` (a price tier on a BPA, not a deliverable shipment). Only `STANDARD` and `BLANKET` type shipments are physically received against in iSupplier. `PRICE BREAK` rows are reference pricing rows on agreements and must be excluded from ASN eligibility queries.

**296. What are PO_DISTRIBUTIONS_ALL columns critical for accounting?**
`PO_DISTRIBUTION_ID` (PK), `LINE_LOCATION_ID`, `PO_LINE_ID`, `PO_HEADER_ID`, `DISTRIBUTION_NUM`, `QUANTITY_ORDERED`, `QUANTITY_DELIVERED`, `QUANTITY_BILLED`, `QUANTITY_CANCELLED`, `CODE_COMBINATION_ID` (the GL charge account — links to `GL_CODE_COMBINATIONS`), `CHARGE_ACCOUNT_ID`, `BUDGET_ACCOUNT_ID`, `ACCRUAL_ACCOUNT_ID`, `VARIANCE_ACCOUNT_ID`, `ORG_ID`, `DESTINATION_TYPE_CODE` (`EXPENSE`, `INVENTORY`, `SHOP FLOOR`), `DELIVER_TO_PERSON_ID`, `DELIVER_TO_LOCATION_ID`. The `CODE_COMBINATION_ID` is joined via `GL_CODE_COMBINATIONS_KFV.CODE_COMBINATION_ID` to get the readable account string.

**297. How do you identify BPA headers vs Standard PO headers in PO_HEADERS_ALL?**
```sql
-- Standard POs:
WHERE ph.type_lookup_code = 'STANDARD'
-- Blanket Purchase Agreements:
WHERE ph.type_lookup_code = 'BLANKET'
-- Planned POs:
WHERE ph.type_lookup_code = 'PLANNED'
-- Contract Purchase Agreements:
WHERE ph.type_lookup_code = 'CONTRACT'
```
BPA releases live in `PO_RELEASES_ALL` with `RELEASE_TYPE = 'BLANKET'`, joined back to the BPA header via `PO_RELEASES_ALL.PO_HEADER_ID = PO_HEADERS_ALL.PO_HEADER_ID`. The GE price-editability bug required querying both the BPA header price (`PO_LINES_ALL.UNIT_PRICE` on the BPA) and the release shipment price (`PO_LINE_LOCATIONS_ALL.PRICE_OVERRIDE`) to determine the correct display price.

**298. Describe RCV_SHIPMENT_HEADERS and its key status values.**
`RCV_SHIPMENT_HEADERS` stores ASN/receipt headers. Key columns: `SHIPMENT_HEADER_ID` (PK), `SHIPMENT_NUM` (ASN number, unique per supplier), `RECEIPT_SOURCE_CODE` (`VENDOR` for supplier ASNs, `INVENTORY` for internal transfers, `CUSTOMER` for returns), `VENDOR_ID`, `VENDOR_SITE_ID`, `SHIP_TO_ORG_ID` (receiving organization), `SHIPPED_DATE`, `EXPECTED_RECEIPT_DATE`, `WAYBILL_AIRBILL_NUM`, `PACKING_SLIP`, `FREIGHT_CARRIER_CODE`, `SHIP_TO_LOCATION_ID`. Status is implicit: if shipment lines are all in `RECEIVED` or `CLOSED` status, the shipment is fully received. There is no explicit header-level "status" column — use `shipment_line_status_code` on `RCV_SHIPMENT_LINES`.

**299. What are key columns in RCV_SHIPMENT_LINES?**
`SHIPMENT_LINE_ID` (PK), `SHIPMENT_HEADER_ID`, `LINE_NUM`, `PO_LINE_LOCATION_ID` (links to `PO_LINE_LOCATIONS_ALL`), `PO_LINE_ID`, `PO_HEADER_ID`, `ITEM_ID`, `ITEM_DESCRIPTION`, `QUANTITY_SHIPPED`, `QUANTITY_RECEIVED`, `UNIT_OF_MEASURE`, `PRIMARY_UNIT_OF_MEASURE`, `SHIPMENT_LINE_STATUS_CODE` (`EXPECTED` = ASN in transit, `FULLY RECEIVED` = all qty received), `COUNTRY_OF_ORIGIN_CODE`, `VENDOR_LOT_NUM` (the custom LOT field added at GE), `FROM_ORGANIZATION_ID`. `QUANTITY_SHIPPED` - `QUANTITY_RECEIVED` = quantity still in transit.

**300. Describe RCV_TRANSACTIONS and its TRANSACTION_TYPE values.**
`RCV_TRANSACTIONS` records every physical receiving action. `TRANSACTION_TYPE` values: `RECEIVE` (physical receipt at dock — creates the receipt record and updates `PLL.QUANTITY_RECEIVED`), `DELIVER` (moves goods from receiving dock to final destination/subinventory), `RETURN TO VENDOR` (sends goods back — reduces `QUANTITY_RECEIVED`), `RETURN TO RECEIVING` (moves from destination back to dock for potential RTV), `CORRECT` (quantity correction against a prior transaction), `MATCH` (matches unordered receipt to a PO), `TRANSFER` (moves between receiving locations). Each transaction has `TRANSACTION_DATE`, `QUANTITY`, `UNIT_OF_MEASURE`, `PO_LINE_LOCATION_ID`, `SHIPMENT_HEADER_ID`, and links back to `RCV_SHIPMENT_LINES.SHIPMENT_LINE_ID`.

**301. What are RCV_HEADERS_INTERFACE and RCV_TRANSACTIONS_INTERFACE used for?**
These are the open interface tables for programmatic ASN/receipt creation. External systems (EDI, custom programs) insert header data into `RCV_HEADERS_INTERFACE` and line data into `RCV_TRANSACTIONS_INTERFACE`. The **Receiving Transaction Processor** concurrent program then validates and processes these rows into `RCV_SHIPMENT_HEADERS` and `RCV_TRANSACTIONS`. If validation fails, errors land in `PO_INTERFACE_ERRORS`. Key columns in `RCV_TRANSACTIONS_INTERFACE`: `TRANSACTION_TYPE` (SHIP for ASN), `PROCESSING_STATUS_CODE` (PENDING/SUCCESS/ERROR), `HEADER_INTERFACE_ID`, `PO_NUMBER`, `DOCUMENT_NUM` (ASN number), `QUANTITY`, `ITEM_ID`, `SHIP_TO_LOCATION_CODE`. The GE ASN creation submitted data via this interface — OAF called PL/SQL that inserted into these tables, then launched the Receiving Transaction Processor.

**302. What does PO_INTERFACE_ERRORS store and how do you use it for debugging?**
`PO_INTERFACE_ERRORS` captures all validation failures from purchasing/receiving open interfaces. Key columns: `INTERFACE_TYPE` (`RCV_HEADERS_INTERFACE`, `RCV_TRANSACTIONS_INTERFACE`, `PO_HEADERS_INTERFACE`, etc.), `INTERFACE_HEADER_ID`, `INTERFACE_LINE_ID`, `TABLE_NAME`, `COLUMN_NAME`, `ERROR_MESSAGE`, `PROCESSING_DATE`. When an ASN fails the Receiving Transaction Processor, query:
```sql
SELECT column_name, error_message
  FROM po_interface_errors
 WHERE interface_header_id = :p_header_interface_id
 ORDER BY processing_date DESC;
```
The `error_message` is the exact Oracle validation that failed — far more specific than the generic "Submission failed" shown to the supplier in iSupplier. At GE, the top error messages from this table drove improvements to ASN validation messaging and supplier training materials.

**303. What are the key WF tables for PO approval and iSupplier notifications?**
`WF_ITEMS` stores the workflow instance (`ITEM_TYPE`, `ITEM_KEY`, `BEGIN_DATE`, `END_DATE`, `USER_KEY`). `WF_ITEM_ACTIVITY_STATUSES` tracks each activity's current state (`ACTIVITY_STATUS`: ACTIVE, COMPLETE, ERROR, NOTIFIED, DEFERRED). `WF_ITEM_ACTIVITY_STATUSES_H` is the history table with completed activities. `WF_NOTIFICATIONS` holds notification records (`NOTIFICATION_ID`, `MESSAGE_TYPE`, `RECIPIENT_ROLE`, `STATUS`, `SUBJECT`, `BEGIN_DATE`, `DUE_DATE`). `WF_NOTIFICATION_ATTRIBUTES` stores per-notification attribute values. For PO approval: `item_type = 'POAPPRV'`, `item_key = po_header_id`. For iSupplier changes: `item_type = 'PONOT'` or `'POSCHNG'`. These tables were queried daily during GE hypercare to verify notification delivery.

**304. What are FND_USER and FND_USER_RESP_GROUPS tables?**
`FND_USER` stores application users: `USER_ID`, `USER_NAME`, `EMAIL_ADDRESS`, `PERSON_PARTY_ID` (TCA link), `START_DATE`, `END_DATE` (null = no expiry), `LAST_LOGON_DATE`, `PASSWORD_DATE`. `FND_USER_RESP_GROUPS_DIRECT` stores direct responsibility assignments: `USER_ID`, `RESPONSIBILITY_ID`, `RESPONSIBILITY_APPLICATION_ID`, `START_DATE`, `END_DATE`. `FND_USER_RESP_GROUPS_ALL` includes both direct and inherited (via role/group) assignments. For audit queries at GE, use `_DIRECT` to see explicitly granted responsibilities, not ones inherited from workflow roles or user groups.

**305. Describe AP_INVOICES_ALL and how it links to PO and receipts.**
`AP_INVOICES_ALL` stores supplier invoice headers: `INVOICE_ID`, `INVOICE_NUM`, `INVOICE_DATE`, `INVOICE_AMOUNT`, `VENDOR_ID`, `VENDOR_SITE_ID`, `ORG_ID`, `INVOICE_TYPE_LOOKUP_CODE` (STANDARD, CREDIT, PREPAYMENT), `SOURCE` (MANUAL, ERS, EDI), `PAYMENT_STATUS_FLAG`, `CANCELLED_DATE`. Link to PO via `AP_INVOICE_DISTRIBUTIONS_ALL.PO_DISTRIBUTION_ID = PO_DISTRIBUTIONS_ALL.PO_DISTRIBUTION_ID`. Link to receipts indirectly via `PO_DISTRIBUTIONS_ALL.LINE_LOCATION_ID = PO_LINE_LOCATIONS_ALL.LINE_LOCATION_ID` then to `RCV_TRANSACTIONS.PO_LINE_LOCATION_ID`. The `MATCH_STATUS_FLAG` on `AP_INVOICE_DISTRIBUTIONS_ALL` tracks: `A` = approved/matched, `N` = needs matching, `T` = tested.

**306. What are PO_CHANGE_REQUESTS and how do supplier changes flow through it?**
`PO_CHANGE_REQUESTS` captures supplier-submitted change requests from iSupplier: `CHANGE_REQUEST_ID`, `DOCUMENT_TYPE` (PO, RELEASE), `DOCUMENT_HEADER_ID` (po_header_id), `DOCUMENT_LINE_ID`, `DOCUMENT_SHIPMENT_ID`, `ACTION_TYPE` (`MODIFICATION`), `REQUEST_STATUS` (PENDING, BUYER_APP, REJECTED, ACCEPTED), `NEW_NEED_BY_DATE`, `NEW_PROMISE_DATE`, `NEW_QUANTITY`, `NEW_PRICE`, `REQUESTER_ID`, `RESPONDER_ID`. After the buyer approves, the PO is updated and `request_status` becomes `ACCEPTED`. At GE, price changes were blocked by making `NEW_PRICE` read-only via OAF personalization before the record even reached this table.

**307. What are the key INV_ORG_PARAMETERS columns relevant to receiving setup?**
`ORGANIZATION_ID`, `ORGANIZATION_CODE`, `ORGANIZATION_NAME`, `RECEIVE_ITEMS_FLAG` (can receive to this org), `RECEIVING_ROUTING_ID` (default receipt routing: 1=Standard, 2=Inspection Required, 3=Direct Delivery), `QTY_RCV_TOLERANCE` (default over-receipt %), `QTY_RCV_EXCEPTION_CODE` (NONE/WARNING/REJECT), `DAYS_EARLY_RECEIPT_ALLOWED`, `DAYS_LATE_RECEIPT_ALLOWED`, `ENFORCE_SHIP_TO_LOCATION_CODE`. These receiving controls flow down to PO shipments as defaults — the GE ASN eligibility engine validated shipment dates against `DAYS_EARLY_RECEIPT_ALLOWED` and `DAYS_LATE_RECEIPT_ALLOWED` from this table.

**308. What are MTL_SYSTEM_ITEMS_B columns relevant to PO and receiving?**
`INVENTORY_ITEM_ID`, `ORGANIZATION_ID` (item is org-specific), `SEGMENT1` (item number), `DESCRIPTION`, `PRIMARY_UOM_CODE`, `PURCHASING_ENABLED_FLAG`, `PURCHASING_ITEM_FLAG`, `INVENTORY_ITEM_FLAG`, `LOT_CONTROL_CODE` (1=No Control, 2=Full Control — drives LOT requirement at receipt), `SERIAL_NUMBER_CONTROL_CODE`, `RECEIPT_REQUIRED_FLAG` (3-way match required if Y), `INSPECTION_REQUIRED_FLAG`, `INVOICE_MATCH_OPTION` (2-way vs 3-way), `QTY_RCV_TOLERANCE`, `TAXABLE_FLAG`. For GE aerospace parts, `LOT_CONTROL_CODE = 2` made LOT capture mandatory at ASN and receipt.

**309. What is HR_ALL_ORGANIZATION_UNITS and how does it relate to Operating Unit in PO?**
`HR_ALL_ORGANIZATION_UNITS` stores all organizations (business groups, legal entities, OUs, inventory orgs). `ORGANIZATION_ID` is the PK. For Operating Units: query where `CLASSIFICATION_CODE = 'OPERATING_UNIT'` via `HR_ORGANIZATION_INFORMATION`. `PO_HEADERS_ALL.ORG_ID` maps to this table's `ORGANIZATION_ID`. `HR_OPERATING_UNITS` is a convenient view filtering to OUs. At GE, the 5 sites mapped to 5 Operating Units in `HR_ALL_ORGANIZATION_UNITS`, and understanding which `org_id` corresponded to which manufacturing site was critical for the multi-OU personalization setup.

**310. Describe GL_CODE_COMBINATIONS and its link to PO distributions.**
`GL_CODE_COMBINATIONS` stores the accounting flexfield (chart of accounts) segment combinations: `CODE_COMBINATION_ID` (PK), `CHART_OF_ACCOUNTS_ID`, individual `SEGMENT1` through `SEGMENT30` columns (each segment is a chart-of-accounts dimension like Company, Department, Account, Cost Center), `ENABLED_FLAG`, `SUMMARY_FLAG`. `GL_CODE_COMBINATIONS_KFV` adds `CONCATENATED_SEGMENTS` as a display column. Join `PO_DISTRIBUTIONS_ALL.CODE_COMBINATION_ID = GL_CODE_COMBINATIONS.CODE_COMBINATION_ID` to get the charge account string. The account derivation for PO distributions follows Purchasing's account generation workflow (typically using `COGS_ACCOUNT_ID` or the PO charge account from the item/category default).

**311. What are PO_ASL_ENTRIES and how do they relate to sourcing and ASN eligibility?**
`PO_ASL_ENTRIES` (Approved Supplier List) stores approved supplier-item-org combinations: `ASL_ID`, `USING_ORGANIZATION_ID`, `OWNER_ORGANIZATION_ID`, `ITEM_ID`, `PRIMARY_VENDOR_ID`, `PRIMARY_VENDOR_SITE_ID`, `ASL_STATUS_ID` (links to `PO_ASL_STATUSES`: Approved, New, Inactive, etc.), `REVIEW_BY_DATE`. Only `ASL_STATUS_ID` corresponding to 'Approved' status allows suppliers to receive POs for that item. The GE ASN eligibility engine optionally checked ASL status to ensure suppliers were still approved for the items they were shipping — flagging cases where ASL approval lapsed but POs existed.

**312. How do you query FND_PROFILE_OPTION_VALUES for a specific profile at responsibility level?**
```sql
SELECT fpot.user_profile_option_name,
       fpov.profile_option_value,
       frt.responsibility_name
  FROM fnd_profile_option_values fpov
  JOIN fnd_profile_options_tl fpot
    ON fpot.profile_option_id = fpov.profile_option_id AND fpot.language='US'
  JOIN fnd_responsibility_tl frt
    ON frt.responsibility_id = fpov.level_value AND frt.language='US'
 WHERE fpov.level_id = 10003  -- Responsibility
   AND fpot.user_profile_option_name LIKE '%Operating Unit%'
ORDER BY frt.responsibility_name;
```
To read a profile value from PL/SQL use `FND_PROFILE.VALUE('PROFILE_OPTION_NAME')` — this returns the value at the highest applicable level for the current session (user > responsibility > application > site).

**313. Where are OAF personalizations stored in the database?**
In MDS (MetaData Services) tables: `JDR_PATHS` (document path/name hierarchy), `JDR_COMPONENTS` (region/item nodes in the page tree), `JDR_ATTRIBUTES` (property name/value pairs per component), `JDR_ELEMENTS` (for XML elements). The base page definitions come from `$OA_HTML` jar files deployed on the filesystem and loaded into MDS at startup. Personalizations are database-only overlays — this is why they survive patching while code file changes can be overwritten. Use `JDR_UTILS` package for programmatic access: `JDR_UTILS.listDocuments`, `JDR_UTILS.printDocument`, `JDR_UTILS.deleteDocument`.

**314. What are the key BNE tables for WebADI integrator definitions?**
`BNE_INTEGRATORS_B/TL/VL` (integrator header — code, name, application), `BNE_INTERFACES_B/TL/VL` (interface definition — links integrator to a target API/table), `BNE_INTERFACE_COLS_B/TL/VL` (interface columns — maps spreadsheet columns to API parameters), `BNE_LAYOUTS_B/TL/VL` (layout definition — visual arrangement of columns), `BNE_LAYOUT_COLS` (per-column layout properties: sequence, prompt, width, required flag), `BNE_CONTENTS_B/TL/VL` (optional content/parameter source for upload). On GE, the Promise Date WebADI integrator was built with a custom interface pointing to a PL/SQL API, and the layout defined exactly which PO columns the user could edit.

**315. Write a SQL to trace a PO from creation through receipt to invoice.**
```sql
SELECT 'PO Header'         AS step, ph.segment1 doc_num, ph.creation_date event_date,
       ph.authorization_status status, NULL qty
  FROM po_headers_all ph WHERE ph.po_header_id = :p_id
UNION ALL
SELECT 'PO Approved', ph.segment1, ph.approved_date, 'APPROVED', NULL
  FROM po_headers_all ph WHERE ph.po_header_id = :p_id AND ph.approved_date IS NOT NULL
UNION ALL
SELECT 'ASN Submitted', rsh.shipment_num, rsh.shipped_date, 'EXPECTED', rsl.quantity_shipped
  FROM rcv_shipment_headers rsh
  JOIN rcv_shipment_lines rsl ON rsl.shipment_header_id = rsh.shipment_header_id
  JOIN po_line_locations_all pll ON pll.line_location_id = rsl.po_line_location_id
  JOIN po_lines_all pl ON pl.po_line_id = pll.po_line_id
 WHERE pl.po_header_id = :p_id AND rsh.receipt_source_code = 'VENDOR'
UNION ALL
SELECT 'Received', rsh.shipment_num, rt.transaction_date, 'RECEIVED', rt.quantity
  FROM rcv_transactions rt
  JOIN rcv_shipment_headers rsh ON rsh.shipment_header_id = rt.shipment_header_id
  JOIN po_line_locations_all pll ON pll.line_location_id = rt.po_line_location_id
  JOIN po_lines_all pl ON pl.po_line_id = pll.po_line_id
 WHERE pl.po_header_id = :p_id AND rt.transaction_type = 'RECEIVE'
UNION ALL
SELECT 'Invoice Matched', ai.invoice_num, ai.invoice_date, ai.payment_status_flag, NULL
  FROM ap_invoices_all ai
  JOIN ap_invoice_distributions_all aid ON aid.invoice_id = ai.invoice_id
  JOIN po_distributions_all pd ON pd.po_distribution_id = aid.po_distribution_id
  JOIN po_lines_all pl ON pl.po_line_id = pd.po_line_id
 WHERE pl.po_header_id = :p_id
ORDER BY event_date;
```

**316. How do you find the promise date change history for a PO acknowledgement?**
```sql
SELECT pcr.change_request_id, pcr.request_status,
       pcr.document_line_id, pcr.document_shipment_id,
       pcr.old_promise_date, pcr.new_promise_date,
       pcr.requester_id, pcr.request_date,
       fu.user_name requester,
       pcr.responder_id, pcr.response_date, pcr.approval_reason
  FROM po_change_requests pcr
  LEFT JOIN fnd_user fu ON fu.user_id = pcr.requester_id
 WHERE pcr.document_header_id = :p_po_header_id
   AND pcr.new_promise_date IS NOT NULL
ORDER BY pcr.request_date;
```
`PO_CHANGE_REQUESTS` tracks every supplier-submitted change. Filtering on `new_promise_date IS NOT NULL` isolates promise-date-specific changes. The GE custom workflow for promise-date approval routed these records through buyer/manager approval before updating `PO_LINE_LOCATIONS_ALL.PROMISED_DATE`.

**317. What is FND_DOCUMENTS and FND_ATTACHED_DOCUMENTS for PO attachments?**
`FND_DOCUMENTS` stores the document metadata: `DOCUMENT_ID`, `DATATYPE_ID` (1=Short Text, 2=Long Text, 3=Image, 5=Web Page, 6=File), `DESCRIPTION`, `CATEGORY_ID`, `SECURITY_TYPE`, `STATUS_TYPE`. `FND_ATTACHED_DOCUMENTS` links documents to entities: `ATTACHED_DOCUMENT_ID`, `DOCUMENT_ID`, `ENTITY_NAME` (e.g., `PO_HEADERS`), `PK1_VALUE` (e.g., `po_header_id`), `SEQ_NUM`. `FND_DOCUMENT_DATATYPES` defines the data type. For actual content: short text in `FND_DOCUMENTS.MEDIA_ID` → `FND_DOCS_ATTRIBUTES`; files in `FND_LOBS`. Useful for querying which POs have supplier instructions or compliance documents attached.

**318. Write a SQL to find supplier bank account details linked to AP setup (safely).**
```sql
SELECT pv.vendor_name, pvs.vendor_site_code,
       ieba.bank_account_name, ieba.bank_account_num,
       ieba.currency_code, ieba.bank_account_type,
       ieb.bank_name, ieb.bank_branch_name
  FROM ap_suppliers pv
  JOIN ap_supplier_sites_all pvs     ON pvs.vendor_id = pv.vendor_id
  JOIN iby_external_payees_all ep    ON ep.payee_party_id = pv.party_id
                                   AND ep.payment_function = 'PAYABLES_DISB'
  JOIN iby_pmt_instr_uses_all ipiu   ON ipiu.ext_pmt_party_id = ep.ext_payee_id
  JOIN iby_ext_bank_accounts ieba    ON ieba.ext_bank_account_id = ipiu.instrument_id
  JOIN iby_ext_banks_v ieb           ON ieb.bank_party_id = ieba.bank_id
 WHERE pvs.pay_site_flag = 'Y'
   AND pv.vendor_id = :p_vendor_id;
```
In R12, bank accounts moved to the IBY (iPayments) schema. `IBY_EXT_BANK_ACCOUNTS` holds external bank accounts; `IBY_EXTERNAL_PAYEES_ALL` links payees (suppliers) to bank accounts. Always handle bank account data with data security controls — restrict this query to DBA/Finance roles.

**319. Write a SQL to find all WebADI uploads and their processing status.**
```sql
SELECT bsl.session_id, bsl.application_id, bsl.filename,
       bsl.creation_date upload_date, bsl.num_rows,
       bsl.status_code, bsl.error_msg,
       fu.user_name uploaded_by
  FROM bne_sessions_log bsl
  LEFT JOIN fnd_user fu ON fu.user_id = bsl.created_by
 WHERE bsl.creation_date >= SYSDATE - 7
ORDER BY bsl.creation_date DESC;
```
`BNE_SESSIONS_LOG` records WebADI upload sessions. Each row error is logged back to the spreadsheet via the WebADI error column — but `status_code` and `error_msg` here give a summary view for admin monitoring of the GE Promise Date bulk-upload tool usage.

**320. Describe the key columns in PO_RELEASES_ALL for BPA release tracking.**
`PO_RELEASE_ID` (PK), `PO_HEADER_ID` (links to the BPA), `RELEASE_NUM`, `RELEASE_TYPE` (`BLANKET` or `SCHEDULED`), `AUTHORIZATION_STATUS` (same values as PO header), `CREATION_DATE`, `APPROVED_DATE`, `REVISED_DATE`, `REVISION_NUM`, `AGENT_ID` (buyer), `COMMENTS`, `CLOSED_CODE`, `CANCELLED_FLAG`. Releases are the actual ordering documents against a BPA. Join to `PO_LINE_LOCATIONS_ALL` via `PO_RELEASE_ID` for the shipment quantities and dates. At GE, the price-editability bug on change requests required checking whether the shipment belonged to a release (BLANKET type) vs a direct Standard PO.

**321. What is the POREQ_INTERFACE table and how does it relate to requisitions?**
`PO_REQUISITIONS_INTERFACE_ALL` (commonly called the Req Interface) is the open interface for importing purchase requisitions from external systems (iProcurement customizations, legacy systems, APIs). Key columns: `INTERFACE_SOURCE_CODE`, `ORG_ID`, `ITEM_ID`, `DESCRIPTION`, `QUANTITY`, `UNIT_PRICE`, `NEED_BY_DATE`, `SUGGESTED_VENDOR_ID`, `DESTINATION_TYPE_CODE`, `PROCESS_FLAG` (PENDING/ACCEPTED/REJECTED). The **Requisition Import** concurrent program processes it into `PO_REQUISITION_HEADERS_ALL` and `PO_REQUISITION_LINES_ALL`. Errors land in `PO_INTERFACE_ERRORS`.

**322. Write a SQL to get on-hand inventory quantity for items received via iSupplier.**
```sql
SELECT msib.segment1 item_number, msib.description,
       moq.subinventory_code,
       SUM(moq.transaction_quantity) on_hand_qty,
       moq.organization_id
  FROM mtl_onhand_quantities_detail moq
  JOIN mtl_system_items_b msib
    ON msib.inventory_item_id = moq.inventory_item_id
   AND msib.organization_id   = moq.organization_id
 WHERE moq.organization_id = :p_org_id
   AND moq.inventory_item_id IN (
         SELECT DISTINCT pl.item_id
           FROM po_lines_all pl
           JOIN po_headers_all ph ON ph.po_header_id = pl.po_header_id
          WHERE ph.vendor_id = :p_vendor_id
            AND pl.item_id IS NOT NULL
       )
GROUP BY msib.segment1, msib.description, moq.subinventory_code, moq.organization_id
ORDER BY msib.segment1;
```

**323. Write a SQL to find all OAF controller substitutions registered in MDS.**
```sql
SELECT jdr_utils.getDocumentName(jp.path_docid) substitution_doc,
       jdc.att_name, jdc.att_value
  FROM jdr_paths jp
  JOIN jdr_attributes jdc ON jdc.doc_id = jp.path_docid
 WHERE jdr_utils.getDocumentName(jp.path_docid) LIKE '%substitution%'
   AND jdc.att_name IN ('controller','am','vo')
ORDER BY jp.path_docid;
```
Controller substitutions are registered in MDS as separate XML documents. `att_name = 'controller'` with `att_value = 'xx.custom.MyController'` tells OAF to use the custom class. After deploying a substitution at GE, the OC4J server needed to be bounced (via CTASK) to flush the MDS cache and pick up the new substitution.

**324. How do you query ICX session attributes for a logged-in iSupplier user?**
```sql
SELECT ics.session_id, ics.vendor_id, ics.vendor_site_id,
       ics.user_id, ics.responsibility_id, ics.language_code,
       ics.creation_date session_start, ics.last_update_date last_activity
  FROM icx_sessions ics
  JOIN fnd_user fu ON fu.user_id = ics.user_id
 WHERE fu.user_name = :p_user_name
   AND ics.disabled_flag = 'N'
ORDER BY ics.last_update_date DESC;
```
`ICX_SESSIONS` stores active web sessions for self-service applications including iSupplier. `vendor_id` and `vendor_site_id` in this table are the session-scoped supplier context used by all iSupplier OAF VOs to enforce row-level security. Understanding this was essential for debugging "wrong supplier's POs showing" issues at GE.

**325. Write a SQL to find all custom FND messages used in iSupplier OAF validations.**
```sql
SELECT fm.message_name, fm.message_text, fm.type,
       fa.application_short_name
  FROM fnd_new_messages fm
  JOIN fnd_application fa ON fa.application_id = fm.application_id
 WHERE fm.message_name LIKE 'XX_%'  -- custom prefix convention
   AND fm.language_code = 'US'
   AND fa.application_short_name IN ('ICX','PO','XX')
ORDER BY fm.message_name;
```
Custom FND messages follow a naming convention (e.g., `XX_ISP_PROMISE_DATE_REQD`). They are migrated using FNDLOAD with the `FNDMSG.lct` lct file: `FNDLOAD apps/pwd 0 Y DOWNLOAD $FND_TOP/patch/115/import/afmdmsg.lct msg.ldt APPLICATION_SHORT_NAME="XX" MESSAGE_NAME="XX_%"`. At GE, all custom validation messages were prefixed `XXGEA_` for easy identification and migration tracking.

---

# Section S — PL/SQL Advanced & Real-time Coding Scenarios (Q326–Q370)

**326. Write a PL/SQL package spec and body to validate ASN headers before submission.**
```sql
CREATE OR REPLACE PACKAGE xxgea_asn_validation_pkg AS
  PROCEDURE validate_asn_header (
    p_shipment_header_id IN  NUMBER,
    p_vendor_id          IN  NUMBER,
    p_waybill            IN  VARCHAR2,
    p_packing_slip       IN  VARCHAR2,
    p_ship_date          IN  DATE,
    x_return_status      OUT VARCHAR2,  -- 'S'=Success 'E'=Error
    x_msg_data           OUT VARCHAR2
  );
END xxgea_asn_validation_pkg;
/

CREATE OR REPLACE PACKAGE BODY xxgea_asn_validation_pkg AS
  PROCEDURE validate_asn_header (
    p_shipment_header_id IN  NUMBER,
    p_vendor_id          IN  NUMBER,
    p_waybill            IN  VARCHAR2,
    p_packing_slip       IN  VARCHAR2,
    p_ship_date          IN  DATE,
    x_return_status      OUT VARCHAR2,
    x_msg_data           OUT VARCHAR2
  ) IS
    l_count NUMBER;
  BEGIN
    x_return_status := 'S';
    -- Mandatory field checks
    IF p_waybill IS NULL THEN
      x_return_status := 'E';
      x_msg_data := 'Waybill/Airbill number is required.';
      RETURN;
    END IF;
    IF p_packing_slip IS NULL THEN
      x_return_status := 'E';
      x_msg_data := 'Packing Slip number is required.';
      RETURN;
    END IF;
    IF p_ship_date > SYSDATE THEN
      x_return_status := 'E';
      x_msg_data := 'Ship Date cannot be in the future.';
      RETURN;
    END IF;
    -- Check duplicate ASN number for this vendor
    SELECT COUNT(*) INTO l_count
      FROM rcv_shipment_headers
     WHERE packing_slip = p_packing_slip
       AND vendor_id    = p_vendor_id
       AND receipt_source_code = 'VENDOR';
    IF l_count > 0 THEN
      x_return_status := 'E';
      x_msg_data := 'Packing Slip ' || p_packing_slip || ' already submitted.';
    END IF;
  EXCEPTION
    WHEN OTHERS THEN
      x_return_status := 'E';
      x_msg_data := 'Unexpected error: ' || SQLERRM;
  END validate_asn_header;
END xxgea_asn_validation_pkg;
/
```
This was the pattern for all GE ASN validation APIs — separate package per functional area, `x_return_status` / `x_msg_data` OUT parameters following the standard Oracle API convention, and `WHEN OTHERS` always capturing `SQLERRM` for logging.

**327. Write a PL/SQL function to auto-generate sequential ASN/Pack-Slip numbers.**
```sql
CREATE OR REPLACE FUNCTION xxgea_get_asn_number (
  p_vendor_id IN NUMBER
) RETURN VARCHAR2 IS
  l_seq  NUMBER;
  l_num  VARCHAR2(30);
BEGIN
  SELECT xxgea_asn_num_s.NEXTVAL INTO l_seq FROM dual;
  l_num := 'ASN-' || TO_CHAR(p_vendor_id) || '-' || LPAD(l_seq, 6, '0');
  RETURN l_num;
EXCEPTION
  WHEN OTHERS THEN
    RETURN 'ASN-ERR-' || TO_CHAR(SYSDATE,'YYYYMMDDHH24MISS');
END;
/
```
At GE, ASN numbers were auto-generated but editable (suppliers could override with their own reference number). The sequence `xxgea_asn_num_s` guaranteed uniqueness across sessions. Pack-Slip numbers used a separate sequence with a different prefix. Both sequences were created in the custom `XX` schema and synonymed into `APPS`.

**328. Write a PL/SQL block using BULK COLLECT with LIMIT to process 500K PO lines for a batch report.**
```sql
DECLARE
  TYPE t_po_rec IS RECORD (
    po_header_id   NUMBER,
    po_number      VARCHAR2(30),
    vendor_id      NUMBER,
    promised_date  DATE,
    need_by_date   DATE,
    open_qty       NUMBER
  );
  TYPE t_po_tab IS TABLE OF t_po_rec;
  l_pos      t_po_tab;
  l_limit    CONSTANT PLS_INTEGER := 1000;
  CURSOR c_pos IS
    SELECT ph.po_header_id, ph.segment1, ph.vendor_id,
           pll.promised_date, pll.need_by_date,
           pll.quantity - NVL(pll.quantity_received,0)
      FROM po_headers_all ph
      JOIN po_lines_all pl ON pl.po_header_id = ph.po_header_id
      JOIN po_line_locations_all pll ON pll.po_line_id = pl.po_line_id
     WHERE ph.authorization_status = 'APPROVED'
       AND pll.closed_code NOT IN ('CLOSED','FINALLY CLOSED');
BEGIN
  OPEN c_pos;
  LOOP
    FETCH c_pos BULK COLLECT INTO l_pos LIMIT l_limit;
    EXIT WHEN l_pos.COUNT = 0;
    FOR i IN 1..l_pos.COUNT LOOP
      -- process each row: insert into staging, calculate metrics, etc.
      INSERT INTO xxgea_po_staging (po_header_id, po_number, open_qty, process_date)
      VALUES (l_pos(i).po_header_id, l_pos(i).po_number, l_pos(i).open_qty, SYSDATE);
    END LOOP;
    COMMIT;  -- commit per batch of 1000 to avoid undo log growth
  END LOOP;
  CLOSE c_pos;
END;
/
```
Always use `LIMIT` with `BULK COLLECT` to cap memory — fetching 500K rows at once will exhaust SGA. `COMMIT` per batch prevents long uncommitted transactions from building undo pressure. The batch size (1000) balances memory vs context-switch frequency.

**329. How do you use a REF CURSOR in a PL/SQL procedure called from OAF?**
```sql
CREATE OR REPLACE PROCEDURE xxgea_get_eligible_shipments (
  p_vendor_id      IN  NUMBER,
  p_org_id         IN  NUMBER,
  x_shipments      OUT SYS_REFCURSOR
) IS
BEGIN
  OPEN x_shipments FOR
    SELECT pll.line_location_id, ph.segment1 po_number,
           pll.need_by_date, pll.promised_date,
           pll.quantity - NVL(pll.quantity_received,0) open_qty
      FROM po_line_locations_all pll
      JOIN po_lines_all pl ON pl.po_line_id = pll.po_line_id
      JOIN po_headers_all ph ON ph.po_header_id = pl.po_header_id
     WHERE ph.vendor_id = p_vendor_id
       AND pll.org_id   = p_org_id
       AND pll.closed_code NOT IN ('CLOSED','FINALLY CLOSED')
     ORDER BY pll.need_by_date;
END;
```
In the OAF AM, call via `OADBTransaction.callProcedure` or `createCallableStatement` with `registerOutParameter(1, OracleTypes.CURSOR)`. Then `rs = (ResultSet) cs.getObject(1)` to iterate the result set. In modern OAF Expert Mode VOs, the VO's SQL directly joins the tables — REF CURSORs from PL/SQL are most useful when the eligibility logic is too complex for a single SQL and needs PL/SQL procedural steps.

**330. Write a trigger that logs changes to PO_HEADERS_ALL to an audit table.**
```sql
CREATE OR REPLACE TRIGGER xxgea_po_audit_trg
AFTER UPDATE OF authorization_status, revision_num, acceptance_required_flag
ON po_headers_all
FOR EACH ROW
DECLARE
  PRAGMA AUTONOMOUS_TRANSACTION;
BEGIN
  INSERT INTO xxgea_po_audit_log (
    audit_id, po_header_id, po_number, old_auth_status, new_auth_status,
    old_revision, new_revision, changed_by, change_date
  ) VALUES (
    xxgea_audit_s.NEXTVAL, :OLD.po_header_id, :OLD.segment1,
    :OLD.authorization_status, :NEW.authorization_status,
    :OLD.revision_num, :NEW.revision_num,
    :NEW.last_updated_by, SYSDATE
  );
  COMMIT;  -- autonomous transaction commit
EXCEPTION
  WHEN OTHERS THEN
    ROLLBACK;  -- don't let audit failure break the main transaction
END;
/
```
`PRAGMA AUTONOMOUS_TRANSACTION` is essential for audit triggers — the `COMMIT` applies only to the audit insert, not the main PO update transaction. Without it, committing inside an AFTER trigger would raise `ORA-04092`. Triggers on base EBS tables should be used sparingly and with caution around patching.

**331. Write a PL/SQL block using dynamic SQL to build a WHERE clause from runtime parameters.**
```sql
DECLARE
  l_sql    VARCHAR2(4000);
  l_where  VARCHAR2(2000) := ' WHERE 1=1';
  l_binds  DBMS_SQL.VARCHAR2_TABLE;
  l_bind_cnt PLS_INTEGER := 0;
  TYPE t_ref IS REF CURSOR;
  l_cur  t_ref;
  l_po_num VARCHAR2(30);
BEGIN
  IF :p_vendor_id IS NOT NULL THEN
    l_where := l_where || ' AND ph.vendor_id = :b_vendor';
    l_bind_cnt := l_bind_cnt + 1;
  END IF;
  IF :p_date_from IS NOT NULL THEN
    l_where := l_where || ' AND ph.creation_date >= :b_date_from';
    l_bind_cnt := l_bind_cnt + 1;
  END IF;

  l_sql := 'SELECT ph.segment1 FROM po_headers_all ph' || l_where;

  -- Use EXECUTE IMMEDIATE with USING clause for clean bind
  IF :p_vendor_id IS NOT NULL AND :p_date_from IS NOT NULL THEN
    OPEN l_cur FOR l_sql USING :p_vendor_id, :p_date_from;
  ELSIF :p_vendor_id IS NOT NULL THEN
    OPEN l_cur FOR l_sql USING :p_vendor_id;
  ELSE
    OPEN l_cur FOR l_sql;
  END IF;

  LOOP
    FETCH l_cur INTO l_po_num;
    EXIT WHEN l_cur%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(l_po_num);
  END LOOP;
  CLOSE l_cur;
END;
```
Always use `USING` clause bind variables with `EXECUTE IMMEDIATE` — never concatenate user input directly into the SQL string. For complex multi-parameter scenarios with varying bind counts, `DBMS_SQL` package gives more control but is more verbose. On GE, the WebADI validation procedure used this pattern to dynamically validate against different sets of rules based on PO type.

**332. Write a PL/SQL procedure to send a custom Oracle Workflow notification.**
```sql
CREATE OR REPLACE PROCEDURE xxgea_send_promise_alert (
  p_po_header_id  IN NUMBER,
  p_recipient     IN VARCHAR2,  -- FND username or role
  p_old_date      IN DATE,
  p_new_date      IN DATE
) IS
  l_nid    NUMBER;
  l_item_key VARCHAR2(100) := 'PROMISE_CHG_' || p_po_header_id || '_' || TO_CHAR(SYSDATE,'YYYYMMDDHH24MISS');
BEGIN
  -- Create workflow item
  WF_ENGINE.CreateProcess(
    itemtype  => 'XXPROMIS',
    itemkey   => l_item_key,
    process   => 'PROMISE_DATE_CHANGE'
  );
  -- Set item attributes
  WF_ENGINE.SetItemAttrNumber('XXPROMIS', l_item_key, 'PO_HEADER_ID', p_po_header_id);
  WF_ENGINE.SetItemAttrDate('XXPROMIS',   l_item_key, 'OLD_DATE',     p_old_date);
  WF_ENGINE.SetItemAttrDate('XXPROMIS',   l_item_key, 'NEW_DATE',     p_new_date);
  WF_ENGINE.SetItemAttrText('XXPROMIS',   l_item_key, 'RECIPIENT',    p_recipient);
  -- Start the process
  WF_ENGINE.StartProcess(itemtype => 'XXPROMIS', itemkey => l_item_key);
EXCEPTION
  WHEN OTHERS THEN
    FND_FILE.PUT_LINE(FND_FILE.LOG, 'WF Error: ' || SQLERRM);
END;
```
This was the core of the GE promise-date notification suppression solution — instead of using the seeded notification (which fired for every promise-date change), we routed through a custom workflow item type `XXPROMIS` that applied business rules before notifying planners.

**333. Write a PL/SQL concurrent program procedure (errbuf/retcode pattern).**
```sql
CREATE OR REPLACE PROCEDURE xxgea_asn_compliance_report (
  errbuf     OUT VARCHAR2,
  retcode    OUT VARCHAR2,
  p_org_id   IN  NUMBER,
  p_days     IN  NUMBER DEFAULT 30
) IS
  l_count PLS_INTEGER := 0;
BEGIN
  retcode := '0';  -- Success
  FND_FILE.PUT_LINE(FND_FILE.LOG, 'Starting ASN Compliance Report. Org: ' || p_org_id);

  FOR r IN (
    SELECT pv.vendor_name, COUNT(*) asn_count
      FROM rcv_shipment_headers rsh
      JOIN po_headers_all ph ON ph.vendor_id = rsh.vendor_id
      JOIN ap_suppliers pv   ON pv.vendor_id = rsh.vendor_id
     WHERE rsh.receipt_source_code = 'VENDOR'
       AND rsh.ship_to_org_id      = p_org_id
       AND rsh.creation_date      >= SYSDATE - p_days
    GROUP BY pv.vendor_name
    ORDER BY asn_count DESC
  ) LOOP
    FND_FILE.PUT_LINE(FND_FILE.OUTPUT, RPAD(r.vendor_name,40) || r.asn_count);
    l_count := l_count + 1;
  END LOOP;

  FND_FILE.PUT_LINE(FND_FILE.LOG, 'Completed. Rows: ' || l_count);
EXCEPTION
  WHEN OTHERS THEN
    errbuf  := SQLERRM;
    retcode := '2';  -- Error
    FND_FILE.PUT_LINE(FND_FILE.LOG, 'Error: ' || SQLERRM);
END;
/
```
`retcode = '0'` = Success, `'1'` = Warning, `'2'` = Error. Always use `FND_FILE.PUT_LINE(FND_FILE.LOG,...)` for log output and `FND_FILE.PUT_LINE(FND_FILE.OUTPUT,...)` for the report output. The `EXCEPTION` block must always set `retcode = '2'` and populate `errbuf` — otherwise the CM shows the request as Completed Normal even when it crashed.

**334. Write a MERGE statement to upsert supplier data into a staging table.**
```sql
MERGE INTO xxgea_supplier_staging tgt
USING (
  SELECT pv.vendor_id, pv.vendor_name, pv.segment1 vendor_num,
         pvs.vendor_site_id, pvs.vendor_site_code, pvs.org_id,
         pvs.city, pvs.country, pvs.email_address
    FROM ap_suppliers pv
    JOIN ap_supplier_sites_all pvs ON pvs.vendor_id = pv.vendor_id
   WHERE pvs.purchasing_site_flag = 'Y'
) src
ON (tgt.vendor_site_id = src.vendor_site_id AND tgt.org_id = src.org_id)
WHEN MATCHED THEN
  UPDATE SET tgt.vendor_name    = src.vendor_name,
             tgt.vendor_num     = src.vendor_num,
             tgt.city           = src.city,
             tgt.last_sync_date = SYSDATE
WHEN NOT MATCHED THEN
  INSERT (vendor_id, vendor_name, vendor_num, vendor_site_id,
          vendor_site_code, org_id, city, country, last_sync_date)
  VALUES (src.vendor_id, src.vendor_name, src.vendor_num, src.vendor_site_id,
          src.vendor_site_code, src.org_id, src.city, src.country, SYSDATE);
```
`MERGE` is the most efficient upsert pattern — one SQL statement replaces separate EXISTS-check + INSERT/UPDATE logic. Used at GE to sync supplier master data from the EBS into a custom reporting table nightly via a concurrent program.

**335. How do you implement retry logic in a PL/SQL integration procedure?**
```sql
PROCEDURE call_external_api (p_po_id IN NUMBER) IS
  l_max_retries  CONSTANT PLS_INTEGER := 3;
  l_retry_wait   CONSTANT PLS_INTEGER := 5;  -- seconds
  l_attempt      PLS_INTEGER := 0;
  l_success      BOOLEAN := FALSE;
BEGIN
  WHILE l_attempt < l_max_retries AND NOT l_success LOOP
    l_attempt := l_attempt + 1;
    BEGIN
      -- call HTTP or pipeline procedure
      xxgea_http_pkg.post_po_data(p_po_id);
      l_success := TRUE;
    EXCEPTION
      WHEN OTHERS THEN
        FND_FILE.PUT_LINE(FND_FILE.LOG,
          'Attempt ' || l_attempt || ' failed: ' || SQLERRM);
        IF l_attempt < l_max_retries THEN
          DBMS_LOCK.SLEEP(l_retry_wait * l_attempt);  -- exponential backoff
        END IF;
    END;
  END LOOP;
  IF NOT l_success THEN
    RAISE_APPLICATION_ERROR(-20001, 'API call failed after ' || l_max_retries || ' attempts');
  END IF;
END;
```
Exponential backoff (`wait * attempt`) prevents hammering a down service. Cap retries at 3 — more than that in a synchronous flow will block user sessions. For async integrations (concurrent programs), use a status table to track retry state across program executions.

**336. Write a PL/SQL procedure to implement idempotent interface table inserts.**
```sql
PROCEDURE insert_asn_interface (p_asn_rec IN xxgea_asn_rec_type) IS
  l_exists NUMBER;
BEGIN
  -- Idempotency check: same packing_slip + vendor_id = already submitted
  SELECT COUNT(*) INTO l_exists
    FROM rcv_headers_interface
   WHERE vendor_id    = p_asn_rec.vendor_id
     AND packing_slip = p_asn_rec.packing_slip
     AND processing_status_code != 'ERROR';  -- allow resubmit of errored ones

  IF l_exists > 0 THEN
    FND_FILE.PUT_LINE(FND_FILE.LOG,
      'Skipping duplicate ASN: ' || p_asn_rec.packing_slip);
    RETURN;
  END IF;

  INSERT INTO rcv_headers_interface (
    header_interface_id, group_id, processing_status_code,
    receipt_source_code, transaction_type, vendor_id, packing_slip,
    ship_to_organization_id, expected_receipt_date, shipped_date,
    waybill_airbill_num, creation_date, created_by
  ) VALUES (
    rcv_headers_interface_s.NEXTVAL, rcv_interface_groups_s.NEXTVAL,
    'PENDING', 'VENDOR', 'NEW', p_asn_rec.vendor_id, p_asn_rec.packing_slip,
    p_asn_rec.ship_to_org_id, p_asn_rec.expected_date, p_asn_rec.shipped_date,
    p_asn_rec.waybill, SYSDATE, FND_GLOBAL.USER_ID
  );
  COMMIT;
END;
```

**337. How do you write a PL/SQL error handler that captures the full call stack?**
```sql
EXCEPTION
  WHEN OTHERS THEN
    DECLARE
      l_stack VARCHAR2(4000) := DBMS_UTILITY.FORMAT_ERROR_STACK
                              || CHR(10)
                              || DBMS_UTILITY.FORMAT_ERROR_BACKTRACE;
    BEGIN
      INSERT INTO xxgea_error_log (
        error_id, program_name, error_code, error_message,
        error_stack, created_by, creation_date
      ) VALUES (
        xxgea_error_s.NEXTVAL, $$PLSQL_UNIT,
        SQLCODE, SQLERRM, l_stack,
        FND_GLOBAL.USER_ID, SYSDATE
      );
      COMMIT;  -- autonomous or use pragma
      RAISE;   -- re-raise to let caller know
    END;
```
`DBMS_UTILITY.FORMAT_ERROR_BACKTRACE` (Oracle 10g+) gives the line number where the error originated even if it was re-raised — far more useful than `SQLERRM` alone. `$$PLSQL_UNIT` is a compile-time directive returning the current package/procedure name. Always re-raise after logging unless you intentionally want to swallow the exception.

**338. Write a PL/SQL package to validate PO acknowledgement eligibility before ASN creation.**
```sql
CREATE OR REPLACE PACKAGE BODY xxgea_asn_elig_pkg AS
  FUNCTION is_ack_required (p_line_location_id IN NUMBER) RETURN BOOLEAN IS
    l_ack_flag   VARCHAR2(1);
    l_accepted   VARCHAR2(1);
    l_rev_num    NUMBER;
  BEGIN
    SELECT ph.acceptance_required_flag, ph.revision_num
      INTO l_ack_flag, l_rev_num
      FROM po_line_locations_all pll
      JOIN po_lines_all pl ON pl.po_line_id = pll.po_line_id
      JOIN po_headers_all ph ON ph.po_header_id = pl.po_header_id
     WHERE pll.line_location_id = p_line_location_id;

    IF NVL(l_ack_flag,'N') = 'N' THEN
      RETURN FALSE;  -- no ack needed
    END IF;

    SELECT NVL(MAX(CASE WHEN pa.accepted_flag='Y' THEN 'Y' END),'N')
      INTO l_accepted
      FROM po_acceptances pa
     WHERE pa.po_header_id = (SELECT ph.po_header_id FROM po_line_locations_all pll
                               JOIN po_lines_all pl ON pl.po_line_id = pll.po_line_id
                               JOIN po_headers_all ph ON ph.po_header_id = pl.po_header_id
                              WHERE pll.line_location_id = p_line_location_id)
       AND pa.revision_num = l_rev_num;

    RETURN (l_accepted = 'N');  -- TRUE = ack still required (block ASN)
  END is_ack_required;
END xxgea_asn_elig_pkg;
```

**339. How do you use PRAGMA AUTONOMOUS_TRANSACTION for error logging?**
Declare `PRAGMA AUTONOMOUS_TRANSACTION` in the logging procedure's declaration section. This runs the procedure in a separate transaction from the caller — so even if the caller rolls back (due to an error), the log record is committed independently. Critical pattern for audit and error logging: without it, a rolled-back main transaction would also rollback your error log entry, defeating the purpose. At GE, all custom error-logging procedures used this pragma to ensure errors were always captured in `XXGEA_ERROR_LOG` regardless of main transaction outcome.

**340. Write a SQL using analytic functions to identify the first ASN per PO shipment.**
```sql
SELECT po_number, shipment_num, vendor_name,
       asn_num, shipped_date, qty_shipped,
       CASE WHEN rn = 1 THEN 'FIRST ASN' ELSE 'SUBSEQUENT' END asn_order
  FROM (
    SELECT ph.segment1 po_number, pll.shipment_num, pv.vendor_name,
           rsh.shipment_num asn_num, rsh.shipped_date, rsl.quantity_shipped,
           ROW_NUMBER() OVER (
             PARTITION BY pll.line_location_id
             ORDER BY rsh.shipped_date
           ) rn
      FROM rcv_shipment_lines rsl
      JOIN rcv_shipment_headers rsh ON rsh.shipment_header_id = rsl.shipment_header_id
      JOIN po_line_locations_all pll ON pll.line_location_id = rsl.po_line_location_id
      JOIN po_lines_all pl ON pl.po_line_id = pll.po_line_id
      JOIN po_headers_all ph ON ph.po_header_id = pl.po_header_id
      JOIN ap_suppliers pv ON pv.vendor_id = ph.vendor_id
     WHERE rsh.receipt_source_code = 'VENDOR'
  )
ORDER BY po_number, shipment_num, rn;
```

**341. Write a PL/SQL block to auto-generate Pack Slip numbers with sequence and vendor prefix.**
```sql
FUNCTION get_pack_slip_num (
  p_vendor_site_code IN VARCHAR2
) RETURN VARCHAR2 IS
  l_seq NUMBER;
BEGIN
  SELECT xxgea_pack_slip_s.NEXTVAL INTO l_seq FROM dual;
  RETURN UPPER(SUBSTR(p_vendor_site_code,1,4))
         || '-PS-'
         || LPAD(l_seq, 8, '0');
EXCEPTION
  WHEN OTHERS THEN
    RETURN 'PS-' || TO_CHAR(SYSDATE,'YYYYMMDDHH24MISS') || '-' || l_seq;
END;
```
At GE, auto-generated Pack Slip numbers used a format like `SITE-PS-00001234` with the first 4 characters of the vendor site code as prefix, making them human-readable and traceable back to the originating site. Suppliers could override with their own reference.

**342. How do you call the standard PO change API from PL/SQL?**
```sql
DECLARE
  l_api_errors   PO_API_ERRORS_REC_TYPE;
  l_return_status VARCHAR2(1);
BEGIN
  PO_DOCUMENT_UPDATE_GRP.update_document (
    p_api_version      => 1.0,
    p_init_msg_list    => FND_API.G_TRUE,
    x_return_status    => l_return_status,
    x_api_errors       => l_api_errors,
    p_changes          => l_changes,  -- PO_CHANGES_REC_TYPE
    p_run_submission_checks => FND_API.G_TRUE,
    p_launch_approvals => FND_API.G_FALSE
  );
  IF l_return_status != FND_API.G_RET_STS_SUCCESS THEN
    RAISE_APPLICATION_ERROR(-20001, l_api_errors.message_text(1));
  END IF;
END;
```
Use Oracle standard PO APIs (`PO_DOCUMENT_UPDATE_GRP`, `PO_CHANGE_API1_S`) rather than direct DML on `PO_HEADERS_ALL` — direct updates bypass business validations, break audit trails, and skip workflow triggers. At GE, promise-date updates via WebADI called `PO_CHANGE_API1_S.update_document` to ensure proper revision tracking.

**343. Write a PL/SQL block to validate LOT/UPN numbers at ASN creation.**
```sql
PROCEDURE validate_lot_num (
  p_item_id     IN  NUMBER,
  p_org_id      IN  NUMBER,
  p_lot_num     IN  VARCHAR2,
  x_status      OUT VARCHAR2,
  x_message     OUT VARCHAR2
) IS
  l_lot_cnt  NUMBER;
  l_lot_ctrl NUMBER;
BEGIN
  x_status := 'S';
  -- Check item LOT control
  SELECT NVL(lot_control_code,1)
    INTO l_lot_ctrl
    FROM mtl_system_items_b
   WHERE inventory_item_id = p_item_id
     AND organization_id   = p_org_id;

  IF l_lot_ctrl = 1 THEN  -- No lot control
    RETURN;
  END IF;

  IF p_lot_num IS NULL THEN
    x_status  := 'E';
    x_message := 'Vendor LOT number is required for this item.';
    RETURN;
  END IF;

  -- Optionally validate against existing approved lots
  SELECT COUNT(*) INTO l_lot_cnt
    FROM mtl_lot_numbers
   WHERE inventory_item_id = p_item_id
     AND organization_id   = p_org_id
     AND lot_number        = p_lot_num
     AND (expiration_date IS NULL OR expiration_date > SYSDATE);

  -- For GE: new lots are allowed; just ensure format is correct
  IF LENGTH(p_lot_num) < 3 THEN
    x_status  := 'E';
    x_message := 'LOT number must be at least 3 characters.';
  END IF;
END;
```

**344. How do you diagnose and fix a mutating table error in an EBS trigger?**
A mutating table error (`ORA-04091`) occurs when a row-level trigger tries to query or modify the table it fired on. The cleanest fix is a **compound trigger** (Oracle 11g+): collect affected rowids in the BEFORE EACH ROW section into a package-level collection, then process them in the AFTER STATEMENT section after the DML is complete. Alternatively, use a package-level collection populated in the BEFORE EACH ROW trigger and processed in a separate AFTER STATEMENT trigger. At GE, a trigger on `RCV_TRANSACTIONS` that tried to aggregate `quantity_received` from the same table caused this — resolved by moving the aggregation to the AFTER STATEMENT section of a compound trigger.

**345. Write a PL/SQL procedure to fix Promise Date data for the GE defaulting issue.**
```sql
PROCEDURE fix_promise_date_defaults (
  p_from_date IN DATE DEFAULT SYSDATE - 90,
  p_commit    IN VARCHAR2 DEFAULT 'N'
) IS
  l_count PLS_INTEGER := 0;
BEGIN
  FND_FILE.PUT_LINE(FND_FILE.LOG,'Fixing Promise Date defaults from ' || p_from_date);

  -- Null out promise dates that equal need_by_date (they were auto-defaulted)
  UPDATE po_line_locations_all pll
     SET pll.promised_date     = NULL,
         pll.last_update_date  = SYSDATE,
         pll.last_updated_by   = FND_GLOBAL.USER_ID
   WHERE TRUNC(pll.promised_date) = TRUNC(pll.need_by_date)
     AND pll.last_update_date    >= p_from_date
     AND EXISTS (
           SELECT 1 FROM po_acceptances pa
            JOIN po_lines_all pl ON pl.po_line_id = pll.po_line_id
           WHERE pa.po_header_id = pl.po_header_id
             AND pa.accepted_flag = 'Y'
         );

  l_count := SQL%ROWCOUNT;
  FND_FILE.PUT_LINE(FND_FILE.LOG,'Updated ' || l_count || ' rows');

  IF p_commit = 'Y' THEN
    COMMIT;
  ELSE
    ROLLBACK;  -- dry-run by default
    FND_FILE.PUT_LINE(FND_FILE.LOG,'DRY RUN - rolled back');
  END IF;
END;
```
Always include a dry-run mode (`p_commit = 'N'`) for data-fix scripts. Run first in DEV, validate the count, then UAT, then PROD with a CTASK. Log the row count so the change is auditable.

**346. How do you use FND_GLOBAL and FND_PROFILE in PL/SQL for session context?**
`FND_GLOBAL.USER_ID` returns the current user's `FND_USER.USER_ID`. `FND_GLOBAL.RESP_ID` returns the current responsibility ID. `FND_GLOBAL.ORG_ID` returns the current Operating Unit (set by MOAC). `FND_PROFILE.VALUE('PROFILE_NAME')` returns a profile option value at the highest applicable level for the current session. In concurrent programs, call `FND_GLOBAL.APPS_INITIALIZE(user_id, resp_id, resp_appl_id)` at the start to set up the session context before calling any EBS APIs. Without this, API calls that check `FND_GLOBAL` will get null values and may fail silently.

**347. Write a PL/SQL block to submit a concurrent request from PL/SQL.**
```sql
DECLARE
  l_request_id NUMBER;
BEGIN
  FND_GLOBAL.APPS_INITIALIZE(
    user_id      => FND_GLOBAL.USER_ID,
    resp_id      => FND_GLOBAL.RESP_ID,
    resp_appl_id => FND_GLOBAL.RESP_APPL_ID
  );

  l_request_id := FND_REQUEST.SUBMIT_REQUEST(
    application => 'PO',
    program     => 'RVCTP',   -- Receiving Transaction Processor
    description => 'Process ASN Interface - GEA',
    start_time  => NULL,      -- run immediately
    sub_request => FALSE,
    argument1   => 'PROCESS',
    argument2   => TO_CHAR(:p_org_id),
    argument3   => NULL
  );

  IF l_request_id = 0 THEN
    RAISE_APPLICATION_ERROR(-20001, 'Failed to submit Receiving Transaction Processor');
  END IF;

  COMMIT;  -- required to actually submit the request
  FND_FILE.PUT_LINE(FND_FILE.LOG, 'Submitted request ID: ' || l_request_id);
END;
```
The `COMMIT` after `FND_REQUEST.SUBMIT_REQUEST` is mandatory — the request is queued via a database table insert that must be committed for the concurrent manager to pick it up.

**348. Write a PL/SQL block to read the last N lines of a concurrent request log.**
```sql
DECLARE
  l_req_id   NUMBER := :p_request_id;
  l_logfile  VARCHAR2(512);
  l_file     UTL_FILE.FILE_TYPE;
  l_line     VARCHAR2(4000);
  l_lines    DBMS_SQL.VARCHAR2_TABLE;
  l_idx      PLS_INTEGER := 0;
BEGIN
  SELECT logfile_name INTO l_logfile
    FROM fnd_concurrent_requests WHERE request_id = l_req_id;

  l_file := UTL_FILE.FOPEN('APPLCSF', l_logfile, 'R', 32767);
  LOOP
    BEGIN
      UTL_FILE.GET_LINE(l_file, l_line);
      l_idx := l_idx + 1;
      l_lines(l_idx) := l_line;
    EXCEPTION WHEN NO_DATA_FOUND THEN EXIT;
    END;
  END LOOP;
  UTL_FILE.FCLOSE(l_file);

  -- Print last 20 lines
  FOR i IN GREATEST(1, l_idx-19)..l_idx LOOP
    DBMS_OUTPUT.PUT_LINE(l_lines(i));
  END LOOP;
END;
```
This pattern was used at GE during hypercare when server log access was restricted — a DBA would run this PL/SQL block to pull the tail of any failing concurrent request log without needing OS access.

**349. How do you implement the errbuf/retcode pattern with FND_FILE for a BI Publisher data template?**
In a PL/SQL procedure registered as the data source for a BIP report (with executable method `PL/SQL Stored Procedure` and output type `XML`): generate the XML document to `FND_FILE.OUTPUT` using `DBMS_XMLGEN` or manual XML construction. Log progress to `FND_FILE.LOG`. Set `retcode='2'` and `errbuf=SQLERRM` on any exception. For large datasets, use `DBMS_XMLGEN.getXML(cursor_handle)` with chunking to avoid memory pressure. At GE, the Collaboration History report's data model was a PL/SQL procedure that queried `RCV_SHIPMENT_HEADERS` and wrote XML to output — BIP then applied the RTF template to produce the formatted PDF/Excel.

**350. Write a PL/SQL block to process all rows in a large table and report per-row errors without stopping.**
```sql
DECLARE
  l_errors    PLS_INTEGER := 0;
  l_processed PLS_INTEGER := 0;
BEGIN
  FOR r IN (SELECT rowid rid, vendor_id, packing_slip
              FROM rcv_shipment_headers
             WHERE receipt_source_code = 'VENDOR'
               AND shipped_date >= SYSDATE - 30) LOOP
    BEGIN
      -- process each row
      xxgea_validate_pkg.check_shipment(r.vendor_id, r.packing_slip);
      l_processed := l_processed + 1;
    EXCEPTION
      WHEN OTHERS THEN
        l_errors := l_errors + 1;
        -- Log but continue
        INSERT INTO xxgea_batch_errors (rid, error_msg, error_date)
        VALUES (r.rid, SQLERRM, SYSDATE);
        -- Don't COMMIT here - batch commit at end or use autonomous
    END;
  END LOOP;

  COMMIT;
  FND_FILE.PUT_LINE(FND_FILE.LOG,
    'Processed: ' || l_processed || ', Errors: ' || l_errors);
  IF l_errors > 0 THEN
    retcode := '1';  -- Warning
    errbuf  := l_errors || ' rows had errors - see XXGEA_BATCH_ERRORS';
  END IF;
END;
```
The inner `BEGIN...EXCEPTION...END` block catches per-row errors without stopping the loop. Committing at the end (not per-row) is usually more efficient — but for very long batches, commit per N rows to limit undo growth.

**351. Write a PL/SQL procedure to populate the RCV interface tables for a programmatic ASN.**
```sql
PROCEDURE create_asn_programmatic (
  p_vendor_id    IN NUMBER,
  p_po_header_id IN NUMBER,
  p_qty          IN NUMBER,
  p_waybill      IN VARCHAR2
) IS
  l_hdr_id   NUMBER;
  l_grp_id   NUMBER;
  l_txn_id   NUMBER;
BEGIN
  SELECT rcv_headers_interface_s.NEXTVAL INTO l_hdr_id FROM dual;
  SELECT rcv_interface_groups_s.NEXTVAL   INTO l_grp_id FROM dual;
  SELECT rcv_transactions_interface_s.NEXTVAL INTO l_txn_id FROM dual;

  INSERT INTO rcv_headers_interface (
    header_interface_id, group_id, processing_status_code,
    receipt_source_code, transaction_type, auto_transact_code,
    vendor_id, waybill_airbill_num, shipped_date, expected_receipt_date,
    validation_flag, created_by, creation_date
  ) VALUES (
    l_hdr_id, l_grp_id, 'PENDING', 'VENDOR', 'NEW', 'RECEIVE',
    p_vendor_id, p_waybill, SYSDATE, SYSDATE+3,
    'Y', FND_GLOBAL.USER_ID, SYSDATE
  );

  INSERT INTO rcv_transactions_interface (
    interface_transaction_id, header_interface_id, group_id,
    transaction_type, processing_status_code,
    quantity, unit_of_measure, po_header_id,
    receipt_source_code, auto_transact_code,
    transaction_date, validation_flag, created_by, creation_date
  ) VALUES (
    l_txn_id, l_hdr_id, l_grp_id,
    'SHIP', 'PENDING',
    p_qty, 'Each', p_po_header_id,
    'VENDOR', 'RECEIVE',
    SYSDATE, 'Y', FND_GLOBAL.USER_ID, SYSDATE
  );

  COMMIT;
  -- Now launch Receiving Transaction Processor
  xxgea_asn_pkg.launch_rcv_processor(l_grp_id);
END;
```

**352. How do you diagnose a long-running PL/SQL batch that is blocking other sessions?**
First identify the blocking session: `SELECT s.sid, s.serial#, s.username, s.status, s.blocking_session, q.sql_text FROM v$session s LEFT JOIN v$sql q ON q.sql_id = s.sql_id WHERE s.blocking_session IS NOT NULL`. Get the exact SQL being run by the blocker from `V$SQL`. If it's your batch, check for missing commit between iterations (row-level lock accumulation) or a table-level lock from a DDL operation. Check `V$LOCK` and `V$LOCKED_OBJECT` to identify the locked objects. Fix by adding periodic `COMMIT` in the batch loop, using `SELECT FOR UPDATE SKIP LOCKED` to allow concurrent processing, or scheduling the batch during off-hours.

**353. Write a PL/SQL function to check ASN eligibility based on Need-by date window.**
```sql
FUNCTION is_eligible_for_asn (
  p_line_location_id IN NUMBER,
  p_org_id           IN NUMBER
) RETURN VARCHAR2 IS  -- 'Y'=eligible, 'N'=not, 'R'=ack required
  l_need_by      DATE;
  l_days_early   NUMBER;
  l_days_late    NUMBER;
  l_closed_code  VARCHAR2(30);
  l_open_qty     NUMBER;
  l_ack_reqd     VARCHAR2(1);
  l_ack_done     VARCHAR2(1) := 'Y';
BEGIN
  SELECT pll.need_by_date, pll.closed_code,
         pll.quantity - NVL(pll.quantity_received,0),
         NVL(iop.days_early_receipt_allowed,0),
         NVL(iop.days_late_receipt_allowed,0),
         ph.acceptance_required_flag
    INTO l_need_by, l_closed_code, l_open_qty,
         l_days_early, l_days_late, l_ack_reqd
    FROM po_line_locations_all pll
    JOIN po_lines_all pl       ON pl.po_line_id = pll.po_line_id
    JOIN po_headers_all ph     ON ph.po_header_id = pl.po_header_id
    JOIN inv_org_parameters iop ON iop.organization_id = p_org_id
   WHERE pll.line_location_id = p_line_location_id;

  IF l_closed_code IN ('CLOSED','FINALLY CLOSED') THEN RETURN 'N'; END IF;
  IF l_open_qty <= 0 THEN RETURN 'N'; END IF;
  IF SYSDATE < l_need_by - l_days_early THEN RETURN 'N'; END IF;
  IF SYSDATE > l_need_by + l_days_late  THEN RETURN 'N'; END IF;

  IF l_ack_reqd = 'Y' THEN
    SELECT NVL(MAX(CASE WHEN pa.accepted_flag='Y' THEN 'Y' END),'N')
      INTO l_ack_done
      FROM po_acceptances pa JOIN po_lines_all pl
        ON pl.po_header_id = pa.po_header_id
     WHERE pl.po_line_id = (SELECT po_line_id FROM po_line_locations_all
                             WHERE line_location_id = p_line_location_id)
       AND pa.revision_num = (SELECT revision_num FROM po_headers_all
                               WHERE po_header_id = (SELECT po_header_id FROM po_lines_all
                                 WHERE po_line_id = (SELECT po_line_id FROM po_line_locations_all
                                   WHERE line_location_id = p_line_location_id)));
    IF l_ack_done = 'N' THEN RETURN 'R'; END IF;
  END IF;

  RETURN 'Y';
END;
```
This function encapsulates the GE ASN eligibility engine logic: date window check, open qty check, closed-code check, and acknowledgement requirement check — called per shipment line during ASN line selection.

**354. Write a PL/SQL exception handler block for a WebADI upload validation API.**
```sql
PROCEDURE validate_promise_date_upload (
  p_po_number    IN  VARCHAR2,
  p_shipment_num IN  NUMBER,
  p_promise_date IN  DATE,
  x_status       OUT VARCHAR2,
  x_message      OUT VARCHAR2
) IS
  l_line_loc_id  NUMBER;
  l_need_by      DATE;
  l_closed       VARCHAR2(30);
BEGIN
  x_status := 'S';

  SELECT pll.line_location_id, pll.need_by_date, pll.closed_code
    INTO l_line_loc_id, l_need_by, l_closed
    FROM po_line_locations_all pll
    JOIN po_lines_all pl ON pl.po_line_id = pll.po_line_id
    JOIN po_headers_all ph ON ph.po_header_id = pl.po_header_id
   WHERE ph.segment1      = p_po_number
     AND pll.shipment_num = p_shipment_num;

  IF l_closed IN ('CLOSED','FINALLY CLOSED') THEN
    x_status  := 'E';
    x_message := 'PO shipment is closed. Cannot update Promise Date.';
  ELSIF p_promise_date < TRUNC(SYSDATE) THEN
    x_status  := 'W';
    x_message := 'Warning: Promise Date is in the past.';
  END IF;

EXCEPTION
  WHEN NO_DATA_FOUND THEN
    x_status  := 'E';
    x_message := 'PO ' || p_po_number || ' shipment ' || p_shipment_num || ' not found.';
  WHEN TOO_MANY_ROWS THEN
    x_status  := 'E';
    x_message := 'Ambiguous PO/shipment combination. Contact buyer.';
  WHEN OTHERS THEN
    x_status  := 'E';
    x_message := 'System error: ' || SQLERRM;
END;
```
Handling `NO_DATA_FOUND` and `TOO_MANY_ROWS` explicitly (not just `WHEN OTHERS`) gives precise error messages that appear in the WebADI upload error column — suppliers and buyers see exactly what's wrong without needing to call support.

"""

with open(OUT, 'a', encoding='utf-8') as f:
    f.write(CONTENT)

print(f"Appended Sections R & S (Q286–Q354) — continuing with remainder of S...")
print(f"File size: {OUT.stat().st_size // 1024} KB")
