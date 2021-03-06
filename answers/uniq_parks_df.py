import sys
from pyspark.sql import SparkSession
from pyspark.sql import Row

file_name = sys.argv[1]

spark = SparkSession.builder.master("local").appName("lab1").getOrCreate()

df = spark.read.csv(file_name, header = True)

df = df.filter(df['Nom_parc'] != '')

df = df.orderBy(['Nom_parc'], ascending = True)

df = df.select('Nom_parc')

df = df.distinct()

for row in df.collect():
	print(row['Nom_parc'])