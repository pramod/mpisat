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
    s = []
    for i in xrange(5):
        si = times[i:15:5]
        s.append(si)


    fig = plt.figure()
    ax = fig.add_subplot(111)
    ind = np.arange(3)

    r = []
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    for i in xrange(5):
        ri = ax.bar(ind+0.125+i*0.15, s[i], width=0.15, color=colors[i])
        r.append(ri)


    ax.set_ylim((0,4))
    ax.legend((r[0][0],r[1][0],r[2][0],r[3][0], r[4][0]), ('Exact comparison', '0.1% tolerance', '1% tolerance', '5% tolerance', '10% tolerance'), loc='best')
    ax.set_xticks(np.arange(3)+0.5)
    ax.set_xticklabels(['n=4', 'n=8', 'n=12'], size='x-large')
    ax.set_ylabel('Speedup over Minisat 2.2', size='x-large')
    ax.set_xlabel('Number of cores.', size='x-large')
    ax.grid(True)

    plt.savefig('aff.pdf')

plot_sharing(sys.argv[1], sys.argv[2:])
