from collections import namedtuple

Outcome = namedtuple("Outcome", 'passing description')

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

    def is_equal(self, a, b, msg=None):
        is_passing = (a == b)

        msgs = ["is_equal: expect {} == {}".format(a, b)]
        if msg: msgs.append(msg)

        outcome = Outcome(is_passing, ' '.join(msgs))
        self.results.append(outcome)
        return outcome

