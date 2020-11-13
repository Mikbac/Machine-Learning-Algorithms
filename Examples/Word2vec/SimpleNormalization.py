# -*- coding: utf-8 -*-

# Created by MikBac on 2020

import re
import string


def getNormalization(d):
	d = d.lower()

	try:
		d = d.encode('ascii',errors='ignore').decode('utf-8')
	except:
		d = 'empty'

	d = re.sub(r'[\W_]', ' ', d)
	d = re.sub(r'\d+', '', d)

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

	d = ' '.join(d.split())
	d = d.split()
	return d
