from dtl_help_methods import *
from tree import *

def decision_tree_learning(examples):
    classification = class_check(examples)
    if classification is not None:
        best_gain = max_gain(data)
    tree = Node(best_gain[0], data, None)
