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

    # performs hillclimbing algorithm on initialized board
    def query(self, nodeQuery):
        print("Performing Query of " + nodeQuery)

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


    def printingNetworkMaps(self):
        print("Prining the network using maps")
        curNode = self.dicNodes.get("amenities")



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
