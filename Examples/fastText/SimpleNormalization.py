#!/usr/bin/python

#  Created by MikBac on 2020

import re

def getNormalization(d):
	d = d.lower()
	d = d.strip()

	d = d.replace(':', ' ').replace('\'', ' ').replace('^', ' ').replace('.', ' ').replace('*', ' ').replace('\"', ' ')
	d = d.replace(' \' ', ' ').replace('\r', ' ').replace('\s', ' ').replace('\t', ' ').replace('\n', ' ').replace(
		'\\n', ' ')
	d = d.replace('`', ' ').replace('~', ' ').replace('!', ' ').replace('@', ' ').replace('#', ' ').replace('$',
	                                                                                                        ' ').replace(
		'%', ' ').replace('^', ' ').replace('&', ' ')
	d = d.replace('*', ' ').replace('-', ' ').replace('_', ' ').replace('+', ' ').replace('=', ' ').replace(';',
	                                                                                                        ' ').replace(
		'"', ' ').replace('|', ' ')
	d = d.replace('\\', ' ').replace(',', ' ').replace('.', ' ').replace('/', ' ').replace('?', ' ').replace('|', ' ')
	d = d.replace('{', ' ').replace('}', ' ').replace('[', ' ').replace(']', ' ').replace('(', ' ').replace(')',
	                                                                                                        ' ').replace(
		'<', ' ').replace('>', ' ')

	d = re.sub('   ', ' ', d)
	d = re.sub('   ', ' ', d)

	return d
