import os
from math import log

def get_examples(traning=True):
    path = os.path.dirname(os.path.abspath(__file__)) + "\\data\\"
    path += ("training.txt" if traning else "test.txt")
    with open(path) as f:
        for line in f:
            content = f.readlines()
            content = [[int(y) for y in x.strip().split('\t')] for x in content]
            return content

def get_subsets(examples, attribute):
    subsets = {1: [], 2: []}
    for row in examples:
        subsets[row[attribute]].append(row[:attribute] + row[attribute + 1:])
    return (subsets[1], subsets[2])

def attribute_value(examples):
    classes = {1: 0, 2: 0}
    for row in examples:
        classes[row[-1]] += 1
    return (classes[1], classes[2])

def entrophy(example):
    pos, neg = attribute_value(example)
    total = pos + neg
    pos, neg = pos/total, neg/total
    part1 = 0
    part2 = 0
    if pos > 0:
        part1 = - pos * log(pos, 2)
    if neg > 0:
        part2 = - neg * log(neg, 2)
    return part1 + part2

def information_gain(examples, attribute):
    total_entrophy = entrophy(examples)
    total_len = len(examples)
    summation = 0
    for subset in get_subsets(examples, attribute):
        summation += (len(subset) / total_len) * entrophy(subset)
    return total_entrophy - summation

def max_gain(examples):
    max_gain = (-1, -1)
    for i in range(len(examples[0]) - 1):
        max_gain = max(max_gain, (information_gain(examples, i), i))
    return max_gain

def class_check(example):
    value = examples[0]
    for row in example:
        if value != row:
            return None
    return value
