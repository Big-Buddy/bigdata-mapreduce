import sys
import csv

csv_name = sys.argv[1]
with open(csv_name, encoding='utf-8') as f:
	count = 0
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		if row[6]:
			count += 1
print(count)
