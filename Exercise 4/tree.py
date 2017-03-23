class Node:

    def __init__(self, examples):
        self.__examples = examples
        self.__children = {}

    def add_child(self, edge, child):
        self.__children[edge] = child

    def get_child(self, edge):
        return self.__children[edge]

    def has_children(self):
        return len(self.__children) != 0

    def get_examples(self):
        return self.__examples
