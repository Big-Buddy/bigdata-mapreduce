import sys
import csv

csv_name = sys.argv[1]
with open(csv_name, encoding='utf-8') as f:
	unique_parks_counts = []
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		if not unique_parks_counts and row[6]:
			unique_parks_counts.append((row[6], 1))

		if row[6] and unique_parks_counts:		
			flag = False		
		
			for unique_tuple in unique_parks_counts:
				if row[6] in unique_tuple:	
					flag = true
					ptr = unique_parks_counts.index(unique_tuple)			
					
			if flag:
				unique_parks_counts[ptr] = (unique_parks_counts[ptr][0], unique_parks_counts[ptr][1]+1)
			else:
				unique_parks_counts.append((row[6], 1))
				
unique_parks_counts.sort()
for row in unique_parks_counts:
	print(row[0] + ": " + row[1])