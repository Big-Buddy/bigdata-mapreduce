import sys
from pyspark.sql import SparkSession

file_name = sys.argv[1]

spark = SparkSession.builder.master("local").appName("lab1").getOrCreate()

df = spark.read.csv(file_name, header = True)

df = df.groupBy('Nom_parc').orderBy(['Nom_parc'], ascending = True)

df.select('Nom_parc').show()
