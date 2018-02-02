import sys
from pyspark.sql import SparkSession
from pyspark.sql import Row

csv_1 = sys.argv[1]
csv_2 = sys.argv[2]

spark = SparkSession.builder.master("local").appName("lab1").getOrCreate()

df_1 = spark.read.csv(csv_1, header = True)
df_1 = df_1.filter(df_1['Nom_parc'] != '')
df_1 = df_1.distinct()

df_2 = spark.read.csv(csv_2, header = True)
df_2 = df_2.filter(df_2['Nom_parc'] != '')
df_2 = df_2.distinct()

df_intersect = df_1.intersect(df_2)
df_intersect = df_intersect.orderBy(['Nom_parc'], ascending = True)

for row in df_intersect.collect():
	print(row['Nom_parc'])