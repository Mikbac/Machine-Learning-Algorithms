xzcat expected.tsv.xz | head -n 300 >expected.tsv &&
  xzcat in.tsv.xz | head -n 300 >in.tsv &&

  #./marian/build/marian \
  #    --train-sets ./../train/train.tsv ./../train/expected.tsv \
  #    --model model.npz

  #    ./marian/build/marian \
  #    --after-epochs 4 \
  #    --cpu-threads 7 \
  #    --train-sets ./../dev-0/in.tsv ./../dev-0/expected.tsv \
  #    --model model.npz

  #    ./marian/build/marian \
  #    --after-epochs 4 \
  #    --cpu-threads 4 \
  #    --normalize 1 \
  #    --train-sets ./../dev-0/in.tsv ./../dev-0/expected.tsv \
  #    --vocabs vocab.pl.yml vocab.en.yml \
  #    --model model.npz
  ./marian/build/marian \
    --after-epochs 1 \
    --cpu-threads 4 \
    --normalize 1 \
    --train-sets ./in.tsv ./expected.tsv \
    --vocabs vocab.pl.yml vocab.en.yml \
    --model model.npz
