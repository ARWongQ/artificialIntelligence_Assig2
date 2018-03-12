#Class for the Nodes that will go inside the Bayesian Network
class Node:
    def __init__(self, name, possibleValues):
        self.name = name
        self.parents = []
        self.children = []
        self.childrenParents = []
        self.evidence = False
        self.currentValue = 0
        self.valueList = []
        self.possibleValues = possibleValues
        self.deleteCnt = 0
        self.iterations = 0
        self.pTable = None

    def assignValue(self):
        self.iterations+=1

        # this will be changed
        self.currentValue = 0

        if self.iterations > self.deleteCnt:
            self.valueList.append(self.currentValue)


    def calcProb(self):
        if(len(self.valueList) < 1):
            return -1

        zeroCnt = self.valueList.count(0)
        oneCnt = self.valueList.count(1)
        twoCnt = self.valueList.count(2)






