from collections import namedtuple

_Outcome = namedtuple("Outcome", 'passing description')

class _ToClause:
    def __init__(self, expector, actual):
        self.expector = expector
        self.actual = actual

    def to(self, matcher, *args, **kwargs):
        is_passing, description = matcher(self.actual, *args, **kwargs)
        self.expector.add_result(is_passing, description)
        return (is_passing, description)

    def to_not(self, matcher, *args, **kwargs):
        is_passing, description = matcher(self.actual, *args, **kwargs)
        inverted_is_passing = not is_passing
        self.expector.add_result(inverted_is_passing, description)
        return (inverted_is_passing, description)

    def __eq__(self, expected):
        return (self.actual == expected,
                '{} == {}'.format(repr(self.actual), repr(expected)))

    def __ne__(self, expected):
        return (self.actual != expected,
                '{} != {}'.format(repr(self.actual), repr(expected)))

    def __gt__(self, expected):
        return (self.actual > expected,
                '{} > {}'.format(repr(self.actual), repr(expected)))

    def __ge__(self, expected):
        return (self.actual >= expected,
                '{} >= {}'.format(repr(self.actual), repr(expected)))

    def __lt__(self, expected):
        return (self.actual < expected,
                '{} < {}'.format(repr(self.actual), repr(expected)))

    def __le__(self, expected):
        return (self.actual <= expected,
                '{} <= {}'.format(repr(self.actual), repr(expected)))

class Expector:
    '''
    Checks things and keeps a tally of the results.

    >>> expect = Expector()
    >>> expect(1).to_not(equal, 2)
    (True, 'equal: expect 1 == 2')
    >>> expect.results
    [Outcome(passing=True, description='equal: expect 1 == 2')]

    >>> expect(1) == 1
    (True, '1 == 1')

    >>> expect('abc') != 'def'
    (True, "'abc' != 'def'")

    >>> expect(1) < 1.1
    (True, '1 < 1.1')
    '''
    def __init__(self):
        self.results = []

    def add_result(self, is_passing, description):
        self.results.append(_Outcome(is_passing, description))

    def __call__(self, actual):
        '''The first part of the `expect(actual).to(matcher, args)` expression.'''
        return _ToClause(self, actual)


def equal(actual, expected):
    '''
    Compare actual and expected using ==

    >>> expect = Expector()
    >>> expect(1).to_not(equal, 2)
    (True, 'equal: expect 1 == 2')

    >>> expect(1).to(equal, 1)
    (True, 'equal: expect 1 == 1')
    '''
    is_passing = (actual == expected)

    description = "equal: expect {} == {}".format(actual, expected)
    return is_passing, description

def raise_error(subject, error_class):
    '''
    Call function `subject` and expect the function to raise an exception.
    >>> expect = Expector()
    >>> expect(lambda: 1 / 0).to(raise_error, ZeroDivisionError)
    (True, 'Expect ZeroDivisionError to be raised')
    '''
    description = 'Expect {} to be raised'.format(error_class.__name__)
    try:
        subject()
        return (False, description)
    except error_class:
        return (True, description)

_NOT_SET = object()
def change(subject, evaluator, by=_NOT_SET, before=_NOT_SET, after=_NOT_SET):
    '''
    Calls function `evaluator` before and after a call function `subject`. Output of `evaluator` should change.

    >>> expect = Expector()
    >>> a = [1, 2, 3]
    >>> expect(a.clear).to(change, lambda: len(a))
    (True, 'expect change: actual before=3 after=0')

    >>> a = [1, 2, 3]
    >>> expect(a.clear).to(change, lambda: len(a), by=-3)
    (True, 'expect change by=-3: actual before=3 after=0')

    >>> a = [1, 2, 3]
    >>> expect(a.clear).to(change, lambda: len(a), before=3, after=0)
    (True, 'expect change before=3 after=0: actual before=3 after=0')
    '''
    output_before = evaluator()
    subject()
    output_after = evaluator()

    clauses = []
    is_passing = output_before != output_after

    if by != _NOT_SET:
        clauses.append(' by={}'.format(repr(by)))
        delta = output_after - output_before
        if delta != by: is_passing = False

    if before != _NOT_SET:
        clauses.append(' before={}'.format(repr(before)))
        if before != output_before: is_passing = False

    if after != _NOT_SET:
        clauses.append(' after={}'.format(repr(after)))
        if after != output_after: is_passing = False

    return (is_passing, 'expect change{}: actual before={} after={}'.format(
        ''.join(clauses),
        repr(output_before),
        repr(output_after)))

