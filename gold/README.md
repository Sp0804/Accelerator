===================================================================
WEEK 2 / DAY 11: TASK 2.6 - GOLD OPERATING STANDARD README
===================================================================
DOCUMENT PURPOSE: OPERATIONAL MANAGEMENT GUIDELINES & REPORTING CHECKLIST

OFFICIAL BLUEPRINT REFERENCES:
- Fabric Medallion Architecture: https://microsoft.com
- Power BI Direct Lake Mode: https://microsoft.com

-------------------------------------------------------------------
SECTION 1: BUSINESS REFRESH & AGGREGATION INTERVALS
-------------------------------------------------------------------
1. EXECUTION CADENCE: The Gold business layer transformations must run immediately following the successful completion and quality sign-off of the parent Silver data layer pipelines.
2. DELTA RE-COMPUTE WINDOW: Upon an executive business metric realignment or definition modification, the Gold orchestration layer must support an automated full-table reload of all reporting datasets.

-------------------------------------------------------------------
SECTION 2: REPORTING TABLE NAMING CONVENTIONS
-------------------------------------------------------------------
1. CATALOG TABLE PREFIXES: All production-grade tables inside the Gold reporting database catalog must explicitly utilize clear architectural business prefixes:
   - Fact Tables: `gold_fact_[business_process_name]` (e.g., gold_fact_taxi_trips)
   - Dimension Tables: `gold_dim_[attribute_name]` (e.g., gold_dim_rate_codes)

-------------------------------------------------------------------
SECTION 3: QUERY PERFORMANCE & CACHING STANDARDS
-------------------------------------------------------------------
To guarantee sub-second rendering speeds for executive dashboards, all Gold layer assets must enforce these performance parameters:
1. MANDATORY V-ORDER COMPACTION: Every single table write transaction must leverage automated V-Order optimizations to compact parquet files cleanly.
2. DIRECT LAKE ALIGNMENT: Tables must map directly into unified Fabric Semantic Models to ensure Power BI reads data frames right out of memory without running slow background data imports.

-------------------------------------------------------------------
SECTION 4: EXCEPTION ROUTING & METRIC LOGGING RULES
-------------------------------------------------------------------
1. BALANCING REJECTIONS: If a Gold summary query calculates a financial deviation error that does not balance back to the matching Silver record balances, the pipeline transaction must fail.
2. INCIDENT NOTIFICATION: Failed aggregation runs must instantly trigger a high-severity alert to the corporate monitoring hub.

-------------------------------------------------------------------
SECTION 5: PRODUCTION DEPLOYMENT VALIDATION CHECKLIST
-------------------------------------------------------------------
Before a developer can mark a Gold business reporting dataset as ready for dashboard deployment, they must verify and check off these 5 operational baselines:
- [ ] 1. Star Schema Pass: A physical check confirms that reporting data is structured as explicit Facts and Dimensions rather than a single messy wide table.
- [ ] 2. Financial Balance Proof: An automated validation log confirms that aggregated metric row totals balance back 100% against raw source entries.
- [ ] 3. V-Order Verification: Storage tracking files prove that Delta parquet tables were saved with structural optimization flags turned on.
- [ ] 4. Direct Lake Setup: The Power BI report canvas is explicitly configured to query the live dataset natively without requiring data schedules or import steps.
- [ ] 5. Monitoring Metric Track: Job runtime durations and row processing metadata details are logging correctly to the central operations dashboard.
