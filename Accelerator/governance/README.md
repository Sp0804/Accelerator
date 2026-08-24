===================================================================
WEEK 2 / DAY 15: TASK 2.10 - GOVERNANCE OPERATING STANDARD README
===================================================================
DOCUMENT PURPOSE: OPERATIONAL MANAGEMENT GUIDELINES & COMPLIANCE CHECKLIST

OFFICIAL BLUEPRINT REFERENCES:
- Microsoft Fabric Governance Standard: https://microsoft.com
- Semantic Link Labs Framework: https://github.com

-------------------------------------------------------------------
SECTION 1: DATA AUDITING & CLASSIFICATION CADENCE
-------------------------------------------------------------------
1. AUDIT FREQUENCY: The data platform must undergo an automated governance scan every rolling 30 days to re-verify classification tags on all schema columns.
2. DISCOVERY POLICY: New tables landing in the catalog must be programmatically scanned for PII/private indicators before being authorized for downstream business reporting users.

-------------------------------------------------------------------
SECTION 2: DATA LINEAGE & META-TRACKING CONVENTIONS
-------------------------------------------------------------------
1. LINEAGE MAP UPDATES: Data path dependency visual records must be tracked and auto-updated inside the catalog hub upon any pipeline configuration change.
2. REPO METADATA ASSIGNMENTS: Every database catalog schema must include documentation links identifying the primary business data owner and engineering contact.

-------------------------------------------------------------------
SECTION 3: ACCESS REVIEW & PERMISSION LIFECYCLES
-------------------------------------------------------------------
To eliminate permission creep across cloud environments, access privileges must follow strict operational lifecycles:
1. PRIVILEGE RE-VALIDATION: All workspace member, contributor, and admin permission tokens must undergo a mandatory review cycle every 90 days.
2. INACTIVE DE-PROVISIONING: Accounts showing zero login or execution activity for a continuous 60-day period must have their data access tokens revoked instantly.

-------------------------------------------------------------------
SECTION 4: GOVERNANCE EXCEPTION ROUTING RULES
-------------------------------------------------------------------
1. MASKING VIOLATION ROUTING: If an active data pipeline fails to apply encryption or masking to classified private fields, the execution instance must immediately terminate.
2. INCIDENT ALERTING: A critical security alert flag must be fired straight to the organizational tracking hub.

-------------------------------------------------------------------
SECTION 5: PRODUCTION DEPLOYMENT VALIDATION CHECKLIST
-------------------------------------------------------------------
Before a developer can mark a workspace configuration or data entity as production-compliant, they must verify and check off these 5 operational baselines:
- [ ] 1. PII Scan Complete: A data scanning run confirms that all columns containing sensitive customer fields are masked.
- [ ] 2. Identity Least Privilege: Workspace user roles are strictly checked to ensure zero business end-users possess developer or contributor access.
- [ ] 3. Lineage Map Pass: The automated catalog scanner maps out the full data path from Bronze ingestion files to Gold summary tables.
- [ ] 4. Owner Registry Logged: The physical target catalog asset documentation records clear business and technical owner labels.
- [ ] 5. Access Token Verification: Active security configuration tables show that all dynamic access profiles match approved security baselines.
