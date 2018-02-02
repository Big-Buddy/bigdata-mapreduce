import sys
from pyspark.sql import SparkSession

file_name = sys.argv[1]

spark = SparkSession.builder.master("local").appName("lab1").getOrCreate()

df = spark.read.csv(file_name, header = True)

df = df.filter(df['Nom_parc'] != '')

df = df.orderBy(['Nom_parc'], ascending = True)

df = df.groupBy('Nom_parc')

df = df.select('Nom_parc')

for row in df.collect():
	print(row)