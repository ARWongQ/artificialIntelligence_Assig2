#Class for the Bayesian Network
class Network:
    def __init__(self, name):
        self.name = name
        self.nodes = []

        #Create all the Node Objects

        #Create all the Node Objects dependencies (parent children etc)

        #Add created nodes into self.nodes list

    # performs hillclimbing algorithm on initialized board
    def query(self, nodeQuery):
        print("Performing Query of " + nodeQuery)
