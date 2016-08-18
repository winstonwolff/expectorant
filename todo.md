To Do
-----

- proper test loader

- write tests in Expectorant itself!

- better expect() syntax

    - check for side-effects to change

    - check for raising exceptions

- allow users to write new test functions easily

- use codec hack to hide `def _():`

- better way to share values through test chain, e.g. pass a mutable 'self'

- Handle exceptions
    - Make samples with exceptions in various places, e.g.
        - inside test that is not expecting it
        - inside setup
        - inside teardown
        - inside testing framework

- Testing system with state / side-effects

- async tests



Done
----
- write in RSpec describe-context-it format
- decouple testing from reporting
