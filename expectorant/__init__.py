import sys as _sys
if _sys.version_info < (3,5):
    raise RuntimeError('expectorant requires Python 3.5 or higher but the current vesion is: {}.{}'.format(_sys.version_info.major, _sys.version_info.minor))

from . import spec
from . import singletons

from .expector import * # all the matchers

from .runner import load_specs, run_specs, main, Scope

#
# Use these global functions for syntactic sugar
#
context  = singletons.global_suite.context
describe = singletons.global_suite.describe
it       = singletons.global_suite.it
before   = singletons.global_suite.before
after    = singletons.global_suite.after

expect = Expector(singletons.global_outcomes)

