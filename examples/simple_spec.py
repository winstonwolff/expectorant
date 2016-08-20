from expectorant import *

@describe("expectorant")
def _():

    @before
    def _(scope, expect):
        scope.dict = {"a": 1}

    @it("supports expectations with == != < etc. operators")
    def _(scope, expect):
        expect(scope.dict["a"]) == 1

    @it("supports expectations on raising exceptions")
    def _(scope, expect):
        def subject(): scope.dict["x"]
        expect(subject).to(raise_error, KeyError)
