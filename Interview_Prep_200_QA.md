---
title: "Interview Preparation Guide — 200 Questions & Answers"
subtitle: "Tailored for Himanshu Kumar · Oracle SCM Techno-Functional Consultant (EBS iSupplier / Procurement → Fusion Cloud SCM)"
author: "Prepared for job-readiness"
date: "May 2026"
---

# How to use this guide

This guide contains **200 interview questions with answers**, grouped into 15 sections covering everything a panel could realistically ask you based on your resume — technical, functional, behavioral, scenario-based, and forward-looking Oracle Fusion Cloud topics.

A few tips before you start:

- **Answer in your own words.** These answers are a study scaffold, not a script. Rephrase them so they sound like you.
- **Use the STAR method** for behavioral and scenario questions: Situation, Task, Action, Result. Every story should end with a measurable or concrete result.
- **Anchor everything to your GE Aerospace iSupplier project.** It is your strongest asset — most technical answers can be illustrated with something you actually built.
- **Practice out loud.** Read each behavioral answer aloud at least twice; technical answers, make sure you can draw or explain the flow without notes.
- **Know your numbers cold:** 6+ years, 5 sites, 100+ suppliers, 67 surrogate accounts, 50+ OAF personalizations, 2 server nodes, full lifecycle ownership.

Sections: (A) Behavioral & HR · (B) Resume & Project Deep-Dive · (C) Oracle EBS Fundamentals · (D) OAF · (E) iSupplier Portal · (F) BI Publisher · (G) WebADI · (H) PL/SQL & SQL · (I) Concurrent Programs / AOL / FND · (J) Oracle Workflow · (K) Java / Spring Boot / REST & SOAP · (L) Procurement & P2P Functional · (M) ASN / Shipments / Receipts / Returns · (N) Oracle Fusion Cloud SCM · (O) Situational & Closing.

---

# Section A — Behavioral, HR & Self-Introduction (Q1–Q22)

**1. Tell me about yourself.**
"I'm an Oracle SCM techno-functional consultant with 6+ years of experience, specializing in the iSupplier Portal and Procure-to-Pay domain on Oracle E-Business Suite R12. Most recently at Genpact I've been the sole functional and technical SME on a greenfield iSupplier Portal rollout for GE Aerospace across five manufacturing sites and 100+ suppliers — owning everything from requirements through go-live and hypercare. Before that I spent four years at TCS doing OAF development, BI Publisher reporting, and PL/SQL across Procurement and Inventory. I'm now looking to take that supplier-collaboration and procurement depth into a larger SCM role, including Oracle Fusion Cloud." Keep it to 60–90 seconds: present role → headline achievement → background → what you want next.

**2. Why are you looking to change jobs?**
Frame it forward, never negative. "I've owned a full greenfield implementation end-to-end, which was a fantastic growth experience. I'm now looking for a role with broader SCM scope and a clearer path into Oracle Fusion Cloud, where I can apply my procurement and supplier-collaboration expertise on a modern platform." Avoid criticizing your current employer, pay, or manager.

**3. Why do you want to work for our company specifically?**
Research the company first. Tie their tech stack or domain to your strengths: "You run Oracle SCM at scale across multiple sites, which is exactly the multi-site, supplier-heavy environment I've been working in. I can contribute from day one on iSupplier/Procurement, and I'm keen to grow with your Fusion Cloud roadmap." Show you've read about them.

**4. What are your biggest strengths?**
Pick two or three and back each with proof. "Three things: I bridge functional and technical — I can sit with a procurement manager to gather requirements and then build the OAF personalization or PL/SQL myself. I'm strong at ownership — I ran a 5-site rollout solo. And I'm good under production pressure — I handled hypercare and ServiceNow CTASKs without escalations spiraling."

**5. What is your biggest weakness?**
Be honest but show growth. "Earlier in my career I tried to do everything myself and was slow to ask for help, which once delayed a fix. I've since learned to escalate early and document blockers — during hypercare I set up a clear defect-triage process so issues were visible, not bottlenecked on me." Avoid clichés like "I'm a perfectionist."

**6. Walk me through your most challenging project.**
Use the GE Aerospace rollout. Situation: greenfield iSupplier across 5 sites with conflicting site-level procurement policies. Task: deliver one unified platform as sole SME. Action: harmonized policies via OAF personalization framework, built surrogate-supplier model, ran CRP/UAT. Result: live across all 5 sites for 100+ suppliers, legacy SCP tools retired.

**7. Tell me about a time you handled conflicting requirements.**
"The five GE sites each had different procurement practices — some wanted Promise Date mandatory, others used Need-by Date. I ran working sessions to find the common denominator, then used OAF personalization at responsibility level so site-specific behavior could coexist within one configuration. The result was a single codebase that still respected local rules."

**8. Describe a time you made a mistake. How did you handle it?**
Pick a real, low-blast-radius example. State what happened, that you owned it immediately, the fix, and the safeguard you added. Example: a personalization deployed to PROD hid a field needed by one responsibility; you caught it in hypercare monitoring, rolled back the personalization (non-code, so reversible), and added a responsibility-level test checklist before future deployments.

**9. How do you handle tight deadlines and pressure?**
"I break the work into must-have vs. nice-to-have, communicate status early, and protect the critical path. During cutover I worked from a sequenced checklist and kept stakeholders updated daily so there were no surprises. Pressure is manageable when scope and communication are controlled."

**10. Tell me about a time you disagreed with a stakeholder.**
Show respectful pushback grounded in data. "A buyer wanted suppliers to edit price on BPA change requests. I explained the compliance risk — uncontrolled price changes on a blanket agreement — and proposed making the price field read-only with a request-change path instead. Once I framed it as protecting agreement integrity, they agreed."

**11. How do you prioritize when everything is urgent?**
"I prioritize by business impact and blast radius: production-down issues first, then items blocking other people, then enhancements. I use a simple severity model and confirm priorities with the lead rather than guessing. During hypercare this kept the queue sane."

**12. Where do you see yourself in 3–5 years?**
"I'd like to grow into a senior/lead SCM consultant role — owning solution design across procurement, mentoring juniors, and being certified and project-experienced on Oracle Fusion Cloud SCM. I want depth in the domain plus breadth across EBS and Cloud."

**13. Why should we hire you?**
"I offer a rare combination: deep iSupplier/Procurement domain knowledge, hands-on OAF/PL-SQL/BI Publisher technical skills, and proven end-to-end implementation ownership. You're not getting someone who only configures or only codes — you get someone who can take a requirement from a procurement manager all the way to production."

**14. How do you keep your skills current?**
"I follow Oracle documentation and My Oracle Support notes, and I'm actively upskilling toward Oracle Fusion Cloud Procurement. I learn best by building — I set up trials and reproduce scenarios rather than just reading."

**15. Describe your ideal work environment.**
"Collaborative, with clear ownership and direct access to business users. I do my best work when I can talk to the actual procurement and warehouse users instead of working off second-hand requirements — that's how I delivered the GE rollout."

**16. Tell me about a time you went above and beyond.**
"During the rollout, planners were getting flooded with notifications whenever suppliers updated promise dates. It wasn't in the original scope, but I built a custom PL/SQL package and workflow to suppress unnecessary planner notifications and route changes for approval. It wasn't asked for, but it removed a major adoption blocker."

**17. How do you handle feedback or criticism?**
"I treat it as data. In UAT, defect feedback is constant — I learned not to take it personally and to dig for the root cause. If a reviewer flags my code or design, I'd rather fix it before production than defend it."

**18. Tell me about a time you worked with a difficult team member or supplier.**
Focus on resolution, not blame. "One supplier repeatedly submitted ASNs that failed validation. Instead of just rejecting them, I walked their team through the eligibility rules and the new mandatory fields, and adjusted an error message to be clearer. The failures dropped sharply."

**19. How do you explain technical concepts to non-technical stakeholders?**
"I use the business outcome, not the mechanism. Instead of 'I added a SPEL expression to the rendered property,' I say 'the field now only appears when it's relevant to that supplier.' I ran CRP demos this way and it kept procurement managers engaged."

**20. Are you willing to relocate / work in the Gulf / work remotely?**
Answer honestly and positively to your real preferences. Since you're open to India metros, remote, and the Gulf: "Yes — I'm open to relocation including the Gulf region, as well as remote roles. I'm flexible for the right opportunity." Flexibility is a hiring advantage; state it confidently.

**21. What are your salary expectations?**
Research the band first. Give a range, not a number, and tie it to value: "Based on my experience and the market for Oracle SCM consultants, I'm looking in the range of X–Y. I'm open to discussing the full package." For the Gulf, factor in tax-free pay; for India, anchor to your years and implementation ownership.

**22. Do you have any questions for us?**
Always have 2–3 ready. Good ones: "Is this role more EBS support or Fusion implementation?", "What does the team's Cloud migration roadmap look like?", "What does success in the first 90 days look like?" Asking smart questions signals seniority.

---

# Section B — Resume & Project Deep-Dive (Q23–Q34)

**23. Explain the GE Aerospace iSupplier project end-to-end.**
"Goal was to replace fragmented legacy SCP tools with a single iSupplier Portal across five GE Aerospace manufacturing sites for 100+ suppliers. I owned it as sole functional/technical SME: gathered requirements, ran CRP demos, configured P2P (PO acknowledgement, promise dates, ASN, receipts, returns), built 50+ OAF personalizations and a surrogate-supplier model, developed BI Publisher reports and WebADI uploads, then handled cutover, go-live, and hypercare." Be ready to drill into any one piece.

**24. What was your specific role — were you functional or technical?**
"Both — I was the techno-functional SME. I gathered and harmonized requirements with procurement and warehouse users (functional), and I personally built the OAF personalizations, PL/SQL packages, workflows, BI Publisher reports, and WebADI integrations (technical). That dual role is exactly why I was effective solo."

**25. What is the surrogate-supplier model you built and why?**
"Some suppliers couldn't or wouldn't transact in the portal directly, so buyers needed to act on their behalf. I designed a custom OAF task flow and onboarded 67 surrogate accounts with role-based responsibilities and supplier–buyer mapping, plus notifications so buyers were alerted when acting as a surrogate. It let GE keep the workflow consistent regardless of supplier maturity."

**26. What were the hardest technical problems you solved on this project?**
Have 2–3 ready: (a) Promise Date defaulting — standard code defaulted Due Date to Need-by when promise was blank, hiding data issues, so I reworked the logic and renamed the column; (b) Unit Price incorrectly pulling from the Blanket Agreement instead of the Standard PO; (c) the ASN eligibility engine filtering shipments by Need-by ± days and validating against receiving controls.

**27. How did you handle the five sites having different processes?**
"I found the common process and configured that as the baseline, then used responsibility-level OAF personalizations and profile options for site-specific differences. This avoided five separate codebases — one configuration that flexed by responsibility."

**28. What did go-live and hypercare look like?**
"Cutover followed a sequenced checklist — config migration, personalization deployment, data validation. In hypercare I monitored issues, triaged defects by severity, logged ServiceNow CTASKs for DBA actions like OACore bounces, and pushed fixes through DEV → UAT → PROD. I also ran end-user training so adoption didn't stall."

**29. How did you measure success on the rollout?**
"Adoption and stability: all 5 sites live with 100+ suppliers transacting, legacy SCP tools decommissioned, ASN validation failures down after I improved eligibility rules and messaging, and a manageable hypercare queue with no recurring critical defects."

**30. What would you do differently if you did it again?**
"I'd invest more in automated regression checks for personalizations before PROD, and I'd document the harmonized process earlier so site stakeholders aligned sooner. Both would have reduced UAT churn."

**31. At TCS, what kind of work did you do?**
"Core OAF development — controller extensions, view objects, application modules for Procurement and Inventory — plus BI Publisher reports with complex PL/SQL data models, Java/Spring Boot REST/SOAP integrations to third-party systems, SQL/PL-SQL tuning, and environment management across DEV/UAT/PROD."

**32. Why did you move from TCS to Genpact?**
"At TCS I was strong on the build side. The Genpact role offered end-to-end ownership of a greenfield implementation as the SME — a step up in responsibility and a chance to own the functional side too, not just code."

**33. How do you ensure quality in your deliverables?**
"Unit-test in DEV, validate against requirements in UAT with the actual users, peer review where available, and migrate in controlled steps. For personalizations I verify at each level (site/responsibility/user) because scope mistakes there are easy to make."

**34. What technologies on your resume are you strongest in?**
"OAF personalization and extensions, PL/SQL, and the iSupplier/Procurement functional domain are my strongest. BI Publisher and WebADI are close behind. I'm building Fusion Cloud Procurement next." Be honest about depth — don't claim expert on everything.

---

# Section C — Oracle EBS Fundamentals (Q35–Q44)

**35. What is the multi-tier architecture of Oracle EBS R12?**
Three tiers: the **desktop/client tier** (browser), the **application/middle tier** (web, forms, concurrent processing, and admin servers — running on Oracle 10g AS / OC4J in R12), and the **database tier** (the Oracle database holding the data model and code). R12 introduced a single APPL_TOP and the use of OC4J instead of standalone JServ.

**36. What is the difference between APPS schema and a product schema?**
Each product (e.g., PO, AP, INV) has its own base schema that owns its tables. The **APPS** schema is a single universal schema that owns all the code objects (packages, views, synonyms) and has access to all product data. Application code connects as APPS, which is why grants and synonyms are centralized there.

**37. What is a Flexfield? Key vs. Descriptive.**
Flexfields let you extend Oracle's data model declaratively. A **Key Flexfield (KFF)** is a configurable multi-segment key that identifies an entity (e.g., the Accounting Flexfield / chart of accounts, Item Categories). A **Descriptive Flexfield (DFF)** captures extra optional attributes on a record without changing the schema, stored in ATTRIBUTE columns.

**38. What is a Value Set?**
A value set defines the validation rules for a flexfield segment or a concurrent program parameter — the format, length, and the list of valid values (e.g., None, Independent, Table-based, Dependent). Table-validated value sets run a SQL query to derive the list.

**39. What is the AOL (Application Object Library)?**
AOL is the foundational FND layer that manages cross-application services: users, responsibilities, menus, functions, concurrent programs, request groups, flexfields, profiles, and lookups. Almost everything you configure in System Administrator lives in AOL/FND tables (FND_*).

**40. Explain Responsibility, Menu, and Function.**
A **function** is the smallest securable unit (a form or a self-service page/region). A **menu** groups functions hierarchically. A **responsibility** ties a menu (and a data-access/security group plus request group) to a user, defining what they can see and do. A user can have multiple responsibilities.

**41. What are Profile Options and their hierarchy levels?**
Profile options control system behavior and can be set at **Site → Application → Responsibility → User** (lowest level wins, i.e., user overrides responsibility, which overrides application, which overrides site). Examples: MO: Operating Unit, FND: Personalization Region Link Enabled.

**42. What is Multi-Org and the difference between MOAC in R12 vs 11i?**
Multi-Org partitions data by Operating Unit. In 11i you set CLIENT_INFO / one OU per responsibility. R12 introduced **MOAC (Multi-Org Access Control)** so a single responsibility can access multiple operating units via a security profile (MO: Security Profile), removing the need for separate responsibilities per OU.

**43. What is the difference between customization, personalization, and extension?**
**Personalization** = declarative UI changes (OAF/Forms personalization) with no code change. **Extension** = adding new logic/behavior by extending standard code (e.g., a controller or VO extension) without modifying Oracle's files. **Customization** is the broad umbrella term; pure customization (editing standard objects directly) is discouraged because it breaks on patching.

**44. What happens to customizations during patching/upgrades?**
Personalizations stored in FND tables/MDS generally survive patches; CEMLI extensions (Configuration, Extension, Modification, Localization, Integration) must be retested and sometimes re-applied. Modifying standard files directly is risky — patches overwrite them — which is why personalization and extension are preferred over modification.

---

# Section D — Oracle Application Framework / OAF (Q45–Q64)

**45. What is OA Framework and the MVC pattern in it?**
OAF is Oracle's Java/J2EE-based framework for building web (self-service) applications in EBS. It follows **MVC**: the **Model** = BC4J business components (Entity Objects, View Objects, Application Modules); the **View** = the page/regions/items defined in MDS XML; the **Controller** = Java classes that handle page logic and events (processRequest / processFormRequest).

**46. Explain EO, VO, AM, and VL.**
**Entity Object (EO)** maps to a database table and handles DML and validation. **View Object (VO)** runs a SQL query to select/join data for display or processing. **Application Module (AM)** is the transaction container — it holds VOs, manages the database connection and transaction state, and exposes service methods. **View Link (VL)** defines a master-detail relationship between two VOs.

**47. What is the difference between processRequest and processFormRequest?**
**processRequest()** runs when the page is first rendered (the GET) — used to initialize the AM, execute VOs, and set up the UI. **processFormRequest()** runs on form submission (the POST) — used to handle button clicks and events, read submitted values, and call AM methods. Setup goes in processRequest; event handling goes in processFormRequest.

**48. What is a root AM vs. a nested AM?**
The **root AM** owns the transaction and database connection for the page. **Nested AMs** are reusable modules embedded under a root AM; they share the root's transaction. This lets you modularize logic while keeping a single commit boundary.

**49. What is the difference between setWhereClause and addWhereClause / using bind variables?**
You restrict a VO's query at runtime by appending a where clause and binding parameters with `setWhereClauseParam`. Best practice is to use **bind variables** (`:1`, `:2`) instead of concatenating literal values — it prevents SQL injection and lets the database reuse the cursor. Always clear previous where clauses before re-applying to avoid stacking.

**50. How do you pass parameters between OAF pages?**
Via the URL with `pageContext.setForwardURL(...)` passing parameters, by setting values on the session using `pageContext.putTransactionValue`/`putSessionValue`, or through page parameters retrieved with `pageContext.getParameter`. Transaction values are cleared at commit; session values persist longer.

**51. What is personalization in OAF and what levels exist?**
Personalization is declarative tailoring of a page's look, layout, or visibility without changing code. Levels include **Function, Site, Operating Unit, Responsibility, Localization, Org, Portlet,** and **User**. Lower/more-specific levels override higher ones. You enable the Personalize link via the FND: Personalization Region Link Enabled profile.

**52. What is SPEL and where did you use it?**
**SPEL (Simplest Possible Expression Language)** lets you bind a UI property (Rendered, ReadOnly, Required, Disabled) to a VO attribute dynamically, using the syntax `${oa.ViewName.AttributeName}`. It returns true/false at runtime so a field can show/hide based on data. On the GE project I used SPEL extensively to make fields conditional rather than hardcoding visibility.

**53. Static vs. dynamic personalization — what's the difference?**
**Static** sets a property to a fixed True/False at personalization time. **Dynamic** uses SPEL so the property is evaluated at runtime against data — e.g., make Promise Date required only when a condition holds. Dynamic personalization is more powerful but requires a VO attribute to bind to.

**54. How do you make a field mandatory or read-only through personalization?**
Open the page in Personalization, locate the item, and set the **Required** property to true (mandatory) or **Read Only** to true. For conditional behavior, set the property using a SPEL expression bound to a VO attribute instead of a static value.

**55. How do you migrate personalizations between instances?**
Using the **Functional Administrator** responsibility → Personalization → Import/Export, you download the personalization XML (from MDS) for a document/page and upload it into the target instance. Alternatively use the `XDFCMD`/`jpximport`/FNDLOAD-style utilities. The XML captures the personalization at its level so it reproduces exactly.

**56. What is MDS (Metadata Services)?**
MDS is the metadata repository where OAF stores page definitions and personalizations as XML in the database (the MDS repository). At runtime OAF reads the base page definition and layers personalizations from MDS on top, which is why personalizations survive patching.

**57. What is a controller extension and how do you do it?**
You create a new controller class that **extends** the standard controller, override processRequest/processFormRequest, call `super.processRequest(...)` to keep standard behavior, and add your logic. Then you **personalize** the region to point to your new controller instead of the seeded one — without touching Oracle's class.

**58. How do you extend a VO (View Object substitution)?**
Create a new VO that extends the base VO (or add transient/expert attributes), then register a **substitution** using JDeveloper's substitution feature / `jpximport`. The framework swaps your VO in wherever the base VO is referenced. Substitutions are instance-wide and must be imported into each environment.

**59. What is the difference between substitution and extension?**
**Extension** is creating a subclass with added behavior; **substitution** is registering that subclass so the framework uses it everywhere in place of the original. You extend to add logic, then substitute to make the framework actually use your extended component.

**60. How do you debug an OAF page?**
Enable **FND: Diagnostics** and use the "About this Page" link to inspect the page structure, AM, VOs, and their SQL. Use `pageContext.writeDiagnostics` / `OADBTransaction.writeDiagnostics` for logging, check the OC4J/Apache logs, and use JDeveloper's debugger against a local run. The About-this-Page XML is invaluable for finding the right VO/region to personalize or extend.

**61. What is the difference between a Region and an Item in OAF?**
A **Region** is a container that groups items or other regions (e.g., a header region, a table region, a messageComponentLayout). An **Item** is an individual UI element (a text field, button, message, image). Pages are trees of regions containing items.

**62. How do you create an LOV (List of Values) in OAF?**
Use the **messageLovInput**/lovInput item bound to an **external LOV region** (its own VO). You map LOV result columns back to base-page items via the LOV Mappings, and can add criteria. On the GE project, the ship-method LOV "No Item Found" bug was about the LOV's VO query not returning matching rows.

**63. How do you commit a transaction in OAF?**
Call `am.getOADBTransaction().commit()` (or `rollback()`), typically from processFormRequest after handling the submit event. OAF manages the connection through the root AM, so you commit through the transaction object rather than issuing raw SQL commits.

**64. What is passivation and pooling in OAF?**
**Passivation** is OAF saving AM state to the database (FND_TM* tables) so it can restore the user's transaction if the middle tier recycles the AM — important for long-running pages. **AM pooling** reuses AM instances across requests for scalability. You design VOs and transient state carefully so passivation works correctly.

---

# Section E — iSupplier Portal (Q65–Q80)

**65. What is Oracle iSupplier Portal and what business problem does it solve?**
iSupplier Portal is a self-service, browser-based collaboration application that lets suppliers interact directly with the buying organization — view POs, acknowledge them, submit ASNs/shipment notices, see receipts and returns, view payment/invoice status, and manage delivery schedules. It replaces phone/email/fax collaboration with a controlled, auditable workflow, improving on-time delivery and data accuracy.

**66. What are the main responsibilities/roles in iSupplier Portal?**
Common seeded responsibilities are **iSupplier Portal Full Access** and **Supplier Profile Manager** for external suppliers, plus internal views like **Supplier Collaboration / Sourcing Supplier** and the buyer-side "iSupplier Portal Internal/Full" used by buyers and surrogate users. On the GE project I configured a Surrogate (buyer-on-behalf) responsibility and supplier/buyer views.

**67. What is the difference between a supplier user and a surrogate (internal) user?**
A **supplier user** is an external party logging in to transact for their own supplier records. A **surrogate user** is an internal buyer transacting on behalf of a supplier (for suppliers who don't self-serve). The surrogate model needs responsibility setup, supplier–buyer mapping, and notification routing — which is what I built for 67 accounts.

**68. How does PO Acknowledgement work in iSupplier?**
When a buyer requires acknowledgement, the PO moves to "Requires Acknowledgement." The supplier opens it in the portal and **Accepts**, **Rejects**, or requests changes (e.g., proposes a different Promise/Commit Date or price). Acknowledgement updates the PO's acceptance status and can trigger notifications. We customized the buttons/messaging and added Promise-vs-Need-by validation.

**69. What is an ASN and what's the difference between ASN and ASBN?**
An **ASN (Advance Shipment Notice)** is a notice the supplier sends in advance of a shipment, listing what's shipping, quantities, and logistics details so receiving can prepare. An **ASBN (Advance Shipment and Billing Notice)** additionally includes invoice/billing information so it can create an invoice on receipt. ASN = shipment only; ASBN = shipment + billing.

**70. Walk through the ASN creation flow you customized.**
Supplier selects eligible PO shipment lines → enters header (Waybill/Airbill, Packing Slip, ship method, dates) → enters lines (quantity shipped, country of origin, LOT/UPN) → submits. We made logistics fields mandatory, added a Balance-Outstanding-Qty column, auto-generated ASN/Pack-Slip numbers, integrated a Vendor LOT field, and built an eligibility filter (Need-by ± days, validating against receiving controls) so only valid shipments could be selected.

**71. What is the eligibility logic that decides which shipments can be ASN'd?**
A shipment is eligible based on the date window (e.g., Need-by Date minus Days Early through Need-by plus Days Late, or "Due This Week"/"Due Any Time"/AuthShip), open quantity remaining, receiving controls (over-receipt tolerance, ship-to validity), and acknowledgement status — POs still in "Requires Acknowledgement" should be blocked from ASN creation.

**72. What is the difference between Promise Date, Need-by Date, and Commit Date?**
**Need-by Date** is when the buyer needs the goods. **Promise Date** is when the supplier commits to deliver (it drives on-time-delivery measurement). **Commit Date** is the supplier-acknowledged date during PO acknowledgement. A common standard behavior is Promise Date defaulting to Need-by when blank — which can mask missing commitments, a logic issue we explicitly fixed.

**73. What is LOT and UPN/serial tracking and why does it matter at ASN?**
**LOT** tracks a batch of material; **serial/UPN** tracks individual units. Capturing LOT/serial at ASN creation enables end-to-end traceability and customs/quality compliance — critical in aerospace. We hid the legacy LOT/UPN field and added a dedicated Vendor LOT field the supplier must enter at shipment.

**74. What are Receiving Controls and how do they interact with ASN?**
Receiving controls are PO/item setups governing receipt behavior — over-receipt tolerance, early/late receipt windows, receipt routing (direct/standard/inspection), ship-to org validity, and allow-substitute-receipts. ASN validation should respect these so a supplier can't notify a shipment that receiving would reject.

**75. What is DPAS and why does it appear on PO acknowledgement?**
**DPAS (Defense Priorities and Allocations System)** is a U.S. government rating (e.g., DO/DX) that prioritizes defense-related orders. For rated POs the acknowledgement flow must surface a DPAS message so the supplier formally accepts/rejects the rating — relevant for aerospace/defense suppliers like GE's.

**76. What is a Blanket Purchase Agreement (BPA/GBPA) and how does it differ from a Standard PO?**
A **Blanket Purchase Agreement** is a long-term agreement on pricing/terms with no firm quantities/dates; releases are issued against it. A **Standard PO** is a one-time order with specific quantities and dates. A key bug we fixed: unit price was incorrectly pulling from the Blanket Agreement instead of the Standard PO on delivery schedules/ASN, and price was wrongly editable on BPA change requests.

**77. How did you restrict price edits on change requests?**
We set the price field to **read-only** through OAF personalization (and validated on submit) for both Standard PO and BPA/GBPA change-request screens, so suppliers could request changes but not alter agreed pricing — protecting agreement integrity and compliance.

**78. How does the Receipts / Returns / On-Time Performance area work in iSupplier?**
Suppliers can view **Receipts** (what the buyer received), **Returns** (rejected/returned goods with reasons), **Overdue Receipts**, and **On-Time Performance** metrics. We reordered and trimmed these tables, made PO fields read-only, and added PO Line Numbers on the Returns screen for clarity.

**79. How do supplier notifications and approvals flow?**
iSupplier uses Oracle Workflow to send notifications (PO acknowledgement, shipment, change requests) to suppliers and internal planners/buyers. We built a custom package + workflow to suppress excessive planner notifications when suppliers updated promise dates and to route promise-date changes to managers for approval.

**80. What are common iSupplier setup steps?**
Define suppliers and supplier sites, register supplier contacts/users and assign iSupplier responsibilities, set up the supplier-buyer/agent assignments, configure profile options and notifications, enable required document types (POs, ASN), and set receiving/sourcing controls. Surrogate setup additionally needs internal responsibilities and supplier mapping.

---

# Section F — BI Publisher / XML Publisher (Q81–Q90)

**81. What is BI Publisher and how does it work in EBS?**
BI Publisher (formerly XML Publisher) separates **data** from **layout**. A data source (SQL query, PL/SQL, or a Data Template) produces XML; a template (RTF, Excel, eText, PDF) defines the layout; BI Publisher merges them to produce the final output in PDF, Excel, RTF, HTML, etc. In EBS it's integrated with concurrent processing.

**82. What are the components needed to register a BIP report in EBS?**
Typically: (1) a **Data Definition** (with a Data Template or a concurrent program that emits XML), (2) a **Template** (RTF/Excel) registered under XML Publisher Administrator and tied to the Data Definition by a shared **code**, and (3) a **concurrent program** with output format XML that runs the data source. The user runs the concurrent program and selects the template.

**83. What is a Data Template?**
A Data Template is an XML definition of the report's data — it holds the SQL query(ies), parameters, data structure/grouping, lexical/bind parameters, and triggers (before/after report PL/SQL). It's an alternative to writing a separate concurrent program to generate XML.

**84. How do you create an RTF template?**
In MS Word with the **BI Publisher (Template Builder) add-in**: load sample XML, then insert fields and **for-each** loops for repeating groups, use `<?if?>` conditions, and built-in functions. You can preview against sample data, then upload the .rtf as the template in XML Publisher Administrator.

**85. What are common RTF template tags?**
`<?for-each:GROUP?> ... <?end for-each?>` for loops, `<?FIELD_NAME?>` to print a value, `<?if:condition?> ... <?end if?>` for conditionals, `<?sum(FIELD)?>` for aggregation, and `<?sort:FIELD?>` for ordering. Form fields hold these tags to keep the layout clean.

**86. What is the difference between bind variables and lexical parameters in a BIP/Reports query?**
A **bind variable** (`:P_PARAM`) substitutes a single value safely at execution. A **lexical parameter** (`&P_WHERE`) substitutes a whole fragment of SQL text (like a dynamic WHERE clause or column list) before parsing — powerful for dynamic queries but must be controlled to avoid injection.

**87. How do you handle multi-language or multi-layout reports?**
BIP supports **translations (XLIFF)** for a single template across languages, and you can register multiple templates against one data definition (e.g., different layouts per locale or business need). You pick the template/locale at runtime.

**88. What is eText and when is it used?**
**eText** templates produce structured text output for **EDI/EFT** — fixed-position or delimited flat files for bank payments and B2B exchange. They're defined in RTF with special table structures mapping fields to record positions.

**89. What was the GEA Collaboration History report you built?**
A BI Publisher report giving GE visibility into supplier collaboration history; I added a **Child-Project-Quantity break-up** column so quantities rolled up correctly by child project. The Mass ASN Label / Pack-Slip print was another — a parameterized report producing labels for many shipments at once, with a WebCenter output option.

**90. How do you tune a slow BIP report?**
Tune the underlying SQL first (the usual cause) — check the explain plan, add indexes/hints, reduce data volume with parameters. For huge outputs, use **scalable mode** (BIP processes XML in chunks instead of memory), simplify the template, and avoid heavy in-template logic. Generate Excel via the proper Excel template rather than HTML-as-xls.

---

# Section G — WebADI (Q91–Q96)

**91. What is WebADI and when do you use it?**
**Web Applications Desktop Integrator** bridges Excel and EBS — it generates an Excel spreadsheet from a defined layout, lets users enter/paste data offline with validation, and uploads it into EBS through an API or interface table. You use it for high-volume data entry/updates where a screen-by-screen UI is too slow (e.g., the Promise-Date and multi-PO mass changes I built).

**92. What are the key components of a WebADI integrator?**
An **Integrator** (the definition), an **Interface** (the API/columns it maps to), a **Layout** (which columns appear and their order), a **Content** (optional seed data / parameter list), and a **Mapping** (source-to-target column mapping for imports). Together they define the spreadsheet and how its data lands in EBS.

**93. How does validation work in WebADI?**
Validation happens at two points: in the **spreadsheet** (list-of-values, required fields, format checks defined in the layout/interface) and on **upload** (the importer/API runs business validation and rejects bad rows, flagging errors back into the sheet). I backed our uploads with custom PL/SQL validation APIs so promise-date and PO changes were checked before commit.

**94. What is the difference between a WebADI document and an integrator?**
The **integrator** is the reusable definition (interface + layouts + mappings). The **document** is a specific generated spreadsheet instance the user works in. One integrator can produce many documents.

**95. Can WebADI call a custom API? How did you implement your uploads?**
Yes — you define an interface that targets a **PL/SQL API** (or an interface table processed by a concurrent program). For the GE project I created custom PL/SQL validation/processing APIs and pointed the WebADI integrator at them, so bulk Promise-Date updates and multi-PO mass changes were validated and applied programmatically, replacing the standard Multi-PO Change button.

**96. What are common WebADI errors and how do you troubleshoot?**
Macro/security issues in Excel (enable macros, trust the source), function/responsibility not granted to the integrator, layout-mapping mismatches, and validation failures on upload. Troubleshoot by checking the integrator's function security, the error column written back to the sheet, and the concurrent/log output of the importer.

---

# Section H — PL/SQL & SQL (Q97–Q120)

**97. What is the difference between a procedure and a function?**
A **procedure** performs an action and may return values via OUT parameters; a **function** must return a single value and can be used in SQL/expressions. Use a function when you need a value back inline; a procedure for actions/side-effects.

**98. What is a package and why use one?**
A **package** groups related procedures, functions, types, cursors, and variables into a specification (public interface) and body (implementation). Benefits: encapsulation, easier maintenance, session-persistent package state, reduced recompilation (changing the body doesn't invalidate dependents), and better performance via one-time loading.

**99. Explain the difference between %TYPE and %ROWTYPE.**
`%TYPE` declares a variable of the same datatype as a column or another variable (e.g., `v_id emp.empno%TYPE`). `%ROWTYPE` declares a record matching an entire table row or cursor structure. Both keep code in sync with the schema automatically.

**100. What is a cursor? Implicit vs. explicit.**
A cursor is a pointer to a result set. **Implicit** cursors are created automatically for single-row SELECT INTO and DML (you read attributes like SQL%ROWCOUNT). **Explicit** cursors are declared, opened, fetched, and closed by you — used for multi-row processing and more control.

**101. What is a ref cursor?**
A **REF CURSOR** is a cursor variable — a pointer to a query result that can be opened dynamically and passed between programs (e.g., returned from a function to a Java/BIP caller). `SYS_REFCURSOR` is the weakly-typed built-in. Useful for returning result sets to OAF/BIP/reports.

**102. What is a BULK COLLECT and FORALL? Why use them?**
`BULK COLLECT` fetches many rows into a collection in one context switch instead of row-by-row; `FORALL` sends many DML statements to the SQL engine in one batch. Together they drastically reduce PL/SQL↔SQL context switching, which is the single biggest PL/SQL performance win for large data sets. Use `LIMIT` with BULK COLLECT to cap memory.

**103. What is the difference between a trigger's BEFORE and AFTER, and row-level vs statement-level?**
**BEFORE** fires before the DML (used to set/validate values), **AFTER** fires after (used for auditing/cascading). **Row-level** (`FOR EACH ROW`) fires once per affected row with `:OLD`/`:NEW`; **statement-level** fires once per statement regardless of row count.

**104. What is a mutating table error and how do you avoid it?**
It occurs when a row-level trigger tries to read or modify the same table that fired it — Oracle can't guarantee a consistent view. Avoid it by using **compound triggers** (collect rows in the row section, act in the after-statement section), package-level collections, or autonomous transactions where appropriate.

**105. What is an autonomous transaction?**
A transaction declared with `PRAGMA AUTONOMOUS_TRANSACTION` that runs independently of the calling transaction — it can commit/rollback without affecting the parent. Common use: logging errors to a table even if the main transaction rolls back.

**106. How do you handle exceptions in PL/SQL?**
With an `EXCEPTION` block catching predefined exceptions (NO_DATA_FOUND, TOO_MANY_ROWS, DUP_VAL_ON_INDEX), user-defined exceptions, or `WHEN OTHERS`. Use `SQLCODE`/`SQLERRM` for details, `RAISE_APPLICATION_ERROR(-20000..-20999, msg)` to throw custom errors, and avoid a bare `WHEN OTHERS` that swallows errors silently.

**107. What is the difference between DELETE, TRUNCATE, and DROP?**
**DELETE** is DML — removes rows (optionally filtered), can be rolled back, fires triggers. **TRUNCATE** is DDL — removes all rows quickly, resets storage, can't be rolled back, no row triggers. **DROP** removes the table object entirely.

**108. What is the difference between WHERE and HAVING?**
`WHERE` filters rows **before** grouping/aggregation; `HAVING` filters **after** aggregation (on group results). You use HAVING to filter on aggregate functions like `COUNT(*) > 5`.

**109. Explain the types of joins.**
**INNER** (matching rows only), **LEFT/RIGHT OUTER** (all rows from one side plus matches), **FULL OUTER** (all rows from both), **CROSS** (cartesian product), and **SELF** join (a table joined to itself). Equi-join uses equality; anti/semi-joins via NOT EXISTS/EXISTS.

**110. What is the difference between UNION and UNION ALL?**
`UNION` combines result sets and removes duplicates (incurring a sort/distinct cost); `UNION ALL` returns everything including duplicates and is faster. Use UNION ALL when you know there are no duplicates or duplicates are acceptable.

**111. What are analytic / window functions?**
Functions like `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`, `SUM() OVER(...)` that compute across a "window" of rows **without collapsing** them (unlike GROUP BY). Great for running totals, ranking within partitions, and comparing a row to its neighbors.

**112. What is the difference between RANK, DENSE_RANK, and ROW_NUMBER?**
`ROW_NUMBER` gives a unique sequential number even for ties. `RANK` gives the same rank to ties but skips the next numbers (1,1,3). `DENSE_RANK` gives the same rank to ties without gaps (1,1,2).

**113. How do you find and remove duplicate rows?**
Find with `GROUP BY key HAVING COUNT(*) > 1` or `ROW_NUMBER() OVER (PARTITION BY key ORDER BY rowid)`. Remove keeping one copy by deleting where `ROWID NOT IN (SELECT MIN(ROWID) ... GROUP BY key)` or deleting rows whose row_number > 1.

**114. What is an index? When does it help and when does it hurt?**
An index is a sorted structure (typically B-tree) that speeds lookups and range scans on selective predicates. It hurts DML (every insert/update/delete maintains it) and wastes space if rarely used or on low-selectivity columns. Bitmap indexes suit low-cardinality, read-mostly columns (data warehousing).

**115. How do you approach SQL performance tuning?**
Get the **execution plan** (EXPLAIN PLAN / AUTOTRACE / `DBMS_XPLAN`), look for full scans on large tables, bad join order, and high-cost operations. Fix by adding/using selective indexes, rewriting the query (avoid functions on indexed columns, SARGable predicates), updating statistics, using bind variables, and partitioning where appropriate. On EBS I also checked for missing FND/standard indexes.

**116. What is the difference between a view and a materialized view?**
A **view** is a stored query, evaluated each time it's used (always current, no storage). A **materialized view** physically stores the result and is refreshed (on commit / on demand / scheduled) — it trades freshness for speed and supports query rewrite, common in reporting/warehousing.

**117. What is a hint and should you use them?**
A hint (e.g., `/*+ INDEX(t idx) */`, `/*+ LEADING(a b) */`) instructs the optimizer to use a specific plan. Use sparingly — prefer fixing statistics/structure first, because hints can become stale as data changes. They're useful for a known, stable problem query.

**118. What is the difference between IN, EXISTS, and a JOIN?**
`IN` compares against a value list/subquery result; `EXISTS` checks for the existence of correlated rows and can short-circuit; a `JOIN` combines rows. EXISTS often outperforms IN on large correlated subqueries; the optimizer may rewrite them anyway, so test with the plan.

**119. What is MERGE (upsert)?**
`MERGE INTO target USING source ON (condition) WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT ...` performs insert-or-update in a single statement — efficient for loading interface/staging data into base tables, common in EBS interfaces.

**120. How do you debug PL/SQL in an EBS context?**
Use `FND_FILE.PUT_LINE(FND_FILE.LOG, ...)` to write to the concurrent request log, `DBMS_OUTPUT` in SQL Developer, exception logging to a custom table via autonomous transactions, and `dbms_application_info` for tracing. For OAF-invoked PL/SQL, also check the diagnostics/OC4J logs.

---

# Section I — Concurrent Programs, AOL & FND (Q121–Q130)

**121. What are the steps to register a concurrent program?**
Create the **executable** (pointing to the host file/PL-SQL package.procedure/Java/Reports/SQL), define the **concurrent program** (linking the executable, output format, incompatibilities), define **parameters** (with value sets), and attach the program to a **request group** so a responsibility can run it. Optionally schedule it.

**122. What executable method types exist?**
**PL/SQL Stored Procedure, SQL*Plus, SQL*Loader, Host (shell), Oracle Reports, Java Concurrent Program, Spawned, Immediate,** and **Request Set Stage Function**, among others. The method determines how the program runs and what signature it expects (e.g., PL/SQL needs errbuf/retcode).

**123. What are errbuf and retcode in a PL/SQL concurrent program?**
A PL/SQL concurrent program's procedure must have the first two parameters `errbuf OUT VARCHAR2` and `retcode OUT VARCHAR2`. **retcode** returns the completion status — 0 = Success, 1 = Warning, 2 = Error; **errbuf** carries the error message. The concurrent manager reads these to set the request status.

**124. What is a request set?**
A request set lets you run multiple concurrent programs together as a unit, sequentially or in parallel, across **stages**, with the next stage conditional on prior completion status. Useful for batch flows (e.g., generate data → print → notify).

**125. What is the concurrent manager and what are its types?**
The concurrent manager schedules and runs concurrent requests. Types include the **Internal Concurrent Manager (ICM)** which controls others, the **Standard Manager** which runs any request, **Conflict Resolution Manager (CRM)** for incompatibilities, and **specialized/transaction managers**. You can define work shifts and specialization rules to balance load.

**126. How do you handle program incompatibilities?**
Define **incompatibility rules** on the concurrent program so two programs that shouldn't run simultaneously (e.g., a report and a purge touching the same data) are serialized by the Conflict Resolution Manager. Can be set as global or domain-specific.

**127. What is FNDLOAD and what do you use it for?**
**FNDLOAD** is a command-line utility to download/upload AOL configuration as portable `.ldt` files — concurrent programs, value sets, lookups, menus, responsibilities, profile options, request groups, messages, flexfields. It's how you migrate setups between instances reliably (DEV → UAT → PROD).

**128. What is the difference between FNDLOAD, XDFCMD/jpximport, and patch deployment?**
**FNDLOAD** moves AOL setup data. **jpximport/jpxexport** moves OAF substitutions; OAF personalizations move via Functional Administrator import/export (or XDFCMD/`akload`-style for some). Patches (via adpatch/adop) deploy code/file-system changes. You pick the tool by what's being migrated.

**129. How do you schedule and monitor concurrent requests?**
Schedule from the Submit Request form (or via API `FND_REQUEST.SUBMIT_REQUEST`) with periodic options. Monitor via **View Requests**, check the **log** and **output** files, and review phase/status (Pending/Running/Completed - Normal/Error/Warning). For recurring issues, check the manager logs and request history.

**130. What were the ServiceNow CTASKs you handled, and how do they relate to AOL/DBA work?**
On the GE project I logged ServiceNow change tasks for DBA-side actions that I couldn't do directly in PROD — bouncing **Apache/OACore** and **OC4J**, deploying personalization/CEMLI files, applying FND message updates, and restarting concurrent managers. I prepared the change, specified the steps, and coordinated the controlled execution.

---

# Section J — Oracle Workflow (Q131–Q136)

**131. What is Oracle Workflow and where is it used in iSupplier?**
Oracle Workflow automates business processes as a sequence of activities, notifications, and approvals defined in the **Workflow Builder**. In iSupplier/Procurement it drives PO approval, PO acknowledgement, change-request routing, and supplier/buyer notifications. I built a custom workflow to control planner notifications and route promise-date changes for approval.

**132. What are the core components of a workflow?**
**Item Type** (the workflow container), **Processes** (the diagram of activities), **Activities** (Functions = PL/SQL, Notifications, Processes), **Attributes** (item-level data), **Messages** (notification content), and **Lookups**. The runtime engine moves the item from activity to activity based on results.

**133. What is the difference between a Function activity and a Notification activity?**
A **Function activity** runs PL/SQL (no human interaction) and returns a result that determines the next transition. A **Notification activity** sends a message to a user/role and waits for a response (or FYI), then continues based on the response.

**134. How do notifications get delivered and responded to?**
Through the **Notification Mailer** (email) and the **Worklist** (in-app). A user can respond from email or the worklist; the response value feeds back into the workflow to drive the next transition. We suppressed unnecessary planner notifications to reduce noise.

**135. What is a workflow background process?**
A concurrent program (**Workflow Background Process**) that processes deferred and timed-out activities and stuck notifications. You schedule it per item type; without it, deferred activities don't progress.

**136. How do you debug a stuck workflow?**
Use the **Workflow Status Monitor** / Status Diagram to see where the item is stuck, query `WF_ITEM_ACTIVITY_STATUSES`, check error activities and the `WF_ERROR` process, run the Background Process for deferred items, and review the notification mailer status. `wfstatus`/`wfstat.sql` scripts help from the backend.

---

# Section K — Java, Spring Boot, REST & SOAP Integration (Q137–Q144)

**137. How did you integrate Oracle EBS with third-party systems?**
At TCS I built Java/Spring Boot components that exposed/consumed **REST and SOAP** services to exchange data with third-party supply-chain systems — e.g., publishing PO/shipment data and consuming external updates, with EBS-side APIs/interface tables landing the data. Integration Repository (IREP) services and custom PL/SQL APIs handled the EBS side.

**138. What is the difference between REST and SOAP?**
**SOAP** is a strict XML-based protocol with a WSDL contract, built-in standards (WS-Security, transactions), heavier payloads. **REST** is an architectural style using HTTP verbs (GET/POST/PUT/DELETE) and typically JSON, lighter and more flexible. SOAP suits formal enterprise contracts; REST suits lightweight, web-friendly integration.

**139. What are the common HTTP methods and status codes?**
Methods: **GET** (read), **POST** (create), **PUT** (replace), **PATCH** (partial update), **DELETE**. Status codes: **2xx** success (200 OK, 201 Created), **3xx** redirect, **4xx** client error (400 bad request, 401 unauthorized, 404 not found), **5xx** server error (500, 503).

**140. What is idempotency and why does it matter for integrations?**
An idempotent operation produces the same result no matter how many times it's called (GET, PUT, DELETE are idempotent; POST usually isn't). It matters because integrations retry on failure — idempotent endpoints (or idempotency keys) prevent duplicate orders/shipments from retries.

**141. How do you secure an API integration?**
Transport security (HTTPS/TLS), authentication (OAuth 2.0 / API keys / WS-Security for SOAP), authorization/scopes, input validation, and not exposing internal IDs/errors. For EBS, restrict the service users and responsibilities and audit calls.

**142. What is Spring Boot and what does it give you over plain Spring?**
Spring Boot is an opinionated layer over Spring that provides **auto-configuration, embedded servers (Tomcat), starter dependencies, and production features (actuator)** so you can stand up a service quickly without heavy XML config. You focus on business logic; Boot wires the rest.

**143. How do you handle errors and retries in an integration layer?**
Use proper status codes and a consistent error schema, implement **retry with backoff** for transient failures, **circuit breakers** to avoid hammering a down system, dead-letter queues for poison messages, and idempotency to make retries safe. Log correlation IDs to trace a transaction end-to-end.

**144. How does this experience translate to Oracle Integration Cloud (OIC)?**
The same integration concepts (REST/SOAP adapters, mapping, orchestration, error handling, security) apply in **OIC**, which provides prebuilt adapters (including for Oracle SaaS/ERP), visual mapping, and managed orchestration. My hand-coded REST/SOAP background means I understand what OIC automates — a strong base for moving to Fusion integrations.

---

# Section L — Procurement & Procure-to-Pay Functional (Q145–Q162)

**145. Walk me through the Procure-to-Pay (P2P) cycle.**
Requisition → Sourcing/RFQ-Quote → Purchase Order → PO Approval → PO Acknowledgement → Shipment/ASN → Receipt → Inspection (optional) → Invoice → 2/3/4-way Match → Payment → Accounting. iSupplier covers the supplier-facing middle: PO acknowledgement, ASN, receipts, returns, and invoice/payment visibility.

**146. What are the types of purchase orders in EBS?**
**Standard PO** (specific goods, qty, price, date), **Blanket Purchase Agreement (BPA)** (pricing/terms over time, released against), **Planned PO** (firm items with tentative schedules, released against), and **Contract Purchase Agreement** (terms only, no lines — referenced by Standard POs).

**147. What is a requisition and its types?**
A request to purchase. **Internal requisition** sources from inventory (internal sales order); **purchase requisition** sources externally (becomes a PO). In iProcurement these are created via self-service and can auto-create POs through document creation/sourcing rules.

**148. What is 2-way, 3-way, and 4-way matching?**
**2-way**: invoice ↔ PO (price & qty). **3-way**: invoice ↔ PO ↔ receipt (adds receipt qty). **4-way**: invoice ↔ PO ↔ receipt ↔ inspection (adds accepted-on-inspection qty). The match level is set on the PO shipment / item and controls when an invoice can be paid.

**149. What is a sourcing rule and ASL?**
A **Sourcing Rule** defines where to source an item (which suppliers and split %). The **Approved Supplier List (ASL)** lists approved supplier/site/item combinations with status and attributes. Together they drive automatic supplier selection during requisition-to-PO.

**150. What are receiving routing options?**
**Direct Delivery** (received straight to stock), **Standard Receipt** (received then delivered in two steps), and **Inspection Required** (received → inspect → accept/reject → deliver). Routing is set on the item/PO and affects the receipt flow and matching.

**151. What is the difference between Buyer and Requester/Approver?**
A **Requester** raises the need (requisition). A **Buyer** is the procurement professional who creates/manages the PO and negotiates with suppliers. An **Approver** authorizes the document per the approval hierarchy. iSupplier surrogate users are typically buyers acting for suppliers.

**152. How does PO approval hierarchy work?**
Via **Approval Groups** and **Approval Assignment Sets** (position or supervisor hierarchy) with document totals/limits, or via **AME (Approvals Management Engine)** for rule-based routing. The PO routes up the chain until someone with sufficient authority approves.

**153. What is AME and why use it?**
**Approvals Management Engine** externalizes approval rules from the application — you define conditions, rules, and approver groups declaratively. It's flexible (route by amount, category, cost center) and reusable across documents without coding workflow changes.

**154. What is the difference between Promise Date and on-time delivery measurement?**
On-time delivery compares the **actual receipt date** to the **Promise Date** (the supplier's committed date), not the Need-by Date. That's why we made Promise Date meaningful and mandatory rather than letting it silently default to Need-by — accurate OTD depends on a real promise.

**155. What happens during PO change requests from a supplier?**
The supplier proposes changes (date, quantity, sometimes price) via iSupplier; the change goes through change-order approval on the buyer side and, if accepted, revises the PO (incrementing the revision). We locked price on change requests so suppliers couldn't alter agreed pricing.

**156. What is a PO revision and when does it increment?**
A PO revision number increments when an **approved** PO is changed in a way that requires re-approval/re-acknowledgement (e.g., price, quantity, key dates). Minor changes may not bump the revision. Revisions create an audit trail of negotiated changes.

**157. What are document types and their controls in Purchasing?**
Document Types (Standard PO, BPA, Requisition, RFQ, Quotation, Release) have setup controls: whether approval/acknowledgement is required, security level (Private/Purchasing/Public/Hierarchy), access level (View/Modify/Full), and forward/owner-can-approve options. These govern who can see and act on documents.

**158. What is the difference between Quotation, RFQ, and BPA?**
An **RFQ** is the buyer's request for pricing sent to suppliers; a **Quotation** is the supplier's priced response; a **BPA** is the negotiated long-term agreement that may result. RFQ → Quotation → (award) → Agreement/PO.

**159. What key Purchasing tables would you query?**
`PO_HEADERS_ALL`, `PO_LINES_ALL`, `PO_LINE_LOCATIONS_ALL` (shipments), `PO_DISTRIBUTIONS_ALL`, `PO_RELEASES_ALL`, `PO_REQUISITION_HEADERS/LINES_ALL`, `PO_VENDORS`/`AP_SUPPLIERS`, `PO_VENDOR_SITES_ALL`, and receiving tables `RCV_SHIPMENT_HEADERS`/`RCV_SHIPMENT_LINES`/`RCV_TRANSACTIONS`.

**160. What is the difference between PO_VENDORS and the R12 supplier model?**
In R12 the supplier model moved to **AP_SUPPLIERS / AP_SUPPLIER_SITES_ALL** (with `PO_VENDORS`/`PO_VENDOR_SITES_ALL` retained as views/synonyms for compatibility) and integrated with **TCA (Trading Community Architecture)** parties. Suppliers are now parties in the TCA registry.

**161. How does the supplier-to-payment data flow work across PO/INV/AP?**
PO creates the commitment; receiving (RCV) records goods receipt and feeds inventory (INV); the supplier invoice in Payables (AP) is matched to PO/receipt; payment is issued and accounting flows to GL. iSupplier gives the supplier visibility into each step (PO, ASN, receipt, invoice, payment status).

**162. How would you troubleshoot "PO not showing in iSupplier for a supplier"?**
Check: supplier contact/user is registered and assigned the right responsibility; the supplier–site mapping and buyer/agent assignment; the PO's document type security/access; whether the PO is approved and in a status the portal displays; profile options and any personalization that hides it; and that the user's responsibility's data security profile includes that supplier.

---

# Section M — ASN, Shipments, Receipts & Returns (Q163–Q170)

**163. What happens in EBS when a supplier submits an ASN?**
The ASN creates records in the receiving open interface (`RCV_HEADERS_INTERFACE` / `RCV_TRANSACTIONS_INTERFACE`); the **Receiving Transaction Processor** validates and creates a shipment (`RCV_SHIPMENT_HEADERS`/`RCV_SHIPMENT_LINES`) in "Expected" state. The buyer's receiving team can then receive against the ASN, speeding up dock processing.

**164. What is the difference between an ASN and a receipt?**
An **ASN** is the supplier's pre-shipment notice (intent/in-transit). A **receipt** is the buyer's confirmation that goods physically arrived. The ASN pre-populates the receipt so receiving just confirms quantities rather than keying everything.

**165. What validations did you enforce at ASN creation and why?**
Mandatory Waybill/Airbill, Packing Slip, Country of Origin, Ship-To City, and Qty Shipped (customs and traceability); ship-method validation against the ship-to org; Promise/Need-by-based eligibility; and blocking ASNs on POs in "Requires Acknowledgement." These prevent downstream receipt rejections and ensure compliant customs documentation.

**166. How do labels and pack slips get generated?**
Via BI Publisher reports tied to the shipment data — single or **mass** print. I built Mass ASN Label / Pack-Slip print with parameterized selection and a WebCenter output option, so users could print for many shipments at once instead of one at a time.

**167. What is a return (RTV) and how does it appear to the supplier?**
A **Return to Vendor** sends received goods back (quality rejection, over-shipment). It's recorded as a return transaction against the receipt. In iSupplier the supplier sees Returns with reasons; we reordered the Returns columns and added PO Line Numbers so suppliers could reconcile against their lines.

**168. What is over/under receipt tolerance?**
Receiving controls allow receipts within a tolerance of the ordered quantity (e.g., over-receipt % allowed before warning/reject) and early/late receipt day windows. These tie directly into ASN eligibility — a supplier shouldn't notify quantities/dates the buyer's controls would reject.

**169. What are the key receiving tables and statuses?**
`RCV_SHIPMENT_HEADERS`, `RCV_SHIPMENT_LINES`, `RCV_TRANSACTIONS`, and the interface tables `RCV_HEADERS_INTERFACE`/`RCV_TRANSACTIONS_INTERFACE`. Shipment line statuses move from EXPECTED (ASN) → partially/fully received; transaction types include RECEIVE, DELIVER, RETURN TO VENDOR, CORRECT.

**170. A supplier says their ASN failed but they got no clear reason — how do you investigate?**
Check the receiving interface error (`RCV_TRANSACTIONS_INTERFACE` / `PO_INTERFACE_ERRORS`), confirm the shipment passed eligibility (dates, open qty, ack status, ship-to validity), review receiving controls/tolerances, and look at the validation/error message shown in the portal. On the GE project I improved error messaging precisely because failures were opaque to suppliers.

---

# Section N — Oracle Fusion Cloud SCM (Procurement, Supplier Portal, OIC, OTBI, FBDI) (Q171–Q190)

> This section is forward-looking. Be honest that your Fusion experience is in-progress, but show that you understand the platform and can map your EBS expertise to it.

**171. How does Oracle Fusion Cloud Procurement compare to EBS Purchasing?**
Same business process (source-to-pay) but a modern SaaS architecture: role-based security (no responsibilities), configuration via **Functional Setup Manager (FSM)** instead of System Administrator, **page composer / Application Composer / VBCS** instead of OAF personalization, **OTBI/BIP** for reporting, **FBDI/REST** for data loads, and quarterly auto-updates instead of patching. The functional concepts (POs, agreements, requisitions, supplier collaboration) carry over directly.

**172. What is the Fusion Supplier Portal and how does it map to iSupplier?**
Supplier Portal is the Fusion equivalent of iSupplier — suppliers manage their profile, view/acknowledge POs and agreements, submit ASNs, view receipts/returns, and submit invoices. My iSupplier/Procurement knowledge maps almost one-to-one; the difference is configuration and extension mechanisms, not the business flow.

**173. What is Supplier Qualification Management (SQM)?**
A Fusion Procurement module to assess and qualify suppliers — questionnaires, qualifications, assessments, and initiatives to evaluate supplier risk/capability. It's new relative to EBS and increasingly important for compliance-heavy industries.

**174. What are the main modules of Oracle Fusion Procurement?**
**Self-Service Procurement** (requisitioning), **Purchasing**, **Sourcing** (RFQ/auctions), **Supplier Portal**, **Supplier Qualification Management**, and **Procurement Contracts**. They sit within the broader Fusion SCM Cloud (Inventory, Order Management, PIM, Cost, Manufacturing).

**175. How is security handled in Fusion vs. EBS responsibilities?**
Fusion uses **Role-Based Access Control**: **job roles** (e.g., Buyer, Procurement Manager) contain **duty roles**, which contain **privileges**; **data security** is applied via data roles/security contexts. There's no "responsibility" — you assign roles to users, often via role provisioning rules.

**176. What is Functional Setup Manager (FSM)?**
FSM is where you configure Fusion — organized into **offerings → functional areas → setup tasks**, exportable/importable as **configuration packages (CSV)** to migrate setup between environments (the Cloud analogue of FNDLOAD/iSetup).

**177. What is FBDI and when do you use it?**
**File-Based Data Import** — Oracle-provided Excel templates that generate a CSV, which you load to interface tables (via UCM) and then run an import process. Used for bulk data migration/loads (suppliers, POs, requisitions) — the Cloud analogue of WebADI/interface loads I already know.

**178. What is ADFdi (ADF Desktop Integration)?**
ADFdi is the spreadsheet-based data entry in Fusion (e.g., manage suppliers, journal entries) — an Excel add-in that reads/writes directly to the application with validation. Conceptually it's the Fusion successor to WebADI.

**179. What is OTBI and how does it differ from BI Publisher in Fusion?**
**OTBI (Oracle Transactional Business Intelligence)** is ad-hoc, real-time analytics built on **subject areas** (predefined data models) — for self-service analyses and dashboards. **BI Publisher** in Fusion is for pixel-perfect, formatted, high-volume output (POs, labels, statements). My EBS BI Publisher skills transfer almost directly to Fusion BIP.

**180. What is a subject area in OTBI?**
A predefined, governed semantic model exposing dimensions and facts (e.g., "Procurement - Purchasing Real Time") so business users build reports without writing SQL. You drag attributes/measures; OTBI generates the query against the transactional data.

**181. What is Oracle Integration Cloud (OIC) and why does it matter for Fusion projects?**
OIC is Oracle's iPaaS for integrating Fusion SaaS with other systems — prebuilt **adapters** (ERP/SCM, REST, SOAP, FTP, DB), visual **integration orchestration**, mapping, scheduling, and error handling. Most Fusion implementations need OIC for inbound/outbound integrations (e.g., supplier feeds, 3PL, banks). My hand-coded REST/SOAP background maps directly.

**182. How do you extend Fusion (since there's no OAF personalization)?**
Layered tooling: **Page Composer** (UI-level changes), **Application Composer** (extend objects/fields, mainly CX/some SCM), **sandboxes** for isolated changes, **VBCS (Visual Builder)** for custom apps/pages, **BIP/OTBI** for reports, and **REST APIs/OIC** for integrations. Changes are sandboxed and published, not coded into the base.

**183. What are Fusion REST APIs and how are they used?**
Fusion exposes REST APIs for most objects (suppliers, purchase orders, requisitions). They're used for integration, bulk operations, and extensions — GET/POST/PATCH with JSON, secured via OAuth/basic auth. They replace much of what custom PL/SQL/forms did in EBS.

**184. How do quarterly updates work in Fusion Cloud?**
Oracle applies mandatory quarterly release updates automatically; customers test new features in a **test/stage pod** before they hit production. There's no choosing not to patch — so regression testing of extensions/integrations each quarter is part of the operating model.

**185. What is the difference between a P2P implementation in EBS vs. Fusion that you'd highlight?**
The functional design (requisition → PO → receipt → invoice → pay, supplier collaboration) is the same and that's where my value is. The delivery differs: configuration via FSM, security via roles, extensions via composers/VBCS, data via FBDI/REST, reporting via OTBI/BIP, integration via OIC — all of which I'm learning, building on concepts I already use.

**186. How would your iSupplier surrogate-supplier work translate to Fusion?**
In Fusion, internal users transacting for suppliers is handled through Supplier Portal roles and "manage suppliers/transact on behalf" capabilities plus data security. The business need (buyers acting for less-mature suppliers) is identical; I'd implement it via role configuration and, if needed, REST/OIC automation rather than a custom OAF flow.

**187. What certification are you pursuing and why?**
"**Oracle Fusion Cloud Procurement (1Z0-1065)** — it's the exact match for my iSupplier/Procurement background and validates Supplier Portal, Self-Service Procurement, Sourcing, and Purchasing. It's the fastest, most credible way to convert my EBS depth into a recognized Cloud credential." Only say this if you're actually studying for it.

**188. How long do you think it will take you to be productive on Fusion?**
"Because the procurement domain is identical and I already know BI Publisher, REST/SOAP, and data-loading concepts, I'd be productive on functional design quickly and ramp on Cloud-specific tooling (FSM, FBDI, OTBI, OIC) within a couple of focused months — faster than someone learning the domain from scratch."

**189. What is a sandbox in Fusion and why is it important?**
A sandbox is an isolated workspace where you make and test configuration/extension changes (flexfields, page composer, object changes) without affecting other users; you **publish** when validated. It's central to safe change management given quarterly updates.

**190. What are Descriptive Flexfields (DFF) and Extensible Flexfields (EFF) in Fusion?**
**DFFs** add extra attributes to a single row (like EBS DFFs). **EFFs** allow more complex, multi-row, context-sensitive attributes with their own pages. Both extend the data model declaratively without customization — configured via FSM and exposed on pages/reports.

---

# Section O — Situational & Closing (Q191–Q200)

**191. Production is down at go-live — suppliers can't submit ASNs. What do you do?**
Stay calm and structured: confirm scope/impact, check the obvious (service status, recent change, OACore/OC4J, errors in logs), communicate an acknowledgement to stakeholders with an ETA cadence, apply a known workaround if available, log/raise the DBA CTASK if it's infrastructure, fix root cause, then write a brief post-incident note and add a safeguard. Emphasize communication and rollback options.

**192. A buyer wants a customization Oracle doesn't support out of the box. How do you handle it?**
First, restate the underlying business need (not the requested solution). Check if a **personalization/configuration** can meet it before custom code. If an extension is truly needed, assess maintainability and patch-impact, propose it with effort/risk, and document it as a CEMLI. Push for the lightest-touch solution that satisfies the need.

**193. You inherit an undocumented customization that's breaking. How do you approach it?**
Reproduce the issue, use "About this Page"/diagnostics to find the components, read the controller/VO/personalization and any custom packages, check version history and migration records, and isolate the change that broke it. Fix minimally, then document what you learned so the next person isn't stuck.

**194. How do you ensure a smooth cutover?**
A sequenced, rehearsed cutover plan: freeze, migrate config (FNDLOAD/personalizations/CEMLI), validate data, smoke-test critical flows, get sign-off gates, and have a documented **rollback** for each step. Communicate the timeline and a clear go/no-go decision point.

**195. Two stakeholders give you conflicting priorities. What do you do?**
Don't unilaterally choose. Make the trade-off explicit (impact, effort, deadline) and escalate to the person who owns the priority decision (lead/PM), then proceed on the agreed order. Document the decision so it's not relitigated.

**196. How do you handle a requirement you think is a bad idea?**
Ask questions to understand the real goal, share your concern with data and an alternative, and respect the final call once made. The price-edit-on-BPA example is a good story: I flagged the compliance risk and offered a safer design, and it was accepted.

**197. How do you keep stakeholders confident during a long implementation?**
Regular, honest status with a simple RAG (red/amber/green), demos at each CRP so they see progress, early surfacing of risks (not last-minute surprises), and clear ownership of action items. Trust comes from predictability.

**198. Tell me about a time you improved a process or saved time.**
"Procurement teams were manually keying promise-date and PO changes one by one. I built WebADI bulk-upload templates backed by custom PL/SQL validation, so they could update many records at once with validation — eliminating repetitive manual entry for high-volume changes."

**199. What do you do when you don't know the answer to a technical problem?**
"I reproduce it, check Oracle documentation and My Oracle Support notes, isolate variables, and use diagnostics/logs. If I'm still blocked after a reasonable effort, I ask a colleague or raise an SR rather than burning days. Knowing when to escalate is part of the skill." Honesty here reads as maturity.

**200. Is there anything else you'd like us to know about you?**
A 20-second close: reinforce your fit. "Just that I've owned an Oracle SCM implementation end-to-end as the sole SME, I bridge the functional and technical sides, and I'm actively investing in Fusion Cloud. I'm confident I can add value quickly and grow with the role." End on enthusiasm for this specific opportunity.

---

*End of guide — 200 questions. Good luck, Himanshu. Review a section a day, practice the behavioral answers out loud, and make sure you can tell your GE Aerospace story three ways: a 60-second version, a 5-minute deep-dive, and a "hardest problem" version.*














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

**276. What is OAF passivation and when does it occur?**
Passivation is the process of serializing an Application Module's state (VO query handles, current rows, transaction context) to the database when the AM pool is full or an AM is being recycled. The state is written to `JBO_SESSION` tables. On the next user request, the AM is activated (deserialized from DB) — this is called activation. Passivation adds DB round-trips and latency. To minimize: (1) Keep AM state minimal — don't cache large collections in AM instance variables. (2) Increase pool size to reduce passivation frequency. (3) Use `prepareSession` to reinitialize lightweight state instead of relying on passivated data. Passivation is transparent to the controller but its performance impact is measurable — monitor via OAF diagnostic logs for `passivate` messages.

**277. What is the difference between OAF Root AM and nested AM?**
The Root AM (`OAApplicationModuleImpl`) is the top-level Application Module instantiated per OAF page session. Nested AMs are child AMs (nested within the Root AM) that handle specific logical components — e.g., a `PoDetailsAM` nested inside the main `PosPoSearchAM`. Nested AMs share the same database connection/transaction as the Root AM. They are defined in the AM structure in JDeveloper and accessed via `getRootApplicationModule().findApplicationModule("PoDetailsAM")`. Nesting allows modular design — each AM handles its own VOs and business methods. On passivation, the entire tree (root + nested AMs) is passivated together. When extending a nested AM via substitution, ensure the substitution path targets the correct AM within the hierarchy.

**278. How do you suppress OAF error messages and show custom user-friendly messages instead?**
In the CO's `processFormRequest` or the AM's save method, catch `OAException` and replace it: `catch (OAException e) { throw new OAException("XXGE", "XXGE_FRIENDLY_MSG", OAException.ERROR); }` where `XXGE_FRIENDLY_MSG` is defined in FND Messages. For validation errors, use `OAException` with `OAException.ERROR` severity — OAF displays these in the page error region automatically. For warnings (non-blocking): `OAException.WARNING` severity. Never expose Oracle error codes (ORA-xxxxx) to end suppliers — always translate to business-friendly messages via FND_MESSAGE. In the GE project, we wrapped all custom PL/SQL package calls in a Java try-catch that mapped specific `APP_EXCEPTION` error names to supplier-friendly messages.

**279. What is SPEL (Simplified Page Expression Language) in OAF and how do you use it?**
SPEL is OAF's expression language for setting UI properties dynamically based on runtime values. Syntax: `${oa.profile.PROFILE_NAME}` (profile value), `${oa.UserName}` (current user), `${oa.OrgId}` (current org), `${ViewObjectName.AttributeName}` (VO attribute value). Used in personalization or page XML to conditionally render elements: setting a field's `rendered` property to `${oa.profile.XXGE_SHOW_PRICE_FIELD == 'Y'}` makes it visible only when the profile is Y. In JDeveloper, SPEL expressions are set on bean properties. Limitations: SPEL is evaluated at render time, not at query time — cannot filter VO results with SPEL. Also, SPEL expressions on standard beans may be lost after a patch if the standard XML is overwritten — always set via controller code for robustness.

**280. How does OAF handle session management and what is ICX_SESSIONS?**
OAF session state is managed via the `ICX_SESSIONS` table. Each supplier login creates a row with `SESSION_ID` (cookie value), `USER_ID`, `RESPONSIBILITY_ID`, `FUNCTION_ID`, `LAST_CONNECT` (timestamp of last activity). The ICX session cookie (`ASESSIONID`) is sent to the browser. On each request, OAF validates the session by querying `ICX_SESSIONS` — if `LAST_CONNECT` is older than the session timeout (`ICX: Session Timeout` profile), the session is invalidated and the user is redirected to login. Session timeout is per-responsibility. For iSupplier suppliers with slow connections, increasing the timeout to 60 minutes reduced "session expired" complaints significantly. Monitor active sessions: `SELECT COUNT(*) FROM icx_sessions WHERE last_connect > SYSDATE - 1/24`.

**281. What is the OAF Dictionary and how is it used?**
The OAF Data Dictionary (not to be confused with Oracle's DB data dictionary) refers to the MDS metadata store in `JDR_PATHS`, `JDR_COMPONENTS`, `JDR_ATTRIBUTES`. It defines the UI structure of OAF pages: page layout, regions, items, their properties. The "dictionary" aspect: OAF reads this metadata at runtime to construct page beans — it's a declarative definition, not compiled code. Personalizations extend this dictionary by adding override layers in `JDR_PATHS` with `TYPE = 'CUSTOMIZATION'`. The "About This Page" link (when enabled via profile `FND: Diagnostics`) shows the full dictionary path for any page element, which is essential for knowing the exact path to target in a personalization or substitution. Exporting the dictionary with FNDLOAD (`JDR_UTILS`) captures the full page definition as an XML file.

**282. How do you extend an OAF AM to add a custom method callable from a CO?**
(1) Create a Java class `XXGEPosPoSearchAMImpl` extending the standard `PosPoSearchAMImpl`. (2) Add your custom method: `public String getCustomSupplierInfo(Number vendorId) { ... }`. (3) Register as a substitution in Oracle MDS: `FNDLOAD APPS/... 0 Y UPLOAD $JTF_TOP/patch/115/import/jtfrs.lct XXGE_AM_SUBST.ldt`. (4) In the CO, access: `XXGEPosPoSearchAMImpl am = (XXGEPosPoSearchAMImpl) pageContext.getApplicationModule(webBean); String info = am.getCustomSupplierInfo(vendorId);`. Key rule: never modify standard AM source files — always extend via substitution. If the AM pool creates a standard AM instance (not the substitute), check that the substitution is registered at the correct level (SITE level) and the JAR is deployed correctly.

**283. What is the difference between OAF Controller processRequest and processFormRequest?**
`processRequest(OAPageContext pageContext, OAWebBean webBean)`: called on every HTTP GET request — page load, navigation, initial render. Use this to: initialize page data, set default field values, conditionally render regions, query VOs. `processFormRequest(OAPageContext pageContext, OAWebBean webBean)`: called on HTTP POST — form submit, button click, LOV selection. Use this to: handle button clicks, validate user input, call AM save methods, navigate to next page. Important: do not query the database in `processFormRequest` unless necessary — the VO data is already available from the previous `processRequest`. Also: `processFormRequest` is called for ALL form submits on the page, not just your specific button — use `pageContext.getParameter("event")` to identify which button was clicked.

**284. How do you create a custom LOV (List of Values) in OAF?**
(1) Create a VO for the LOV data: `XXGEVendorLOVVO` with SQL `SELECT VENDOR_ID, VENDOR_NAME FROM AP_SUPPLIERS WHERE ENABLED_FLAG='Y'`. (2) In JDeveloper, create a new OAF page of type `ListOfValues`. (3) Add a `OATableLayoutBean` displaying the LOV VO columns. (4) On the calling page, set the item's `lovRegion` property to the LOV page path. (5) Set `lovCriteria` to map the parent field to the LOV's search column. (6) Set `returnItems` to map the LOV selected value back to the parent form field. In a personalization: you cannot create a new LOV — you can only change an existing item's lovRegion to point to a different page. For a net-new LOV, use a CO extension and programmatically set `setListOfValues` on the `OAMessageLovInputBean` instance.

**285. What causes "No data found" vs "Too many rows" OAF errors and how do you fix them?**
Both originate from PL/SQL `SELECT INTO` statements called by OAF AMs/controllers. `NO_DATA_FOUND` (ORA-01403): the SELECT returned zero rows — typically a misconfigured WHERE clause (wrong org_id, wrong primary key). Fix: add a COUNT check before the SELECT INTO, or use `OPEN cursor FOR SELECT; FETCH...` with a null check. `TOO_MANY_ROWS` (ORA-01422): the SELECT returned >1 row — the WHERE clause is not selective enough (missing a join condition like `AND VENDOR_SITE_ID = :p_site_id`). Fix: add the missing filter, or use `SELECT MAX(...)` if you genuinely want one value. In OAF, these surface as Java `oracle.jbo.SQLStmtException` wrapping the PL/SQL error — trace with `DBMS_UTILITY.FORMAT_ERROR_BACKTRACE` enabled in your package exception handler.

---

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
FNDLOAD apps/appsdev@devdb 0 Y DOWNLOAD   $FND_TOP/patch/115/import/afcpprog.lct   XXGEA_ASN_COMPLIANCE.ldt   PROGRAM APPLICATION_SHORT_NAME="XX"   CONCURRENT_PROGRAM_NAME="XXGEA_ASN_COMPLIANCE"

# In PROD - Upload (within CTASK)
FNDLOAD apps/appsprod@proddb 0 Y UPLOAD   $FND_TOP/patch/115/import/afcpprog.lct   XXGEA_ASN_COMPLIANCE.ldt
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


# Section X — Advanced Architecture & Scenario Design (Q481–Q530)

**481. You are asked to design the Oracle EBS iSupplier rollout for 5 manufacturing sites. What is your architecture approach?**
Phase approach: (1) **Foundation** — single EBS instance with MOAC enabled, one Business Group, org_id per site (BU). Each site gets its own Operating Unit, Inventory Org, and supplier assignment via `AP_SUPPLIER_SITES_ALL.ORG_ID`. (2) **Shared master data** — supplier master at party level (TCA/HZ_PARTIES) shared across all OUs; site-specific bank accounts, payment terms, and contacts per OU. (3) **iSupplier access** — `POS_SUPPLIER_USERS` controls which supplier users see which OU's POs. Use ICX responsibility assignments to scope access. (4) **Rollout sequencing** — pilot site 1, stabilize, then parallel-onboard remaining 4 in 60-day windows. (5) **Single OC4J cluster** with sticky sessions and shared DB — no data isolation issues since MOAC handles it.

**482. How do you handle OAF personalizations when you have 5 different sites with different business rules?**
Use OAF personalization levels: Site > Responsibility > User. For site-specific rules, create separate Responsibilities per site (e.g., `GE_ISUPPLIER_SITE_A`, `GE_ISUPPLIER_SITE_B`), then apply Responsibility-level personalizations. This avoids overwriting shared Site-level personalizations. If the difference is minor (e.g., one field required at site A but optional at site B), use SPEL expressions like `${oa.profile.ORG_ID == '101'}` in the Required property. Store personalizations in `JDR_PATHS`/`JDR_COMPONENTS` — they're OB-aware and org-scoped. Document each personalization in a CEMLI register with the responsible site.

**483. A business stakeholder presents a requirement that Oracle standard iSupplier cannot support out-of-the-box. Walk through your approach.**
Step 1: Document the exact requirement — what the user wants to see/do, the business justification, and frequency of use. Step 2: Attempt standard config first — can a DFF, profile option, or existing OAF personalization (hide/show field, change LOV) satisfy it? Step 3: If not, assess CEMLI type: is it a custom form/page (OAF extension), a report (BIP), a workflow customization, or a data load (WebADI/interface)? Step 4: Create a Technical Design Document (TDD) with DB impact, patching risk, upgrade path. Step 5: Get sign-off from functional lead and IT manager. Step 6: Build in DEV, unit test, regression test iSupplier core flows (PO view, ASN creation, invoice view). Step 7: Deploy via FNDLOAD + CTASK through UAT → PROD.

**484. Describe your approach to designing the surrogate vendor model for GE's 67 accounts across 5 sites.**
The challenge: GE's subsidiaries are both customer and supplier. Solution: (1) Create a `XXGE_SURROGATE_VENDOR` table mapping `VENDOR_ID` + `VENDOR_SITE_ID` to an internal `ORGANIZATION_ID` (GE entity). (2) For PO creation, a pre-insert trigger on `PO_HEADERS_ALL` checks if the vendor is in the surrogate table and stamps `XXGE_SURROGATE_FLAG = 'Y'` on a DFF. (3) The iSupplier supplier portal view is filtered to show surrogates a custom tab ("Internal Transfers") — implemented as an OAF substitution on `PosPoSummaryPG`. (4) Approvals bypass standard sourcing rules for surrogates via a custom Workflow attribute check. (5) Reporting separates surrogate POs from external vendor POs using the DFF flag.

**485. How do you design the ASN eligibility engine — determining which PO lines are eligible for ASN creation?**
Eligibility rules: (1) PO must be Approved (`AUTHORIZATION_STATUS = 'APPROVED'`). (2) Line type must be Goods (`ORDER_TYPE_LOOKUP_CODE = 'GOODS'`). (3) Receipt routing must be Standard Receipt (not Direct Delivery). (4) `CLOSED_CODE` must not be 'CLOSED FOR RECEIVING'. (5) Quantity remaining > 0 (`QUANTITY_ORDERED - QUANTITY_RECEIVED - QUANTITY_CANCELLED > 0`). (6) Promise date not expired (if enforced). Implementation: a PL/SQL function `XXGE_ASN_PKG.IS_ELIGIBLE(p_po_line_location_id)` encapsulates all rules, called from the OAF VO's WHERE clause as a view object filter. This centralizes rule logic — when business rules change, only the package changes, not the VO or UI.

**486. What artifacts would you produce for a supplier onboarding data migration from legacy to Oracle EBS?**
(1) **Data mapping spreadsheet** — legacy field → EBS table.column, transformation rules, default values. (2) **Supplier conversion program** — PL/SQL using `AP_VENDOR_PUB_PKG.CREATE_VENDOR` and `CREATE_VENDOR_SITE` APIs; log errors to `XXGE_MIGRATION_ERRORS`. (3) **Reconciliation report** — count of legacy suppliers vs EBS suppliers post-load; highlight rejected records with reasons. (4) **Data quality scripts** — pre-migration: identify duplicates, missing mandatory fields, invalid payment terms. (5) **Cutover runbook** — freeze legacy system, run migration, validate, open EBS. (6) **Rollback plan** — script to delete loaded suppliers if validation fails (use `VENDOR_ID` range). Present artifacts in weekly migration steering meetings.

**487. You have a 5-site cutover planned for a single weekend. What does your cutover plan contain?**
A detailed runbook with: (1) **T-4 weeks:** freeze legacy transactions, data reconciliation sign-off, mock cutover in UAT. (2) **T-1 week:** final data migration run in PROD sandbox, CTASK submitted for go-live weekend. (3) **Friday 6 PM:** freeze source systems, lock EBS for migration. (4) **Friday 8 PM:** run conversion programs (supplier, open PO, on-hand balance). (5) **Saturday AM:** validation team runs reconciliation reports — supplier count, PO count, on-hand quantity by org. (6) **Saturday PM:** UAT sign-off from functional leads per site. (7) **Sunday AM:** go-live — cut over DNS/URL, send supplier communication, open EBS. (8) **Go/No-Go checkpoint at each stage** with named decision-makers. Rollback trigger: if validation fails >5% threshold, revert to legacy for 48 hours.

**488. How do you triage a backlog of 40 UAT defects two weeks before go-live?**
Priority matrix: Severity × Likelihood. (1) **Blocker** (P1): defects that prevent core flows — PO view, ASN creation, invoice view. Fix immediately. (2) **High** (P2): incorrect data, wrong calculations, workflow not routing. Fix before go-live. (3) **Medium** (P3): UI cosmetic issues, non-critical validations. Fix in hypercare sprint post-go-live. (4) **Low** (P4): enhancement requests that snuck into UAT. Defer to Phase 2. Assign each defect to a developer with a 2-day fix SLA for P1/P2. Run a daily triage call with the functional lead. Track in JIRA board. Re-test every P1/P2 fix the same day in UAT. Document risk acceptance for any P2 deferred to post-go-live.

**489. How would you design a supplier training program for 200+ supplier contacts across 5 sites?**
(1) **Role-based training** — Supplier PO Viewer (read-only), Supplier ASN Creator, Supplier Invoice Submitter — separate 1-hour sessions per role. (2) **Delivery** — live WebEx sessions per site, recorded for async access. (3) **Quick reference cards** — 1-page PDFs for each core task (how to view PO, how to create ASN). (4) **Sandbox environment** — dedicated EBS instance with dummy POs for practice. (5) **Train-the-trainer** — designate 1 super-user per site who handles first-level support. (6) **Helpdesk FAQ** — top 10 common questions documented in a SharePoint/Confluence page. (7) **Post-go-live check-in** — 2-week follow-up call with each site. Track training completion in a spreadsheet; make it a go-live dependency.

**490. Describe how you would design a notification suppression feature for high-frequency workflow alerts.**
Problem: planners receive 100+ WF notifications/day from promise-date updates — alert fatigue. Design: (1) Create a profile option `XXGE_WF_NOTIF_SUPPRESS_FREQ` (values: IMMEDIATE, DAILY_DIGEST, NEVER) per user. (2) Instead of direct WF notification, route through a custom `XXGE_NOTIF_QUEUE` table: `INSERT INTO XXGE_NOTIF_QUEUE (recipient_id, message_type, entity_id, created_date)`. (3) A nightly concurrent program `XXGE_NOTIF_DIGEST_CP` aggregates queued notifications per recipient, generates one summary email using UTL_MAIL with a BIP-formatted HTML table. (4) For immediate-mode users, a post-insert trigger on `XXGE_NOTIF_QUEUE` calls `WF_NOTIFICATION.SEND` directly. (5) Suppress duplicates: if same `(recipient_id, entity_id, message_type)` already queued today, skip.

**491. How would you design a regression testing strategy for EBS iSupplier after each quarterly patch?**
(1) **Test script library** — 30 core test scripts covering: supplier login, PO search by PO number/date/status, ASN creation full flow, shipment confirmation, invoice view, promise date update, change request submission. (2) **Test data** — maintain a set of permanent test POs in PROD (do not close/receive them) or use a PROD-clone UAT. (3) **Patch testing window** — after patch applied to UAT, run all 30 scripts within 48 hours. (4) **Personalization regression** — run `FNDLOAD` export of personalizations before patch; compare JDR_PATHS content after patch to detect overwritten personalizations. (5) **Automation** — use Oracle Application Testing Suite (OATS) or Selenium to automate the 10 most critical test scripts. (6) **Sign-off** — functional lead signs off UAT before PROD patch application.

**492. What is your rollback plan if a go-live on Friday fails and users need access Monday?**
(1) **Pre-go-live:** export current PROD DB (Data Pump export of key tables: `PO_HEADERS_ALL`, `AP_SUPPLIERS`, `RCV_SHIPMENT_HEADERS`) as a restore point. Keep the legacy system in read-only mode (not shut down) for 72 hours. (2) **Decision trigger:** if >20% of users cannot complete core workflows by Saturday noon, activate rollback. (3) **Rollback steps:** re-point DNS/load balancer to legacy URL; notify all supplier contacts with template email; import any transactions entered into EBS during the window back to legacy (if feasible — usually freeze EBS transactions during validation window). (4) **Root-cause fix:** identify the blocker defect, fix in DEV, test in UAT over the weekend, reschedule go-live for following Friday. (5) **Communication:** designated go/no-go owner (IT manager + functional lead) makes the call; status updates every 2 hours to stakeholders.

**493. How do you handle changing requirements that arrive after UAT sign-off?**
Invoke change control: (1) Log as a change request in JIRA with business justification and urgency. (2) Impact assess: is it a config change (low risk, possibly done in PROD directly) or a code change (high risk, must go through DEV→UAT→PROD)? (3) If critical for go-live: negotiate a scope freeze with the project manager — only P1 blockers get in. (4) If non-critical: defer to Phase 2 sprint (first 30 days post-go-live). (5) Document all deferred changes in a "Phase 2 backlog" in JIRA so nothing is lost. (6) Update the functional design document and obtain re-sign-off from the business if scope changes significantly. The key message to stakeholders: every post-UAT change adds risk and delays; decisions have a cost.

**494. Walk through the steps to onboard a new supplier in Oracle EBS iSupplier.**
(1) Procurement team creates supplier in EBS: `Purchasing > Suppliers > Entry` — enter name, TIN, DUNS, payment terms, bank account. (2) Create supplier site(s) with address, OU assignment, contact email. (3) IT creates FND user for supplier contact: `System Administrator > Security > User > Define` — assign `iSupplier Portal Full Access` responsibility. (4) Map FND user to supplier: `iSupplier Portal > Administration > Users > Supplier User Management` — link user to `VENDOR_ID` in `POS_SUPPLIER_USERS`. (5) Notify supplier with login URL, username, and temp password. (6) Supplier logs in, views POs assigned to their site, and can create ASNs/invoices. (7) Optional: run `XXGE_SUPPLIER_ONBOARD_CP` to send welcome email and verify setup via validation checks.

**495. Design a promise-date approval workflow — when a supplier sets a promise date beyond X days, escalate for approval.**
(1) Trigger: OAF controller in `PosUpdatePromiseDateCO` — on Save, call `XXGE_PROMISE_DATE_PKG.CHECK_THRESHOLD(p_po_line_location_id, p_promise_date)`. If promise date > `NEED_BY_DATE + threshold_days`, return flag `'APPROVAL_REQUIRED'`. (2) OAF shows a warning message and routes to a confirmation page. (3) On confirm, insert record into `XXGE_PROMISE_DATE_APPROVALS` with status `PENDING`, then launch custom WF item (`XXGE_PD_APPROVAL`). (4) WF sends notification to planner's responsibility inbox with Accept/Reject responses. (5) On Accept: update `PO_LINE_LOCATIONS_ALL.PROMISED_DATE`, close WF item. On Reject: notify supplier, revert to original promise date. (6) Escalation: if planner doesn't respond in 24 hours, auto-escalate to manager (WF timeout transition).

**496. How would you architect a KPI metrics framework for measuring iSupplier portal success?**
Key metrics: (1) **Supplier adoption rate** — % of active suppliers using iSupplier vs total suppliers (source: `POS_SUPPLIER_USERS` vs `AP_SUPPLIERS`). (2) **ASN submission rate** — ASNs submitted / PO shipments expected (source: `RCV_SHIPMENT_HEADERS.SOURCE_DOCUMENT_CODE = 'PO'`). (3) **On-time delivery** — POs with `ACTUAL_DATE <= NEED_BY_DATE` (source: `RCV_TRANSACTIONS`). (4) **Promise date accuracy** — `PROMISED_DATE` vs actual receipt date variance. (5) **Invoice processing time** — invoice creation to payment. Implementation: custom BIP report/dashboard querying these metrics, scheduled weekly. Present in Oracle OBIEE or a simple HTML dashboard served from EBS. Review monthly with procurement managers.

**497. A supplier self-registration requirement asks for an online form for new suppliers to apply. Can EBS support this?**
Oracle Supplier Lifecycle Management (SLM) in EBS R12.2+ supports supplier self-registration: `iSupplier Portal > Supplier Registration`. The supplier fills out a web form — company info, bank details, commodity codes — which creates a record in `AP_SUP_SITE_CONTACT_INT` and triggers a workflow for internal review/approval before the supplier is created in the vendor master. If SLM is not licensed: build a custom OAF page (unauthenticated, accessed via ICX guest user session) that inserts into a custom registration table, triggers a WF notification to procurement, and upon approval calls `AP_VENDOR_PUB_PKG.CREATE_VENDOR`. Security consideration: rate-limit the registration page and add CAPTCHA via a custom JavaScript controller extension.

**498. How do you manage and document CEMLIs (Customizations, Extensions, Modifications, Localizations, Integrations) in a large EBS project?**
Maintain a CEMLI Register (Excel or JIRA Epic) with columns: CEMLI ID, Type, Module, Object Name (package/page/report), Business Purpose, Dev Owner, Status (Dev/UAT/PROD), Test Script ID, FNDLOAD command, Last Patched Date, Upgrade Risk (High/Med/Low). Each CEMLI gets a unique ID (e.g., `XXGE-OAF-001`). On each patch cycle: run impact analysis — check if patched standard objects overlap with our modifications (compare `AD_BUGS` with CEMLI object list). High-risk CEMLIs (OAF substitutions, standard package overrides) are regression-tested first. The register is stored in SharePoint and linked from each JIRA ticket for full traceability.

**499. What is your approach to handling schema changes during an EBS upgrade?**
(1) **Pre-upgrade:** run `ADZDSHWSQL.sql` (AutoPatch driver analysis) to identify which standard objects change. Cross-reference with CEMLI register. (2) **Custom tables** (`XXGE_*`): safe — Oracle won't touch them. (3) **Custom packages referencing standard tables** (`PO_HEADERS_ALL`): check if new columns added, old columns removed, or column type changes — recompile and test. (4) **OAF substitutions:** substituted classes may have changed constructor signatures or method names — test all substitutions. (5) **JDR personalizations:** run `FNDLOAD` export before upgrade; after upgrade, import back and verify. (6) **Post-upgrade:** run `utlrp.sql` to recompile invalid objects; run regression test suite. Document all CEMLI changes needed in a patch impact report.

**500. Design a 12-month migration strategy from Oracle EBS to Oracle Fusion Cloud SCM.**
Phase 1 (M1–M3): **Discovery & Design** — map EBS configurations to Fusion equivalents; identify CEMLIs that need to be reimplemented in OTBI/BIP/VBCS; assess integrations (Spring Boot services, WebADI). Phase 2 (M4–M6): **Build** — configure Fusion SCM (Procurement, Inventory); build OTBI reports to replace BIP; rebuild integrations using OIC (Oracle Integration Cloud) instead of ISG. Phase 3 (M7–M9): **Data Migration** — suppliers, open POs, on-hand balances via Fusion FBDI (File-Based Data Import). Phase 4 (M10–M11): **UAT & Training** — parallel run: enter transactions in both EBS and Fusion, compare outputs. Phase 5 (M12): **Cutover** — freeze EBS, load final delta transactions in Fusion, go-live. Keep EBS read-only for 6 months post-go-live for historical reporting.

**501. What does a quarterly patch process look like in a well-managed EBS environment?**
(1) **Patch notification:** Oracle releases RUP/CPU quarterly — subscribe to My Oracle Support alerts. (2) **Impact analysis (Week 1):** download patch, run `opatch prereq CheckConflictAgainstOHWithDetail` in DEV; review `README`; check CEMLI register for conflicts. (3) **DEV patch (Week 2):** apply with `adpatch` or `adop` (R12.2); run `utlrp.sql`; test DEV. (4) **UAT patch (Week 3):** apply in UAT; run 30-script regression suite; fix any broken CEMLIs; functional sign-off. (5) **PROD patch (Week 4):** submit CTASK in ServiceNow for production change window (typically Saturday night); apply patch; validate; close CTASK. (6) **Documentation:** update CEMLI register with "last patched" date; archive patch README in SharePoint.

**502. What lessons learned would you document after a successful 5-site iSupplier rollout?**
(1) **Personalization testing must be regression-tested post every patch** — we missed this once and a supplier-facing page showed wrong fields for 2 days. (2) **Supplier onboarding takes 3x longer than estimated** — account for supplier IT approvals, firewall rules for SSL certs, and contact turnover. (3) **MOAC profile setup errors are silent** — if `MO: Security Profile` is wrong, suppliers see blank PO lists with no error. Build a sanity-check concurrent program. (4) **Surrogate vendor logic should be centralized in one package** — early in the project we had it in 3 places, causing inconsistencies. (5) **Communication plan matters** — suppliers need 4 weeks notice, not 1 week. (6) **Parallel run for 2 weeks** is critical — catching transaction discrepancies before legacy shutdown saved us from 2 major data issues.

**503. How do you approach a multi-org (MOAC) security model design for a supplier portal?**
MOAC design: (1) Define one Operating Unit per business unit/site. (2) Create one `MO: Security Profile` per responsibility that lists the OUs a user can access. (3) For iSupplier: supplier users should see only POs from OUs where their `VENDOR_SITE_ID` is assigned. Map this via `AP_SUPPLIER_SITES_ALL.ORG_ID`. (4) Avoid giving supplier users access to multiple OUs unless they genuinely serve multiple sites — over-permissioning creates data leakage risk. (5) Internal procurement staff need access to all OUs for cross-org reporting — create a `ALL_ORG_SEC_PROFILE`. (6) Test with a supplier user who has sites in OU 101 and OU 102 — verify they see POs from both, but not OU 103. Test with a user with only OU 101 — verify they cannot see OU 102 POs.

**504. Explain how you would design a technical design document (TDD) for an OAF customization.**
TDD sections: (1) **Overview** — business requirement, CEMLI ID, type (Extension/Substitution/New Page). (2) **Functional Design Summary** — what the UI change does, screenshots of before/after mockup. (3) **Technical Approach** — OAF component extended (CO/VO/AM/EO), substitution path, new attributes. (4) **Database Impact** — new tables (`XXGE_*`), columns, indexes, sequences. (5) **PL/SQL Packages** — package name, procedure signatures, logic overview. (6) **Integration Points** — APIs called, WF events raised. (7) **Error Handling** — what errors can occur, how they are surfaced to user. (8) **Test Scenarios** — happy path, error path, edge cases. (9) **Deployment Steps** — FNDLOAD commands, JAR deployment steps, profile options to set. (10) **Rollback Steps** — how to undo if deployment fails.

**505. A go-live is 24 hours away and a critical defect is found — the ASN creation page throws ORA-01422 for multi-line POs. What do you do?**
ORA-01422 = `exact fetch returns more than requested number of rows` — a `SELECT INTO` returned multiple rows. Immediate action: (1) Reproduce in UAT within 30 minutes. (2) Identify the exact PL/SQL line — check `DBMS_UTILITY.FORMAT_ERROR_BACKTRACE` in the OAF error log. (3) Likely cause: a custom VO override or controller calls a function with `SELECT INTO` that doesn't filter by `PO_LINE_LOCATION_ID` — might only filter by `PO_HEADER_ID`, returning one row per line. Fix: add `AND PO_LINE_LOCATION_ID = p_line_location_id` to the WHERE clause. (4) Fix, test, deploy to UAT in 2 hours. (5) If fix isn't ready: implement a workaround — restrict ASN creation to single-line POs via a validation message, communicate to business that multi-line ASNs will be available in 48 hours. (6) Go/no-go decision with IT manager and functional lead.

**506. What is your approach to capacity planning for the EBS iSupplier portal?**
(1) **Baseline:** current peak concurrent users (query `ICX_SESSIONS` for active sessions at peak hours). (2) **Growth projection:** if rolling out 3 new sites, estimate 50 new suppliers × 2 contacts each = 100 new users. Add 30% buffer. (3) **OC4J heap sizing:** each active OAF session holds ~5 MB heap. 200 concurrent = 1 GB heap minimum. Set `java.heap` in `opmn.xml` to 2 GB with 25% growth headroom. (4) **DB connections:** 200 sessions × 2 connections/session (main + BC4J) = 400 DB connections. Check `PROCESSES` and `SESSIONS` DB parameters. (5) **Load test:** use Oracle Load Testing (OAT) or JMeter to simulate 200 concurrent ASN creations — measure response time, error rate, OC4J heap. (6) **Recommendation:** document findings in a capacity plan document; review quarterly.

**507. How do you handle a situation where a supplier claims they submitted an ASN but it doesn't appear in EBS?**
Troubleshooting steps: (1) Check `RCV_HEADERS_INTERFACE` and `RCV_TRANSACTIONS_INTERFACE` for the supplier's records with any status (`PROCESSING`, `ERROR`). (2) If records exist with `PROCESSING_STATUS_CODE = 'ERROR'`, check `PO_INTERFACE_ERRORS` for error message. (3) If no records found: check `ICX_SESSIONS` for the supplier's session around the claimed submission time — did the session expire mid-submit? (4) Check OC4J logs for the submission timestamp — look for any `Exception` in the AM method that handles ASN commit. (5) Check if a concurrent program `Receiving Transaction Processor` is running — stuck RTP would leave records in interface tables. (6) Response to supplier: provide evidence of the error message or session expiry; help them resubmit; if data issue, fix and manually process the interface record.

**508. Describe your experience facilitating technical design reviews.**
In the GE project, I facilitated weekly tech design reviews for new CEMLIs. Format: 30-minute structured review with developer presenting TDD + live demo in DEV. Reviewers: senior developer, functional lead, DBA. Review checklist: (1) Does the design use standard APIs (no direct DML on Oracle standard tables)? (2) Are error messages user-friendly and using `FND_MESSAGES`? (3) Is the solution patching-safe (no modifications to standard shipped files)? (4) Are all database objects in `XXGE_` schema? (5) Is there a rollback plan? Action items logged in JIRA; must be resolved before UAT deployment. Reviews caught ~30% of design issues before they became defects — significant time savings.

**509. How do you design a DPAS/customs compliance feature for PO acknowledgement in iSupplier?**
DPAS (Defense Priorities and Allocations System) ratings are required for US defense contracts. Design: (1) Add a DFF segment `DPAS_RATING` (values: DO-A1, DO-A2, DO-C9, etc.) on `PO_HEADERS_ALL` using a value set with validation. (2) In iSupplier PO acknowledgement page, extend the OAF controller to display DPAS rating if present — read-only for supplier. (3) For supplier acknowledgement, add a custom checkbox "I acknowledge the DPAS rating" that stamps `PO_ACCEPTANCES.ACCEPTED_FLAG = 'Y'` with a timestamp. (4) A BIP report lists all DPAS-rated POs with acknowledgement status — sent to compliance team weekly. (5) A workflow notification to the supplier includes the DPAS clause text in the email body. All DPAS logic gated behind a profile option `XXGE_DPAS_ENABLED` so it can be toggled per OU.

**510. A major supplier (30% of GE's spend) complains that iSupplier is unusable and they want to revert to email POs. How do you handle this?**
(1) **Immediate response:** schedule an urgent call within 24 hours with the supplier's operations team and GE procurement lead. (2) **Root cause:** ask the supplier to screen-share and walk through their workflow — identify the specific pain point (slow page, confusing UI, missing feature, frequent errors). (3) **Quick wins:** if it's a UI training issue, arrange a 1-hour live training session. If it's a specific bug, log a P1 JIRA and commit to a fix within 48 hours. (4) **Short-term:** if the issue genuinely can't be fixed quickly, agree on a temporary manual process (email PO copy + manual ASN entry by GE team) for 2 weeks while fix is developed. (5) **Long-term:** add this supplier's use case to the regression test suite. (6) **Escalation:** document the issue and resolution for the weekly steering committee — a major supplier's satisfaction is a project KPI.

**511. How do you ensure your OAF customizations are testable (TDD approach)?**
OAF doesn't have native unit test support, but you can structure for testability: (1) Keep business logic in PL/SQL packages, not in Java controllers — PL/SQL can be unit-tested with `utPLSQL`. (2) Controller (`processRequest`/`processFormRequest`) should only orchestrate — call one method on a service object, check return, set UI state. Thin controllers are easier to review and debug. (3) For Java-layer testing: mock the `OAApplicationModule` in JUnit tests using Mockito — test the service layer independently of OAF. (4) Maintain a test data set in the DEV instance with known-good POs, suppliers, and user accounts. (5) Write a test script for each CEMLI — numbered steps, expected result, actual result columns. Treat the test script as a living document updated with each defect fix.

**512. How would you design a procurement manager dashboard within iSupplier/EBS?**
Options: (1) **BIP Report** — SQL-based dashboard with charts (pie chart of PO status, bar chart of on-time delivery by supplier) embedded in a BIP layout. Schedule daily and email to managers. (2) **OAF custom page** — embed dashboard VO results in a table/graph region on a custom OAF page accessible via a menu function. Use `OABarGraphBean` for charts. (3) **Oracle OTBI/OBIEE** — if licensed, create a subject area connecting `PO_HEADERS_ALL`, `RCV_TRANSACTIONS`, `AP_INVOICES_ALL` in the semantic layer. Self-serve analytics for managers. Best choice depends on licensing and user sophistication. For GE, we delivered a BIP report with drill-down links to iSupplier pages — low cost, high value.

**513. What are the key considerations when designing a CEMLI rollback strategy?**
(1) **Database objects** (`XXGE_*` tables, packages, views): keep `DROP TABLE` and `DROP PACKAGE` scripts version-controlled in Git. Never drop a table that has data — truncate and rename instead for rollback safety. (2) **OAF personalizations** — before deploying, export current JDR to a file: `FNDLOAD ... DOWNLOAD JDR_*`. Rollback = re-import old file. (3) **OAF JAR files** — keep the previous JAR in the deployment folder. Rollback = copy old JAR, restart OC4J. (4) **Profile options, Lookups, Messages** — export via FNDLOAD before any change. (5) **Concurrent program registration** — FNDLOAD export. (6) **Workflow** — export WF definition XML before changes. (7) **Test rollback** in UAT once before PROD deployment — many teams skip this and discover it doesn't work during a PROD emergency.

**514. How do you communicate a technical blocker to a non-technical project manager?**
Use the "impact–cause–fix–timeline" format: "The ASN creation feature is blocked because a database index that we rely on doesn't exist in the PROD environment (cause) — this means suppliers will get an error when trying to submit shipments (impact). The fix is a 10-minute database script; I've tested it in UAT and it's ready to deploy. I need a 15-minute CTASK approved by the DBA team (fix). I can have this resolved by 3 PM today if the approval comes through by noon (timeline)." Avoid jargon. Give a specific time commitment and a specific ask. Follow up in writing. Escalate if the approval path is unclear — don't let a technical fix wait on a process gap.

**515. What is your approach to effort estimation for OAF development tasks?**
Break down by component: (1) **VO change** (add column, change WHERE clause): 0.5–1 day including test. (2) **CO extension** (add field, validation): 1–2 days. (3) **AM extension** (new method, API call): 1–3 days. (4) **New OAF page** (from scratch): 5–10 days. (5) **OAF substitution** (replace a class): 3–5 days plus 2 days regression test. Add 30% buffer for EBS patching surprises, environment issues, and code review revisions. For estimation, use planning poker with the team on stories >3 days — a second opinion catches hidden complexity. Always separate dev estimate from test estimate — testers add 50% of dev time for complex features. Document assumptions (e.g., "assumes no multi-org complexity") so scope creep is visible.

**516. How would you handle technical debt in an EBS customization that was built under time pressure?**
First, document the debt: add a JIRA "Tech Debt" label with a description of the issue (e.g., "direct SQL instead of API", "no error handling", "hard-coded org_id"). Prioritize: (1) Security debt (SQL injection risk, hard-coded credentials): fix immediately. (2) Reliability debt (missing exception handlers that could cause data corruption): fix in next sprint. (3) Performance debt (row-by-row processing): fix when performance complaint is raised. (4) Maintainability debt (undocumented packages): fix during slow periods. Present tech debt backlog to project manager quarterly — frame it as risk reduction, not perfectionism. When you touch a module for a new feature, clean up the debt in that module (boy scout rule) — don't leave it worse.

**517. Design a hypercare support process for the 30 days after go-live.**
(1) **War room:** daily 30-minute standup with dev, functional, and DBA for the first 2 weeks. (2) **SLA tiers:** P1 (system down, core workflow broken) — 2-hour response, 4-hour fix. P2 (significant impact, workaround available) — 4-hour response, 1-day fix. P3 (minor issue, cosmetic) — next business day. (3) **Issue tracker:** JIRA board visible to all stakeholders. (4) **Supplier hotline:** dedicated email alias (`isupplier-support@ge.com`) monitored hourly during business hours. (5) **Daily metrics:** track logins, ASN submissions, errors from application logs — alert if error rate spikes >5%. (6) **Escalation path:** P1 → dev lead → IT manager → executive sponsor within 1 hour. (7) **Handover:** after 30 days, transition to regular support; document top 10 recurring issues in the support runbook.

**518. A new requirement asks for a BPA restriction feature — suppliers should not be able to edit unit price on BPA-sourced POs. How do you design this?**
(1) **Detection:** In the OAF acknowledgement/edit page controller, check if the PO line has `FROM_HEADER_ID IS NOT NULL AND FROM_TYPE_LOOKUP_CODE = 'BLANKET'` (BPA-sourced). (2) **Restriction:** Set the Unit Price field's `ReadOnly` attribute to true via SPEL or controller code: `unitPriceItem.setReadOnly(true)`. (3) **Server-side validation:** Add a server-side check in the AM's save method — if `FROM_HEADER_ID IS NOT NULL` and `UNIT_PRICE` changed from original, throw `OAException` with FND message `XXGE_BPA_PRICE_READONLY`. (4) **Bypass for authorized users:** If a procurement manager needs to override (e.g., negotiated discount), add a `XXGE_BPA_PRICE_OVERRIDE` function security — users with this function can edit price. Check `FND_FUNCTION.TEST('XXGE_BPA_PRICE_OVERRIDE')` in the controller.

**519. How would you design a comprehensive test plan for the iSupplier implementation?**
Test plan structure: (1) **Scope** — list of CEMLIs and standard functions in scope. (2) **Test types** — Unit (dev), System Integration (SIT), UAT, Performance, Security, Regression. (3) **Test cases** — for each scope item: test case ID, description, preconditions, steps, expected result, actual result, pass/fail. (4) **Test data** — suppliers, POs, receiving transactions pre-created in UAT. (5) **Entry/exit criteria** — SIT starts when dev completes unit test sign-off; UAT starts when SIT pass rate >95%. (6) **Defect management** — JIRA board; P1/P2 must be resolved before UAT exit. (7) **Performance test scenarios** — 200 concurrent ASN submissions; response time <3 seconds. (8) **Security test** — verify supplier A cannot see supplier B's POs; verify XSS is not possible in free-text fields. (9) **Sign-off matrix** — functional lead, IT manager, security officer.

**520. What is your experience with OIC (Oracle Integration Cloud) and how does it compare to ISG for EBS integrations?**
**ISG (Integrated SOA Gateway):** built into EBS R12; exposes EBS PL/SQL APIs as SOAP/REST services through `isg_deploy.pl`; runs on Oracle WebLogic; good for EBS-to-EBS or legacy systems already on-prem; no additional licensing; limited monitoring UI. **OIC:** cloud-based iPaaS; drag-and-drop integration flows; built-in adapters for EBS (SOAP), Fusion, Salesforce, REST, File; rich monitoring dashboard; supports orchestration, transformations, error handling, retries; requires Oracle Cloud subscription. **When to use OIC:** new integrations where one side is cloud (Fusion, SaaS); when complex transformation/orchestration is needed; when business wants self-service integration monitoring. **When to use ISG:** simple, low-volume EBS-only integrations; air-gapped environments that can't connect to cloud. In GE's hybrid environment, we used ISG for EBS-to-EBS (Spring Boot calling EBS APIs) and planned OIC for future Fusion integration.

**521. How do you manage a multi-team development effort where 3 developers are modifying related OAF pages simultaneously?**
(1) **Branching strategy:** each developer works on a feature branch (`feature/XXGE-OAF-101-asn-eligibility`). Daily merge from `develop` branch to stay current. (2) **OAF JAR conflict:** OAF Java code is compiled to JAR — two developers modifying the same page create a merge conflict on the JAR binary. Solution: never commit JARs to Git. Commit only Java source (`.java`) and XML metadata (`.xml`). JARs built by CI pipeline from source. (3) **JDR personalization conflicts:** export JDR as XML to Git; two developers changing the same personalization is a conflict in XML — use `diff3` merge strategy in Git. (4) **Test isolation:** each developer has a personal DEV instance login with unique test data (different PO numbers) to avoid stepping on each other. (5) **Daily standup:** flag dependencies — if developer A's VO change affects developer B's CO, coordinate merge order.

**522. Describe how you conducted knowledge transfer to the support team after project go-live.**
Delivered a 3-day KT program: Day 1 — architecture overview (EBS setup, CEMLI register walkthrough, key tables); Day 2 — hands-on: support team troubleshoots pre-created scenarios (stuck CP, missing ASN, WF notification not sent) in a sandbox with guidance; Day 3 — tools and logs (OC4J log locations, SQL queries for diagnosis, ServiceNow CTASK process). Deliverables: (1) Support runbook (30 pages): top 20 issues with diagnostic steps and resolution. (2) CEMLI register with developer contacts. (3) Architecture diagram. (4) Recorded Zoom sessions. (5) Escalation matrix. Measured success: after KT, support team resolved 70% of P2/P3 tickets independently within 1 week (tracked in ServiceNow).

**523. What metrics would you use to track iSupplier portal health post-go-live?**
(1) **Availability:** uptime % (target 99.5%); measured via synthetic monitor that logs in and navigates to PO search. (2) **Performance:** average page load time for PO search and ASN creation (target <3s); measured via OAF diagnostics or synthetic monitor. (3) **Error rate:** `FND_LOG_MESSAGES` error count per hour; alert if >10 errors/hour. (4) **ASN submission success rate:** `RCV_SHIPMENT_HEADERS` created / attempted (ideally >99%). (5) **Support tickets:** P1/P2 tickets per week (target: 0 P1s after 30 days). (6) **Active users:** weekly unique logins to `ICX_SESSIONS`. (7) **Session timeout rate:** unexpectedly terminated sessions (`ICX_SESSIONS.DISCONNECTED_REASON = 'TIMEOUT'`) — indicates session timeout too short. Review metrics in weekly ops meeting.

**524. Explain how you would design a change request routing workflow for PO changes by suppliers.**
Flow: (1) Supplier submits change request in iSupplier (quantity, delivery date, unit price) — stored in `PO_CHANGE_REQUESTS` with `REQUEST_STATUS = 'PENDING'`. (2) OAF triggers `XXGE_PO_CHANGE_WF` item. (3) WF routes based on change type: price change → buyer + manager approval; date change → buyer approval only; quantity reduction → auto-approve if <10%. (4) WF notification sent to buyer's Worklist with Accept/Reject/Modify responses and change details in notification body. (5) On Accept: call `PO_CHANGE_API_PVT.ACCEPT_CHANGE_REQUEST` to update PO. On Reject: update `PO_CHANGE_REQUESTS.REQUEST_STATUS = 'REJECTED'`, notify supplier. (6) Escalation: if buyer doesn't respond in 48 hours, escalate to supervisor. (7) Audit: all actions logged in `PO_ACTION_HISTORY`.

**525. How do you handle a situation where a CEMLI breaks in production after a patch, affecting live users?**
Incident response: (1) **Immediate (0–15 min):** assess impact — how many users affected, is core functionality broken? If so, declare P1. (2) **Short-term fix (15–60 min):** can the CEMLI be temporarily disabled? If it's an OAF personalization, disable it via OAF Personalization Manager without a code deploy. If it's a package, check if you can swap in the pre-patch version from backup. (3) **Root cause (1–4 hours):** compare pre/post patch OAF class or standard package — what changed? Common cause: a method signature changed in the patched version that our substitution overrides. Fix: update our Java class to call the new method signature. Recompile JAR, test in UAT (or emergency copy of PROD), deploy via CTASK. (4) **Post-incident:** write a 1-page incident report — timeline, root cause, fix, prevention (add this CEMlI to patch pre-check list).

**526. What would you include in an implementation handover document for a new support team?**
Sections: (1) **System Overview** — EBS instance URL, Oracle version, module list, APPL_TOP path, key server names. (2) **Custom Objects List** — all `XXGE_*` packages, tables, OAF JARs, BIP report names, WF items, FNDLOAD scripts. (3) **Key Business Flows** — step-by-step for PO approval, ASN creation, invoice processing — with screenshots. (4) **Common Issues & Resolutions** — top 15 support scenarios with diagnostic SQL and fix steps. (5) **Environment Access** — how to log in to DEV/UAT/PROD, SSH access to app servers, SQL Developer connection details. (6) **Contacts** — Oracle Support SR process, DBA contact, network team for firewall issues. (7) **Change Management** — how to raise a CTASK, approval workflow, deployment checklist. (8) **Monitoring** — what to check daily: CP queue, OC4J logs, `FND_LOG_MESSAGES` errors.

**527. How would you design a supplier scorecard feature in iSupplier?**
Supplier scorecard tracks: on-time delivery %, quality (returns/rejects), ASN accuracy, invoice accuracy. Design: (1) **Data source** — BIP data template joining `RCV_TRANSACTIONS` (receipt dates vs `NEED_BY_DATE`), `RCV_RETURNS` (return count), `AP_INVOICES_ALL` (invoice accuracy). Calculate monthly by `VENDOR_ID`. (2) **Score storage** — `XXGE_SUPPLIER_SCORECARD` table: `VENDOR_ID, PERIOD, OTD_PCT, QUALITY_SCORE, ASN_ACCURACY, OVERALL_SCORE`. (3) **Concurrent program** `XXGE_SCORECARD_CP` runs monthly, populates the table. (4) **iSupplier display** — custom OAF region on supplier home page showing current and 3-month trend (simple table; no charting needed). (5) **Email notification** — if supplier's overall score drops below threshold, WF notification to supplier and GE procurement manager. (6) **PDF export** — BIP report for formal scorecard PDF, sent monthly.

**528. What is your experience resolving conflicts between functional requirements and technical constraints?**
Example: functionals wanted real-time supplier inventory visibility in iSupplier (pull data from supplier's ERP via REST every page load). Technically: supplier systems had rate limits, unreliable uptime, and variable response formats. My resolution: (1) Proposed a "last-known" model — suppliers push inventory updates via a scheduled REST call every 4 hours to our OIC endpoint, which stores in `XXGE_SUPPLIER_INVENTORY`. (2) iSupplier reads from this table (fast, no external call). (3) Display shows "as of [timestamp]" so procurement knows data age. (4) Manual refresh button for on-demand pull. The functional lead accepted this after I showed that real-time pull would add 2–5 seconds to every page load and could take the page down if the supplier API was unavailable. Documented the trade-off in the TDD.

**529. How do you manage risk in an EBS project with tight deadlines?**
(1) **Risk register** — maintain in JIRA or Excel: risk description, probability (H/M/L), impact (H/M/L), mitigation, owner. Review weekly. (2) **Early identification** — flag risks in design phase, not during UAT. "This WF customization requires OC4J restart for deployment — risk: impacts all users" → mitigate by scheduling deploys after hours. (3) **Buffer** — protect 20% of sprint capacity for unplanned work (environment issues, patch surprises). (4) **Prototyping** — for high-risk CEMLIs, build a proof-of-concept in week 1 rather than week 8. Catch technical blockers early. (5) **Dependency tracking** — if dev depends on DBA completing a table grant, track that dependency in JIRA. Unblocked dependencies are the most common cause of delay. (6) **Honest reporting** — if a task is at risk, raise it immediately. "We're on track" when you're not is the most damaging thing a developer can do.

**530. How would you handle a post-migration login failure where supplier users cannot authenticate after the EBS upgrade?**
Likely causes: (1) **ICX session configuration changed** — check `ICX: Session Timeout` profile, `ICX: Limit Time` profile. (2) **FND user password encryption changed** — EBS upgrades sometimes change password hash algorithm; force password reset via `FNDCPASS`. (3) **SSL certificate expired** — check the OHS/Apache SSL certificate. (4) **SSO configuration broken** — if using Oracle SSO (OSSSO) or LDAP, check `FND_LDAP_USER` table and `LDAP_SYNCH_*` profile options. Test with a direct EBS login (bypass SSO) to isolate. (5) **Responsibility assignment lost** — check `FND_USER_RESP_GROUPS` for affected users. (6) **MOS SR history** — search My Oracle Support for known issues with the specific patch level and login failures. Resolve by restoring from the pre-upgrade backup of `FND_USER` / `FND_RESPONSIBILITY` configuration, or applying a one-off patch from Oracle Support.


# Section Y — Oracle Inventory & Receiving (Q531–Q560)

**531. How does Oracle Inventory (INV) relate to the Procure-to-Pay process?**
The P2P cycle ends in INV: after a PO is approved and a supplier ships goods, the receiving process (PO Receipt) creates an entry in `RCV_TRANSACTIONS` and simultaneously updates `MTL_ONHAND_QUANTITIES` in Inventory. Specifically: `RCV_TRANSACTIONS.TRANSACTION_TYPE = 'RECEIVE'` records the receipt; if routing is Direct Delivery, `TRANSACTION_TYPE = 'DELIVER'` also triggers an `MTL_TRANSACTIONS` record updating on-hand. If routing is Standard Receipt (two-step), the Deliver step moves goods from receiving dock to subinventory. The financial side: receipt creates a `RCV_RECEIVING_SUB_LEDGER` entry debit `Receiving Inspection / Inventory`; PO match in AP creates the credit to `AP_INVOICES_ALL`. INV is where the physical on-hand balance is maintained.

**532. What is the difference between a Receipt and a Delivery in Oracle Receiving?**
**Receipt:** recorded at the dock — goods arrive from the supplier; creates `RCV_SHIPMENT_HEADERS` and `RCV_TRANSACTIONS` with `TRANSACTION_TYPE = 'RECEIVE'`. At this point, goods are in the "receiving dock" location, not yet in inventory. **Delivery:** moves goods from receiving dock to a subinventory/locator within inventory; creates `RCV_TRANSACTIONS` with `TRANSACTION_TYPE = 'DELIVER'` and triggers an `MTL_MATERIAL_TRANSACTIONS` record updating `MTL_ONHAND_QUANTITIES`. For routing = Direct Delivery, both happen simultaneously in one step. For routing = Inspection Required: receipt → inspect (`ACCEPT`/`REJECT`) → deliver. Understanding this distinction is critical for debugging "goods received but not in inventory" issues.

**533. What is RVCTP and what does it process?**
RVCTP (Receiving Transaction Processor) is the concurrent program `RVCTP` that processes records from `RCV_TRANSACTIONS_INTERFACE` into `RCV_TRANSACTIONS`. It also handles the inventory delivery step (updating `MTL_ONHAND_QUANTITIES`). In a normal flow: iSupplier ASN submit → records inserted into `RCV_HEADERS_INTERFACE` and `RCV_TRANSACTIONS_INTERFACE` → RVCTP runs → records moved to `RCV_SHIPMENT_HEADERS` and `RCV_TRANSACTIONS`. If RVCTP is stuck or not running, ASN submissions appear "pending" forever with no error to the supplier. Diagnose by checking `FND_CONCURRENT_REQUESTS` for RVCTP status, and `RCV_TRANSACTIONS_INTERFACE.PROCESSING_STATUS_CODE` (should be `PENDING` waiting for RVCTP, `ERROR` if failed, `SUCCESS` if processed).

**534. What are the standard receiving routing options in Oracle EBS and when would you use each?**
Three routing options in `RCV_ROUTING_RULES`: (1) **Standard Receipt** — goods go to receiving dock first, then manually delivered to subinventory. Use for: high-value items needing physical inspection before stocking. (2) **Inspection Required** — receipt → inspection (Accept/Reject) → deliver. Use for: items with quality requirements, aerospace components requiring incoming inspection. GE used this for critical manufacturing parts. (3) **Direct Delivery** — receipt and delivery in one step; goods immediately posted to inventory. Use for: low-value consumables, MRO items where dock-to-inventory speed matters. Controlled at item/supplier site/receiving options level. Override via `RCV_PARAMETERS.RECEIVING_ROUTING_ID`.

**535. What is the difference between Subinventory and Locator in Oracle Inventory?**
**Subinventory:** a logical subdivision of an inventory organization (warehouse) — e.g., "FG-STORE" (Finished Goods), "RM-STORE" (Raw Materials), "QUARANTINE". Each subinventory has its own GL account codes. Items are stocked and tracked at subinventory level. **Locator:** a physical location within a subinventory — e.g., Row A, Bin 3, Shelf 2. Locators are optional and controlled by `MTL_PARAMETERS.STOCK_LOCATOR_CONTROL_CODE`. When locator control is enabled, every transaction (receipt, transfer, issue) requires specifying the exact locator. For aerospace parts at GE, locator control was enabled in the critical parts subinventory for lot traceability. Query locators: `MTL_ITEM_LOCATIONS` table.

**536. Explain Standard Delivery vs Direct Delivery for a purchase order receipt.**
Same as routing options: **Standard Receipt / Standard Delivery** is a two-step process — you first receive (creates RCV entry at dock) then separately deliver to a subinventory (creates INV transaction). **Direct Delivery** collapses both into one step at receive time — the system prompts for the destination subinventory/locator and immediately transfers on-hand. The choice impacts accounting timing: with standard, `Receiving Inspection` account is debited at receipt and cleared at delivery; with direct, inventory account is debited immediately at receipt. For financial close accuracy, many organizations prefer direct delivery for simple items to avoid timing differences between receipt and delivery.

**537. What is the Inspection Routing and how is it processed in Oracle?**
When a PO line has `INSPECTION_REQUIRED_FLAG = 'Y'` (set on item or receiving options), the receipt creates an inspection record. The quality inspector must then run `Receiving > Receiving Transactions > Inspect` to record Accept or Reject with a quantity. Accepted quantity proceeds to delivery; rejected quantity goes to `REJECT` disposition (vendor return, scrap, or rework). In Oracle tables: `RCV_TRANSACTIONS` has a record with `TRANSACTION_TYPE = 'ACCEPT'` or `'REJECT'`. The inspection step creates `QA_RESULTS` records if Oracle Quality (QA) module is integrated. For GE aerospace, incoming inspection for critical fasteners was mandatory — integrated with QA collection plans requiring dimensional measurements before acceptance.

**538. What are MTL_SUPPLY and MTL_DEMAND and how are they used?**
`MTL_SUPPLY` tracks expected future supply: open PO shipments, in-transit shipments, WIP completions, internal requisitions. Each row represents a supply source with expected receipt date and quantity. Used by MRP/ASCP for planning calculations. `MTL_DEMAND` tracks demand: sales orders, WIP requirements, internal orders. The net requirement is supply - demand. In the context of iSupplier/receiving: when a PO is approved, `MTL_SUPPLY` gets a row with `SUPPLY_TYPE_CODE = 'PO'`. When the receipt is processed by RVCTP, the supply row is reduced (or deleted if fully received). If you see a PO still showing in supply after full receipt, it means RVCTP didn't complete successfully or `QUANTITY_RECEIVED` wasn't updated properly.

**539. How do you perform a receipt correction in Oracle EBS?**
Use `Receiving > Receiving Transactions > Receiving Corrections`. Select the original receipt transaction, enter the corrected quantity (can be negative to reduce received quantity). This creates a new `RCV_TRANSACTIONS` row with `TRANSACTION_TYPE = 'CORRECT'` and the correction quantity. The correction reverses the inventory and accounting impact of the original receipt proportionally. Important: corrections have limits — you cannot correct below zero or above the original shipment quantity. For a full reversal (return to vendor), use the `RETURN TO VENDOR` transaction type instead. In iSupplier, suppliers cannot perform corrections — only internal receiving staff. A supplier who submitted a wrong ASN quantity must ask the GE receiving team to perform the correction.

**540. How do you perform a Subinventory Transfer in Oracle Inventory?**
`Inventory > Transactions > Subinventory Transfer` — enter item, from-subinventory (and locator if controlled), to-subinventory (and locator), quantity. This creates an `MTL_MATERIAL_TRANSACTIONS` record with `TRANSACTION_TYPE_ID` corresponding to "Subinventory Transfer" (typically type 2). The accounting impact: debit the receiving subinventory's valuation account, credit the sending subinventory's account. No external cost impact. In tables: `MTL_ONHAND_QUANTITIES` is updated — source subinventory quantity decreases, destination increases. Common use case: moving items from QUARANTINE subinventory to RM-STORE after quality release.

**541. What INV transaction types are commonly used in Oracle EBS?**
Key `MTL_TRANSACTION_TYPES`: (1) `RECEIVE` (type 18) — receipt from PO. (2) `DELIVER` (type 17) — delivery from receiving to subinventory. (3) `RETURN TO RECEIVING` (type 15) — return from subinventory to receiving dock. (4) `RETURN TO VENDOR` (type 10) — return from receiving to vendor. (5) `SUBINVENTORY TRANSFER` (type 2) — move between subinventories. (6) `ISSUE` (type 1) — issue to WIP or cost center. (7) `MISC RECEIPT` (type 42) — ad-hoc receipt not from PO. (8) `CYCLE COUNT ADJUSTMENT` (type 4) — inventory adjustment from cycle count. (9) `PHYSICAL INVENTORY ADJUSTMENT` (type 8) — adjustment from physical inventory count. Each type has a defined accounting template in `MTL_TRANSACTION_ACCOUNTS`.

**542. What is over-receipt tolerance and how is it enforced in Oracle EBS?**
Over-receipt tolerance defines how much more than the PO quantity a receiver can accept. Controlled by: `PO_LINE_LOCATIONS_ALL.OVER_RECEIPT_TOLERANCE` (quantity %) and `OVER_RECEIPT_ACTION` (`NONE` = allow, `WARNING` = warn but allow, `REJECT` = block). Set at PO shipment level, defaulted from receiving options. For example: tolerance = 10%, PO qty = 100, max receivable = 110. If supplier ships 115 and `OVER_RECEIPT_ACTION = 'REJECT'`, the receipt transaction is blocked with an error message. For aerospace procurement where exact quantities matter (lot traceability), GE used `REJECT` with 0% tolerance for critical parts. Tolerance is also checked in the `RVCTP` program — errors appear in `PO_INTERFACE_ERRORS` if processing via interface.

**543. Explain the columns QUANTITY_RECEIVED, QUANTITY_DELIVERED, and QUANTITY_BILLED on PO_LINE_LOCATIONS_ALL.**
- `QUANTITY_RECEIVED`: total quantity received at the dock (sum of `RCV_TRANSACTIONS` with `TRANSACTION_TYPE = 'RECEIVE'` for this shipment). Updated by RVCTP. - `QUANTITY_DELIVERED`: total quantity delivered from dock to inventory (sum of `DELIVER` transactions). For direct delivery, equals `QUANTITY_RECEIVED`. - `QUANTITY_BILLED`: total quantity matched on approved AP invoices (`AP_INVOICE_LINES_ALL` matched to this PO shipment). Used for three-way match. The relationship: `QUANTITY_ORDERED >= QUANTITY_RECEIVED >= QUANTITY_DELIVERED`. `QUANTITY_BILLED <= QUANTITY_DELIVERED` for 3-way match. If `QUANTITY_BILLED > QUANTITY_DELIVERED`, an AP match exception is raised. These columns are critical for the P2P reconciliation report.

**544. How does LOT and Serial number control work in Oracle Inventory for aerospace components?**
**Lot control** (`MTL_LOT_NUMBERS`): a batch of items sharing the same production run/supplier lot. For aerospace fasteners, every receipt must specify the supplier lot number — stored in `MTL_TRANSACTION_LOT_NUMBERS`. Lot genealogy tracks which lots were used in which assemblies. **Serial control** (`MTL_SERIAL_NUMBERS`): each unit has a unique serial number. Used for engines, landing gear assemblies. Receiving requires entering each serial number individually. **Lot + Serial:** some items (rotable parts) use both. In Oracle: `MTL_SYSTEM_ITEMS_B.LOT_CONTROL_CODE` and `SERIAL_NUMBER_CONTROL_CODE` control this. Receiving transaction for a lot-controlled item: `MTL_TRANSACTION_LOT_NUMBERS` is populated alongside `MTL_MATERIAL_TRANSACTIONS`. Traceability query: from `MTL_TRANSACTION_LOT_NUMBERS` trace `LOT_NUMBER` back to `RCV_SHIPMENT_LINES.SHIPMENT_LINE_ID` to find originating PO.

**545. How do you diagnose a stuck Receiving Transaction Interface record?**
Step 1: Query `RCV_TRANSACTIONS_INTERFACE WHERE PROCESSING_STATUS_CODE = 'ERROR'` — note `INTERFACE_TRANSACTION_ID`. Step 2: Join to `PO_INTERFACE_ERRORS ON INTERFACE_LINE_ID = INTERFACE_TRANSACTION_ID` — read `ERROR_MESSAGE`. Common errors: `PO_PDOI_VALUE_TOO_LONG` (a text value too long), `RCV_INVALID_ORGANIZATION` (ship-to org not set up), `RCV_SHIPMENT_NUM_FROZEN` (shipment already closed). Step 3: Fix the root cause — correct the data in the interface table directly (update the column with the invalid value) or fix the master data (add the organization). Step 4: Reset `PROCESSING_STATUS_CODE = 'PENDING'` and `PROCESSING_MODE_CODE = 'BATCH'` in `RCV_TRANSACTIONS_INTERFACE`. Step 5: Run `RVCTP` to reprocess. Step 6: Verify `RCV_SHIPMENT_HEADERS` and `RCV_TRANSACTIONS` are created.

**546. What is Kanban replenishment and how does it work in Oracle Inventory?**
Kanban is a pull-based replenishment system: when a Kanban card's on-hand falls to the replenishment point, a replenishment signal is automatically generated. In Oracle INV: (1) Define Kanban cards (`MTL_KANBAN_CARDS`) with `SUPPLY_STATUS = 'WAIT'` initially. (2) When a card's bin is emptied, the signal changes to `SUPPLY_STATUS = 'EMPTY'`. (3) Oracle generates a replenishment request — for supplier Kanban, this creates an `RCV_SUPPLY` record or triggers a blanket release. (4) Supplier ships, receipt is processed, card status returns to `FULL`. Used in GE's manufacturing sites for low-value, high-frequency MRO items (fasteners, consumables) — reduced purchase order processing overhead significantly.

**547. What is consigned inventory and how is it managed in Oracle EBS?**
Consigned inventory: supplier owns the goods physically stored at the customer's location; ownership transfers only upon consumption. In Oracle INV/iSupplier: (1) Supplier ships consigned stock — a "consigned receipt" in `RCV_TRANSACTIONS` with `CONSIGNED_FLAG = 'Y'`. On-hand is tracked in `MTL_ONHAND_QUANTITIES` but in a consigned subinventory. (2) When the manufacturer consumes the item (issues to WIP), Oracle generates a consumption advice. (3) The consumption advice triggers an invoice from the supplier. (4) Reporting: `PO_APOOL_DETAILS` and `PO_CONSIGNED_CONSUMPTION` views. Benefits: reduced inventory carrying costs, improved cash flow. For GE, consignment was used for fastener programs where suppliers managed replenishment levels on-site.

**548. What is Oracle WMS (Warehouse Management System) and how does it extend INV?**
Oracle WMS adds directed putaway, task dispatching, pick wave management, and RF/barcode integration to base INV. Extensions: (1) **Directed putaway** — system suggests optimal locator for receipts based on item characteristics, subinventory capacity rules. (2) **Task interleaving** — combines pick and putaway tasks for warehouse workers to minimize travel. (3) **Label printing** — automatic GS1 label generation on receipt. (4) **Mobile transactions** — RF device integration for real-time transaction recording. (5) **Lot genealogy** — enhanced tracking for aerospace. In EBS, WMS is a licensed module; its tables are in the INV schema. For GE's distribution centers, WMS directed putaway reduced mis-stocking by 30% for lot-controlled items.

**549. What are RCV_ACCOUNTING_EVENTS and when are they created?**
`RCV_ACCOUNTING_EVENTS` captures the trigger events for receiving accounting (Subledger Accounting). Created when: (1) PO receipt is processed (`RECEIVE` transaction) — creates events for Accrual and Receiving Inspection accounts. (2) Delivery to inventory — creates Inventory Valuation debit. (3) Return to Vendor — reversal entries. (4) Price correction — if PO price is corrected after receipt, accounting event created to adjust the difference. The actual journal entries are in `XLA_AE_HEADERS` and `XLA_AE_LINES` (Subledger Accounting). The link: `RCV_ACCOUNTING_EVENTS.ACCOUNTING_EVENT_ID` → `XLA_EVENTS.EVENT_ID` → `XLA_AE_HEADERS.AE_HEADER_ID`. Use this chain to debug "receipt not showing in GL" issues.

**550. Describe a complex receiving scenario from your GE Aerospace experience.**
A critical fastener batch (Lot GE-2024-001) was received against a PO with inspection-required routing. The receipt went into QUARANTINE subinventory. Quality ran dimensional checks, found 5% out-of-spec, and rejected 50 units out of 1000. The 50 units were returned to vendor (`RCV_TRANSACTIONS.TRANSACTION_TYPE = 'RETURN TO VENDOR'`); the 950 were accepted and delivered to RM-STORE subinventory at Locator A-3-12. Two weeks later, a production issue was traced to this lot — we needed to quarantine all remaining units. I wrote a SQL query joining `MTL_TRANSACTION_LOT_NUMBERS → MTL_MATERIAL_TRANSACTIONS → MTL_ONHAND_QUANTITIES` to find every bin containing Lot GE-2024-001, then created a subinventory transfer request to move them back to QUARANTINE. Report went to quality and production management within 2 hours.

**551. What is an Internal Requisition and an Internal Sales Order (ISO) in Oracle?**
An **Internal Requisition** (IR) is a request from one inventory organization to transfer goods to another organization within the same company. It flows: (1) Requesting org raises IR in `PO_REQUISITION_HEADERS_ALL` with `TYPE_LOOKUP_CODE = 'INTERNAL'`. (2) Auto-created into an Internal Sales Order (ISO) in Order Management (`OE_ORDER_HEADERS_ALL`). (3) Shipping org picks, ships, creates an `RCV_SHIPMENT_HEADERS` with `SHIPMENT_TYPE = 'INTERNAL'`. (4) Requesting org receives via standard receiving process. Distinguishing column: `RCV_SHIPMENT_HEADERS.SHIPMENT_TYPE` = 'STANDARD' for supplier receipts, 'INTERNAL' for inter-org transfers. Used at GE for transferring excess fastener stock from one manufacturing site to another without a new external PO.

**552. What are the functional steps for a Return to Vendor (RTV) transaction?**
(1) Navigate to `Receiving > Returns > Return to Supplier`. (2) Find the original receipt via PO number or receipt number. (3) Enter return quantity and reason code (e.g., 'DEFECTIVE', 'WRONG_ITEM'). (4) Select return routing: RMA if supplier requires a Return Merchandise Authorization, or standard return. (5) System creates `RCV_TRANSACTIONS` with `TRANSACTION_TYPE = 'RETURN TO VENDOR'`. (6) If goods are in inventory (delivered), a reverse `MTL_MATERIAL_TRANSACTIONS` reduces on-hand. (7) AP debit memo is created (or AP team manually handles the credit). (8) A `PO_ACCEPTANCES` record or `PO_ACTION_HISTORY` entry records the return reason. Impact on PO: `QUANTITY_RECEIVED` on `PO_LINE_LOCATIONS_ALL` is reduced by the return quantity.

**553. What happens to the accounting period in MTL_PARAMETERS during inventory close?**
`MTL_PARAMETERS.PERIOD_CLOSE_STATUS` and the `ORG_ACCT_PERIODS` table track the current and past periods. During month-end: (1) Run `Inventory > Accounting Close Cycle > Inventory Accounting Periods` — verify all pending transactions are processed (no uncosted transactions in `MTL_MATERIAL_TRANSACTIONS` with `COSTED_FLAG = 'N'`). (2) Transfer to GL (`MTL_PENDING_OSP_TRANSACTIONS` cleared). (3) Close period — sets `ORG_ACCT_PERIODS.PERIOD_CLOSE_DATE`. After close, new transactions are booked in the next open period. If a transaction is entered in a closed period, Oracle either rejects it or books it in the next open period depending on the `INV: Allow Posting in Prior Period` profile option.

**554. How does the costing method impact the receiving accounting in Oracle Inventory?**
Oracle INV supports: Standard Cost, Average Cost, FIFO, LIFO (last three in 11i/R12 with Average costing). (1) **Standard Cost**: receipts are booked at the PO's standard cost; any variance between PO price and standard goes to a `PURCHASE PRICE VARIANCE` account. Common in manufacturing. (2) **Average Cost**: receipt cost = PO unit price; running average is recalculated: `(existing qty × avg cost + receipt qty × PO price) / (existing qty + receipt qty)`. No PPV. (3) **FIFO**: cost layers maintained in `CST_INV_LAYERS` — oldest cost layers are consumed first on issues. For aerospace traceability (lot-specific costs), FIFO with lot costing provides true cost per lot. The costing method affects `RCV_RECEIVING_SUB_LEDGER` and ultimately the GL entries generated by RVCTP.

**555. What are blanket release tolerances and how do they affect receiving?**
A Blanket Purchase Agreement (BPA) has a total committed amount. Each release against the BPA consumes that commitment. Tolerances: (1) **Amount tolerance** — a release can exceed its scheduled amount by X% before a hold is placed. (2) **Quantity tolerance** — similar for quantity-based BPAs. Set at `PO_HEADERS_ALL` (BPA header) or `PO_LINE_LOCATIONS_ALL` (release shipment). At receiving: if `QUANTITY_RECEIVED > QUANTITY_ORDERED + tolerance`, `CLOSED_CODE` may be set to prevent further receipts. For GE's blanket fastener programs, we allowed 5% quantity tolerance to accommodate shipping variances. Relevant columns: `PO_LINE_LOCATIONS_ALL.OVER_RECEIPT_TOLERANCE`, `PO_HEADERS_ALL.BLANKET_TOTAL_AMOUNT`, `AMOUNT_LIMIT`.

**556. Write a SQL query to find current on-hand quantities for a specific item across all organizations.**
```sql
SELECT moq.organization_id,
       ood.organization_name,
       moq.subinventory_code,
       msib.segment1 item_number,
       msib.description,
       SUM(moq.transaction_quantity) on_hand_qty,
       msib.primary_unit_of_measure uom
FROM   mtl_onhand_quantities moq
JOIN   mtl_system_items_b msib
       ON msib.inventory_item_id = moq.inventory_item_id
       AND msib.organization_id  = moq.organization_id
JOIN   org_organization_definitions ood
       ON ood.organization_id = moq.organization_id
WHERE  msib.segment1 = :p_item_number
GROUP  BY moq.organization_id, ood.organization_name,
          moq.subinventory_code, msib.segment1,
          msib.description, msib.primary_unit_of_measure
ORDER  BY ood.organization_name, moq.subinventory_code;
```

**557. What is FIFO dating in Oracle Inventory and how does it relate to lot control?**
FIFO (First In, First Out) dating ensures that the oldest lot/receipt is consumed first during issues or picks. In Oracle WMS, FIFO putaway/picking rules use `MTL_LOT_NUMBERS.EXPIRATION_DATE` or `CREATION_DATE` to sequence lot consumption. In standard INV without WMS, FIFO isn't automatically enforced — the user must select the lot during issue. With `MTL_PARAMETERS.FIFO_COSTING = 'Y'` (Average Costing with FIFO layers), cost layers in `CST_INV_LAYERS` are consumed in creation order. For aerospace shelf-life-controlled items (e.g., adhesives, lubricants with expiry dates), FIFO is mandatory. WMS FIFO rule: `CST_INV_LAYER_COST_DETAILS` stores per-layer costs; `MTL_LOT_NUMBERS.EXPIRATION_DATE` drives picking sequence.

**558. How do you reconcile PO receipts with inventory on-hand quantities when there is a discrepancy?**
Discrepancy scenario: PO shows 1000 units received but inventory on-hand shows 950. Steps: (1) Confirm `PO_LINE_LOCATIONS_ALL.QUANTITY_RECEIVED = 1000`. (2) Check `RCV_TRANSACTIONS` — are all 1000 units in `DELIVER` transactions (not just `RECEIVE`)? Direct delivery should have both. (3) Check `MTL_MATERIAL_TRANSACTIONS` for `TRANSACTION_TYPE_ID = 17` (Deliver) against this receipt — sum should be 1000. (4) If only 950 delivered, check for a correction transaction reversing 50 units. (5) Also check `RCV_TRANSACTIONS.TRANSACTION_TYPE = 'RETURN TO VENDOR'` — were 50 returned? (6) Check `MTL_ONHAND_QUANTITIES` — are there negative adjustments (cycle count, physical inventory adjustment, issues to WIP) explaining the difference? Report findings to the warehouse manager with transaction-level detail.

**559. What INV profile options are critical for a receiving setup?**
Key profile options: (1) `RCV: Processing Mode` — ONLINE (immediate) vs BATCH (via RVCTP). For iSupplier ASN, BATCH is standard. (2) `RCV: Warn if Outside Receipt Days` — warn when receipt is outside the allowed receipt days window. (3) `INV: Lot Expiration Action` — WARN or REJECT when receiving a lot past expiry date. (4) `INV: Interorg Transfer Type` — 1=Direct, 2=Intransit; defines how inter-org transfers work. (5) `TP: INV Transfer to GL` — 'Y' means automatic transfer; 'N' means manual. (6) `INV: Allow Expense to Asset Transfer` — controls whether items in expense subinventories can be transferred to asset subinventories. (7) `PO: Warn/Enforce Receiving Date Range` — allows/blocks receipts outside the PO date window. Set these correctly during implementation to avoid hard-to-diagnose receiving errors.

**560. What is lot genealogy and why is it important for aerospace manufacturing?**
Lot genealogy traces the complete history of a lot: from supplier (origin lot, certificate of conformance) → incoming receipt (EBS lot number, receiving date, receiving transaction) → quality inspection result → subinventory location → WIP issue (which work order, which assembly) → finished goods lot. In Oracle, this is tracked via: `MTL_TRANSACTION_LOT_NUMBERS` (links lot to every transaction), `WIP_REQUIREMENT_OPERATIONS` (WIP component lots), `WIP_COMPLETED_LOTS` (finished goods lots). For aerospace, if a part is found defective in service, lot genealogy answers: which other assemblies used parts from the same supplier lot? This drives the "affected units" list for an airworthiness directive. In GE's implementation, we built a custom BIP report `XXGE_LOT_GENEALOGY_RPT` that traverses the full chain from `RCV_SHIPMENT_LINES` to final assembly, used by quality engineering within minutes of a reported defect.


# Section Z — Tools, DevOps & Agile (Q561–Q600)

**561. How did you apply Agile/Scrum in the GE iSupplier rollout?**
We ran 2-week sprints with a backlog of user stories broken down by CEMLI (each CEMLI as an epic, subtasks for design/dev/unit test/UAT fix). Sprint ceremonies: planning (Monday AM — commit stories for the sprint), daily standups (15 min — what done, what today, blockers), sprint review (Friday — demo to functional leads in UAT), retrospective (30 min — what to improve). Velocity tracked in JIRA — story points based on complexity (1=simple config, 3=CO extension, 8=new OAF page, 13=new workflow). Releases aligned to go-live phases: Phase 1 sprint 1–6 (core PO view + ASN), Phase 2 sprint 7–10 (invoice view + promise date). Agile worked well for iterative delivery; functional leads gave feedback every 2 weeks rather than waiting until UAT.

**562. How did you use JIRA to manage the iSupplier project?**
JIRA structure: one Project (`ISUP`), Epics per CEMLI (`ISUP-E01: OAF ASN Creation`, `ISUP-E02: BIP PO Acknowledgement Report`), Stories for functional requirements, Sub-tasks for dev/test. Labels: `P1`, `P2`, `BLOCKED`, `TECH-DEBT`. Custom fields: CEMLI ID, Dev Owner, Test Script ID, Patch Risk. Workflows: `Open → In Progress → Code Review → UAT → Done` (P1 bugs get an `EMERGENCY` lane bypassing normal flow). JIRA board views: sprint board (developer view), Kanban board (bug triage), Release dashboard (UAT sign-off status). Automation rules: when Sub-task status = Done and all sibling sub-tasks Done → auto-transition parent Story to Review. Reported sprint metrics and defect trends to PM and stakeholders in weekly reports generated from JIRA dashboards.

**563. How do you use Git for managing EBS customization source code?**
Git repo structure: `ebs-customizations/` with directories: `sql/` (DDL scripts, data fix scripts), `plsql/` (package specs/bodies organized by module), `oaf/` (Java source, XML metadata), `bip/` (BIP data template XML, RTF template files), `fndload/` (FNDLOAD `.ldt` export files), `workflow/` (WF `.wft` export files), `scripts/deployment/` (deployment runbook scripts). Each CEMLI in its own sub-directory under the appropriate module. Commit message convention: `[JIRA-ID] Brief description`. Never commit: compiled JARs, binary files, credentials, `APPS_PASSWD` values. `.gitignore` excludes `*.class`, `*.jar`, `*.lox`. PRs required for merges to `develop` and `main` — at least one reviewer.

**564. What is your branching strategy for EBS development?**
Git Flow variant: `main` (PROD-ready code), `develop` (integration branch), `feature/JIRA-ID-description` (individual CEMLI dev), `hotfix/JIRA-ID-description` (emergency PROD fixes). Workflow: developer creates feature branch from `develop`; develops and unit tests locally; raises PR to `develop`; code reviewed by lead; merged to `develop`; weekly `develop` → `release/sprint-N` branch for UAT deployment; after UAT sign-off, `release/sprint-N` → `main` → tagged `v1.2.0`. Hotfixes: branch from `main`, fix, test, merge to `main` AND back-merge to `develop`. No force-pushes to `main` or `develop` — protected branches. This strategy gives us a clear history of what's in each environment at any time.

**565. How is Jenkins used in an EBS development pipeline?**
Our Jenkins pipeline had stages: (1) **Build** — compile Java/OAF source using JDeveloper headless build (`ojdeploy`); produce JAR artifact. (2) **PL/SQL deploy to DEV** — run SQL scripts via JDBC (`sqlplus` with `@` scripts); compile packages. (3) **FNDLOAD to DEV** — upload LDT files for menus, responsibilities, profile options. (4) **OAF JAR deploy to DEV** — copy JAR to `$JAVA_TOP`, restart OC4J (via `adapcctl.sh` on the app server). (5) **Smoke test** — hit a health-check URL to verify OAF startup. (6) **Notify** — Slack/email notification with build status and link to logs. Triggered by merge to `develop` branch. Manual trigger for UAT and PROD deployments (with approval gate). Jenkins ran on an internal server with SSH access to app/DB servers.

**566. What automated testing approaches work for OAF customizations?**
Full OAF UI automation is difficult due to EBS's complex session management (ICX cookies, BC4J state). Practical approaches: (1) **PL/SQL unit tests with utPLSQL** — test all business logic in packages independently of the UI. Best ROI for EBS. (2) **Oracle Application Testing Suite (OATS)** — Oracle's official tool; can record and replay OAF sessions; handles ICX session tokens automatically. Used for critical smoke tests after each deployment. (3) **Selenium with custom session management** — authenticate via EBS login, then navigate; brittle due to dynamic IDs in OAF-generated HTML. (4) **Manual test scripts** — numbered steps with expected results; executed by QA tester. Even without full automation, having utPLSQL on the PL/SQL layer catches ~60% of regressions at the logic level before any UI testing.

**567. What is an environment refresh and when is it needed?**
An environment refresh copies PROD data (or a sanitized subset) to DEV/UAT. Needed when: (1) UAT data is too stale — test data doesn't reflect current PROD configurations (responsibilities, profile options, supplier setup). (2) After a PROD patch — UAT must match PROD's patch level. (3) Preparing for a major feature regression test — needs realistic data volumes. Process: DBA takes a Data Pump export of PROD, imports to UAT (with password scrambling for security — `FND_USER.ENCRYPTED_FOUNDATION_PASSWORD` masked). Then apply any environment-specific config (DEV/UAT profile options, test users). Schedule during a weekend to minimize disruption. After refresh: verify CEMLI deployments — code deployed to UAT pre-refresh may be lost and needs redeployment.

**568. How do you manage EBS releases and coordinate deployments across DEV → UAT → PROD?**
Release management process: (1) JIRA release version (e.g., `v2.3`) tags all tickets going into the release. (2) Developer generates a deployment package: FNDLOAD scripts, SQL scripts, JAR files, deployment runbook — all in a versioned folder in Git. (3) UAT deployment: change request in ServiceNow; DBA and app team execute the runbook in UAT; functional tester validates. (4) PROD deployment: CTASK in ServiceNow with: change description, deployment steps, validation steps, rollback steps, risk assessment, approval from IT manager. Change window: Saturday 10 PM – 2 AM. (5) Post-deployment: developer validates in PROD using a smoke test script; closes CTASK with evidence. (6) Version tag applied to Git `main` branch. Release notes documented in Confluence.

**569. How does ServiceNow fit into the EBS change management process?**
ServiceNow is the IT change management system. Every PROD deployment requires a **Change Request** (CR) in ServiceNow. CR contains: change title, description, risk level (Low/Medium/High), impacted systems, deployment window, implementation steps, backout steps, approvers (dev lead, IT manager, CAB for High risk). For urgent fixes: use an **Emergency Change** type — same fields but faster approval (CAB chair approval only). **CTASKs** (change tasks) are sub-tasks within a CR for specific actions: CTASK-1 "DBA: Run DDL scripts", CTASK-2 "App team: Deploy OAF JAR", CTASK-3 "Dev: Validate smoke test". Each CTASK assignee updates their task with completion notes. The CR is closed only when all CTASKs are closed and the functional owner verifies the change. This creates an audit trail for SOX/compliance requirements.

**570. Walk through writing a CTASK for an OC4J bounce.**
CTASK Title: `CTASK-2 — Bounce OC4J on APP01 and APP02 for OAF JAR deployment`

Implementation Steps:
```
1. SSH to APP01 as oracle user
2. Stop OC4J: $ADMIN_SCRIPTS_HOME/adapcctl.sh stop
3. Wait 60 seconds for graceful shutdown
4. Verify stopped: ps -ef | grep opmn (no opmn process)
5. Copy JAR: cp /deploy/XXGE_ASN.jar $JAVA_TOP/xxge/
6. Clear OAF cache: rm -rf $OA_HTML/.cache/*
7. Start OC4J: $ADMIN_SCRIPTS_HOME/adapcctl.sh start
8. Wait 2 minutes for startup
9. Verify: tail -100 $LOG_HOME/opmn/opmn.log — check for "opmn ready"
10. Repeat steps 2-9 on APP02
```

Backout Steps:
```
1. Stop OC4J on both nodes
2. Restore previous JAR: cp /deploy/backup/XXGE_ASN_v1.1.jar $JAVA_TOP/xxge/XXGE_ASN.jar
3. Start OC4J
```

Estimated Duration: 20 minutes. User Impact: OAF pages unavailable during bounce (rolling bounce minimizes downtime).

**571. How do you deploy concurrent programs in EBS and ensure they work in PROD?**
Deployment steps: (1) **PL/SQL package** — deploy via SQL script: `CREATE OR REPLACE PACKAGE BODY XXGE_CP_PKG...`; grant execute to PUBLIC. (2) **Executable registration** — FNDLOAD: `FNDLOAD APPS/... 0 Y UPLOAD $FND_TOP/patch/115/import/afcpprog.lct XXGE_CP_PROG.ldt`. This registers the executable in `FND_EXECUTABLES`. (3) **Program definition** — FNDLOAD with `afcpprog.lct` for the program definition (`FND_CONCURRENT_PROGRAMS`), parameters (`FND_CONCURRENT_PROGRAM_PARAMETERS`). (4) **Request group assignment** — FNDLOAD with `afcpreqg.lct`. (5) **Validation** — in PROD, navigate to `System Administrator > Concurrent > Programs > Define` and verify the program appears; submit it manually, verify it completes with status `Normal`. Check output/log files via `View Concurrent Requests`.

**572. What documentation standards do you follow for EBS customizations?**
(1) **Technical Design Document (TDD)** — mandatory for all CEMLIs before dev starts. Stored in Confluence. (2) **Inline code comments** — only for non-obvious logic (not for every line). PL/SQL package header comment: package purpose, author, creation date, modification history. (3) **FNDLOAD scripts** — each `.ldt` file has a header comment with CEMLI ID and description. (4) **Deployment runbook** — step-by-step instructions that any developer can follow, not just the author. Include expected output for each step. (5) **Test scripts** — numbered steps with expected vs actual result columns. (6) **CEMLI register** — master spreadsheet with all custom objects cross-referenced to JIRA tickets. (7) **Git commit messages** — `[JIRA-ID] Brief description of change`. (8) **Post-go-live runbook** — support procedures for top issues. All documentation stored in Confluence and linked from JIRA tickets.

**573. How do you store FNDLOAD LCT and LDT files in a Git repository?**
Store in `fndload/` directory organized by object type: `fndload/menus/`, `fndload/responsibilities/`, `fndload/concurrent_programs/`, `fndload/profile_options/`, `fndload/messages/`, `fndload/lookups/`, `fndload/value_sets/`, `fndload/request_groups/`. Each LDT file named by CEMLI ID: `XXGE_ISUP_RESP.ldt`, `XXGE_PROMISE_DATE_MSG.ldt`. The corresponding FNDLOAD download command is documented in a `README.md` in each subdirectory. On deployment, the runbook references the specific LDT files and the correct LCT file from `$FND_TOP/patch/115/import/`. This ensures the Git history shows exactly when and what AOL objects changed — critical for debugging "something changed in PROD that we didn't intend" scenarios.

**574. What are the risks of patching EBS without adequate UAT?**
(1) **CEMLI breakage** — OAF substitutions may fail if patched class signatures changed; PL/SQL packages calling patched standard APIs may get compile errors. (2) **Profile option changes** — patches sometimes add or modify profile option default values, changing system behavior silently. (3) **Data model changes** — patches occasionally add NOT NULL columns to standard tables; custom packages inserting into those tables will error. (4) **Workflow changes** — WF item type changes can break in-flight workflow instances. (5) **Personalization reset** — MDS (JDR) patches can wipe personalizations. (6) **Performance regressions** — new code paths may be slower. Without UAT: you discover these in PROD during business hours. With UAT: you catch them in a controlled environment. Minimum viable UAT for a patch: run the 30 core test scripts + compile XXGE packages after patch and check for errors.

**575. How do you use SQL Developer in your daily EBS development work?**
Daily uses: (1) **Query data** — write and run SQL against EBS tables; use SQL Developer's code completion for table/column names. (2) **Debug PL/SQL** — set breakpoints in packages, step through code with the PL/SQL Debugger (requires `DEBUG CONNECT SESSION` privilege). (3) **Explain Plan** — F10 key shows execution plan inline; switch to Plan tab for graphical plan. (4) **AUTOTRACE** — View > Autotrace — see statistics for any query. (5) **Export results** — export query results to CSV/Excel for data analysis. (6) **Schema browser** — explore table structure, constraints, indexes without writing DDL queries. (7) **Run scripts** — execute `.sql` deployment scripts directly. (8) **DB connections** — maintain connection profiles for DEV/UAT/PROD (with PROD being read-only for safety). Keyboard shortcut: F5 runs the current statement; Ctrl+Enter runs the script.

**576. How do you set up JDeveloper for OAF development?**
Steps: (1) Install JDeveloper 10.1.3.x (must match EBS OAF version — for R12.1.x use 10.1.3.4, for R12.2.x use 10.1.3.5). (2) Copy OAF libraries from EBS application server: `$JAVA_TOP/*.jar`, `$OAF_CLASSPATH jars` to local `jdevlib/` folder. (3) In JDeveloper: Tools > Manage Libraries — add a new library pointing to the copied JARs. (4) Create a new project, add the OAF library. (5) Download the page XML from EBS using `FNDLOAD DOWNLOAD JDR_*` and open in JDeveloper OA Extension. (6) For coding: extend `OAPageLayoutController`, override `processRequest`, import `oracle.apps.fnd.framework.*`. (7) Build and deploy: `ojdeploy` to create JAR; copy to `$JAVA_TOP` on app server. Key: JDeveloper version and EBS OAF version must match exactly, or you get mysterious class compatibility errors at runtime.

**577. How do you use Eclipse or another IDE for the Spring Boot EBS integration service?**
For the Spring Boot REST service (Java, EBS SOAP integration): Eclipse IDE with Spring Tools Suite (STS) plugin. Project setup: Maven or Gradle project; Spring Boot starter dependencies (`spring-boot-starter-web`, `spring-boot-starter-ws` for SOAP, `spring-boot-starter-jdbc` for direct DB access). Local development: point `application.properties` to a local EBS DEV database. Run/debug with embedded Tomcat. Key Eclipse features used: (1) Spring Boot Dashboard — start/stop app with one click. (2) Breakpoints in `@RestController` methods. (3) HTTP client (REST Client plugin) to test endpoints. (4) Maven dependency management — `pom.xml` for adding Oracle JDBC driver. Code review: PRs in GitHub reviewed in browser. Deployments to test server via Jenkins pipeline (Git push → Jenkins build → Docker image → Kubernetes pod or standalone JAR on app server).

**578. What EBS log files do you check when debugging an issue?**
(1) **OAF/OC4J logs** — `$LOG_HOME/ora/10.1.3/j2ee/OC4J_oacore/application.log` — exceptions from OAF controllers and AMs. (2) **Apache/OHS access log** — `$IAS_ORACLE_HOME/Apache/Apache/logs/access_log` — HTTP requests; useful for 404s and timeouts. (3) **FND Concurrent log** — `View Concurrent Requests > View Log` in EBS UI; or directly at `$APPLCSF/$APPLLOG/XXXXXXXX.req` (req file number). (4) **Alert log** — `$ORACLE_BASE/diag/rdbms/.../alert_<SID>.log` — DB-level errors (ORA- messages, startup/shutdown). (5) **FND_LOG_MESSAGES** — for EBS modules with FND logging enabled; query: `SELECT * FROM fnd_log_messages WHERE module LIKE 'pos.%' ORDER BY log_sequence DESC`. (6) **OPMN log** — `$ORACLE_HOME/opmn/logs/ons.log` — OC4J process management. Check #1 first for OAF issues; #3 for CP issues.

**579. What is the ADX utility and when is it used in EBS?**
ADX (Applications DBA) is a menu-driven utility (`adadmin`) for EBS system administration tasks: (1) **Compile APPS schema** — recompile invalid objects (`utlrp` equivalent with EBS awareness). (2) **Recreate grants and synonyms** — required after installing custom objects; ensures `APPS` user can access new tables in custom schemas. (3) **Maintain snapshot information** — tracks installed patches. (4) **Generate forms and reports** — recompile Oracle Forms `.fmx` and Reports `.rdf` files after source changes. (5) **Maintain current view snapshots** — used during patching to maintain `_all` views. Commonly used after: deploying new `XXGE_*` tables (run "Recreate grants/synonyms" so APPS can access them), after patching (run "Compile APPS schema" to catch broken packages), after JDeveloper errors suggest class path issues.

**580. What is the difference between adpatch and ADOP in Oracle EBS?**
**adpatch** (pre-R12.2 / R12.1): traditional patch application tool; requires bringing down all application tier services during patching — downtime window. (2) **ADOP** (AD Online Patching, R12.2+): supports online patching — the system remains available during most of the patch cycle. Uses a dual file system ("run" edition + "patch" edition). ADOP phases: `prepare` (creates patch edition), `apply` (applies patch to patch edition — system runs on run edition), `finalize` (prepares for cutover), `cutover` (switches run edition to patch edition — brief ~5-minute downtime), `cleanup` (removes old run edition). ADOP dramatically reduces patching downtime from 4–8 hours (adpatch) to 10–30 minutes (cutover window only). For GE's quarterly patches, switching to ADOP in R12.2 was a major operational improvement.

**581. What is the APPL_TOP directory and what does it contain?**
`APPL_TOP` is the root directory of the Oracle Applications product file system. Key subdirectories: (1) `$APPL_TOP/APPSORA.env` — environment setup script sourced before any EBS command. (2) `$APPL_TOP/po/12.0.0/` — Oracle Purchasing product home (similar for other products). Within each product home: `bin/` (executables), `forms/US/` (Forms `.fmx`), `reports/US/` (Reports `.rdf`), `sql/` (SQL scripts), `patch/115/import/` (FNDLOAD control files). (3) `$JAVA_TOP` — custom and standard Java classes and JARs. (4) `$OA_HTML` — OAF HTML files, static resources, `.cache/` for OAF page cache. (5) `$COMMON_TOP/admin/scripts/` — admin scripts (`adapcctl.sh`, `adcmctl.sh`). Knowing APPL_TOP structure is essential for deploying OAF JARs, FNDLOAD scripts, and finding log files.

**582. What is a RUP (Release Update Pack) and how does it affect customizations?**
A RUP is a major cumulative patch bundle for EBS (e.g., "HR RUP6"). It applies all patches released for that module since the last RUP. Impact on customizations: (1) Standard packages we referenced may have new signatures or behavior. (2) OAF pages we substituted may have new methods — our substitution class must override the correct new method. (3) Database columns may have been added to standard tables — custom VOs querying `SELECT *` may get unexpected extra columns. (4) BPA/security changes may affect profile options. Pre-RUP protocol: (1) Review RUP readme for "Impact on Customizations" section. (2) Run CEMLI impact analysis. (3) Apply in DEV first, recompile custom packages, check for errors. (4) Test all CEMLIs in the affected module. (5) Document changes needed before UAT.

**583. How do you track the CEMLI inventory and ensure nothing is lost during patching?**
CEMLI register (Excel/Confluence) with: CEMLI ID, Type (OAF/PL/SQL/BIP/WF/FNDLOAD), Object name, Description, Patch risk (standard objects modified?), Last tested date, Last patched version when tested. Before each patch: (1) Query `AD_BUGS` for the patch number — check if any standard objects in our CEMLI dependencies are included. (2) Run `SELECT object_name, status FROM dba_objects WHERE status = 'INVALID' AND owner = 'APPS'` post-patch. (3) Cross-reference invalid objects with CEMLI register. High-patch-risk CEMLIs (those substituting or wrapping standard classes) are always regression-tested. The register is the single source of truth — if a CEMLI isn't in it, it doesn't exist officially and can't be supported.

**584. How do you conduct a code review for an EBS customization?**
Code review checklist: (1) **Standards** — objects named with `XXGE_` prefix; no direct DML on standard Oracle tables. (2) **APIs** — uses standard EBS APIs (`AP_VENDOR_PUB_PKG`, `PO_CHANGE_API_PVT`) not direct inserts. (3) **Error handling** — all PL/SQL exceptions caught; errors logged via `FND_LOG.STRING`, user messages via `FND_MESSAGE`. (4) **Security** — no hard-coded org_id; MOAC context set before multi-org queries. (5) **Performance** — no row-by-row processing for bulk data; bulk collect/FORALL for >100 rows; no `SELECT *`. (6) **Patching safety** — OAF substitution overrides minimal methods; no copies of standard files. (7) **Test coverage** — TDD includes test scenarios for happy path and error path. Review via Git PR with inline comments. Developer must address all comments before merge. Critical issues (security, data corruption risk) are blockers; style issues are suggestions.

**585. How do you estimate effort for OAF development tasks?**
Breakdown by complexity: (1) **Simple config** (hide/show field via personalization): 0.5 days. (2) **VO attribute change** (add column, change WHERE): 1 day. (3) **CO extension** (add validation, field default): 1–2 days. (4) **AM method + PL/SQL** (new business logic): 2–4 days. (5) **New OAF region** (table region with LOV, save): 3–5 days. (6) **New OAF page** (full flow): 7–15 days. (7) **OAF substitution** (replace standard class): 3–5 days dev + 2 days regression. Add: 50% of dev time for unit testing, 30% buffer for environment issues and code review rework, 10% for FNDLOAD/deployment scripts. Validate estimates with a reference task from the same project — "this is similar to XXGE-OAF-005 which took 4 days" calibrates better than abstract points.

**586. How do you handle technical debt in an EBS customization built under time pressure?**
(Already covered in Q516 — see that answer for the full detail on tech-debt management strategy.)

**587. What is your approach to a hotfix / emergency deployment in EBS PROD?**
Emergency deployment protocol: (1) Confirm P1 severity — is the system down or are users blocked from core operations? (2) Fix in DEV within 1 hour; have another developer review the change (even a quick 15-minute peer review). (3) Test in UAT — at minimum, test the specific broken scenario. Skip full regression if time-critical (document the risk). (4) Raise Emergency CTASK in ServiceNow; get fast-track approval from IT manager. (5) Deploy to PROD following runbook steps — DBA and app team on standby. (6) Validate in PROD immediately post-deployment. (7) Notify stakeholders once resolved. (8) Next business day: write incident report, backfill the normal test coverage, and schedule a proper regression test for the affected area. Never skip step 4 even in an emergency — the audit trail protects you and the organization.

**588. How did you document PL/SQL packages in the GE project?**
Package header: brief description, author, creation date, modification log (date, developer, change description). Procedure headers: only if the purpose is non-obvious from the name. No line-by-line comments — code should be self-explanatory via good naming. Exception: document workarounds explicitly — `-- Oracle Bug 12345678: must call COMMIT before querying FND_GLOBAL`. All packages stored in Git under `plsql/<module>/` with the `.pks` (spec) and `.pkb` (body) files separately — allows easy diff of spec changes (which affect calling code) vs body changes (internal). Deployment script: `CREATE OR REPLACE PACKAGE SPEC...` then `CREATE OR REPLACE PACKAGE BODY...`. Package versioning: `G_VERSION CONSTANT VARCHAR2(10) := '2.3.1'` as a package-level constant, readable via `XXGE_PKG.G_VERSION` for quick version check in PROD.

**589. How do you run a JIRA sprint planning session for an EBS sprint?**
Preparation: product owner prioritizes backlog; dev lead estimates story points (or team does planning poker for complex items). Session agenda (2 hours for a 2-week sprint): (1) Review last sprint velocity (baseline for this sprint). (2) PO presents top backlog stories — explains business value and acceptance criteria. (3) Dev lead asks clarifying questions: "Is this a substitution or personalization?" "Does this need a new DB table?" (4) Team estimates points; if gap between dev and PO expectations, negotiate scope. (5) Dev lead commits to achievable scope for the sprint based on capacity (headcount × 5 days × 6 hours/day × 0.7 productivity = available hours). (6) Stories assigned to developers based on module expertise. (7) Sprint goal stated in one sentence: "By end of sprint, suppliers can view and acknowledge POs via iSupplier." Document outcomes in JIRA sprint; share with stakeholders.

**590. How do you communicate blockers to a non-technical project manager?**
(Already covered detail in Q514.) Short answer: use impact–cause–fix–timeline format. Be specific about what you need and by when. Follow up in writing after any verbal conversation. Don't wait until the daily standup if you're blocked — message the PM immediately.

**591. How do you review a technical design presented by a junior developer?**
Structured review approach: (1) **Functional accuracy** — does the design actually address the requirement? Ask the developer to walk through the happy path step by step. (2) **Standard approach** — is there a simpler OOB solution they missed? (3) **Risk assessment** — what breaks if this fails? Is the rollback plan realistic? (4) **Performance** — will this be OK with PROD data volumes? Ask about the expected row count. (5) **Maintainability** — can another developer understand and maintain this in 6 months? (6) Give feedback as questions, not commands: "How would this handle the case where the PO is on hold?" rather than "This doesn't handle holds." Coaching > critiquing. Document agreed changes in the JIRA ticket. Follow up at code review stage to verify the design was implemented as discussed.

**592. What is ADOP and how does it differ from adpatch?**
(Already covered in Q580 — see that answer for the full adpatch vs ADOP comparison.)

**593. Walk through a CEMLI rollback scenario — what happens if a PROD deployment fails halfway?**
Scenario: OAF JAR deployed but the corresponding PL/SQL package wasn't updated due to a script error — the JAR calls a method that doesn't exist in the DB package yet. Result: OAF page throws a Java exception. Rollback procedure: (1) Check CTASK rollback steps (these were written pre-deployment). (2) Stop OC4J on all nodes. (3) Restore previous JAR from backup folder: `cp /deploy/backup/XXGE_ASN_v1.1.jar $JAVA_TOP/xxge/`. (4) Restart OC4J. (5) Verify the previous JAR version is active: check `XXGE_VERSION` function in PROD. (6) Notify stakeholders: "Deployment rolled back due to partial failure; system is on previous version and fully operational." (7) Fix the script failure, re-test in UAT, schedule a new deployment window. Key lesson: always test rollback steps in UAT before PROD — at least once per quarter.

**594. What is your experience with multi-node OAF setup in EBS?**
GE's setup: 2 application server nodes (APP01, APP02) behind an F5 load balancer with sticky sessions (session affinity based on `ICX_SESSION` cookie). Each node runs: OC4J_oacore (OAF), OC4J_forms, Apache/OHS. OAF is stateful — AM passivation writes state to the DB (`JBO_SESSION`), allowing session recovery if one node fails. Configuration points: (1) `$INST_TOP/ora/10.1.3/j2ee/OC4J_oacore/config/data-sources.xml` — DB connection pool config; identical on both nodes. (2) `jbo.pool.maxsize` in `OAApplicationModule.xml` — AM pool size per node. (3) Apache `mod_oc4j` config for load balancing in `oc4j-connectors.xml`. (4) Sticky sessions ensured via F5 cookie persistence — without this, a user's second request goes to a different node and the AM is not found, causing a re-login. Deployment: JAR must be deployed on ALL nodes simultaneously (rolling bounce to minimize downtime).

**595. Why does OC4J bounce and what are common reasons in EBS?**
Common OC4J bounce causes: (1) **Java OutOfMemoryError (OOM)** — heap exhaustion from memory leak (e.g., growing collection in a static variable, unclosed AM pool). Monitor JVM heap via `JVM Diagnostics` in EM or `jstat -gcutil <pid>`. (2) **New JAR deployment** — OAF class loading requires restart for new JARs. (3) **OAF cache corruption** — stale OAF metadata in `.cache/` after JDR personalization update; clear cache + bounce. (4) **EBS patch application** — patches touching Java code require OC4J restart. (5) **OC4J deadlock** — AM pool starvation combined with a long-running transaction can cause deadlock. (6) **OS-level issue** — NFS mount for `$OA_HTML` becoming unavailable. After each unexpected bounce, check `application.log` for the root cause exception before restarting — bouncing without understanding the cause means it will happen again.

**596. How do you load-balance iSupplier across multiple OC4J nodes?**
Load balancing is configured in Apache `mod_oc4j`: `Oc4jMountCopies 2` and `Oc4jMount /OA_HTML ajp13://APP01:12602|ajp13://APP02:12602` — Apache distributes requests round-robin across both nodes. Sticky sessions: configured at the F5 layer using cookie persistence on the `ASESSIONID` cookie (set by OC4J). Without sticky sessions: user's AM state is on APP01, next request goes to APP02 — AM not found — OAF falls back to creating a new AM (performance hit) or throws an error. For high availability: if APP01 goes down, F5 detects via health check, stops routing to APP01, all traffic to APP02. OC4J on APP02 handles the increased load — size the pool at 60% of max to handle failover. During maintenance: drain APP01 connections (set weight=0 in F5) before bounce to avoid mid-session disruptions.

**597. What documentation artifacts would you hand over at the end of an EBS implementation project?**
Handover package: (1) **CEMLI Register** — all custom objects with JIRA links and deployment commands. (2) **Architecture Document** — network diagram, server names, EBS version, module list, integration diagram. (3) **Support Runbook** — top 20 support scenarios with diagnostic SQL and resolution steps. (4) **Test Scripts** — all 30+ UAT test scripts with last-pass evidence. (5) **Deployment Guide** — how to deploy each type of CEMLI (OAF, PL/SQL, BIP, WF, FNDLOAD). (6) **Environment Guide** — how to access DEV/UAT/PROD, key profile options, admin procedures. (7) **Vendor Contacts** — Oracle Support SR process, DBA team contact, network team contact. (8) **Known Issues / Workarounds** — deferred items from Phase 1, known limitations. (9) **Recorded KT Sessions** — video recordings from the 3-day KT. (10) **Git Repository Access** — onboard support team to the Git repo. Handover acknowledged via sign-off from the receiving support manager.

**598. What is your experience with OAF performance in a multi-node EBS setup?**
Key observations from GE's 2-node setup: (1) **AM pool contention** — peak hours (9–11 AM supplier login time) caused AM pool exhaustion on both nodes simultaneously. Fixed by increasing `jbo.pool.maxsize` from 20 to 40 per node. (2) **Session affinity issues** — a misconfigured F5 maintenance window disabled sticky sessions; users experienced AM not found errors. Fixed by restoring sticky session config. (3) **Cache inconsistency** — OAF page cache (`.cache/`) was not shared between nodes (each node has its own cache). After a JDR personalization update, one node still served the old page. Fixed: always clear cache on ALL nodes simultaneously. (4) **JDBC connection pool** — each node maintains its own pool to the DB. A DB failover event caused stale connections on both nodes. Fixed: enable connection validation (`test-connections-on-match`) to purge stale connections automatically.

**599. How do you write effort estimates that account for EBS-specific risks?**
Standard development estimate × EBS complexity multipliers: (1) **Multi-org risk** (+20%) — if the feature touches multiple OUs, MOAC testing adds significant scope. (2) **Patching risk** (+15%) — if the feature touches a module with a quarterly patch due, add buffer for potential post-patch rework. (3) **OAF substitution** (+30% vs CO extension) — substitutions are higher risk, require more regression testing. (4) **New WF item type** (+50% vs WF notification change) — new item types require thorough testing of all activities and timeout transitions. (5) **Data migration** (2× dev estimate for validation and reconciliation) — data migration validation always takes longer than the migration itself. Present estimates in ranges: "3–5 days depending on MOAC complexity" — never a single point for estimates over 3 days. Document assumptions in the JIRA ticket so scope creep is visible when assumptions change.

**600. Describe your overall approach to delivering a complex OAF feature from requirements to PROD.**
End-to-end delivery: (1) **Requirements** — attend functional workshops; document use cases and acceptance criteria in JIRA stories. Ask "what if" questions to surface edge cases early. (2) **Design** — write TDD; get peer review and functional lead sign-off before writing code. (3) **Development** — feature branch in Git; follow CEMLI standards; write PL/SQL unit tests for business logic using utPLSQL. (4) **Code review** — PR against `develop`; address all review comments; merge only after approval. (5) **DEV testing** — run through all test scenarios manually; verify in OAF diagnostics that VO queries are efficient. (6) **UAT deployment** — deploy via runbook; hand test scripts to functional tester. (7) **UAT fixes** — P1/P2 defects fixed same-sprint; P3 deferred. (8) **UAT sign-off** — functional lead signs the UAT evidence form. (9) **PROD deployment** — CTASK in ServiceNow; deploy during change window; validate smoke test. (10) **Post-go-live** — monitor `FND_LOG_MESSAGES` for errors; be available for hypercare support. Each step documented and traceable. This disciplined approach is what makes EBS customizations maintainable and supportable long-term.
