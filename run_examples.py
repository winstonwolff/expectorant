#! /usr/bin/env python3
import glob
import expectorant

if __name__=='__main__':
    files = glob.glob('examples/*_spec.py')
    test_tree = expectorant.load_tests(files)
    expectorant.run_tests(test_tree)
