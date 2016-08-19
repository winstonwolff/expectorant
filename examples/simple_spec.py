from expectorant import *

@describe("dict")
def _():

    @before
    def _(scope, expect):
        scope.dict = {"a": 1}

    @it("retrieves by key")
    def _(scope, expect):
        expect.is_equal(scope.dict["a"], 1)

