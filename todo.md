## Working on


## To Do

- use codec hack to hide `def _():`

- executable to run specs from command line.

- parameterized specs, e.g.

    for input, output in [(1, 1), (2, 4)]:
        @it("raises input with itself:", input, output)
        def _(scope, expect):
            expect(input ** input) == output
    ---
        @it("raises input with itself:", input, output):
            expect(input ** input) == output
    ---
    raises input with itself: 1, 1
        1 == 1
    raises input with itself: 2, 4
        4 == 4

- alternative to 'scope'

- improve output descriptions
    - get line of source?

- `expect() == ...` should use same function as `expect().to(equal,...)`

- documentation
    - matchers
    - easy to write new matchers -- two line function
    - expect() does not raise so several are OK in an 'it' block
    - show what output looks like
    - easy to output different formats like JUnit xml
    - codec version

- user can run a subset of specs

- Handle exceptions within the spec
    - Make samples with exceptions in various places, e.g.
        - inside test that is not expecting it
        - inside setup
        - inside teardown
        - inside testing framework

- async specs



## Done
- better expect() syntax
- allow users to write new test functions easily
- check for side-effects to change
- check for raising exceptions
- install with pip
- better way to share values through test chain, e.g. pass a mutable 'self'
- proper test loader
- write in RSpec describe-context-it format
- decouple testing from reporting
- write tests in Expectorant itself!

