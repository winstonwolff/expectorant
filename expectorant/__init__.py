
from . import spec

from .expector import * # all the matchers

from .runner import load_specs, run_specs, main

#
# Use these global functions for syntactic sugar
#
context  = spec.global_suite.context
describe = spec.global_suite.describe
it       = spec.global_suite.it
before   = spec.global_suite.before
after    = spec.global_suite.after

