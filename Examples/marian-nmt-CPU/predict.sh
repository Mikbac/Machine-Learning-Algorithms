# echo "Musimy powiedzieć nie" | ./marian/build/marian-decoder -m model.npz
# echo "Musimy powiedzieć NIE," | ./marian/build/marian-decoder -m model.npz -v vocab.pl.yml vocab.en.yml --cpu-threads 3 --beam-size 1 --n-best
# echo "Musimy powiedzieć nie" | ./marian/build/marian-decoder -m model.npz --cpu-threads 3

cat ./in.tsv | ./marian/build/marian-decoder \
  -m model.npz \
  -v vocab.pl.yml vocab.en.yml \
  --cpu-threads 3 \
  --beam-size 1 \
  --n-best >./product.tsv &&
  cat ./product.tsv | python3 filter.py >./out.tsv
