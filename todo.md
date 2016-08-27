## Test the package

    mkdir /tmp/ex
    cd /tmp/ex
    pyenv shell 3.5.1
    pip3 install --target . git+git://github.com/winstonwolff/expectorant.git




## Working on


## To Do

- alternative to 'scope'

- get 'expect' out of 'def _():'

- separate TreeNode from Spec

- use codec hack to hide `def _():`

- have runner run doctests too? With nicer colored output?

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

