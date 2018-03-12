from Network import Network

#Main Function
def main():
    print("Running Gibbs Sampling")

    #Getting the inputs from the user

    #Node to query
    nodeQuery= raw_input("Node to query ")

    #Observed Evidence
    evidencesStr = raw_input("Add all the evidences ")
    evidences = evidencesStr.replace('=',' ').split(' ')
    print(evidences)

    numUpdates= raw_input("Number of updates to perform ")
    numDrops =  raw_input("Number of initial samples to drop ")


    #Create the network
    myNetwork = Network("Bayesian Network")

    #Set All the children parents for each node
    myNetwork.setChildrenParents();

    #Perform Query
    myNetwork.query(nodeQuery)

#Run the main function
if __name__ == "__main__":
    main()
