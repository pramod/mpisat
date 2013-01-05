#! /bin/bash

cnt=0
# for i in `cat benchmarks/sr2008/big.list`
for i in `cat benchmarks/sr2008/good.list`
do
    echo "running $i [count=$cnt]"
    let "cnt=cnt+1"
    for n in 4 8 12;
    do
        mpirun -np $n ./minisat -cpu-lim=1200 -activity-ff=1     benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv3.n$n.aff1
        mpirun -np $n ./minisat -cpu-lim=1200 -activity-ff=0.999 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv3.n$n.aff999
        mpirun -np $n ./minisat -cpu-lim=1200 -activity-ff=0.99  benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv3.n$n.aff99
        mpirun -np $n ./minisat -cpu-lim=1200 -activity-ff=0.95  benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv3.n$n.aff95
        mpirun -np $n ./minisat -cpu-lim=1200 -activity-ff=0.9   benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv3.n$n.aff9
    done
done
