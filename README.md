Experimenting with a new Unit Testing framework
===============================================

UnitTesting is great but I don't love python's unittest.TestCase. It
feels awkward compared to Ruby's rspec and it also feels like it was
grafted from Java. I know that in Nose, there is no need to write a
class if you don't need a setup() or teardown() which is a nice
simplification. But I have another thing I often need when testing:
running a test with a set of inputs. I don't know a good way to do
this with unittest. Nose has a way but it seems awkward again. So
here's an attempt to re-think unittesting.


Simple Example
--------------
Here a simple example--not that much different from a unittest or Nose
test. Notice that the test case is not a class though--just a
function. 

    def add(a, b):
        return a + b

    @test
    def simple_test(check):
        check.equal(add(1, 1), 2, 'should add 1 and 1')

Output looks like this:

    simple_test
      should add 1 and 1                      2 == 2 [OK] 


Parameterized Tests
-------------------
Here's a more exciting example--something that is difficult to do
with unittest.TestCase--test one function with a whole set of
inputs and expected outputs. In unittest, you can write a function
that does all these tests but the testing stops with the first
failure. Here, all the tests will run and report failures. Not the
parameters to check.equal() can take multiple parameters after your
two test values and they will be printed out with spaces between
each paramater, just like with print()

    @test
    def parameterized_test(check):
        for a, b, e in (
            [1, 1, 99],
            [2, 2, 4],
            [3, 4, 99]
        ):
            check.equal(add(a, b), e, 'adding', a, b)

Output looks like this:

    parameterized_test
      adding 1 1                           2 == 99 [FAIL]
      adding 2 2                            4 == 4 [OK]
      adding 3 4                           7 == 99 [FAIL]

Proper Setup/Teardown for each Test
-----------------------------------
In the above example, one test function made several tests. The
unittest rationale for not doing that is that each test should be
independent to keep side-effects from messing with your tests. The
add() function has no side-effects so it was not a problem. But what
if there is a more complicated setup or a function with sideaffects so
each check must be independent?

Here's a function that has a strong side-effect so each run must be
independent.

    _acc = 0
    def accumulate(a):
        global _acc
        _acc += a

    def reset():
        global _acc
        _acc = 0

    @test
    def accumulate_test(check):

        @test_setup
        def zeroed_accumulator():
            reset()

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

Output:

    accumulate_test
      zeroed_accumulator
        inputs= (1, 1)                        2 == 2 [OK]
      zeroed_accumulator
        inputs= (2, 3)                        5 == 5 [OK]
      zeroed_accumulator
        inputs= (1, 2, 3, 4)                10 == 10 [OK]

Conclusion
----------

This is an experiment in making a new style of unittesting framework for python. My goals are: 
 * allow easy parameterized tests
 * more succinct code, e.g. no classes to define, setup uses regular functions so programmer can choose if setup is for ever test or just once
 * nice looking output, especially for complex tests that have many
   setup steps.

Let me know your thoughts--is this insane, am I missing an important use-case, what would be a nicer way to write tests?

Also, if you or your child wants to learn electricity, try my game Electropocalyse at http://electropocalypse.com

