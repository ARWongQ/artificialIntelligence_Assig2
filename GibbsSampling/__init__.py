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

    #Delete white spaces
    evidences = filter(None, evidences)
    #print(evidences)

    numUpdates= raw_input("Number of updates to perform ")
    numDrops =  raw_input("Number of initial samples to drop ")


    #Create the network
    myNetwork = Network("Bayesian Network")

    #Set random values for the nodes
    myNetwork.setRandomValues()

    #setting the evidence
    myNetwork.setAllEvidence(evidences)

    #Perform Query
    myNetwork.query(nodeQuery,int(numUpdates),int(numDrops))

#Run the main function
if __name__ == "__main__":
    main()
