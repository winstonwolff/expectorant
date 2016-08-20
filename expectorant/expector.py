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


class Expector:
    '''
    Checks things and keeps a tally of the results.

    >>> expect = Expector()
    >>> expect.is_equal(1, 2)
    Outcome(passing=False, description='is_equal: expect 1 == 2')
    >>> expect.results
    [Outcome(passing=False, description='is_equal: expect 1 == 2')]
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

def raise_error(actual, expected):
    '''
    >>> expect = Expector()
    >>> expect(lambda: 1 / 0).to(raise_error, DivisionByZero)
    '''

#     >>> expect(lambda: 1 / 0).to(raise_error, DivisionByZero)
#     >>> d = 0
#     >>> expect(lambda: d += 0).to_not(change, lambda: d)
#     >>> expect(lambda: d += 1).to(change, lambda: d, by=1)
#     >>> expect(lambda: d += 1).to(change, lambda: d, from=0, to=1)
