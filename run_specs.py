#!/usr/bin/env python3

import doctest
import expectorant
from expectorant import ansi
from pathlib import Path

from expectorant import expector, spec

HERE = Path(__file__).absolute().parent

def run_doctest(module):
    print(' ', Path(module.__file__).relative_to(HERE))
    result = doctest.testmod(module)
    pass_count = result.attempted - result.failed
    color = ansi.RED if result.failed else ansi.GREEN
    print('{}    pass={} fail={}{}'.format(color, pass_count, result.failed, ansi.RESET))

print("Running doctests...")
run_doctest(spec)
run_doctest(expector)

expectorant.main()



