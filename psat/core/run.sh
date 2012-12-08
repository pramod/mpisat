#! /bin/bash

for i in `cat benchmarks/sr2008/good.list`
do
    echo "running $i"
    mpirun -np 1 ./minisat -cpu-lim=1200 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat1.out
    mpirun -np 2 ./minisat -cpu-lim=1200 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat2.out
done
