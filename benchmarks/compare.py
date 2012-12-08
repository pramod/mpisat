import sys

SAT         = 0
UNSAT       = 1
TIMEOUT     = 2

def get_status(filename):
    status = -1
    lines = open(filename, 'rt').read().split('\n')
    for l in lines:
        if l.strip() == 'SATISFIABLE':
            status = SAT
            break
        elif l.strip() == 'UNSATISFIABLE':
            status = UNSAT
            break
        elif l.strip() == 'INDETERMINATE':
            status = TIMEOUT
            break
    assert status != -1

    time = -1
    for l in lines:
        if l.strip().startswith('CPU time'):
            words = l.split()
            time = float(words[3])
    assert time != -1
    return status, time

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

    speed_strings = ('%-40s' % filename) + (' '.join([('%6.1f' % s) for s in speedups]))
    print speed_strings

def compare_all(filelist, suffixes):
    for line in open(filelist, 'rt'):
        if line.strip():
            compare(line.strip(), suffixes)

compare_all(sys.argv[1], sys.argv[2:])