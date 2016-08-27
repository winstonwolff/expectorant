
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

