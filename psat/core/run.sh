#! /bin/bash

for i in `cat benchmarks/sr2008/good.list`
do
    echo "running $i/2"
    mpirun -np 2 ./minisat -cpu-lim=1200 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat_stats_2.out
    echo "running $i/4"
    mpirun -np 4 ./minisat -cpu-lim=1200 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat_stats_4.out
    echo "running $i/8"
    mpirun -np 8 ./minisat -cpu-lim=1200 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat_stats_8.out
done
