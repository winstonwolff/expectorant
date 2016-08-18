#! /usr/bin/env python3
import expectorant
import ansi

# def find_test_files():
#     return ['sample_test.py']

def load_tests():
    import sample_test # todo: load test_files instead
    return expectorant._suite


def run_tests(test_accumulator):
    for node in test_accumulator.nodes():
        print("  " * node.depth(), node.name, sep="")
        if node.is_test():
            checker = expectorant.Checker(node)
            for result in checker.results:
                color = ansi.GREEN if result.passing else ansi.RED
                print(color, "  " * (node.depth() + 1), result.description, ansi.RESET, sep="")

if __name__=='__main__':
    test_tree = load_tests()
#     test_tree.debug_print()
#     print('---')
    run_tests(test_tree)
