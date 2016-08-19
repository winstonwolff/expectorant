import importlib.util
from pathlib import Path

from . import spec
from . import ansi


def load_tests(files):
    for filename in files:
        import_spec(filename)

    return spec._suite

def import_spec(filename):
    stem = Path(filename).stem
    import_spec = importlib.util.spec_from_file_location(stem, filename)
    m = importlib.util.module_from_spec(import_spec)
    import_spec.loader.exec_module(m)

def run_tests(suite):
    for node in suite.nodes():
        print("  " * node.depth(), node.name, sep="")
        if node.is_test():
            expector = spec.Expector()
            node.run(expector)
            for result in expector.results:
                color = ansi.GREEN if result.passing else ansi.RED
                print(color, "  " * (node.depth() + 1), result.description, ansi.RESET, sep="")

