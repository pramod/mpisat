#! /bin/bash

cnt=0
# for i in `cat benchmarks/sr2008/big.list`
for i in `cat benchmarks/sr2008/good.list`
do
    echo "running $i [count=$cnt]"
    let "cnt=cnt+1"
    for n in 8 16 24;
    do
        mpirun -np $n ./minisat -cpu-lim=1200 -max-share-size=8 -cluster-size=4 -max-shareout-size=2 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv2.n$n.cl8_4_2.out
        mpirun -np $n ./minisat -cpu-lim=1200 -max-share-size=8 -cluster-size=4 -max-shareout-size=4 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv2.n$n.cl8_4_4.out
        mpirun -np $n ./minisat -cpu-lim=1200 -max-share-size=16 -cluster-size=4 -max-shareout-size=4 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv2.n$n.cl16_4_4.out
        mpirun -np $n ./minisat -cpu-lim=1200 -max-share-size=16 -cluster-size=4 -max-shareout-size=8 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv2.n$n.cl16_4_8.out
    done

    for n in 16 24;
    do
        mpirun -np $n ./minisat -cpu-lim=1200 -max-share-size=8 -cluster-size=8 -max-shareout-size=2 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv2.n$n.cl8_8_2.out
        mpirun -np $n ./minisat -cpu-lim=1200 -max-share-size=8 -cluster-size=8 -max-shareout-size=4 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv2.n$n.cl8_8_4.out
        mpirun -np $n ./minisat -cpu-lim=1200 -max-share-size=16 -cluster-size=8 -max-shareout-size=4 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv2.n$n.cl16_8_4.out
        mpirun -np $n ./minisat -cpu-lim=1200 -max-share-size=16 -cluster-size=8 -max-shareout-size=8 benchmarks/sr2008/$i >& benchmarks/sr2008/$i.psatv2.n$n.cl16_8_8.out
    done
done
