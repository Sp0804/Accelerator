#!/usr/bin/env python3
"""Resolve environment placeholders in Fabric artifact files from config/env.json.
Run this script BEFORE committing/syncing the generated Fabric artifacts to the connected workspace.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = ROOT / "config" / "env.json"


def required(obj, path):
    cur = obj
    for key in path.split('.'):
        cur = cur[key]
    if cur in (None, ""):
        raise ValueError(f"Missing required value: {path} in {ENV_FILE}")
    return cur


env = json.loads(ENV_FILE.read_text(encoding="utf-8"))
workspace = required(env, "fabric.workspaceId")
bronze = required(env, "lakehouses.bronze.id")
silver = required(env, "lakehouses.silver.id")
azure_sql_conn = required(env, "connections.azureSql")
control_conn = required(env, "connections.controlDb")
source_db = required(env, "databases.source")
control_db = required(env, "databases.control")

replacements = {
    "__WORKSPACE_ID__": workspace,
    "__BRONZE_LAKEHOUSE_ID__": bronze,
    "__SILVER_LAKEHOUSE_ID__": silver,
    "__AZURE_SQL_CONNECTION_ID__": azure_sql_conn,
    "__CONTROL_DB_CONNECTION_ID__": control_conn,
    "__SOURCE_DB_NAME__": source_db,
    "__CONTROL_DB_NAME__": control_db,
}

files = [
    ROOT / "platform/ingestion/azure-sql/Master ELT ASQL.DataPipeline/pipeline-content.json",
    ROOT / "platform/ingestion/azure-sql/Ingest ASQL Table.DataPipeline/pipeline-content.json",
    ROOT / "silver/pipelines/level1-transform/Level1 Transform.DataPipeline/pipeline-content.json",
    ROOT / "silver/pipelines/level1-transform/Master Level1 Transform.DataPipeline/pipeline-content.json",
    ROOT / "silver/notebooks/L1Transform-Generic-Fabric.Notebook/notebook-content.py",
    ROOT / "silver/notebooks/delta-lake/Optimize Delta Lake Tables.Notebook/notebook-content.py",
]

for path in files:
    text = path.read_text(encoding="utf-8")
    for token, value in replacements.items():
        text = text.replace(token, value)
    path.write_text(text, encoding="utf-8")
    print(f"Configured: {path.relative_to(ROOT)}")

print("Environment values applied successfully. Validate the generated artifacts before Git sync.")
