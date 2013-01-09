# command line for sharing.
#  python ../plot_cluster.py small.list .baseline.out `cat clustered.suffixes2`

import sys
import itertools

import numpy as np
import matplotlib.pyplot as plt

from get_status import get_status, SAT, UNSAT, TIMEOUT

def strip_cnfgz(str):
    if str.endswith('.cnf.gz'):
        return str[:-7]
    else:
        return str

def compare(filename, suffixes):
    stats = []
    times = []
    for pos, s in enumerate(suffixes):
        fullname = filename + s
        status, time = get_status(fullname)
        stats.append(status)
        times.append(time)

    bs = stats[0]
    for s in stats:
        assert s == bs, 'SAT SOLVER BUG!'
    t0 = times[0]

    speedups = []
    for t in times[1:]:
        speedup = t0 / t
        speedups.append(speedup)

    speed_strings = ('%-40s & ' % strip_cnfgz(filename)) + (' & '.join([('%6.1f' % s) for s in speedups])) + ' \\\\'
    print speed_strings
    return times

def add(t1, t2):
    return [x+y for x,y in itertools.izip(t1, t2)]

def plot_sharing(filename, suffixes):
    filelist = []
    for line in open(filename, 'rt'):
        if line.strip():
            filelist.append(line.strip())

    t = [0] * len(suffixes)
    all_times = []
    for s in suffixes:
        total_time = 0
        for f in filelist:
            fullname = f + s
            status, time = get_status(fullname)
            total_time +=time
        print s, total_time
        all_times.append(total_time)

    times = [ all_times[0] / t for t in all_times[1:]]
    c44 = times[0:6:2]
    c48 = times[1:6:2]
    c84 = times[6:10:2]
    c88 = times[7:10:2]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ind1 = np.arange(3)
    ind2 = np.arange(2) + 1

    r0 = ax.bar(ind1+0.1, c44, width=0.2, color='red')
    r1 = ax.bar(ind1+0.3, c48, width=0.2, color='green')
    r2 = ax.bar(ind2+0.5, c84, width=0.2, color='blue')
    r3 = ax.bar(ind2+0.7, c88, width=0.2, color='orange')


    ax.set_ylim((0,4.25))
    ax.legend((r0[0],r1[0],r2[0],r3[0]), ('ClusterSz=4; MSCSOut=4', 'ClusterSz=4; MSCSOut=8', 'ClusterSz=8; MSCSOut=4', 'ClusterSz=8;MSCSOut=8'), loc='upper left')
    ax.set_xticks(np.arange(3)+0.5)
    ax.set_xticklabels(['n=8', 'n=16', 'n=24'], size='x-large')
    ax.set_ylabel('Speedup over Minisat 2.2', size='x-large')
    ax.set_xlabel('Number of cores.', size='x-large')
    ax.grid(True)

    plt.savefig('cluster.pdf')

plot_sharing(sys.argv[1], sys.argv[2:])
