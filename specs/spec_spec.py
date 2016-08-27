from expectorant import *

from expectorant.spec import TestCase

@describe("TestCase")
def _():

    @it("formats name with args")
    def _(scope, expect):
        tc = TestCase([], "foo {} bar {}", None, ("FOO", "BAR"))
        expect(tc.name) == "foo FOO bar BAR"

#     @it("does something nice when {} doest match args")
#     def _(scope, expect):
#         tc = TestCase([], "foo {} bar {} baz {}", None, ("FOO", "BAR"))
#         expect(tc.name) == "foo FOO bar BAR"
