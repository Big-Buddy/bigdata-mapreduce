import sys
import csv
from operator import itemgetter

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
					flag = True
					ptr = unique_parks_counts.index(unique_tuple)			
					
			if flag:
				unique_parks_counts[ptr] = (unique_parks_counts[ptr][0], unique_parks_counts[ptr][1]+1)
			else:
				unique_parks_counts.append((row[6], 1))

most_frequent = []
for row in unique_parks_counts:
	if not most_frequent:
		most_frequent.append(row)
	
	if len(most_frequent) == 10:
		if row[1] > min(most_frequent, key = itemgetter(1))[1]:
			del most_frequent[most_frequent.index(min(most_frequent))]
			most_frequent.append(row)
	else:
		most_frequent.append(row)

most_frequent.sort(key = itemgetter(1), reverse = True)

for row in most_frequent:
	print(row[0] + ": " + str(row[1]))