import os
import sys
import itertools
import argparse

import numpy as np
import matplotlib.pyplot as plt

from get_status import get_status, SAT, UNSAT, TIMEOUT

def get_benches(filename):
    with open(filename, 'rt') as fobj:
        slurp = fobj.read()
        lines = [l.strip() for l in slurp.split('\n') if len(l.strip())]
        return lines
    raise IOError, ("Unable to read file: %s" % filename)

def get_out_files(benches, path, suffix):
    filenames = []
    for b in benches:
        fn = os.path.join(path, b+suffix)
        if not os.path.exists(fn):
            raise IOError, "File does not exist: %s" % fn
        filenames.append(fn)
    return filenames

def printresults(benchfile, groups):
    benches = get_benches(benchfile)
    file_list = []
    for (rdir, suf) in groups:
        files = get_out_files(benches, rdir, suf)
        file_list.append(files)
    for i, b in enumerate(benches):
        pstr = '%-35s  ' % b
        for files in file_list:
            si, ti = get_status(files[i])
            pstr += '%8.2f  ' % ti
        print pstr

def main(argv):
    benchfile = argv[1]
    if (len(argv) - 2) < 2:
        print 'Syntax error.'
    if (len(argv) - 2) % 2 != 0:
        print 'Syntax error.'

    directories = argv[2::2]
    suffixes = argv[3::2]
    printresults(benchfile, itertools.izip(directories, suffixes))

if __name__=="__main__":
    main(sys.argv)

