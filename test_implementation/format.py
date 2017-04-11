def just_webaddress(x):
	start = x.find('//') + 2
	end = x.find('/', start)
	return x[start:end]

import csv
even =  open('beta.csv', 'r')

with open('alpha.csv',"r") as f:
	reader = csv.reader(f,delimiter = ",")
	data = list(reader)
	row_count = len(data)

with open('alpha.csv', 'r') as odd:
	odd_reader = csv.reader(odd)
	even_reader  = csv.reader(even)

	f = open('result.csv','w')

	for x in range(0,row_count):
		m = str(next(odd_reader)[4])
		n = str(next(even_reader)[4])
		f.write( just_webaddress(m) + "," + just_webaddress(n) )
		f.write("\n")
	f.close()
	
