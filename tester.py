'''
Winston's automated test system
'''
import sys
import random
import contextlib
import traceback
import inspect
import itertools
from collections import namedtuple

_TEST_RUNNER_FUNC = 'run_tests'

class _Ansi:
    NONE =   "\x1B[39m"
    RED =    "\x1B[31m"
    GREEN =  "\x1B[32m"
    CYAN =   "\x1B[36m"
    YELLOW = "\x1B[33m"
    GREY =   "\x1B[38;5;237m"

CheckFailure = namedtuple('CheckFailure', 'message contexts stack')

class Checker:
    '''
    Stores all test results. Passed to each test function.
    '''
    def __init__(self):
        self.num_checks = 0
        self.failures = []
        self.cur_context = []

    def _depth(self):
        '''how many contexts are we within?'''
        return len(self.cur_context)

    def _indent(self):
        indent = len(self.cur_context) + 1
        return '  ' * indent

    def begin_context(self, name):
        color = _Ansi.NONE if self._depth() == 0 else _Ansi.GREY
        print('{color}{indent}{name}{nocolor}'.format(
            color=color,
            indent=self._indent(), 
            name=name,
            nocolor=_Ansi.NONE))
        self.cur_context.append(name)

    def end_context(self):
        self.cur_context.pop()

    def record_failure(self, msg_str, stack, trim_stack_end):
        # Ignore stack frames in test runner
        stack = list(itertools.dropwhile(lambda f:f[2] != _TEST_RUNNER_FUNC, stack))
        stack = stack[1:trim_stack_end]

        self.failures.append(CheckFailure(msg_str, tuple(self.cur_context), stack))

    def equal(self, a, b, *msgs):
        self.num_checks += 1
        is_okay = a == b
        result = 'OK' if is_okay else 'FAIL'
        user_msg = ' '.join(str(m) for m in msgs)
        matcher_msg = '{a} == {b} [{result}]'.format(
            a=repr(a),
            b=repr(b),
            result=result
        )
        msg_str = '{user_msg:50s}{matcher_msg:>30s}'.format(
            user_msg=self._indent() + user_msg, 
            matcher_msg=matcher_msg
        )

        if not is_okay:
            self.record_failure(msg_str, traceback.extract_stack(), -1)

        color = _Ansi.GREEN if is_okay else _Ansi.RED
        nocolor = _Ansi.NONE
        print('{color}{msg_str}{nocolor}'.format(**locals()))

    @contextlib.contextmanager
    def setup(self, setup_func):
        '''
        decorator for test harness
        '''
        args = setup_func()
        msg = '{} with {}'.format(setup_func.__name__, args)
        self.begin_context(msg)
        yield args
        self.end_context()

test_setup = contextlib.contextmanager

_all_tests = []

def test(func):
    '''
    Decorator for your test functions
    '''
    _all_tests.append(func)
    return func

def run_tests(tests=None):
    '''
    Runs some tests. Pass a list of test functions, 
    or all tests will be run.
    '''
    tests = tests or _all_tests
#     random.shuffle(tests)
    check = Checker()
    for t in tests:
        check.begin_context(t.__name__)
        try:
            t(check)
        except Exception as exc:
            msg = ' test failure: {}'.format(exc)
            check.record_failure(msg, traceback.extract_tb(sys.exc_info()[2]), 9999)
            print(_Ansi.RED, msg, _Ansi.NONE)
        finally:
            check.end_context()

    print('\nSummary of Failures:\n--------------------')
    for f in check.failures:
        print(' ', ' > '.join(f.contexts))
        print(_Ansi.RED, f.message, _Ansi.NONE)
        print(''.join(traceback.format_list(f.stack)))

    print('---------------------------')
    color = _Ansi.RED if check.failures else _Ansi.GREEN
    print('{color}{num_fails} failures out of {num_checks} checks.{nocolor}'.format(
        color=_Ansi.RED, 
        num_fails=len(check.failures),
        num_checks=check.num_checks,
        nocolor=_Ansi.NONE))
