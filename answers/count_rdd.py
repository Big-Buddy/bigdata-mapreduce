import sys
import csv
from pyspark import SparkContext, SparkConf

file_name = sys.argv[1]

conf = SparkConf().setAppName("lab1").setMaster(master)
sc = SparkContext(conf=conf)

rdd = sc.textFile(file_name)
rdd = rdd.mapParitions(lambda x: csv.reader(x))
header = rdd.first()
rdd = rdd.filter(lambda x: x != header)

print(rdd.count())
