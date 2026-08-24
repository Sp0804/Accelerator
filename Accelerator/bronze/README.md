===================================================================
WEEK 2 / DAY 7: TASK 2.2 - BRONZE OPERATING STANDARD README
===================================================================
DOCUMENT PURPOSE: OPERATIONAL MANAGEMENT GUIDELINES & VALIDATION CHECKLIST

OFFICIAL BLUEPRINT REFERENCES:
- Fabric Medallion Architecture: https://microsoft.com
- Data Factory Testing Framework: https://github.com

-------------------------------------------------------------------
SECTION 1: RAW DATA RETENTION RULES
-------------------------------------------------------------------
1. IMMUTABILITY STANDARD: Data landed within the Bronze layer is strictly read-only. Modifying, truncating, or updating raw historical records is explicitly forbidden.
2. PURGING RULE: Retain all raw source delta files and untransformed blobs for a minimum rolling period of 365 days to support disaster recovery, schema tracing, and point-in-time table re-processing.

-------------------------------------------------------------------
SECTION 2: FOLDER & TABLE NAMING CONVENTIONS
-------------------------------------------------------------------
1. REPOSITORY DIRECTORY PATHS: Files must land under standard paths using lowercase notation: Files/bronze/[source_system]/[entity_name]/yyyy/mm/dd/
2. CATALOG DATABASE TABLES: All native catalog tables sitting inside the Bronze zone must follow a strict prefix syntax: bronze_[source_system]_[entity_name]_raw

-------------------------------------------------------------------
SECTION 3: MANDATORY SYSTEM AUDIT COLUMNS
-------------------------------------------------------------------
To guarantee data lineage tracking, every single dataset injected into the Bronze layer must attach these 3 tracking fields:
1. `src_system_name` (String): The original name of the source database or API endpoint.
2. `ingestion_timestamp` (Timestamp): The exact cosmic timestamp the record hit OneLake storage.
3. `pipeline_run_id` (String): The tracking execution ID pulled straight from the Data Factory engine logs.

-------------------------------------------------------------------
SECTION 4: EXCEPTION & ERROR HANDLING STANDARDS
-------------------------------------------------------------------
1. CAPTURE LOGIC: If a raw file fails schema mapping validation, the pipeline must intercept the broken block, copy it into a separate `Files/bronze/exceptions/` sub-folder, and bypass loading it into the active table.
2. NOTIFICATION TRIGGER: Any validation exception must immediately send a priority webhook ping to the monitoring hub to alert data operators.

-------------------------------------------------------------------
SECTION 5: PRODUCTION DEPLOYMENT VALIDATION CHECKLIST
-------------------------------------------------------------------
Before a developer can mark a Bronze ingestion workflow as ready for production, they must verify and check off these 5 operational baselines:
- [ ] 1. Metadata Schema Rulebook: A valid JSON metadata rule block is registered inside the onboarding config matrix.
- [ ] 2. Lineage Audit Check: The target table matches the explicit prefix naming schema convention perfectly.
- [ ] 3. Column Tracking Pass: A quick select query confirms that all 3 mandatory system audit fields populate values cleanly.
- [ ] 4. Failure Routing Test: A broken dummy record was successfully intercepted and moved into the exceptions directory folder.
- [ ] 5. Run History Log: The data ingestion activity can be tracked with green checkmarks inside the Fabric Monitor Hub.
