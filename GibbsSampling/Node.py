from random import random

#Class for the Nodes that will go inside the Bayesian Network
class Node:
    def __init__(self, name, possibleValues):
        self.name = name
        self.parents = []
        self.children = []
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

        #Assigns the currentValue
        self.naiveBayes()

        #append value after reached deleting count
        if self.iterations > self.deleteCnt:
            self.valueList.append(self.currentValue)

    #Sets the current value based on the formula, ranges and random numb
    def naiveBayes(self):
        #Number of possible outcomes
        size = len(self.possibleValues)

        #Store the probabilites
        probabilities = []

        #Loop 2 times to get 2 probabilities (0, 1)
        for i in xrange(size):

            #The probability to be added into probabilities
            curProb = 1.0
            currString = ""


            #Loop to get parents information dependencies
            for curParent in self.parents:
                #Get the value as a number
                value = curParent.currentValue
                #Get the name and append it
                currString += curParent.numToString(value)
                currString += " "

            #Add the current node string
            currString += self.numToString(i)
            currString += " "
            # print(currString)

            toMultiplySelf= self.pTableDic.get(currString)
            # print("Trying to get from table " + self.name + " The String:" + currString + "End" )
            # print(toMultiplySelf)

            #Add the first piece of information
            curProb *= toMultiplySelf


            #Loop to get the number of children
            for curChildren in self.children:
                #From the children we need to know the parents info
                string = ""
                for curParent in curChildren.parents:
                    #Get the value as a number
                    value = curParent.currentValue
                    #You don't want your own value twice therefore you put i (the current value in the loop)
                    if(curParent.name == self.name):
                        value = i

                    #Get the name and append it
                    string += curParent.numToString(value)
                    string += " "

                #We now have the string missing the current node
                childValue =curChildren.currentValue
                string += curChildren.numToString(childValue)
                string += " "
                # print("Trying to get from table " + curChildren.name + " The String:" + string + "End" )
                # print(curChildren.pTableDic.get(string))
                #get the number from the table
                toMultiply = curChildren.pTableDic.get(string)

                #Add the next piece of information
                curProb *= toMultiply

            #Now append the curProb
            probabilities.append(curProb)



        #Get the normalization factor
        sum = 0.0
        for x in probabilities:
            sum += x

        #Set new probabilities
        for i, val in enumerate(probabilities):
            probabilities[i] = val/sum

        #Making sure the probabilities add to 1
        # print("Printing Probabilities!!!")
        # for x in probabilities:
        #         print(x)


        #Random number
        randValue = random()

        #Set the current Value randomly
        totalProb = 0
        for i in xrange(len(self.possibleValues)):
            totalProb += probabilities[i]
            if(randValue <= totalProb):
                self.currentValue = i
                break



    #This function calculates the probabilty of the node which was query
    def calcFinalProb(self):
        if(len(self.valueList) < 1):
            print('Not enough updates to overcome count of updates to delete.')
            return -1

        #Loop through all possible values and count them and with that print
        for x in xrange(len(self.possibleValues)):
            numCnt = self.valueList.count(x)

            #print('P('+self.name+' = '+self.possibleValues[x]+') = ' + str(numCnt/len(self.valueList)))
            print('P('+self.name+' = '+self.possibleValues[x]+') = ' + str(float(numCnt)/float(len(self.valueList))))



    #Converts a number to a string
    def numToString(self, index):
        return self.possibleValues[index]

    #Converts a string to a number
    def stringToNum(self, string):
        #Loop through the possible values and get the correct index
        for i in xrange(len(self.possibleValues)):
            if(self.possibleValues[i] == string):
                return i
        else:
            return -1
