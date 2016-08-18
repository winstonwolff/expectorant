To Do
-----

- better expect() syntax

    - check for side-effects to change

    - check for raising exceptions

- allow users to write new test functions easily

- decouple testing from reporting

- use codec hack to hide `def _():`

- better way to share values through test chain, e.g. pass a mutable 'self'

- Handle exceptions
    - Make samples with exceptions in various places, e.g.
        - inside test that is not expecting it
        - inside setup
        - inside teardown
        - inside testing framework

- Testing system with state / side-effects

