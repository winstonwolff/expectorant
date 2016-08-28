Expectorant - RSpec for Python
==============================

A testing framework for Python 3.5 or later in the style of Ruby's Rspec.  Here
the prominent features:

* __Readable code__ --- Expectorant's syntax is easier to read than `unittest` and
  descriptions of intent are more prominent.

* __Nested before/after functions__ --- it has nested levels of setup/teardown,
  e.g. setup data for the method under test plus setup for each situation you
  want to test under.

* __Repeat a test with different data__ --- There is a built in `repeat` argument to
tests to easily run the same test with different sets of data.

* __Simple custom matchers__ --- It's easy to write your own matcher
  functions to compare you specific data types. A matcher function takes two
  values and returns a description and Pass/Fail.

* __Easy to modify output__ --- Currently there is one output format, but other
  formats such as JUnit XML for integration with CI servers would be easy.

* __A failing check does not abort the test__ --- `unittest` and Rspec use
  assertions to signal a failure. Expectorant does not which means one test
  case can check several outputs and can show several failures.  This was an
  intentional part of Unittest's design---you don't want side effects from one
  expectation distorting the results of another expectation.  But we are all
  adults here---the programmer should be able to decide for herself.  E.g. if
  you are only checking the contents of an immutable return value, there is no
  need run the subject over and over---the output is going to be the same in
  each run.

A simple example of Expectorant style test:

```python
from expectorant import *

@describe('expectorant')                                    # describe, context, before,
def _():                                                    # after, and it, just like RSpec
    scope = None
    @before
    def _():
        nonlocal scope
        scope = Scope()                                     # A new scope every test run
        scope.dict = {'a': 'expectorant is like rspec', 'b': 3}

    @it('supports "expect" syntax similar to rspec')
    def _():
        expect(scope.dict['a']).to(contain, 'rspec')        # expectations are similar to RSpec

    @it('expectations with == != < etc. operators are convenient syntactic sugar')
    def _():
        expect(scope.dict['b']) == 3

    @it('supports rspec\'s great "change" expectation')
    def _():
        expect(scope.dict.clear).to(change, lambda: len(scope.dict), frm=2, to=0)
```

Run all your specs from the command line, e.g. `expectorant [filename | directory]`,
or from a Python script:

```python
import expectorant
expectorant.main()
```

The output looks like this:

<img src="./docs/simple_spec.png" width=537 height=139 />

Also, if you or your child wants to learn electricity, try my game
Electropocalyse at http://stratolab.com/electropocalypse

Requirements
------------
* Python 3.5 --- we use: importlib.util.module_from_spec

Installation
------------

```
pip3 install git+https://github.com/winstonwolff/expectorant/
```

