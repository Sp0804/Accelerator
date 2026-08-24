# Operations & Monitoring Framework

This directory houses the foundational operational runbooks, monitoring checklists, and cost management guidelines for the Microsoft Fabric platform implementation.

## 📋 Table of Contents
- [Monitoring & Alerting Checklist](#-monitoring--alerting-checklist)
- [Support Runbook & Incident Management](#-support-runbook--incident-management)
- [FinOps & Cost Optimization Guidelines](#-finops--cost-optimization-guidelines)
- [Upstream Reference Assets](#-upstream-reference-assets)

---

## 🔍 Monitoring & Alerting Checklist

To ensure platform health, availability, and capacity optimization, the following monitoring checks must be implemented and reviewed regularly:

| Check Item | Target Metric / Area | Frequency | Tooling / Source Reference |
| :--- | :--- | :--- | :--- |
| **Capacity Utilization** | CU consumption spikes & throttling limits | Real-time / Daily | Fabric Capacity Metrics App |
| **Pipeline Failures** | Data Factory pipeline and trigger execution status | Automated Alert | Fabric Monitor Hub / Azure Monitor |
| **Semantic Model Refreshes**| Power BI semantic model refresh durations & gaps | Daily | Semantic Link Labs (`microsoft/semantic-link-labs`) |
| **Workspace Storage Logs** | OneLake storage growth trends and retention policies | Weekly | Fabric Admin Portal |

---

## 🛠️ Support Runbook & Incident Management

### 1. Level 1 Triage Workflow
1. Identify the alert category via the **Fabric Monitor Hub** (Data Factory / Notebook / Semantic Model failure).
2. Isolate the failure scope: Check if it is a transient Azure service disruption or a localized data engineering issue.
3. Review the job run history and error codes within the Fabric workspace log history.

### 2. Common Remediation Steps
* **Notebook Job Interruption:** Verify if execution failure is due to capacity limits. Use the Fabric Capacity Metrics App to assess if throttling or high CU usage caused the timeout.
* **Semantic Model Refresh Timeout:** Use `semantic-link-labs` utilities to check for underlying data source lockups or model definition corruption.

---

## 💰 FinOps & Cost Optimization Guidelines

To maintain sustainable platform costs, adhere to the following management principles:

* **Capacity Auto-Pause & Scale:** Utilize automated scripting hooks via the `fabric-cli` toolset to dynamically scale or pause capacities during non-production windows.
* **Storage Optimization:** Regularly audit unused or duplicate Lakehouse files using OneLake retention thresholds. Eliminate stale materialized lake views.
* **Workspace Cleanliness:** Implement lifecycle policies to prevent redundant development environments from consuming active operational budgets.

---

## 🔗 Upstream Reference Assets

Operational configurations are aligned with the following standardized reference architectures:
* **Deployment Automation Hooks:** [microsoft/fabric-cli](https://github.com)
* **CI/CD Lifecycle Tracking:** [microsoft/fabric-cicd](https://github.com)
* **Framework Grounding:** [MicrosoftDocs/cloud-adoption-framework](https://github.com)
