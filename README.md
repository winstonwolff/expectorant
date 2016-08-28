RSpec for Python
================

A simple example

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

Run all your specs from the command line or from a python script
```
expectorant [filename | directory]
```

```python
import expectorant
expectorant.main()
```

<img src="./docs/simple_spec.png" width=537 height=139 />

Let me know your thoughts--is this insane, am I missing an important use-case,
what would be a nicer way to write tests?  In particular, I'd like how the only
shared global is this library is the list of test functions. I.e. `scope` and
`expect` are not globals but are passed in to the tests as they are run.
However it is tedious to write them for each @before and @it clause. Is there
another way to do this?

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

