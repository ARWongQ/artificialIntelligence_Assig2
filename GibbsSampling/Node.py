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
        # self.currentValue = 0
        
        

        if self.iterations > self.deleteCnt:
            self.valueList.append(self.currentValue)


    def calcFinalProb(self):
        if(len(self.valueList) < 1):
            print('Not enough updates to overcome count of updates to delete.')
            return -1

        for x in xrange(len(self.possibleValues)):
            numCnt = self.valueList.count(x)
            print('P('+self.name+' = '+self.possibleValues[x]+') = ' + str(numCnt/len(self.valueList)))








