from dtl_help_methods import *
from tree import *


def decision_tree_learinng(examples, attributes, parent_examples, random=False):  # Algorithm accourding to page 702 in the book
    if not examples:
        return Node(plurality(parent_examples))
    elif is_pure(examples):
        return Node(examples[0][-1])
    elif not attributes:
        return Node(plurality(examples))
    else:
        if random:
            A = attributes[randint(0, len(attributes)-1)]
        else:
            A = importance(examples, attributes)
        node_picked = Node(A)
        attributes.remove(A)
        for i, subset in get_subsets(examples, A):
            child = decision_tree_learinng(subset, attributes, examples, random)
            node_picked.add_child(i, child)
    return node_picked

def test(node, examples):  # Checks if the classification given by the tree matches data
    correct_tests = 0
    for row in examples:
        if row[-1] == classify(node, row):
            correct_tests += 1
    return correct_tests / len(examples)

def main():
    test_examples = get_examples(False)
    training_examples = get_examples()

    root = decision_tree_learinng(training_examples, list(range(len(training_examples[0])-1)), [], True)
    print("Result:", test(root, test_examples), r"% correct")


main()
