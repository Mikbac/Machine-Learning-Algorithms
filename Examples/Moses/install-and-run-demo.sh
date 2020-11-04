#!/bin/bash

#  Created by MikBac on 2020

# http://www.statmt.org/moses/?n=Development.GetStarted
# http://sntllaventhiran.blogspot.com/2016/06/how-to-install-moses-on-ubuntu-1604-x64.html

export HOME=/mnt/c/Users/MikBac/Desktop/Machine-Learning-Algorithms/Examples/Moses && # for WSL2

git clone https://github.com/moses-smt/mosesdecoder.git &&
cd mosesdecoder &&

# sudo apt-get install g++ &&
# sudo apt-get install git &&
# sudo apt-get install subversion &&
# sudo apt-get install automake &&
# sudo apt-get install libtool &&
# sudo apt-get install zlib1g-dev &&
# sudo apt-get install libboost-all-dev &&
# sudo apt-get install libbz2-dev &&
# sudo apt-get install liblzma-dev &&
# sudo apt-get install python-dev &&
# sudo apt-get install graphviz &&
# sudo apt-get install imagemagick &&
# sudo apt-get install make &&
# sudo apt-get install cmake &&
# sudo apt-get install libgoogle-perftools-dev (for tcmalloc) &&

sudo ./bjam -j5 &&  # 4 is threats quantity
# sudo ./bjam --with-boost=~/workspace/temp/boost_1_64_0 -j5 &&

cd .. &&
git clone https://github.com/moses-smt/giza-pp.git &&
cd giza-pp &&
make &&

cd  ./../mosesdecoder &&

mkdir tools &&

cp ./../giza-pp/GIZA++-v2/GIZA++ ./../giza-pp/GIZA++-v2/snt2cooc.out \
 ./../giza-pp/mkcls-v2/mkcls tools &&

cd .. &&

mkdir corpus &&

cd corpus &&

wget http://www.statmt.org/wmt13/training-parallel-nc-v8.tgz &&
tar zxvf training-parallel-nc-v8.tgz &&

cd training &&

head -n 30000 news-commentary-v8.fr-en.en > news-commentary-v8.fr-en-small.en &&
head -n 30000 news-commentary-v8.fr-en.fr > news-commentary-v8.fr-en-small.fr &&

cd ./../.. &&

# normalization
./mosesdecoder/scripts/tokenizer/tokenizer.perl -l en \
    < ./corpus/training/news-commentary-v8.fr-en-small.en    \
    > ./corpus/news-commentary-v8.fr-en.tok.en &&
./mosesdecoder/scripts/tokenizer/tokenizer.perl -l fr \
    < ./corpus/training/news-commentary-v8.fr-en-small.fr    \
    > ./corpus/news-commentary-v8.fr-en.tok.fr &&

./mosesdecoder/scripts/recaser/train-truecaser.perl \
     --model ./corpus/truecase-model.en --corpus     \
     ./corpus/news-commentary-v8.fr-en.tok.en &&
./mosesdecoder/scripts/recaser/train-truecaser.perl \
     --model ./corpus/truecase-model.fr --corpus     \
     ./corpus/news-commentary-v8.fr-en.tok.fr &&

./mosesdecoder/scripts/recaser/truecase.perl \
   --model ./corpus/truecase-model.en         \
   < ./corpus/news-commentary-v8.fr-en.tok.en \
   > ./corpus/news-commentary-v8.fr-en.true.en &&
./mosesdecoder/scripts/recaser/truecase.perl \
   --model ./corpus/truecase-model.fr         \
   < ./corpus/news-commentary-v8.fr-en.tok.fr \
   > ./corpus/news-commentary-v8.fr-en.true.fr &&

./mosesdecoder/scripts/training/clean-corpus-n.perl \
    ./corpus/news-commentary-v8.fr-en.true fr en \
    ./corpus/news-commentary-v8.fr-en.clean 1 80 &&

mkdir lm &&

cd lm &&

./../mosesdecoder/bin/lmplz -o 3 <./../corpus/news-commentary-v8.fr-en.true.en > news-commentary-v8.fr-en.arpa.en &&

./../mosesdecoder/bin/build_binary \
   news-commentary-v8.fr-en.arpa.en \
   news-commentary-v8.fr-en.blm.en &&

echo "is this an English sentence ?" | ./../mosesdecoder/bin/query news-commentary-v8.fr-en.blm.en &&

cd .. &&

mkdir working &&
cd working &&
nohup nice $HOME/mosesdecoder/scripts/training/train-model.perl -root-dir train \
-corpus ./../corpus/news-commentary-v8.fr-en.clean                             \
-f fr -e en -alignment grow-diag-final-and -reordering msd-bidirectional-fe \
-lm 0:3:$HOME/lm/news-commentary-v8.fr-en.blm.en:8 \
-external-bin-dir ./../mosesdecoder/tools >& training.out  \
-cores 5 &&

cd ../corpus &&

wget http://www.statmt.org/wmt12/dev.tgz &&
tar zxvf dev.tgz &&

./../mosesdecoder/scripts/tokenizer/tokenizer.perl -l en \
   < dev/news-test2008.en > news-test2008.tok.en &&
./../mosesdecoder/scripts/tokenizer/tokenizer.perl -l fr \
   < dev/news-test2008.fr > news-test2008.tok.fr &&
./../mosesdecoder/scripts/recaser/truecase.perl --model truecase-model.en \
   < news-test2008.tok.en > news-test2008.true.en &&
./../mosesdecoder/scripts/recaser/truecase.perl --model truecase-model.fr \
   < news-test2008.tok.fr > news-test2008.true.fr &&

cd ./../working &&
nohup nice $HOME/mosesdecoder/scripts/training/mert-moses.pl \
$HOME/corpus/news-test2008.true.fr $HOME/corpus/news-test2008.true.en \
$HOME/mosesdecoder/bin/moses train/model/moses.ini --mertdir $HOME/mosesdecoder/bin/ \
&> mert.out --decoder-flags="-threads 4" --maximum-iterations=5 &&

#./../mosesdecoder/bin/moses -f ./mert-work/moses.ini &&

cd ./../corpus &&
./../mosesdecoder/scripts/tokenizer/tokenizer.perl -l en \
  < dev/newstest2011.en > newstest2011.tok.en &&
./../mosesdecoder/scripts/tokenizer/tokenizer.perl -l fr \
  < dev/newstest2011.fr > newstest2011.tok.fr &&
./../mosesdecoder/scripts/recaser/truecase.perl --model truecase-model.en \
  < newstest2011.tok.en > newstest2011.true.en &&
./../mosesdecoder/scripts/recaser/truecase.perl --model truecase-model.fr \
  < newstest2011.tok.fr > newstest2011.true.fr &&

cd ./../working &&
./../mosesdecoder/scripts/training/filter-model-given-input.pl             \
   filtered-newstest2011 mert-work/moses.ini ./../corpus/newstest2011.true.fr   &&

nohup nice $HOME/mosesdecoder/bin/moses            \
   -f $HOME/working/filtered-newstest2011/moses.ini   \
   < $HOME/corpus/newstest2011.true.fr                \
   > $HOME/working/newstest2011.translated.en         \
   2> $HOME/working/newstest2011.out &&

$HOME/mosesdecoder/scripts/generic/multi-bleu.perl \
   -lc $HOME/corpus/newstest2011.true.en              \
   < $HOME/working/newstest2011.translated.en