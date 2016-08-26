RSpec for Python
================

A simple example

```python
from expectorant import *

@describe("expectorant")                                    # describe, context, before,
def _():                                                    # after, and it, just like RSpec

    @before
    def _(scope, expect):                                   # 'scope' is for holding values
        scope.dict = {"a": 1}                               # from before to it clauses.

    @it("supports expectations with == != < etc. operators")
    def _(scope, expect):
        expect(scope.dict["a"]) == 1                        # expectations are similar to RSpec

    @it("supports expectations on raising exceptions")
    def _(scope, expect):
        def subject(): scope.dict["x"]                      # change and raise_error matchers take functions
        expect(subject).to(raise_error, KeyError)
```
See the examples directory, e.g. [sample_spec.py](examples/sample_spec.py)

Assuming your spec files are in the `specs` directory, you can run all specs with:

```python3 -m expectorant```


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

