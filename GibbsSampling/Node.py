#Class for the Nodes that will go inside the Bayesian Network
class Node:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.childrenParents = []
        self.evidence = False
        self.currentValue = 0
        self.iterations = 0
        self.pTable = None
