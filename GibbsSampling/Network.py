from Node import Node

#Class for the Bayesian Network
class Network:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.dicNodes = {}

        #Create all the Node Object
        amenitiesOp = []
        amenitiesOp.append("Lots")
        amenitiesOp.append("Little")
        amenities =     Node("amenities", amenitiesOp)

        neighborhoodOp = []
        neighborhoodOp.append("Bad")
        neighborhoodOp.append("Good")
        neighborhood =  Node("neighborhood", neighborhoodOp)

        locationOp = []
        locationOp.append("Bad")
        locationOp.append("Good")
        locationOp.append("Ugly")
        location =      Node("location", locationOp)

        childrenOp = []
        childrenOp.append("Bad")
        childrenOp.append("Good")
        children =      Node("children", childrenOp)

        ageOp = []
        ageOp.append("Old")
        ageOp.append("New")
        age =           Node("age", ageOp)

        sizeOp = []
        sizeOp.append("Small")
        sizeOp.append("Medium")
        sizeOp.append("Large")
        size =          Node("size", sizeOp)

        schoolsOp = []
        schoolsOp.append("Bad")
        schoolsOp.append("Good")
        schools =       Node("schools", schoolsOp)

        priceOp = []
        priceOp.append("Cheap")
        priceOp.append("Ok")
        priceOp.append("Expensive")
        price =         Node("price", priceOp)


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

        #Variables for the tables
        lots= 0
        little= 1

        bad=0
        good=1
        ugly=2

        small=0
        medium=1
        large=2

        cheap=0
        ok=1
        expensive=2

        old=0
        new=1

        #Add tables
        amenitiespTable = [0 for x in range(2)]
        #lots=0 little=1
        amenitiespTable[lots]=0.3
        amenitiespTable[little]= 1 - amenitiespTable[0]
        amenities.pTable = amenitiespTable

        nbpTable = [0 for x in range(2)]
        #bad=0 good=1
        nbpTable[bad]=0.4
        nbpTable[good]= 1 - nbpTable[0]
        neighborhood.pTable = nbpTable

        sizepTable = [0 for x in range(3)]
        # small=0 medium=1 large=2
        sizepTable[small]=0.33
        sizepTable[medium]=0.34
        sizepTable[large]=0.33
        size.pTable = sizepTable

        childrenpTable = [[0 for x in range(2)] for y in range(2)]
        #Neighborhood: index1
        #Children: index2
        childrenpTable[bad][bad]=0.6
        childrenpTable[bad][good]=0.4
        childrenpTable[good][bad]=0.3
        childrenpTable[good][good]=0.7
        children.pTable = childrenpTable

        schoolspTable = [[0 for x in range(2)] for y in range(2)]
        # children: index1
        # schools: index2
        schoolspTable[bad][bad]=0.7
        schoolspTable[bad][good]=0.3
        schoolspTable[good][bad]=0.8
        schoolspTable[good][good]=0.2
        schools.pTable = schoolspTable

        agepTable = [[0 for x in range(3)] for y in range(3)]
        #location :index1
        #age :index2
        agepTable[0][0]=0.6
        agepTable[1][0]=0.3
        agepTable[2][0]=0.9

        agepTable[0][1]=0.4
        agepTable[1][1]=0.7
        agepTable[2][1]=0.1
        age.pTable = agepTable


        locationpTable = [[[0 for k in xrange(3)] for x in xrange(3)] for y in xrange(3)]
        #amenities :index1
        #neighborhood :index2
        #location :index3

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

        #Price table [][][][][]
        #location: index1 #bad=0, good=1, ugly= 2
        #age: index2 #old=0 new=1
        #schools: index3 #bad=0, good=1
        #size : index4 #small=0, medium=1, large=2
        #price: index5 #cheap=0, ok=1, expensive=2
        pricepTable = [[[[[0 for k in xrange(3)] for x in xrange(3)] for y in xrange(3)] for j in xrange(3)] for i in xrange(3)]
        pricepTable[good][old][bad][small][cheap] = 0.5
        pricepTable[good][old][bad][medium][cheap] = 0.4
        pricepTable[good][old][bad][large][cheap] = 0.35
        pricepTable[good][old][good][small][cheap] = 0.4
        pricepTable[good][old][good][medium][cheap] = 0.35
        pricepTable[good][old][good][large][cheap] = 0.3
        pricepTable[good][new][bad][small][cheap] = 0.45
        pricepTable[good][new][bad][medium][cheap] = 0.4
        pricepTable[good][new][bad][large][cheap] = 0.35
        pricepTable[good][new][good][small][cheap] = 0.25
        pricepTable[good][new][good][medium][cheap] = 0.2
        pricepTable[good][new][good][large][cheap] = 0.1
        pricepTable[bad][old][bad][small][cheap] = 0.7
        pricepTable[bad][old][bad][medium][cheap] = 0.65
        pricepTable[bad][old][bad][large][cheap] = 0.65
        pricepTable[bad][old][good][small][cheap] = 0.55
        pricepTable[bad][old][good][medium][cheap] = 0.5
        pricepTable[bad][old][good][large][cheap] = 0.45
        pricepTable[bad][new][bad][small][cheap] = 0.6
        pricepTable[bad][new][bad][medium][cheap] = 0.55
        pricepTable[bad][new][bad][large][cheap] = 0.5
        pricepTable[bad][new][good][small][cheap] = 0.4
        pricepTable[bad][new][good][medium][cheap] = 0.3
        pricepTable[bad][new][good][large][cheap] = 0.3
        pricepTable[ugly][old][bad][small][cheap] = 0.8
        pricepTable[ugly][old][bad][medium][cheap] = 0.75
        pricepTable[ugly][old][bad][large][cheap] = 0.75
        pricepTable[ugly][old][good][small][cheap] = 0.65
        pricepTable[ugly][old][good][medium][cheap] = 0.6
        pricepTable[ugly][old][good][large][cheap] = 0.55
        pricepTable[ugly][new][bad][small][cheap] = 0.7
        pricepTable[ugly][new][bad][medium][cheap] = 0.64
        pricepTable[ugly][new][bad][large][cheap] = 0.61
        pricepTable[ugly][new][good][small][cheap] = 0.48
        pricepTable[ugly][new][good][medium][cheap] = 0.41
        pricepTable[ugly][new][good][large][cheap] = 0.37

        pricepTable[good][old][bad][small][ok] = 0.4
        pricepTable[good][old][bad][medium][ok] = 0.45
        pricepTable[good][old][bad][large][ok] = 0.45
        pricepTable[good][old][good][small][ok] = 0.3
        pricepTable[good][old][good][medium][ok] = 0.3
        pricepTable[good][old][good][large][ok] = 0.25
        pricepTable[good][new][bad][small][ok] = 0.4
        pricepTable[good][new][bad][medium][ok] = 0.45
        pricepTable[good][new][bad][large][ok] = 0.45
        pricepTable[good][new][good][small][ok] = 0.3
        pricepTable[good][new][good][medium][ok] = 0.25
        pricepTable[good][new][good][large][ok] = 0.2
        pricepTable[bad][old][bad][small][ok] = 0.299
        pricepTable[bad][old][bad][medium][ok] = 0.33
        pricepTable[bad][old][bad][large][ok] = 0.32
        pricepTable[bad][old][good][small][ok] = 0.35
        pricepTable[bad][old][good][medium][ok] = 0.35
        pricepTable[bad][old][good][large][ok] = 0.4
        pricepTable[bad][new][bad][small][ok] = 0.35
        pricepTable[bad][new][bad][medium][ok] = 0.35
        pricepTable[bad][new][bad][large][ok] = 0.4
        pricepTable[bad][new][good][small][ok] = 0.4
        pricepTable[bad][new][good][medium][ok] = 0.4
        pricepTable[bad][new][good][large][ok] = 0.3
        pricepTable[ugly][old][bad][small][ok] = 0.1999
        pricepTable[ugly][old][bad][medium][ok] = 0.24
        pricepTable[ugly][old][bad][large][ok] = 0.23
        pricepTable[ugly][old][good][small][ok] = 0.3
        pricepTable[ugly][old][good][medium][ok] = 0.33
        pricepTable[ugly][old][good][large][ok] = 0.37
        pricepTable[ugly][new][bad][small][ok] = 0.27
        pricepTable[ugly][new][bad][medium][ok] = 0.3
        pricepTable[ugly][new][bad][large][ok] = 0.32
        pricepTable[ugly][new][good][small][ok] = 0.42
        pricepTable[ugly][new][good][medium][ok] = 0.39
        pricepTable[ugly][new][good][large][ok] = 0.33

        pricepTable[good][old][bad][small][expensive] = 0.1
        pricepTable[good][old][bad][medium][expensive] = 0.15
        pricepTable[good][old][bad][large][expensive] = 0.2
        pricepTable[good][old][good][small][expensive] = 0.3
        pricepTable[good][old][good][medium][expensive] = 0.35
        pricepTable[good][old][good][large][expensive] = 0.45
        pricepTable[good][new][bad][small][expensive] = 0.15
        pricepTable[good][new][bad][medium][expensive] = 0.15
        pricepTable[good][new][bad][large][expensive] = 0.2
        pricepTable[good][new][good][small][expensive] = 0.45
        pricepTable[good][new][good][medium][expensive] = 0.55
        pricepTable[good][new][good][large][expensive] = 0.7
        pricepTable[bad][old][bad][small][expensive] = 0.001
        pricepTable[bad][old][bad][medium][expensive] = 0.02
        pricepTable[bad][old][bad][large][expensive] = 0.03
        pricepTable[bad][old][good][small][expensive] = 0.1
        pricepTable[bad][old][good][medium][expensive] = 0.15
        pricepTable[bad][old][good][large][expensive] = 0.15
        pricepTable[bad][new][bad][small][expensive] = 0.05
        pricepTable[bad][new][bad][medium][expensive] = 0.1
        pricepTable[bad][new][bad][large][expensive] = 0.1
        pricepTable[bad][new][good][small][expensive] = 0.2
        pricepTable[bad][new][good][medium][expensive] = 0.3
        pricepTable[bad][new][good][large][expensive] = 0.4
        pricepTable[ugly][old][bad][small][expensive] = 0.0001
        pricepTable[ugly][old][bad][medium][expensive] = 0.01
        pricepTable[ugly][old][bad][large][expensive] = 0.02
        pricepTable[ugly][old][good][small][expensive] = 0.05
        pricepTable[ugly][old][good][medium][expensive] = 0.07
        pricepTable[ugly][old][good][large][expensive] = 0.08
        pricepTable[ugly][new][bad][small][expensive] = 0.03
        pricepTable[ugly][new][bad][medium][expensive] = 0.06
        pricepTable[ugly][new][bad][large][expensive] = 0.07
        pricepTable[ugly][new][good][small][expensive] = 0.1
        pricepTable[ugly][new][good][medium][expensive] = 0.2
        pricepTable[ugly][new][good][large][expensive] = 0.3
        price.pTable = pricepTable

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
    def query(self, nodeQuery, numUpdates, numDrops):
        node = self.dicNodes.get(nodeQuery)
        print("Performing Query of " + node.name)


        # #Performing markov blanket
        # parents = node.parents
        # children = node.children
        # childrenParents = []
        # for curNode in children:
        #     for curParent in curNode.parents:
        #         if curParent is not node:
        #             childrenParents.append(curParent)
        #
        # print("The Markov Blanket if this query is")
        # print("Parents")
        # self.printNodeList(parents)
        # print("Children")
        # self.printNodeList(children)
        # print("Children Parents")
        # self.printNodeList(childrenParents)

        for i in xrange(numUpdates):
            currentNode = self.nodes[i%len(self.nodes)]
            currentNode.assignValue()

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
