from dtl_help_methods import *
from tree import *


def decision_tree_learinng(examples, attributes, parent_examples, random=False):
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
            child = decision_tree_learinng(subset, list(attributes), examples, random)
            node_picked.add_child(i + 1, child)
    return node_picked

def main():
    test = get_examples(False)
    training = get_examples()

    tree = decision_tree_learinng(training, list(range(len(training[0])-1)), [], False)
    print(tree.print_tree())
    print("random: ")
    tree = decision_tree_learinng(training, list(range(len(training[0])-1)), [], True)
    print(tree.print_tree())


main()  # Vizualize at http://ironcreek.net/phpsyntaxtree/
