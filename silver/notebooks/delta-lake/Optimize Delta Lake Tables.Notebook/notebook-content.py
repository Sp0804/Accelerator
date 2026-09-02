# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "__SILVER_LAKEHOUSE_ID__",
# META       "default_lakehouse_name": "lh_silver",
# META       "default_lakehouse_workspace_id": "__WORKSPACE_ID__"
# META     }
# META   }
# META }

# MARKDOWN ********************

# ### Spark Optimization Configs

# CELL ********************

# Environment values are resolved by devops/configure-env.py before Git sync.
bronzeWorkspaceId = "__WORKSPACE_ID__"
silverWorkspaceId = "__WORKSPACE_ID__"
goldWorkspaceId = "__WORKSPACE_ID__"
bronzeLakehouseName = "lh_bronze"
silverLakehouseName = "lh_silver"
goldLakehouseName = "lh_gold"

spark.conf.set("spark.native.enabled", "true")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run /DeltaLakeFunctions

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Iterate through all tables in lakehouse and run OPTIMIZE and VACCUM commands

# CELL ********************

df = spark.sql("show tables")
tableList = df.select("tableName").rdd.flatMap(lambda x:x).collect()
# print (tables)
for table in tableList:
    print ("optimizing",table)
    optimizeDelta(table)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
