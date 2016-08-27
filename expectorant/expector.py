from collections import namedtuple

Outcome = namedtuple("Outcome", 'passing description')


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
        outcome = (self.actual == expected,
                   '{} == {}'.format(repr(self.actual), repr(expected)))
        self.expector.add_result(*outcome)
        return outcome

    def __ne__(self, expected):
        outcome = (self.actual != expected,
                   '{} != {}'.format(repr(self.actual), repr(expected)))
        self.expector.add_result(*outcome)
        return outcome

    def __gt__(self, expected):
        outcome = (self.actual > expected,
                   '{} > {}'.format(repr(self.actual), repr(expected)))
        self.expector.add_result(*outcome)
        return outcome

    def __ge__(self, expected):
        outcome = (self.actual >= expected,
                   '{} >= {}'.format(repr(self.actual), repr(expected)))
        self.expector.add_result(*outcome)
        return outcome

    def __lt__(self, expected):
        outcome = (self.actual < expected,
                   '{} < {}'.format(repr(self.actual), repr(expected)))
        self.expector.add_result(*outcome)
        return outcome

    def __le__(self, expected):
        outcome = (self.actual <= expected,
                   '{} <= {}'.format(repr(self.actual), repr(expected)))
        self.expector.add_result(*outcome)
        return outcome

class Expector:
    '''
    Checks things and keeps a tally of the results. An expectation inspector = expector.

    >>> outcomes = []
    >>> expect = Expector(outcomes)
    >>> expect(1).to_not(equal, 2)
    (True, 'equal: expect 1 == 2')
    >>> outcomes
    [Outcome(passing=True, description='equal: expect 1 == 2')]

    >>> expect(1) == 1
    (True, '1 == 1')

    >>> expect('abc') != 'def'
    (True, "'abc' != 'def'")

    >>> expect(1) < 1.1
    (True, '1 < 1.1')
    '''
    def __init__(self, outcomes):
        self.results = outcomes

    def add_result(self, is_passing, description):
        self.results.append(Outcome(is_passing, description))

    def __call__(self, actual):
        '''The first part of the `expect(actual).to(matcher, args)` expression.'''
        return _ToClause(self, actual)


def equal(actual, expected):
    '''
    Compare actual and expected using ==

    >>> expect = Expector([])
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
    >>> expect = Expector([])
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
def change(subject, evaluator, by=_NOT_SET, frm=_NOT_SET, to=_NOT_SET):
    '''
    Calls function `evaluator` before and after a call function `subject`. Output of `evaluator` should change.

    >>> expect = Expector([])
    >>> a = [1, 2, 3]
    >>> expect(a.clear).to(change, lambda: len(a))
    (True, 'expect change: actual from=3 to=0')

    >>> a = [1, 2, 3]
    >>> expect(a.clear).to(change, lambda: len(a), by=-3)
    (True, 'expect change by=-3: actual from=3 to=0')

    >>> a = [1, 2, 3]
    >>> expect(a.clear).to(change, lambda: len(a), frm=3, to=0)
    (True, 'expect change from=3 to=0: actual from=3 to=0')
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

    if frm != _NOT_SET:
        clauses.append(' from={}'.format(repr(frm)))
        if frm != output_before: is_passing = False

    if to != _NOT_SET:
        clauses.append(' to={}'.format(repr(to)))
        if to != output_after: is_passing = False

    return (is_passing, 'expect change{}: actual from={} to={}'.format(
        ''.join(clauses),
        repr(output_before),
        repr(output_after)))

def startswith(a, b):
        is_passing = a.startswith(b)
        description = 'Expect {} to start with {}'.format(repr(a), repr(b))
        return (is_passing, description)

def contain(a, b):
        is_passing = b in a
        description = 'Expect {} to contain {}'.format(repr(a), repr(b))
        return (is_passing, description)

