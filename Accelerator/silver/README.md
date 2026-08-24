===================================================================
WEEK 2 / DAY 9: TASK 2.4 - SILVER OPERATING STANDARD README
===================================================================
DOCUMENT PURPOSE: OPERATIONAL MANAGEMENT GUIDELINES & QUALITY CHECKLIST

OFFICIAL BLUEPRINT REFERENCES:
- Fabric Medallion Architecture: https://microsoft.com
- Semantic Link Labs Framework: https://github.com

-------------------------------------------------------------------
SECTION 1: DATA CLEANING & REFINEMENT FREQUENCY
-------------------------------------------------------------------
1. EXECUTION INTERVAL: The Silver transformation layer must execute on an automated micro-batch or daily schedule immediately following the successful completion verification of the parent Bronze ingestion pipeline.
2. RE-PROCESSING WINDOW: In the event of an upstream schema corruption fix, the Silver processing engine must support an automated full-table historical rebuild spanning a rolling 90-day data window.

-------------------------------------------------------------------
SECTION 2: TABLE & PARTITION NAMING CONVENTIONS
-------------------------------------------------------------------
1. CATALOG TABLE NAMES: All production-grade tables sitting inside the Silver catalog database must follow a strict prefix naming convention: silver_[source_system]_[entity_name]
2. PARTITIONING PARMS: Large relational tables containing over 50 million rows must be partitioned by business execution timelines using lowercase formats: `year=yyyy/month=mm/`.

-------------------------------------------------------------------
SECTION 3: HISTORICAL DATA UPDATE STANDARDS
-------------------------------------------------------------------
To handle row modifications, historical records must be updated using these strict transactional engineering criteria:
1. TYPE 1 CHANGES (OVERWRITE): Standard operational columns that do not require history tracking must use optimized Delta Lake MERGE statements to execute clean inline upserts based on target primary keys.
2. TRANSACTION BOUNDS: All write processes must use explicit transaction isolation blocks to ensure that incomplete data runs never corrupt active reporting tables.

-------------------------------------------------------------------
SECTION 4: EXCEPTION ROUTING & RECOVERY RULES
-------------------------------------------------------------------
1. REJECTION THRESHOLD: If an incoming data block contains a corrupt primary key or an un-castable timestamp data type, the row must be dropped from the target table.
2. TRACKING DIRECTORY: Errant records must be routed to a centralized logging repository for operational troubleshooting, and a failure webhook must be fired immediately.

-------------------------------------------------------------------
SECTION 5: PRODUCTION DEPLOYMENT VALIDATION CHECKLIST
-------------------------------------------------------------------
Before a developer can mark a Silver data refinement workflow as production-compliant, they must verify and check off these 5 operational baselines:
- [ ] 1. Deduplication Proof: A validation script confirms that all composite primary key blocks contain exactly zero duplicate entries.
- [ ] 2. Schema Matching Pass: A layout verification run proves that table field parameters match the semantic data models exactly.
- [ ] 3. Structural Null Check: A direct row calculation confirms that zero records contain blank or null text inside critical key columns.
- [ ] 4. Transactional Merge Test: An operational test confirms that updates overwrite matching rows correctly without duplicating records.
- [ ] 5. Telemetry Tracking Pass: Processing status and row execution stats are logged clearly inside the central monitoring hub dashboards.
