import sys
import itertools

from get_status import get_status, SAT, UNSAT, TIMEOUT, STATUS_STRINGS

def compare(filename, suffixes):
    stats = []
    times = []
    for pos, s in enumerate(suffixes):
        fullname = filename + s
        status, time = get_status(fullname)
        stats.append(status)
        times.append(time)

    bs = stats[0]
    for i, s in enumerate(stats):
        if s != bs and s != TIMEOUT:
            assert False, 'SAT SOLVER BUG for %s! expected=%s actual=%s' % (filename, STATUS_STRINGS[bs], STATUS_STRINGS[s])
    t0 = times[0]

    timed_out = False
    speedups = []
    for s, t in itertools.izip(stats[1:], times[1:]):
        if s != TIMEOUT:
            speedup = t0 / t
            speedups.append(speedup)
        else:
            timed_out = True
            speedups.append(-1)

    speed_strings = ('%-40s' % filename) + (' '.join([('%6.1f' % s if s != -1 else ('%6s' % '--')) for s in speedups]))
    print speed_strings
    return times, timed_out

def add(t1, t2):
    return [x+y for x,y in itertools.izip(t1, t2)]

def compare_all(filelist, suffixes):
    t = [0] * len(suffixes)
    for line in open(filelist, 'rt'):
        if line.strip():
            ti, timedout = compare(line.strip(), suffixes)
            if not timedout:
                t = add(t, ti)

    n = [t[0] / ni for ni in t[1:]]
    print (' '*40) + (' '.join([('%6.1f' % ti) for ti in n]))

compare_all(sys.argv[1], sys.argv[2:])
# get_status(sys.argv[1])
