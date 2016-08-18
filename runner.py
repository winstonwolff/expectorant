#! /usr/bin/env python3
import expectorant
import ansi

# def find_test_files():
#     return ['sample_test.py']

def load_tests():
    import sample_test # todo: load test_files instead
    return expectorant._tacc

def run_one_test(test_node):
    assert isinstance(test_node, expectorant.TestCase)

    # run before funcs
    for c in test_node.containers:
        assert isinstance(c, expectorant.Container)
        if c.before: c.before()

    # run the test itself
    expect = expectorant.ExpectationTester(test_node)
    test_node.test_func(expect)

    # run after funcs
    for c in test_node.containers:
        assert isinstance(c, expectorant.Container)
        if c.after: c.after()

    return expect.results


def run_tests(test_accumulator):
    for node in test_accumulator.nodes():
        print("  " * node.depth(), node.name, sep="")
        if node.is_test():
            test_results = run_one_test(node)
            for result in test_results:
                color = ansi.GREEN if result.passing else ansi.RED
                print(color, "  " * (node.depth() + 1), result.description, ansi.RESET, sep="")

if __name__=='__main__':
    test_tree = load_tests()
    test_tree.debug_print()
    print('---')
    run_tests(test_tree)
