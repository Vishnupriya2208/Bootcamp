# Databricks notebook source
print ("hello world")

# COMMAND ----------

# DBTITLE 1,all
import pandas as pd
from pyspark.sql import SparkSession


cell_phones_path =import pandas as pd
from pyspark.sql import SparkSession


cell_phones_path = dbfs:/FileStore/shared_uploads/vishnupriya.r.ad.2022@snsce.ac.in/rise_of_cell_phones_vishnu_final-1.xlsx


df_cell_phones = pd.read_excel(cell_phones_path, engine='openpyxl')
df_population = pd.read_excel(population_path, engine='openpyxl')


spark = SparkSession.builder.getOrCreate()
df_cell_phones_spark = spark.createDataFrame(df_cell_phones)
df_population_spark = spark.createDataFrame(df_population)


df_cell_phones_spark.show(5)
df_population_spark.show(5)
]


df_cell_phones = pd.read_excel(cell_phones_path, engine='openpyxl')
df_population = pd.read_excel(population_path, engine='openpyxl')


spark = SparkSession.builder.getOrCreate()
df_cell_phones_spark = spark.createDataFrame(df_cell_phones)
df_population_spark = spark.createDataFrame(df_population)


df_cell_phones_spark.show(5)
df_population_spark.show(5)
]

# COMMAND ----------

pip install pandas


# COMMAND ----------

import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Year": [2000, 2005, 2010, 2015, 2020],
    "Total Cell Phones": [500000000, 2000000000, 4500000000, 7000000000, 8500000000],
    "Population": [6000000000, 6500000000, 7000000000, 7500000000, 7800000000],
}
df = pd.DataFrame(data)
df["Cell Phones per Person"] = df["Total Cell Phones"] / df["Population"]
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Total Cell Phones"], marker='o', label="Total Cell Phones", color='blue')
plt.plot(df["Year"], df["Cell Phones per Person"], marker='s', label="Cell Phones per Person", color='red')
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Rise of Cell Phones & Cell Phones Per Person Over Time")
plt.legend()
plt.grid(True)
plt.show()
