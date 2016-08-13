#! /usr/bin/env python3
import expectorant

def find_test_files():
    return ['sample_test.py']

def run_tests(test_files):
    import sample_test # todo: load test_files instead

    for container_nodes in expectorant._tacc.nodes():
        depth = len(container_nodes)
        test_node = container_nodes[-1]
        print("  " * depth, test_node.name, sep="")
        for test_node in container_nodes:
            if test_node.before: test_node.before()
            if test_node.test_func: test_node.test_func()

if __name__=='__main__':
    run_tests(find_test_files())
