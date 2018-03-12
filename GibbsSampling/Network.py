from Node import Node

#Class for the Bayesian Network
class Network:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.dicNodes = {}

        #Create all the Node Objects
        amenities =     Node("amenities")
        neighborhood =  Node("neighborhood")
        location =      Node("location")
        children =      Node("children")
        age =           Node("age")
        size =          Node("size")
        schools =       Node("schools")
        price =         Node("price")


        #Create all the Node Objects dependencies (parent children etc)
        #Set parents
        location.parents.append(amenities)
        location.parents.append(neighborhood)

        children.parents.append(neighborhood)

        age.parents.append(location)

        schools.parents.append(children)

        price.parents.append(age)
        price.parents.append(location)
        price.parents.append(size)
        price.parents.append(price)

        #Set children
        amenities.children.append(location)

        neighborhood.children.append(location)
        neighborhood.children.append(children)

        location.children.append(age)
        location.children.append(price)

        children.children.append(schools)

        age.children.append(price)

        size.children.append(price)

        schools.children.append(price)

        #Add tables
        amenitiespTable = [0 for x in range(2)]
        #lots=0 little=1
        amenitiespTable[0]=0.3
        amenitiespTable[1]= 1 - amenitiespTable[0]
        amenities.pTable = amenitiespTable

        nbpTable = [0 for x in range(2)]
        #bad=0 good=1
        nbpTable[0]=0.4
        nbpTable[1]= 1 - nbpTable[0]
        neighborhood.pTable = nbpTable

        sizepTable = [0 for x in range(3)]
        # small=0 medium=1 large=2
        sizepTable[0]=0.33
        sizepTable[1]=0.34
        sizepTable[2]=0.33
        size.pTable = sizepTable

        childrenpTable = [[0 for x in range(2)] for y in range(2)]
        #Bad=0 good=1
        childrenpTable[0][0]=0.6
        childrenpTable[0][1]=0.4
        childrenpTable[1][0]=0.3
        childrenpTable[1][1]=0.7
        children.pTable = childrenpTable

        schoolspTable = [[0 for x in range(2)] for y in range(2)]
        #Bad=0 good=1
        schoolspTable[0][0]=0.7
        schoolspTable[0][1]=0.3
        schoolspTable[1][0]=0.8
        schoolspTable[1][1]=0.2
        schools.pTable = schoolspTable

        agepTable = [[0 for x in range(3)] for y in range(3)]
        #Old, 0=bad 1=good 2=ugly
        agepTable[0][0]=0.6
        agepTable[1][0]=0.3
        agepTable[2][0]=0.9
        #New
        agepTable[0][1]=0.4
        agepTable[1][1]=0.7
        agepTable[2][1]=0.1
        age.pTable = agepTable


        locationpTable = [[[0 for k in xrange(3)] for j in xrange(3)] for i in xrange(3)]
        #lots=0 bad=0
        #little=1 good=1

        #Bad=0
        locationpTable[0][0][0]=0.4
        locationpTable[0][1][0]=0.15
        locationpTable[1][0][0]=0.4
        locationpTable[1][1][0]=0.35

        #Good=1
        locationpTable[0][0][1]=0.3
        locationpTable[0][1][1]=0.8
        locationpTable[1][0][1]=0.2
        locationpTable[1][1][1]=0.5

        #Ugly=2
        locationpTable[0][0][2]=0.3
        locationpTable[0][1][2]=0.05
        locationpTable[1][0][2]=0.4
        locationpTable[1][1][2]=0.15

        #Missing last table [][][][][]

        #Add created nodes into self.nodes list
        self.nodes.append(amenities)
        self.nodes.append(neighborhood)
        self.nodes.append(location)
        self.nodes.append(children)
        self.nodes.append(age)
        self.nodes.append(size)
        self.nodes.append(schools)
        self.nodes.append(price)

        #Hashmaps
        self.dicNodes = dict([ (n.name, n) for n in self.nodes ])

    #Query
    def query(self, nodeQuery):
        node = self.dicNodes.get(nodeQuery)
        print("Performing Query of " + node.name)


        #Performing markov blanket
        parents = node.parents
        children = node.children
        childrenParents = []
        for curNode in children:
            for curParent in curNode.parents:
                if curParent is not node:
                    childrenParents.append(curParent)

        print("The Markov Blanket if this query is")
        print("Parents")
        self.printNodeList(parents)
        print("Children")
        self.printNodeList(children)
        print("Children Parents")
        self.printNodeList(childrenParents)

    #Prints the name of the list of nodes
    def printNodeList(self, list):
        str = ""
        #add all of the node's names to the string
        for curNode in list:
            str += curNode.name + ", "
        print(str)

    def printingNetwork(self):
        print("Prining the network")
        myNodes = self.nodes

        for curNode in myNodes:
            print("Evaluating the node: " + curNode.name)
            curChildren = curNode.children
            curParents = curNode.parents

            #Print the parents of the node
            parentStr = ""
            for curNode in curParents:
                parentStr += curNode.name + ", "
            print("Parents: " + parentStr)

            #Print the children of the nodes
            childStr = ""
            for curNode in curChildren:
                childStr += curNode.name + ", "
            print("Children: " + childStr)

    def setChildrenParents(self):
        print("Setting all children parents")

    def printingNetworkMaps(self):
        print("Prining the network using maps")
        myNodes = self.dicNodes

        for curNode in myNodes.itervalues():
            print("Evaluating the node: " + curNode.name)
            curChildren = curNode.children
            curParents = curNode.parents

            #Print the parents of the node
            parentStr = ""
            for curNode in curParents:
                parentStr += curNode.name + ", "
            print("Parents: " + parentStr)

            #Print the children of the nodes
            childStr = ""
            for curNode in curChildren:
                childStr += curNode.name + ", "
            print("Children: " + childStr)
