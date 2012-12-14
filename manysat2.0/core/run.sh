#! /bin/bash

for i in `cat benchmarks/sr2008/good.list`
do
    echo "running $i"
    ./manysat2.0 -cpu-lim=1200 -ncores=1 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.manysat1.out
    ./manysat2.0 -cpu-lim=1200 -ncores=2 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.manysat2.out
    ./manysat2.0 -cpu-lim=1200 -ncores=4 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.manysat4.out
    ./manysat2.0 -cpu-lim=1200 -ncores=8 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.manysat8.out
done
