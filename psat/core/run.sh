#! /bin/bash

for i in `cat benchmarks/sr2008/good.list`
do
    echo "running $i/2"
    mpirun -np 2 ./minisat -cpu-lim=1200 -rfirst=50 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat_stats_2_r50.out
    mpirun -np 2 ./minisat -cpu-lim=1200 -rfirst=100 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat_stats_2_r100.out
    echo "running $i/4"
    mpirun -np 4 ./minisat -cpu-lim=1200 -rfirst=50 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat_stats_4_r50.out
    mpirun -np 4 ./minisat -cpu-lim=1200 -rfirst=100 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat_stats_4_r100.out
    echo "running $i/8"
    mpirun -np 8 ./minisat -cpu-lim=1200 -rfirst=50 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat_stats_8_r50.out
    mpirun -np 8 ./minisat -cpu-lim=1200 -rfirst=100 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat_stats_8_r100.out
done
