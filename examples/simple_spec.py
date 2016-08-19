from expectorant import *

@describe("dict")
def _():

    @before
    def _(scope, expect):
        scope.dict = {"a": 1}

    @it("retrieves by key")
    def _(scope, expect):
        expect(scope.dict["a"]).to(equal, 1)
