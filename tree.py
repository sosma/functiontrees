from random import choice as rc
from random import randint as ri
from random import random
from anytree import Node, RenderTree, PreOrderIter

class treeNode(Node):
    separator = "|"

class Tree:
    def __init__(self, complexity, variables):
        self.numrange = 5
        self.complexity = complexity
        self.variables = variables
        self.operations = {"+" : 2, "-" : 2, "*" : 2, "/" : 2}
        self.base = treeNode(self.get_operation())
        self.nodes = [self.base]

    def create_nodes(self, parent):
        if random() > 0.4 and self.depth(parent) <= self.complexity:
            node1 = treeNode(self.get_operation(), parent=parent)
            node2 = treeNode(self.get_operation(), parent=parent)
            self.nodes.append(node1)
            self.nodes.append(node2)
            self.create_nodes(node1)
            self.create_nodes(node2)
        else:
            self.nodes.append(treeNode(random()*self.numrange, parent=parent))
            self.nodes.append(treeNode(random()*self.numrange, parent=parent))

    def tree_values(self):
        return [node.name for node in PreOrderIter(self.base)]

    def get_operation(self):
        return rc(list(self.operations.keys()))

    def depth(self, node):
        return len(str(node).split("|"))

    def draw(self):
        print(RenderTree(self.base))

    def resolve(self):
        numbcount = 0
        i = -1
        val = self.tree_values()
        while True:
            i+=1
            if val[i] not in self.operations:
                numbcount += 1
            else:
                numbcount = 0
            if numbcount == 2:
                op = val.pop(i-2)
                val1 = val.pop(i-2)
                val2 = val.pop(i-2)
                if val2 == 0 and op == "/":
                    val2 = 1
                newval = eval(str(val1)+op+str(val2))
                val = val[:i-2] + [newval] + val[i-2:]
                i=-1
            if len(val) == 1:
                return(val[0])
