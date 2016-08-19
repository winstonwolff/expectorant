from copy import copy
from collections import namedtuple

import ansi

TestResult = namedtuple("TestResult", 'passing description')

class Expector:
    '''
    Runs one test case and all it's before/after functions and collects the
    `results`.
    '''
    def __init__(self):
        self.results = []

    def is_equal(self, a, b, msg=None):
        is_passing = (a == b)

        msgs = ["is_equal: expect {} == {}".format(a, b)]
        if msg: msgs.append(msg)

        self.results.append(TestResult(is_passing, ' '.join(msgs)))


class Node:
    '''Common behavior for TestNodes and Containers'''
    def __init__(self, containers):
        self.containers = copy(containers)

    def depth(self):
        '''Return how many containers, i.e. describe or contexts, enclose this node.'''
        return len(self.containers)

class Scope:
    '''A place for specs to store values during the test run.'''
    pass

class TestCase(Node):
    '''A leaf in the tree of tests that represents one `it` statement'''
    def __init__(self, containers, name, test_func):
        super().__init__(containers)
        self.name = name
        self.test_func = test_func

    def is_container(self): return False

    def is_test(self): return True

    def __repr__(self):
        return "<TestCase:  {}>".format(self.name)

    def run(self, expector):
        scope = Scope()

        # run before funcs
        for c in self.containers:
            assert isinstance(c, Container)
            if c.before: c.before(scope, expector)

        # run the test itself
        self.test_func(scope, expector)

        # run after funcs
        for c in reversed(self.containers):
            assert isinstance(c, Container)
            if c.after: c.after(scope, expector)


class Container(Node):
    '''A node in the tree of tests that represents one `context` or `describe` branch.'''
    def __init__(self, containers, name):
        super().__init__(containers)
        self.name = name
        self.before = None
        self.after = None
        self.children = []

    def __repr__(self):
        return "<Container: {}>".format(self.name)

    def is_container(self): return True

    def is_test(self): return False


class Suite:
    '''Builds tree of tests and their contexts'''
    def __init__(self):
        self.stack = [Container([], "root")]

    def push_container(self, name):
        container = Container(self.stack, name)
        self.current_container().children.append(container)
        self.stack.append(container)

    def pop_container(self):
        self.stack.pop()

    def add_test(self, name, test_func):
        test_node = TestCase(self.stack, name, test_func)
        self.current_container().children.append(test_node)
        return test_node

    def current_container(self):
        return self.stack[-1]

    def nodes(self, node=None):
        '''walks through tree and yields each node'''
        if node is None:
            for root in self.stack:
                yield from self.nodes(root)
        else:
            yield node
            if node.is_container():
                for child in node.children:
                    yield from self.nodes(child)

    def debug_print(self):
        '''Print tree'''

        def print_node(node, depth=0):
            print('{}{}'.format('  ' * depth, repr(node)))
            if node.is_container():
               for child in node.children:
                   print_node(child, depth + 1)

        for root in self.stack:
            print_node(root)

_suite = Suite()

def context(message):
    def wrapper(func):
        _suite.push_container(message)
        func()
        _suite.pop_container()
    return wrapper

describe = context

def it(message):
    def wrapper(func):
        _suite.add_test(message, func)
    return wrapper

def before(func):
    _suite.current_container().before = func

def after(func):
    _suite.current_container().after = func

