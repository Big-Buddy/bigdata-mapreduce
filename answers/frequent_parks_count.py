import sys
import csv
from operator import itemgetter

csv_name = sys.argv[1]
with open(csv_name, encoding='utf-8') as f:
	most_frequent = []
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		if not most_frequent and row[6]:
			most_frequent.append((row[6], 1))

		if row[6] and most_frequent:		
			flag = False		
		
			for unique_tuple in most_frequent:
				if row[6] in unique_tuple:	
					flag = True
					ptr = most_frequent.index(unique_tuple)			
					
			if flag:
				most_frequent[ptr] = (most_frequent[ptr][0], most_frequent[ptr][1]+1)
			else:
				most_frequent.append((row[6], 1))

most_frequent.sort(key = itemgetter(1), reverse = True)


for row in most_frequent[0:10]:
	print(row[0] + ": " + str(row[1]))