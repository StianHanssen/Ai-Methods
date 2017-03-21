class Node:

    def __init__(self, data):
        self.__data = data
        self.__children = {}

    def add_child(self, edge, child):
        self.__children[edge] = child

    def print_tree(self):
        if not self.__children:
            return "[" + str(self.__data) + "]"
        else:
            temp = "[" + str(self.__data) + " "
        for key, _ in self.__children.items():
            temp += self.__children[key].print_tree()
        return temp + "]"
