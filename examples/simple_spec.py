from expectorant import *


@describe("expectorant")
def _():
    scope = None
    @before
    def _():
        nonlocal scope
        scope = Scope()  # A new scope every test run
        scope.dict = {"a": 1}

    @it("supports expectations with == != < etc. operators")
    def _():
        expect(scope.dict["a"]) == 1

    @it("supports expectations on raising exceptions")
    def _():
        def subject(): scope.dict["x"]
        expect(subject).to(raise_error, KeyError)


