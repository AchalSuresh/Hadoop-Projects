#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words=line.split(' ')
	# Iterating each line
	for i in range(len(words)):
		# Iterating through the lines and forming pairs
		j=i+1
		while(j<len(words)):
			print('%s,%s,%s' % (words[i], words[j], 1))
			j+=1
			