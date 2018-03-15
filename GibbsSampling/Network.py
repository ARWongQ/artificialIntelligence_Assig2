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
        price.parents.append(schools)

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

        #Tables are dictionaries
        #Add tables

        #Amenities
        #lots=0 little=1
        amenitiespTableDic = {}
        amenitiespTableDic.update({'lots': 0.3})
        amenitiespTableDic.update({'little': 0.7})
        amenities.pTableDic = amenitiespTableDic

        #Neighborhood
        #bad=0 good=1
        neighborhoodpTableDic = {}
        neighborhoodpTableDic.update({'bad': 0.4})
        neighborhoodpTableDic.update({'good': 0.6})
        neighborhood.pTableDic = neighborhoodpTableDic

        #Location
        #amenities :index1
        #neighborhood :index2
        #location :index3
        locationpTableDic = {}
        locationpTableDic.update({'lots bad good ': 0.3})
        locationpTableDic.update({'lots good good ': 0.8})
        locationpTableDic.update({'little bad good ': 0.2})
        locationpTableDic.update({'little good good ': 0.5})

        locationpTableDic.update({'lots bad bad ': 0.4})
        locationpTableDic.update({'lots good bad ': 0.15})
        locationpTableDic.update({'little bad bad ': 0.4})
        locationpTableDic.update({'little good bad ': 0.35})

        locationpTableDic.update({'lots bad ugly ': 0.3})
        locationpTableDic.update({'lots good ugly ': 0.05})
        locationpTableDic.update({'little bad ugly ': 0.4})
        locationpTableDic.update({'little good ugly ': 0.15})
        location.pTableDic = locationpTableDic

        #Children
        #Neighborhood: index1
        #Children: index2
        childrenpTableDic = {}
        childrenpTableDic.update({'bad bad ': 0.6})
        childrenpTableDic.update({'good bad ': 0.3})

        childrenpTableDic.update({'bad good ': 0.4})
        childrenpTableDic.update({'good good ': 0.7})
        children.pTableDic = childrenpTableDic

        #Size
        # small=0 medium=1 large=2
        sizepTableDic = {}
        sizepTableDic.update({'small': 0.33})
        sizepTableDic.update({'medium': 0.34})
        sizepTableDic.update({'large': 0.33})
        size.pTableDic = sizepTableDic


        #School
        # children: index1
        # schools: index2
        schoolpTableDic = {}
        schoolpTableDic.update({'bad bad ': 0.7})
        schoolpTableDic.update({'good bad ': 0.8})

        schoolpTableDic.update({'bad good ': 0.3})
        schoolpTableDic.update({'good good ': 0.2})
        schools.pTableDic = schoolpTableDic


        #Age
        #location :index1
        #age :index2
        agepTableDic = {}
        agepTableDic.update({'good old ': 0.3})
        agepTableDic.update({'bad old ': 0.6})
        agepTableDic.update({'ugly old ': 0.9})

        agepTableDic.update({'good new ': 0.7})
        agepTableDic.update({'bad new ': 0.4})
        agepTableDic.update({'ugly new ': 0.1})
        age.pTableDic = agepTableDic


        #Price
        #location: index1 #bad=0, good=1, ugly= 2
        #age: index2 #old=0 new=1
        #schools: index3 #bad=0, good=1
        #size : index4 #small=0, medium=1, large=2
        #price: index5 #cheap=0, ok=1, expensive=2
        pricepTableDic = {}
        pricepTableDic.update({'good old bad small cheap ': 0.5})
        pricepTableDic.update({'good old bad medium cheap ': 0.4})
        pricepTableDic.update({'good old bad large cheap ': 0.35})
        pricepTableDic.update({'good old good small cheap ': 0.4})
        pricepTableDic.update({'good old good medium cheap ': 0.35})
        pricepTableDic.update({'good old good large cheap ': 0.3})
        pricepTableDic.update({'good new bad small cheap ': 0.45})
        pricepTableDic.update({'good new bad medium cheap ': 0.4})
        pricepTableDic.update({'good new bad large cheap ': 0.35})
        pricepTableDic.update({'good new good small cheap ': 0.25})
        pricepTableDic.update({'good new good medium cheap ': 0.2})
        pricepTableDic.update({'good new good large cheap ': 0.1})
        pricepTableDic.update({'bad old bad small cheap ': 0.7})
        pricepTableDic.update({'bad old bad medium cheap ': 0.65})
        pricepTableDic.update({'bad old bad large cheap ': 0.65})
        pricepTableDic.update({'bad old good small cheap ': 0.55})
        pricepTableDic.update({'bad old good medium cheap ': 0.5})
        pricepTableDic.update({'bad old good large cheap ': 0.45})
        pricepTableDic.update({'bad new bad small cheap ': 0.6})
        pricepTableDic.update({'bad new bad medium cheap ': 0.55})
        pricepTableDic.update({'bad new bad large cheap ': 0.5})
        pricepTableDic.update({'bad new good small cheap ': 0.4})
        pricepTableDic.update({'bad new good medium cheap ': 0.3})
        pricepTableDic.update({'bad new good large cheap ': 0.3})
        pricepTableDic.update({'ugly old bad small cheap ': 0.8})
        pricepTableDic.update({'ugly old bad medium cheap ': 0.75})
        pricepTableDic.update({'ugly old bad large cheap ': 0.75})
        pricepTableDic.update({'ugly old good small cheap ': 0.65})
        pricepTableDic.update({'ugly old good medium cheap ': 0.6})
        pricepTableDic.update({'ugly old good large cheap ': 0.55})
        pricepTableDic.update({'ugly new bad small cheap ': 0.7})
        pricepTableDic.update({'ugly new bad medium cheap ': 0.64})
        pricepTableDic.update({'ugly new bad large cheap ': 0.61})
        pricepTableDic.update({'ugly new good small cheap ': 0.48})
        pricepTableDic.update({'ugly new good medium cheap ': 0.41})
        pricepTableDic.update({'ugly new good large cheap ': 0.37})

        pricepTableDic.update({'good old bad small ok ': 0.4})
        pricepTableDic.update({'good old bad medium ok ': 0.45})
        pricepTableDic.update({'good old bad large ok ': 0.45})
        pricepTableDic.update({'good old good small ok ': 0.3})
        pricepTableDic.update({'good old good medium ok ': 0.3})
        pricepTableDic.update({'good old good large ok ': 0.25})
        pricepTableDic.update({'good new bad small ok ': 0.4})
        pricepTableDic.update({'good new bad medium ok ': 0.45})
        pricepTableDic.update({'good new bad large ok ': 0.45})
        pricepTableDic.update({'good new good small ok ': 0.3})
        pricepTableDic.update({'good new good medium ok ': 0.25})
        pricepTableDic.update({'good new good large ok ': 0.2})
        pricepTableDic.update({'bad old bad small ok ': 0.299})
        pricepTableDic.update({'bad old bad medium ok ': 0.33})
        pricepTableDic.update({'bad old bad large ok ': 0.32})
        pricepTableDic.update({'bad old good small ok ': 0.35})
        pricepTableDic.update({'bad old good medium ok ': 0.35})
        pricepTableDic.update({'bad old good large ok ': 0.4})
        pricepTableDic.update({'bad new bad small ok ': 0.35})
        pricepTableDic.update({'bad new bad medium ok ': 0.35})
        pricepTableDic.update({'bad new bad large ok ': 0.4})
        pricepTableDic.update({'bad new good small ok ': 0.4})
        pricepTableDic.update({'bad new good medium ok ': 0.4})
        pricepTableDic.update({'bad new good large ok ': 0.3})
        pricepTableDic.update({'ugly old bad small ok ': 0.1999})
        pricepTableDic.update({'ugly old bad medium ok ': 0.24})
        pricepTableDic.update({'ugly old bad large ok ': 0.23})
        pricepTableDic.update({'ugly old good small ok ': 0.3})
        pricepTableDic.update({'ugly old good medium ok ': 0.33})
        pricepTableDic.update({'ugly old good large ok ': 0.37})
        pricepTableDic.update({'ugly new bad small ok ': 0.27})
        pricepTableDic.update({'ugly new bad medium ok ': 0.3})
        pricepTableDic.update({'ugly new bad large ok ': 0.32})
        pricepTableDic.update({'ugly new good small ok ': 0.42})
        pricepTableDic.update({'ugly new good medium ok ': 0.39})
        pricepTableDic.update({'ugly new good large ok ': 0.33})

        pricepTableDic.update({'good old bad small expensive ': 0.1})
        pricepTableDic.update({'good old bad medium expensive ': 0.15})
        pricepTableDic.update({'good old bad large expensive ': 0.2})
        pricepTableDic.update({'good old good small expensive ': 0.3})
        pricepTableDic.update({'good old good medium expensive ': 0.35})
        pricepTableDic.update({'good old good large expensive ': 0.45})
        pricepTableDic.update({'good new bad small expensive ': 0.15})
        pricepTableDic.update({'good new bad medium expensive ': 0.15})
        pricepTableDic.update({'good new bad large expensive ': 0.2})
        pricepTableDic.update({'good new good small expensive ': 0.45})
        pricepTableDic.update({'good new good medium expensive ': 0.55})
        pricepTableDic.update({'good new good large expensive ': 0.7})
        pricepTableDic.update({'bad old bad small expensive ': 0.001})
        pricepTableDic.update({'bad old bad medium expensive ': 0.02})
        pricepTableDic.update({'bad old bad large expensive ': 0.03})
        pricepTableDic.update({'bad old good small expensive ': 0.1})
        pricepTableDic.update({'bad old good medium expensive ': 0.15})
        pricepTableDic.update({'bad old good large expensive ': 0.15})
        pricepTableDic.update({'bad new bad small expensive ': 0.05})
        pricepTableDic.update({'bad new bad medium expensive ': 0.1})
        pricepTableDic.update({'bad new bad large expensive ': 0.1})
        pricepTableDic.update({'bad new good small expensive ': 0.2})
        pricepTableDic.update({'bad new good medium expensive ': 0.3})
        pricepTableDic.update({'bad new good large expensive ': 0.4})
        pricepTableDic.update({'ugly old bad small expensive ': 0.0001})
        pricepTableDic.update({'ugly old bad medium expensive ': 0.01})
        pricepTableDic.update({'ugly old bad large expensive ': 0.02})
        pricepTableDic.update({'ugly old good small expensive ': 0.05})
        pricepTableDic.update({'ugly old good medium expensive ': 0.07})
        pricepTableDic.update({'ugly old good large expensive ': 0.08})
        pricepTableDic.update({'ugly new bad small expensive ': 0.03})
        pricepTableDic.update({'ugly new bad medium expensive ': 0.06})
        pricepTableDic.update({'ugly new bad large expensive ': 0.07})
        pricepTableDic.update({'ugly new good small expensive ': 0.1})
        pricepTableDic.update({'ugly new good medium expensive ': 0.2})
        pricepTableDic.update({'ugly new good large expensive ': 0.3})
        price.pTableDic = pricepTableDic


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

        #Set all the numDrops for the nodes in the network
        for curNode in self.nodes:
            curNode.deleteCnt = numDrops


        #Looping through all the nodes and assigns a new value every update for each node
        for i in xrange(numUpdates):
            currentNode = self.nodes[i%len(self.nodes)]
            currentNode.assignValue()

        node.calcFinalProb()

    #Set random values to the whole newtork
    def setRandomValues(self):
        #Currently they all start with "0"
        for curNode in self.nodes:
            curNode.currentValue = 0


    # #Sets all the childrenParents in the network
    # def setChildrenParents(self):
    #     print("Setting all children parents")
    #     #Getting nodes form the netwrok
    #     myNodes = self.nodes
    #
    #     #loop through all the nodes
    #     for curNode in myNodes:
    #         print("setting Node " + curNode.name)
    #         children = curNode.children
    #         childrenParList = []
    #         if(children):
    #             childrenParList.append(curNode)
    #         for childrenNode in children:
    #             for childrenParNode in childrenNode.parents:
    #                 if(childrenParNode.name != curNode.name):
    #                     print("adding " + childrenParNode.name)
    #                     childrenParList.append(childrenParNode)
    #
    #         print("setting")
    #         curNode.childrenParents = childrenParList


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
            curChildrenParents = curNode.childrenParents

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

            #Print the childrenParents of the nodes
            childParentStr = ""
            for curNode2 in curChildrenParents:
                childParentStr += curNode2.name + ", "
            print("ChildrenParents: " + childParentStr)


    def printingNetworkMaps(self):
        print("Printing the network using maps")
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
