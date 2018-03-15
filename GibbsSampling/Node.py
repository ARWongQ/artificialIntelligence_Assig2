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
        self.pTableDic = None

    #Sets the specific value based on the Markov blanket of the node its probability and a random number
    def assignValue(self):
        self.iterations+=1
        name = self.name


        # this will be changed
        # self.currentValue = 0


        if(name == "amenities"):
            print("checking amenities")
            self.amenitiesMath2()

        elif(name == "neighborhood"):
            print("checking neighborhood")

        elif(name == "location"):
            print("checking location")

        elif(name == "children"):
            print("checking children")

        elif(name == "age"):
            print("checking age")

        elif(name == "size"):
            print("checking size")

        elif(name == "schools"):
            print("checking schools")

        elif(name == "price"):
            print("checking price")


        #append value after reached deleting count
        if self.iterations > self.deleteCnt:
            self.valueList.append(self.currentValue)

    #Sets the current value based on the formula, ranges and random numb
    def amenitiesMath(self):
        print("Calculating Amenities")
        #MAGIC
        #the range [] //to get it we need the function
        #the random number to pick to set the currentValue

        #Number of possible outcomes
        size = len(self.possibleValues)
        childrenNum = len(self.children)
        parentNum= len(self.children)
        childrenParentNum = len(self.childrenParents)

        #Store the probabilites
        probabilities = []
        stringsOfEvidence = []

        #My Table
        currpTableDic = self.pTableDic
        #Loop 2 times to get 2 probabilities (0, 1)
        for i in xrange(size):
            currString = self.numToString(i)

            #Now get location prob
            for curNode in self.children:
                print()

            currProb = currpTableDic.get(currString)
            probabilities.append(currProb)


    #Uses a map instead of array
    def amenitiesMath2(self):
        myTable = self.pTableDic
        locationTable = self.children[0].pTableDic
        locationCV = self.children[0].currentValue
        neighborhoodCV = self.children[0].parents[0].currentValue

        aLotsTemp = myTable.get("lots") * locationTable.get("lots bad bad ")
        aLittleTemp = myTable.get("little") * locationTable.get("little bad bad ")

        alpha= aLotsTemp + aLittleTemp

        aLots = aLotsTemp/alpha
        aLittle = aLittleTemp/alpha

        print(aLots)
        print(aLittle)

    #This function calculates the probabilty of the node which was query
    def calcFinalProb(self):
        if(len(self.valueList) < 1):
            print('Not enough updates to overcome count of updates to delete.')
            return -1

        #Loop through all possible values and count them and with that print
        for x in xrange(len(self.possibleValues)):
            numCnt = self.valueList.count(x)
            print('P('+self.name+' = '+self.possibleValues[x]+') = ' + str(numCnt/len(self.valueList)))



    #Converts a number to a string
    def numToString(self, index):
        print("Converting to String")
        return self.possibleValues[index]

    #Converts a string to a number
    def stringToNum(self, string):
        print("Converting to Num")

        for i in xrange(len(self.possibleValues)):
            if(self.possibleValues[i] == string):
                return i
        else:
            return -1
