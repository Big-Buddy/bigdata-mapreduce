import sys

file_name = sys.argv[1]
with open(file_name, encoding = 'utf-8') as f:
	f.readline()
	line = f.readline()
	count = 0
	while line:
		line = f.readline()
		count += 1
print(count)
