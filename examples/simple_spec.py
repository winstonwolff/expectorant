from expectorant import *

@describe('expectorant')                                    # describe, context, before,
def _():                                                    # after, and it, just like RSpec
    scope = None
    @before
    def _():
        nonlocal scope
        scope = Scope()                                     # A new scope every test run
        scope.dict = {'a': 'expectorant is like rspec', 'b': 3}

    @it('supports "expect" syntax similar to rspec')
    def _():
        expect(scope.dict['a']).to(contain, 'rspec')        # expectations are similar to RSpec

    @it('expectations with == != < etc. operators are convenient syntactic sugar')
    def _():
        expect(scope.dict['b']) == 3

    @it('supports rspec\'s great "change" expectation')
    def _():
        expect(scope.dict.clear).to(change, lambda: len(scope.dict), frm=2, to=0)
