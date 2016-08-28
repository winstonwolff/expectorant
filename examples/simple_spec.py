from expectorant import *

@describe('expectorant')                                    # what is being specified in this file?
def _():                                                    # this line is a bit ugly but not too bad.
    scope = None

    @before                                                 # The setup function--called before each `it`
    def _():
        nonlocal scope                                      # Create an empty object for storing values
        scope = Scope()                                     # between `before` and `it`
        scope.dict = {'a': 'expectorant is like rspec', 'b': 3}

    @it('supports "expect" syntax similar to rspec')
    def _():
        expect(scope.dict['a']).to(contain, 'rspec')        # expectations are similar to RSpec.  `contain` is
                                                            # a matcher function--write your own in 3 lines.
    @it('expectations with == != < etc. operators are convenient syntactic sugar')
    def _():
        expect(scope.dict['b']) == 3

    @it('supports rspec\'s great "change" expectation')
    def _():
        expect(scope.dict.clear).to(change, lambda: len(scope.dict), frm=2, to=0)
