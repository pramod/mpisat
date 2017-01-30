#! /bin/bash

cnt=0
# for i in `cat benchmarks/sr2008/big.list`
for i in `cat benchmarks/sr2008/good.list`
do
    echo "running $i [count=$cnt]"
    let "cnt=cnt+1"
    for n in 4 8 12;
    do
            mpirun -np $n ./minisat -cpu-lim=1200 -heap-depth=$n benchmarks/sr2008/$i >& benchmarks/sr2008/no_iprobe/$i.psatv4.n$.no_iprobe
            # mpirun -np $n ./minisat -cpu-lim=1200 -heap-depth=$n -flip-sign benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv4.n$n.flip
    done
done
