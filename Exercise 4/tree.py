class Node:

    def __init__(self, examples):
        self.examples = examples
        self.children = {}

    def add_child(self, edge, child):
        self.children[edge] = child

    def get_child(self, edge):
        return self.children[edge]

    def has_children(self):
        return len(self.children) != 0

    def get_examples(self):
        return self.examples
