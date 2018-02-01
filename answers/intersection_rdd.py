import sys
import csv
from pyspark import SparkContext, SparkConf

csv_1 = sys.argv[1]
csv_2 = sys.argv[2]

conf = SparkConf().setAppName("lab1").setMaster("local")
sc = SparkContext(conf=conf)

rdd_1 = sc.textFile(csv_1)
rdd_1 = rdd_1.mapPartitions(lambda x: csv.reader(x))
header_1 = rdd_1.first()
rdd_1 = rdd_1.filter(lambda x: x != header_1)
rdd_1 = rdd_1.filter(lambda x: x[6] != '')
rdd_1 = rdd_1.map(lambda x: x[6])
rdd_1 = rdd_1.distinct()

rdd_2 = sc.textFile(csv_2)
rdd_2 = rdd_2.mapPartitions(lambda x: csv.reader(x))
header_2 = rdd_2.first()
rdd_2 = rdd_2.filter(lambda x: x != header_2)
rdd_2 = rdd_2.filter(lambda x: x[6] != '')
rdd_2 = rdd_2.map(lambda x: x[6])
rdd_2 = rdd_2.distinct()

intersection_rdd = rdd_1.intersection(rdd_2)

