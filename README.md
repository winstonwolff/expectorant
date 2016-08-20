RSpec for Python
================

A simple example

```python
from expectorant import *

@describe("expectorant")
def _():

    @before
    def _(scope, expect):
        scope.dict = {"a": 1}

    @it("supports expectations with == != < etc. operators")
    def _(scope, expect):
        expect(scope.dict["a"]) == 1

    @it("supports expectations on raising exceptions")
    def _(scope, expect):
        def subject(): scope.dict["x"]
        expect(subject).to(raise_error, KeyError)
```

Let me know your thoughts--is this insane, am I missing an important use-case, what would be a nicer way to write tests?

Also, if you or your child wants to learn electricity, try my game Electropocalyse at http://stratolab.com/electropocalypse

Requirements
------------
* Python 3.5 --- we use: importlib.util.module_from_spec

Installation
------------

> pip3 install git+https://github.com/winstonwolff/expectorant/

