import os
from math import log
from random import randint

def get_examples(traning=True):
    path = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    path += ("training.txt" if traning else "test.txt")
    with open(path) as f:
        return [[int(y) for y in x.strip().split('\t')] for x in f.readlines()]

def get_subsets(examples, attribute):
    subsets = {1: [], 2: []}
    for row in examples:
        subsets[row[attribute]].append(row)
    return (1, subsets[1]), (2, subsets[2])

def is_pure(examples):
    value = examples[0][-1]
    for row in examples:
        if value != row[-1]:
            return False
    return True

def plurality(examples):
    count = {1: 0, 2: 0}
    for row in examples:
        count[row[-1]] += 1
    if count[1] != count[2]:
        return max((count[1], 1), (count[2], 2))[1]
    return randint(1, 2)

def b_entrophy(probabilty):
    if probabilty == 0:
        return probabilty
    else:
        return -((probabilty * log(probabilty, 2)) + ((1.0 - probabilty) * log((1.0 - probabilty), 2)))

def importance(examples, attributes):
    attribute_entropy = {}
    for attribute in attributes:
        count = 0
        for row in examples:
            if row[attribute] == examples[0][attribute]:
                count += 1
        attribute_entropy[attribute] = b_entrophy(count / len(examples))
    minimum = 1.1  # Guaranteed to be bigger than any attribute entropy
    index = None
    for i in attribute_entropy:
        if attribute_entropy[i] < minimum:
            minimum = attribute_entropy[i]
            index = i
    return index
