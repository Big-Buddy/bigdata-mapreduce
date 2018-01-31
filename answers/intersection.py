import sys
import csv

csv_1 = sys.argv[1]
csv_2 = sys.argv[2]

with open(csv_1, encoding='utf-8') as f:
	unique_parks_1 = []
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		if row[6] and row[6] not in unique_parks_1:
			unique_parks_1.append(row[6])

intersection = []

with open(csv_2, encoding='utf-8') as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		if row[6] and row[6] in unique_parks_1 and row[6] not in intersection:
			intersection.append(row[6])

intersection.sort()
for row in intersection:
	print(row)