import ansi

# TestResult = namedtuple("TestResult", 'passing test_nodes')

class ExpectationTester:
    def __init__(self):
        self.results = []

    def is_equal(self, a, b, msg=""):
        is_passing = (a == b)
        if is_passing:
            color = ansi.GREEN
            outcome = "pass"
        else:
            color = ansi.RED
            outcome = "fail"
        print(color + "is_equal", msg, outcome, ansi.RESET)

class TestNode:
    def __init__(self, name, test_func):
        self.name = name
        self.test_func = test_func
        self.before = None
        self.children = []


class TestAccumulator:
    def __init__(self):
        self.stack = [TestNode("root", None)]

    def push_container(self, name):
        test_node = self.append(name, None)
        self.stack.append(test_node)
        print("  "*len(self.stack), "push container:", name)

    def pop_container(self):
        self.stack.pop()

    def append(self, name, test_func):
        test_node = TestNode(name, test_func)
        self.current_node().children.append(test_node)
        print("  "*len(self.stack), "added test:", name)
        return test_node

    def current_node(self):
        return self.stack[-1]

    def nodes(self, container_nodes=(), test_node=None):
        '''yields all the tests in the tree'''
        test_node = test_node or self.stack[0]
        for n in test_node.children:
            lineage = container_nodes + (n,)
            yield (lineage)
            yield from self.nodes(lineage, n)

_tacc = TestAccumulator()


def describe(message):
    def wrapper(func):
        _tacc.push_container(message)
        func()
        _tacc.pop_container()
    return wrapper

def context(message):
    def wrapper(func):
        _tacc.push_container(message)
        func()
        _tacc.pop_container()
    return wrapper

def it(message):
    def wrapper(func):
        _tacc.append(message, func)
    return wrapper

def before(func):
    _tacc.current_node().before = func


