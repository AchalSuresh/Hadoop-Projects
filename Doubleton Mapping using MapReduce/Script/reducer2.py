#!/usr/bin/env python

import sys

numdict = {}
 
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input from mapper.py
	key1, key2, count = line.split(',', 2)


	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, ignore
		continue
    #Add the keys to a tuple forming doubleton  
	num = (key1,key2)
    #Adding the tuple pair to a dictionary and adding the values
	try:
		numdict[num] = numdict[num] + count
	except:
		numdict[num] = count

for num in numdict.keys():
    #Selecting only doubletons that appear atleast twice
	if numdict.get(num) >=2:
		print('(%s,%s) \n' % (num,numdict[num]))
