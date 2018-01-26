import sys
import csv

csv_name = sys.argv[1]
with open(csv_name, encoding='utf-8') as f:
	unique_parks = []
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		if row[6] not in unique_parks:
			unique_parks.append(row[6])
unique_parks.sort()
print(unique_parks)