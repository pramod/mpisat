#! /bin/bash

cnt=0
# for i in `cat benchmarks/sr2008/big.list`
for i in `cat benchmarks/sr2008/good.list`
do
    echo "running $i [count=$cnt]"
    let "cnt=cnt+1"
    for n in 2 4 8;
    do
            mpirun -np $n ./minisat -cpu-lim=1200 -heap-depth=$n benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv4.n$n.noflip
            mpirun -np $n ./minisat -cpu-lim=1200 -heap-depth=$n -flip-sign benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv4.n$n.flip
    done
done
