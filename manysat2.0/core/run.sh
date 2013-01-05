#! /bin/bash

for i in `cat benchmarks/sr2008/good.list`
do
    echo "running $i"
    for c in 1 2 4 8 16;
    do
        echo ./manysat2.0 -cpu-lim=1200 -ncores=$c benchmarks/sr2008/$i benchmarks/sr2008/$i.manysat_r2_$c.out
    done
done
