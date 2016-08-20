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


Let me know your thoughts--is this insane, am I missing an important use-case, what would be a nicer way to write tests?

Also, if you or your child wants to learn electricity, try my game Electropocalyse at http://stratolab.com/electropocalypse

Requirements
------------
* Python 3.5 --- we use: importlib.util.module_from_spec

Installation
------------

```
pip3 install git+https://github.com/winstonwolff/expectorant/
```

