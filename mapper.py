#!/usr/bin/env python
import sys
import string
from nltk.corpus import stopwords
 
stops = set(stopwords.words('english'))
# get all lines from stdin
for line in sys.stdin:	
    # remove leading and trailing whitespace
	line = line.strip().lower()

# remove puntuation
	line = line.translate(None, string.punctuation)

    # split the line into words; splits on any whitespace
	words = line.split()

    # output tuples (word, 1) in tab-delimited format
	for word in words:
		if word not in stops:
			print '%s\t%s' % (word, "1")
