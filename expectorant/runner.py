import importlib.util
from pathlib import Path
import glob
import sys
from os import path
from collections import namedtuple

from . import spec
from . import ansi
from . import expector
from . import singletons

class Scope:
    '''A place for specs to store values during the test run.'''
    pass

def find_files(args):
    '''
    Return list of spec files. `args` may be filenames which are passed right
    through, or directories in which case they are searched recursively for
    *._spec.py
    '''
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
    '''
    Return Suite of specs, built up from `filenames`
    '''
    for filename in filenames:
        import_spec(filename)

    return singletons.global_suite

def import_spec(filename):
    pkg_name = 'expectorantloader_' + str(Path(filename).with_suffix('')).replace('/', '_')

    import_spec = importlib.util.spec_from_file_location(pkg_name, filename)
    m = importlib.util.module_from_spec(import_spec)
    import_spec.loader.exec_module(m)
    sys.modules[pkg_name] = m

def run_specs(suite, outcomes=singletons.global_outcomes):
    all_outcomes = []
    for node in suite.nodes():
        print("  " * node.depth(), node.name, sep="")
        if node.is_test():
            outcomes.clear()
            node.run()
            all_outcomes.extend(outcomes)
            for outcome in outcomes:
                color = ansi.GREEN if outcome.passing else ansi.RED
                print(color, "  " * (node.depth() + 1), outcome.source_line, ansi.RESET, sep="")
                print(color, "  ", "  " * (node.depth() + 1), outcome.description, ansi.RESET, sep="")
    return all_outcomes # e.g. [[node1, outcome1.1], [node1, outcome1.2], [node2, outcome2.1]...]



def main():
    files = find_files(sys.argv[1:])
    suite = load_specs(files)
    outcomes = run_specs(suite)

    passing = [outcome for outcome in outcomes if outcome.passing]
    failures = [outcome for outcome in outcomes if not outcome.passing]
    num_failing = len(failures)
    print()
    print('{ansi.GREEN}Passing: {count}{ansi.RESET}'.format(count=len(passing), ansi=ansi))
    print('{color}Failing: {count}{ansi.RESET}'.format(
        count=num_failing,
        color = ansi.RED if num_failing else '',
        ansi=ansi))
    for i, outcome in enumerate(failures):
        print(ansi.RED, '  (', i, ') ', outcome.source.filename, ':', outcome.source.lineno, ansi.RESET, sep='')
        print('     ', outcome.source_line)
        print('     ', outcome.description)
    exit_code = 1 if num_failing else 0
    print('Exit code:', exit_code)
    exit(exit_code)

