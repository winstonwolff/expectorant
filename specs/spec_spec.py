from expectorant import *

from expectorant.spec import TestCase

def startswith(a, b):
        is_passing = a.startswith(b)
        description = 'Expect {} to start with {}'.format(repr(a), repr(b))
        return (is_passing, description)

def contain(a, b):
        is_passing = b in a
        description = 'Expect {} to contain {}'.format(repr(a), repr(b))
        return (is_passing, description)

@describe("TestCase")
def _():

    @it("formats name with args")
    def _(scope, expect):
        tc = TestCase([], "foo {} bar {}", None, ("FOO", "BAR"))
        expect(tc.name) == "foo FOO bar BAR"

    @it("does something nice when {} doesn\'t match args")
    def _(scope, expect):
        tc = TestCase([], "foo {} bar {} baz {}", None, ("FOO", "BAR"))
        expect(tc.name).to(contain, "could not format")
