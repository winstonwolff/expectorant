#! /usr/bin/env python3
import glob
import expectorant

if __name__=='__main__':
    files = glob.glob('examples/*_spec.py')
    suite = expectorant.load_specs(files)
    expectorant.run_specs(suite)
