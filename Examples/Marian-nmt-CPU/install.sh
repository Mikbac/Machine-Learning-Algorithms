#!/bin/bash

#  Created by MikBac on 2020

git clone https://github.com/marian-nmt/marian &&
mkdir marian/build &&
cd marian/build &&
cmake .. -DCOMPILE_CPU=on -DCOMPILE_CUDA=off &&
make -j4 &&
cd ../../
