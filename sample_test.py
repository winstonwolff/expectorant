#! /usr/bin/env python3
'''
Winston Tester
==============

To Do
-----
*** exception reporting at end needs better visuals
    - context should be indented, and colorized

***- get setup() context working
    - maybe this is:
        with context(...):
      where: context() prints the message or values, 
      and limits how far an exception will roll back.
    - It's not calling the teardown

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

- run some unittest.TestCases too.
'''

import random

from tester import *

def add(a, b):
    '''A function to be tested.'''
    return a + b


@test
def simple_test(check):
    '''Here is a simple test.'''
    check.equal(add(1, 1), 2, 'adding', 1, 1)

#
# Test sets of data with one function
#

@test
def parameterized_test(check):
    '''
    Here is a test that runs add() against a whole
    set of input values.
    '''
    for a, b, e in (
        [1, 1, 2],
        [2, 2, 4],
        [3, 4, 7]
    ):
        check.equal(add(a, b), e, 'adding', a, b)

_acc = 0
def accumulate(a):
    global _acc
    _acc += a
    return _acc

def reset():
    global _acc
    _acc = 0

@test
def accumulate_test(check):

    @test_setup
    def zeroed_accumulator():
        reset()
        yield

    for inputs, expected in (
        [(1, 1), 2],
        [(2, 3), 5],
        [(1,2,3,4), 10],
    ):
        with zeroed_accumulator():
            out = None
            for a in inputs:
                out = accumulate(a)
            check.equal(out, expected, 'inputs=', inputs)

def divide(a, b):
    '''
    Another function to be tested. I wonder what will happen
    if 'b' is zero?
    '''
    return a / b

@test
def exception_in_function_under_test(check):
    '''
    This demonstrates handling of unexpected exceptions raised by
    the function under test.
    '''
    check.equal(2.0, divide(2, 1), 'divides 2 1')
    check.equal(0.0, divide(2, 0), 'divides 2 0')

            
def engage_dilithium_thrusters():
    '''pretend setup function'''
    pass

@test
def using_setup_function(check):
    '''
    This demonstrates how you can use a setup function.

        with setup(my_setup_function) as x:

    The function 'my_setup_fuction()' is called and whatever it
    returns or yields can be used as inputs for the block.
    '''

    def random_integers():
        a = random.randint(0, 5)
        b = random.randint(0, 5)
        want = a + b
        return a, b, want

    for i in range(3):
        with check.setup(engage_dilithium_thrusters):
            with check.setup(random_integers) as (a, b, want):
                check.equal(add(a, b), want, 'a,b=', a, b)

# test exceptions
# - Make samples with exceptions in various places, e.g.
#     - inside test that is not expecting it
#     - inside setup
#     - inside teardown
#     - inside testing framework
# ---------------

@test
def exception_during_setup(check):
    '''
    This demonstrates how exceptions raised during setup are handled.
    '''
    def faulty_setup():
        raise ValueError('sample error in setup function')
    
    with check.setup(engage_dilithium_thrusters):
        with check.setup(faulty_setup):
            check.equal(2, 2)

@test
def exception_during_teardown(check):
    '''
    This demonstrates how exceptions raised during setup are handled.
    '''
    def faulty_setup():
        yield
        raise ValueError('sample error in teardown function')
    
    with check.setup(faulty_setup):
        check.equal(2, 2)
    
                
if __name__=='__main__':
#     run_tests([nested])
    run_tests()
