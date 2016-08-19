#! /usr/bin/env python3
import glob
import importlib.util
from pathlib import Path

import expectorant
import ansi

def load_tests(file_pattern='spec/*_spec.py'):
    files = glob.glob(file_pattern)
    print(files)

    for filename in files:
        import_spec(filename)

    return expectorant._suite

def import_spec(filename):
    stem = Path(filename).stem
    spec = importlib.util.spec_from_file_location(stem, filename)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

def run_tests(test_accumulator):
    for node in test_accumulator.nodes():
        print("  " * node.depth(), node.name, sep="")
        if node.is_test():
            expector = expectorant.Expector()
            node.run(expector)
            for result in expector.results:
                color = ansi.GREEN if result.passing else ansi.RED
                print(color, "  " * (node.depth() + 1), result.description, ansi.RESET, sep="")

if __name__=='__main__':
    test_tree = load_tests('*_spec.py')
#     test_tree.debug_print()
#     print('---')
    run_tests(test_tree)
