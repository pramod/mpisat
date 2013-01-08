SAT         = 0
UNSAT       = 1
TIMEOUT     = 2

STATUS_STRINGS = [ "SAT", "UNSAT", "TIMEOUT" ]


def get_status(filename):
    status = -1
    lines = open(filename, 'rt').read().split('\n')

    manysat = False
    manysat_cores = -1

    # manysat wrangling
    for l in lines:
        if l.find('manysat2.0') != -1:
            manysat = True
            break
    if manysat:
        for l in lines:
            l = l.strip()
            if not len(l): continue
            if l[0] == '|': l = l[1:].strip()
            if l[-1] == '|': l = l[:-1].strip()
            l = l.strip()
            words = [s.strip( ) for s in l.split(':')]
            if len(words) == 2:
                if words[0] == 'Number of cores':
                    manysat_cores = int(words[1])
                    break
        assert manysat_cores != -1

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
    assert status != -1, filename

    time = -1
    for l in lines:
        if l.strip().startswith('CPU time'):
            words = l.split()
            time = float(words[3])
    assert time != -1, filename

    if manysat:
        time = time / manysat_cores
    return status, time


