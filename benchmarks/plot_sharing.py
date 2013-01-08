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
    s0 = times[0:len(times):4]
    s1 = times[1:len(times):4]
    s2 = times[2:len(times):4]
    s3 = times[3:len(times):4]

    print ' '.join([('%6.1f' % ti) for ti in s0])
    print ' '.join([('%6.1f' % ti) for ti in s1])
    print ' '.join([('%6.1f' % ti) for ti in s2])
    print ' '.join([('%6.1f' % ti) for ti in s3])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ind = np.arange(3)

    r0 = ax.bar(ind+0.2, s0, 0.15, color='red')
    r1 = ax.bar(ind+0.35, s1, 0.15, color='green')
    r2 = ax.bar(ind+0.5, s2, 0.15, color='blue')
    r3 = ax.bar(ind+0.65, s3, 0.15, color='black')

    ax.legend((r0[0],r1[0],r2[0],r3[0]), ('MSCS=8', 'MSCS=16', 'MSCS=32', 'MSCS=64'), loc='upper left')
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(['n=2', 'n=4', 'n=8'], size='x-large')
    ax.set_ylabel('Speedup over Minisat 2.2', size='x-large')
    ax.set_xlabel('Number of cores.', size='x-large')
    ax.grid(True)

    plt.savefig('mcs.pdf')
    plt.show()

plot_sharing(sys.argv[1], sys.argv[2:])
