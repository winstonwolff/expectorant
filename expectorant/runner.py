import importlib.util
from pathlib import Path
import glob
import sys
from os import path

from . import spec
from . import ansi
from . import expector

def find_files(args):
    files_or_dirs = args or ['.']
    filenames = []
    for f in files_or_dirs:
        if path.isdir(f):
            filenames.extend(glob.glob(path.join(f, '**', '*_spec.py'), recursive=True))
        elif path.isfile(f):
            filenames.append(f)
        else:
            raise FileNotFoundError('could not spec file {}'.format(repr(f)))
    return filenames


def load_specs(filenames):
    for filename in filenames:
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
    files = find_files(sys.argv[1:])
    suite = load_specs(files)
    run_specs(suite)
