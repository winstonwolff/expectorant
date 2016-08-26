import importlib.util
from pathlib import Path
import glob
import argparse

from . import spec
from . import ansi
from . import expector


def load_specs(files):
    for filename in files:
        import_spec(filename)

    return spec._suite

def import_spec(filename):
    stem = Path(filename).stem
    import_spec = importlib.util.spec_from_file_location(stem, filename)
    m = importlib.util.module_from_spec(import_spec)
    import_spec.loader.exec_module(m)

def run_specs(suite):
    for node in suite.nodes():
        print("  " * node.depth(), node.name, sep="")
        if node.is_test():
            expect = expector.Expector()
            node.run(expect)
            for result in expect.results:
                color = ansi.GREEN if result.passing else ansi.RED
                print(color, "  " * (node.depth() + 1), result.description, ansi.RESET, sep="")

def main():
    files = glob.glob('specs/*_spec.py')
    suite = load_specs(files)
    run_specs(suite)
