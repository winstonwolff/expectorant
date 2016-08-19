#! /usr/bin/env python3
import glob
import expectorant
from expectorant import runner

if __name__=='__main__':
    files = glob.glob('examples/*_spec.py')
    test_tree = runner.load_tests(files)
    runner.run_tests(test_tree)
