import sys
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import lit

file_name = sys.argv[1]

spark = SparkSession.builder.master("local").appName("lab1").getOrCreate()

df = spark.read.csv(file_name, header = True)

df = df.filter(df['Nom_parc'] != '')

df = df.withColumn('num_of_trees', lit(1))

df = df.orderBy(['Nom_parc'], ascending = True)

df = df.groupBy('Nom_parc').agg()

for row in df.collect():
	print(row['Nom_parc'] + ": " + str(row['num_of_trees']))