Part 1:  Gibbs sampling

The program takes the following command-line arguments:
1) The node to query, and the observed evidence nodes.  You can assume we are only interested in the probabilities of one of the nodes.
2) The number of updates to perform.  You can assume that each time a node changes value that is an update.
3) The number of initial samples to drop before computing the probability.

Note: everything inside quotations("") is the user input!

Sample Program:
Running Gibbs Sampling
Node to query "price"
Add all the evidences "schools=good location=ugly"
Number of updates to perform "10000"
Number of initial samples to drop "0"

Result:
Performing Query of price
P(price = cheap) = 0.5152
P(price = ok) = 0.3416
P(price = expensive) = 0.1432
