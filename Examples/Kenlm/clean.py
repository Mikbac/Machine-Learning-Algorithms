#!/usr/bin/env python

#  Created by MikBac on 2020

import sys

for line in sys.stdin:
	line = line.strip()
	fields = line.split('\t')
	if len(fields) == 1:
		print(fields[0])
