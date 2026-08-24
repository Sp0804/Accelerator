# Solution Design Document (SDD) & Architectural Overview

This directory contains the central engineering documentation, architecture designs, and onboarding instructions for the Microsoft Fabric implementation platform.

## 🏛️ Architecture Blueprint
The platform follows a standardized Medallion Architecture pattern built on Microsoft Fabric OneLake:
1. **Bronze Layer:** Raw data landing, retention, and schema ingestion.
2. **Silver Layer:** PySpark transformation, cleansing, and deduplication.
3. **Gold Layer:** Curated dimensional star-schemas optimized for reporting.

## 🚀 Deployment & Configuration Overview
Platform provisioning and CI/CD promotion utilize a programmatic approach:
* **Source Control:** Git integration handles workspace synchronization across environments.
* **CLI Engine:** Deployment orchestrations rely on standard automation scripting via the `fabric-cli` toolset.
* **Artifact Delivery:** Asset lifecycles follow defined deployment pipeline boundaries.

## 📁 Repository Map
* `/platform` - Core Landing Zone environment parameters and workspace setups.
* `/bronze`, `/silver`, `/gold` - Medallion layer processing configurations and notebooks.
* `/devops` - Git branching mechanics, release manifests, and checklist patterns.
* `/governance` & `/operations` - Access matrices, active guardrails, and L1 runbooks.
