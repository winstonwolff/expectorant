from copy import copy

from . import ansi



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
    '''
    A leaf in the tree of tests that represents one `it` statement

    containers = parents of this test
    name = human readable description
    test_func = function that executes the test.
    args = Optional extra parameters that are passed to the test function. See example

        >>> def the_test_case(scope, expect): print('the_test_case ran')
        >>> tc = TestCase([], "I am a test case", the_test_case)
        >>> tc.run(None)
        the_test_case ran

    '''
    def __init__(self, containers, name, test_func, args=None):
        super().__init__(containers)
        self.test_func = test_func
        self.args = args if args is not None else ()
        self.name = name.format(*self.args)

    def _format(self, name, args):
        if not args:
            return name
        else:
            return name.format(*args)


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
        self.test_func(scope, expector, *self.args)

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

    def add_test(self, name, test_func, args=None):
        test_node = TestCase(self.stack, name, test_func, args)
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
    def decorator(func):
        _suite.push_container(message)
        func()
        _suite.pop_container()
    return decorator

describe = context

def it(message, repeat=None):
    '''
        #>>> _suite = Suite()
        #>>> @it("I am a test case")
        #... def _(scope, expect): print('Test case ran')
        #>>> for node in _suite.nodes(): print(node)
        #...     if node.is_test(): node.run(None)
        #Test case ran
    '''
#     You can repeat the test with raw data:

#         >>> _suite = Suite()
#         >>> @it("I am a test case", repeat=[(1, 2), (3, 4)])
#         ... def _(scope, expect, alpha, beta):
#         ...    print('Ran with alpha=', alpha, 'beta=', beta)
#         ...
#         >>> for node in _suite.nodes():
#         ...     if node.is_test(): node.run(None)
#         Ran with alpha= 1 beta= 2
#         Ran with alpha= 3 beta= 4
#     '''
    def decorator(func):
        if repeat:
            for set_of_args in repeat:
                _suite.add_test(message, func, set_of_args)
        else:
            _suite.add_test(message, func)
    return decorator

def before(func):
    _suite.current_container().before = func

def after(func):
    _suite.current_container().after = func

