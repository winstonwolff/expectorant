## Test the package

    mkdir /tmp/ex
    cd /tmp/ex
    pyenv shell 3.5.1
    pip3 install --target . git+git://github.com/winstonwolff/expectorant.git

## Working on

- Publish on PyPi

    python setup.py sdist upload -r pypitest


## To Do

- write documentation
    - How does this compare with other RSpec clones?
        - https://github.com/nestorsalceda/mamba
        - NoseOfYeti
        - pspec
    - What matchers are available?  How do they work?
    - How do I run my specs? All? Just a few?
    - How do I repeat an `it` test with different data?
    - How do I write a new matcher?
    - How many `expect`s should I put in one `it`?
    - expect() does not raise so several are OK in an 'it' block
    - easy to output different formats like JUnit xml

- publish docs on ReadTheDocs

- user can run a subset of specs

- Handle exceptions within the spec
    - Make samples with exceptions in various places, e.g.
        - inside test that is not expecting it
        - inside setup
        - inside teardown
        - inside testing framework

- have runner run doctests too? With nicer colored output?

- extract TreeNode from Spec

- use codec hack to hide `def _():`

- improve output descriptions
    - get line of source?

- `expect() == ...` should use same function as `expect().to(equal,...)`

- async specs

- how about AST manipulation? e.g.
    ```
    def describe("My great module"):
        def before():
            self.mgm = MyGreatModule()

        def context("when something is prepared"):
            def before():
                self.mgm.prepare()

            def test("it works"):
                expect(self.mgm.a) == 3
    ```





## Done
- alternative to 'scope'
- get 'expect' out of 'def _():'
- parameterized specs
- executable to run specs from command line.
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

