import sys
import csv
from pyspark import SparkContext, SparkConf

file_name = sys.argv[1]

conf = SparkConf().setAppName("lab1").setMaster("local")
sc = SparkContext(conf=conf)

rdd = sc.textFile(file_name)
rdd = rdd.mapPartitions(lambda x: csv.reader(x))
header = rdd.first()
rdd = rdd.filter(lambda x: x != header)

rdd = rdd.filter(lambda x: x[6] != '')
rdd = rdd.map(lambda x: (x[6], 1))
rdd = rdd.reduceByKey(lambda a, b: a+b)
rdd = rdd.sortBy(False, lambda x: x[1])

for row in rdd.take(10):
	print(row[0] + ": " + str(row[1]))