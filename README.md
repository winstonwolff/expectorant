# RSpec for Python


## A simple example
```python
from expectorant import *

@describe("dict")
def _():

    @before
    def _(scope, expect):
        scope.dict = {"a": 1}

    @it("retrieves by key")
    def _(scope, expect):
        expect.is_equal(scope.dict["a"], 1)
```


Let me know your thoughts--is this insane, am I missing an important use-case, what would be a nicer way to write tests?

Also, if you or your child wants to learn electricity, try my game Electropocalyse at http://stratolab.com/electropocalypse
