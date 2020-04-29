#!/usr/bin/python3

#  Created by MikBac on 2020

import re
import string

from NGram.NGram import getNGramTuples


def getHandmadeNormalization(d, ngram=1):
	d = d.lower()

	d = d.strip()

	d = d.replace('0', ' ').replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ')
	d = d.replace('5', ' ').replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ')

	d = d.replace(' zero ', ' ').replace(' one ', ' ').replace(' two ', ' ').replace(' three ', ' ').replace(' four ',
	                                                                                                         ' ')
	d = d.replace(' five ', ' ').replace(' six ', ' ').replace(' seven ', ' ').replace(' eight ', ' ').replace(' nine ',
	                                                                                                           ' ')

	d = d.replace(' ten ', ' ').replace(' eleven ', ' ').replace(' twelve ', ' ').replace(' thirteen ', ' ').replace(
		' fourteen ', ' ').replace(' fifteen ', ' ')
	d = d.replace(' sixteen ', ' ').replace(' seventeen ', ' ').replace(' eighteen ', ' ').replace(' nineteen ', ' ')

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

	d = d.replace('http', '').replace('https', '').replace('youtube', '')

	d = re.sub('\\\\n', '', d)
	d = re.sub('[\[\(\)\]]', ' ', d)
	d = re.sub('this[\.\:]', 'this ', d)
	d = re.sub('https?://\S*', '', d)
	d = re.sub('[a-zA-Z]\.[a-zA-Z]', ' ', d)

	d = re.sub('   ', ' ', d)
	d = re.sub('  ', ' ', d)

	d = d.translate(str.maketrans('', '', string.punctuation))

	d = d.strip()

	d = ' '.join(d.split())
	d = d.split()

	d = getNGramTuples(d, ngram)

	return d
