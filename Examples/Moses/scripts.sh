#!/bin/bash

#  Created by MikBac on 2020

#wget https://gonito.net/get/bin/geval &&
#chmod u+x geval &&

export HOME=/mnt/c/Users/MikBac/Desktop/Machine-Learning-Algorithms/Examples/Moses && # for WSL2

xzcat ./train/in.tsv.xz > ./train/in.tsv &&
xzcat ./train/expected.tsv.xz > ./train/expected.tsv &&

head -n 30000 ./train/expected.tsv > ./train/expected-small.tsv &&
head -n 30000 ./train/in.tsv > ./train/in-small.tsv &&

./mosesdecoder/scripts/tokenizer/tokenizer.perl -l en \
    < ./train/expected-small.tsv    \
    > ./corpus/expected-tok-en.tsv &&
./mosesdecoder/scripts/tokenizer/tokenizer.perl -l pl \
    < ./train/in-small.tsv    \
    > ./corpus/in-tok-pl.tsv &&

#./mosesdecoder/scripts/tokenizer/tokenizer.perl -l en \
#    < ./train/expected.tsv    \
#    > ./corpus/expected-tok-en.tsv &&
#./mosesdecoder/scripts/tokenizer/tokenizer.perl -l pl \
#    < ./train/in.tsv    \
#    > ./corpus/in-tok-pl.tsv &&

./mosesdecoder/scripts/recaser/train-truecaser.perl \
     --model ./corpus/truecase-model.en --corpus     \
     ./corpus/expected-tok-en.tsv &&
./mosesdecoder/scripts/recaser/train-truecaser.perl \
     --model ./corpus/truecase-model.pl --corpus     \
     ./corpus/in-tok-pl.tsv &&

./mosesdecoder/scripts/recaser/truecase.perl \
   --model ./corpus/truecase-model.en         \
   < ./corpus/expected-tok-en.tsv \
   > ./corpus/data-pl-en-true.en &&
./mosesdecoder/scripts/recaser/truecase.perl \
   --model ./corpus/truecase-model.pl         \
   < ./corpus/in-tok-pl.tsv \
   > ./corpus/data-pl-en-true.pl &&

./mosesdecoder/scripts/training/clean-corpus-n.perl \
    ./corpus/data-pl-en-true pl en \
    ./corpus/data-pl-en-clean 1 80 &&

#mkdir lm &&
cd lm &&
./../mosesdecoder/bin/lmplz -o 3 <./../corpus/data-pl-en-true.en > data-pl-en-arpa.en &&

./../mosesdecoder/bin/build_binary \
   data-pl-en-arpa.en \
   data-pl-en-blm.en &&

#echo "is this an English sentence ?" | ./../mosesdecoder/bin/query data-pl-en-blm.en &&

cd .. &&

#mkdir working &&
cd working &&

nohup nice $HOME/mosesdecoder/scripts/training/train-model.perl -root-dir train \
-corpus ./../corpus/data-pl-en-clean                             \
-f pl -e en -alignment grow-diag-final-and -reordering msd-bidirectional-fe \
-lm 0:3:$HOME/lm/data-pl-en-blm.en:8 \
-external-bin-dir ./../mosesdecoder/tools >& training.out  \
-max-phrase-length 20 \
-cores 5 &&

cd ../corpus &&

./../mosesdecoder/scripts/tokenizer/tokenizer.perl -l en \
   < ./../dev-0/expected.tsv > data-test-tok-pl-en.en &&
./../mosesdecoder/scripts/tokenizer/tokenizer.perl -l pl \
   < ./../dev-0/in.tsv > data-test-tok-pl-en.pl &&

./../mosesdecoder/scripts/recaser/truecase.perl --model truecase-model.en \
   < data-test-tok-pl-en.en > data-test-true-pl-en.en &&
./../mosesdecoder/scripts/recaser/truecase.perl --model truecase-model.pl \
   < data-test-tok-pl-en.pl > data-test-true-pl-en.pl &&

cd ./../working &&

nohup nice $HOME/mosesdecoder/scripts/training/mert-moses.pl \
$HOME/corpus/data-test-true-pl-en.pl $HOME/corpus/data-test-true-pl-en.en \
$HOME/mosesdecoder/bin/moses train/model/moses.ini --mertdir $HOME/mosesdecoder/bin/ \
&> mert.out --decoder-flags="-threads 4" \
--maximum-iterations=25 &&

#./../mosesdecoder/bin/moses -f ./mert-work/moses.ini &&

cd ./../corpus &&

./../mosesdecoder/scripts/tokenizer/tokenizer.perl -l pl \
  < ./../test-A/in.tsv > in-tok-test-A-pl.tsv &&

./../mosesdecoder/scripts/recaser/truecase.perl --model truecase-model.pl \
  < in-tok-test-A-pl.tsv > in-true-test-A-pl.tsv &&

cd ./../working &&

./../mosesdecoder/scripts/training/filter-model-given-input.pl             \
   filtered-test-A mert-work/moses.ini ./../corpus/in-true-test-A-pl.tsv   &&

nohup nice $HOME/mosesdecoder/bin/moses            \
   -f $HOME/working/filtered-test-A/moses.ini   \
   < $HOME/corpus/in-true-test-A-pl.tsv             \
   > $HOME/test-A/simple.tsv        \
   2> $HOME/working/test-A-2.out &&

nohup nice $HOME/mosesdecoder/bin/moses            \
   -f $HOME/working/filtered-test-A/moses.ini   \
   < $HOME/corpus/data-test-true-pl-en.pl            \
   > $HOME/dev-0/simple.tsv        \
   2> $HOME/working/test-dev-0.out &&

cd .. &&

$HOME/mosesdecoder/scripts/recaser/detruecase.perl  \
  < $HOME/dev-0/simple.tsv \
  > $HOME/dev-0/detruecase.tsv &&

$HOME/mosesdecoder/scripts/tokenizer/detokenizer.perl  -l en \
  < $HOME/dev-0/detruecase.tsv \
  > $HOME/dev-0/out.tsv &&

$HOME/mosesdecoder/scripts/recaser/detruecase.perl  \
  < $HOME/test-A/simple.tsv \
  > $HOME/test-A/detruecase.tsv &&

$HOME/mosesdecoder/scripts/tokenizer/detokenizer.perl  -l en \
  < $HOME/test-A/detruecase.tsv \
  > $HOME/test-A/out.tsv &&

./geval --test-name dev-0