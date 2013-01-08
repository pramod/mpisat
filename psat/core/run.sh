#! /bin/bash

cnt=0
# for i in `cat benchmarks/sr2008/big.list`
for i in `cat benchmarks/sr2008/good.list`
do
    echo "running $i [count=$cnt]"
    let "cnt=cnt+1"
    for n in 4 8 12;
    do
        for j in 16 256 1024;
        do
            mpirun -np $n ./minisat -cpu-lim=1200 -share-act-vars=$j -freq-th=2 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv3.n$n.sav.$j.f2
            mpirun -np $n ./minisat -cpu-lim=1200 -share-act-vars=$j -freq-th=3 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv3.n$n.sav.$j.f3
            mpirun -np $n ./minisat -cpu-lim=1200 -share-act-vars=$j -freq-th=4 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv3.n$n.sav.$j.f4
        done
    done
done
