#! /bin/bash

for i in `cat benchmarks/sr2008/good.list`
do
    echo "running $i"
    for j in 8 16 32 64
    do
        mpirun -np 2 ./minisat -cpu-lim=1200 -max-share-size=$j benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat2_mcs$j.out
        mpirun -np 4 ./minisat -cpu-lim=1200 -max-share-size=$j benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat4_mcs$j.out
        mpirun -np 8 ./minisat -cpu-lim=1200 -max-share-size=$j benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psat8_mcs$j.out
    done
done
