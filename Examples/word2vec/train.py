# -*- coding: utf-8 -*-

#  Created by MikBac on 2020

from gensim import models
import logging
logging.basicConfig(level=logging.INFO)

def main():
	if models.word2vec.FAST_VERSION > -1:
		print('multicore version works')
		sentences = models.word2vec.LineSentence('./data/preprocessed_data.tsv')
		model = models.word2vec.Word2Vec(sentences, min_count=1, workers=8, iter=2)
		model.save('./data/model.bin')
		model.wv.save_word2vec_format('./data/model.tsv')
	else:
		print('multicore version does not work')


if __name__ == '__main__':
	main()
