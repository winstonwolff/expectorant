To Do
-----
*** exception reporting at end needs better visuals
    - context should be indented, and colorized

- Make samples with exceptions in various places, e.g.
    - inside test that is not expecting it
    - inside setup
    - inside teardown
    - inside testing framework

- Testing system with state / side-effects

- More matchers. Maybe pyhamcrest
    with context('value', a, 'equals', b):
        expect(a, equals, b, msg, more_msg)
        expect(a, has_jquery_descriptor('p.is_disabled'), msg, more_msg)
        expect(a).to(equal, b).msg(msg, more_msg)
        expect('values are equal', a).to(equal, b).msg(msg, more_msg)
