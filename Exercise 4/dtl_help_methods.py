import os
from math import log
from random import randint

def get_examples(traning=True):  # Uses relative path to import data into 2D list
    path = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    path += ("training.txt" if traning else "test.txt")
    with open(path) as f:
        return [[int(y) for y in x.strip().split('\t')] for x in f.readlines()]

def get_subsets(examples, attribute):  # Split examples into the children blonging to attribute
    subsets = {1: [], 2: []}
    for row in examples:
        subsets[row[attribute]].append(row)
    return (1, subsets[1]), (2, subsets[2])

def is_pure(examples):  # Check if all values in examples have the same class
    value = examples[0][-1]
    for row in examples:
        if value != row[-1]:
            return False
    return True

def plurality(examples):  # In case of noisy sets in which one can not have a pure set this will pick the most common value or random if it fails at that
    count = {1: 0, 2: 0}
    for row in examples:
        count[row[-1]] += 1
    if count[1] != count[2]:
        return max((count[1], 1), (count[2], 2))[1]
    return randint(1, 2)

def b_entrophy(probabilty):  # Caluclates the boolean random variable given on page 704 in the book
    if probabilty == 0 or probabilty == 1:
        return 0
    else:
        return -((probabilty * log(probabilty, 2)) + ((1.0 - probabilty) * log((1.0 - probabilty), 2)))

def importance(examples, attributes):  # Picks attribute accourding to importance described in lectures
    attribute_entropy = {}
    for attribute in attributes:
        count = 0
        for row in examples:
            if row[attribute] == examples[0][attribute]:
                count += 1
        attribute_entropy[attribute] = b_entrophy(count / len(examples))
    pair = (1.1, None)
    for i in attribute_entropy:
        pair = min(pair, (attribute_entropy[i], i))
    return pair[1]

def classify(root, row):  # Moves down tree accourding to row until leaf node is reached
    current = root
    while current.has_children():
        current = current.get_child(row[current.get_examples()])
    return current.get_examples()
