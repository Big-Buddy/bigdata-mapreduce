import sys
import csv

csv_name = sys.argv[1]
with open(csv_name) as f:
	count = 0
	reader = csv.reader(f)
	for row in reader:
		if row[6]:
			print(row[6])
			count += 1
print(count)
