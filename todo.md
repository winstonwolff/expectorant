## Working on

- better expect() syntax


## To Do

- write tests in Expectorant itself!

- install with pip

- check for side-effects to change

- check for raising exceptions

- allow users to write new test functions easily

- use codec hack to hide `def _():`


- Handle exceptions within the spec
    - Make samples with exceptions in various places, e.g.
        - inside test that is not expecting it
        - inside setup
        - inside teardown
        - inside testing framework

- async tests



## Done
- better way to share values through test chain, e.g. pass a mutable 'self'
- proper test loader
- write in RSpec describe-context-it format
- decouple testing from reporting
