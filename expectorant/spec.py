from copy import copy

from . import ansi



class Node:
    '''Common behavior for TestNodes and Containers'''
    def __init__(self, containers):
        self.containers = copy(containers)

    def depth(self):
        '''Return how many containers, i.e. describe or contexts, enclose this node.'''
        return len(self.containers)

class TestCase(Node):
    '''
    A leaf in the tree of tests that represents one `it` statement

    containers = parents of this test
    name = human readable description
    test_func = function that executes the test.
    args = Optional extra parameters that are passed to the test function. See example

        >>> def the_test_case(): print('the_test_case ran')
        >>> tc = TestCase([], "I am a test case", the_test_case)
        >>> tc.run()
        the_test_case ran
    '''
    def __init__(self, containers, name, test_func, args=None):
        super().__init__(containers)
        self.test_func = test_func
        self.args = args if args is not None else ()
        self.name = self._format(name, self.args)

    def _format(self, name, args):
        try:
            return name.format(*args)
        except:
            return name + ' -- Warning: could not format this repeating description with args: {})'.format(repr(args))


    def is_container(self): return False

    def is_test(self): return True

    def __repr__(self):
        return "<TestCase:  {}>".format(self.name)

    def run(self):
        # run before funcs
        for c in self.containers:
            assert isinstance(c, Container)
            if c.before: c.before()

        # run the test itself
        self.test_func(*self.args)

        # run after funcs
        for c in reversed(self.containers):
            assert isinstance(c, Container)
            if c.after: c.after()


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

    def context(self, message):
        '''
        Function decorator which adds "context" around a group of TestCases and may have
        a `before` and `after` func.

            >>> s = Suite()
            >>> @s.context('context 1')
            ... def _():
            ...     @s.before
            ...     def _(): print('before 1 called.')
            ...     @s.it('runs a test')
            ...     def _(): print('test case 1 called.')
            >>> @s.context('context 2')
            ... def _():
            ...     @s.before
            ...     def _(): print('before 2 called.')
            ...     @s.it('runs a test')
            ...     def _(): print('test case 2 called.')
            >>> tc1 = list(s.nodes())[2]
            >>> tc1.run()
            before 1 called.
            test case 1 called.
            >>> tc1 = list(s.nodes())[4]
            >>> tc1.run()
            before 2 called.
            test case 2 called.
        '''
        def decorator(context_func):
            self.push_container(message)
            context_func()
            self.pop_container()
        return decorator

    describe = context  # synonym

    def it(self, message, repeat=None):
        '''
        Function decorator which adds a TestCase to the Suite

            >>> s = Suite()
            >>> @s.it('always passes')
            ... def _(): pass
            >>> list(s.nodes())
            [<Container: root>, <TestCase:  always passes>]


        `repeat` will add multiple test cases with extra parameters.

            >>> s = Suite()
            >>> @s.it('a={} b={}', repeat=[(1, 2), (3, 4)])
            ... def _(a, b): pass
            >>> list(s.nodes())
            [<Container: root>, <TestCase:  a=1 b=2>, <TestCase:  a=3 b=4>]
        '''
        def decorator(test_func):
            if repeat:
                for set_of_args in repeat:
                    self.add_test(message, test_func, set_of_args)
            else:
                self.add_test(message, test_func)
        return decorator

    def before(self, func):
        '''
        Function decorator which causes `func` to be run before the test case.

            >>> s = Suite()
            >>> @s.before
            ... def _(): print('before called.')
            >>> @s.it('the test case')
            ... def _(): print('test case called.')
            >>> tc = list(s.nodes())[1]
            >>> tc.run()
            before called.
            test case called.
        '''
        self.current_container().before = func

    def after(self, func):
        self.current_container().after = func

