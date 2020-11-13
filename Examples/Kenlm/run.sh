#!/bin/bash

#  Created by MikBac on 2020

# Installing
git clone https://github.com/kpu/kenlm.git && cd kenlm && mkdir -p build && cd build && cmake .. && make -j 4 && cd ../..
pip3 install https://github.com/kpu/kenlm/archive/master.zip

paste ./train/expected.tsv ./train/in.tsv | python3 clean.py > ./train/data.tsv

./kenlm/build/bin/lmplz -o 3 < ./train/data.tsv > ./train/dataIn.arpa

python3 ./predictDemo.py

cat ./test/in.tsv | python3 predict.py > ./test/out.tsv

./geval --test-name dev-0
