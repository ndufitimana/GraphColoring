## TL;DR

This repo provides 3 local search algorithms to solve Graph Coloring problem and the results of performance comparison in a paper "GCP.pdf", it requires python packages listed in "requirements.txt" to run and you can use command "pip install -r requirements.txt" to install them. To run the program use "LocalSearch.py" script with arguments of Algorithm keywords: "HC" for Hill Climbing, "SA" for Simulated Annealing, "BS" for Stochastic Beam Search, and providing -nodes [number] -p [probability] to generate a random graph. You can also alter algorithm parameters by making a copy of "default_config.json" and using flag "-config [filename]" . The final solution will be saved as "coloredGraph.pdf"
here is an example:
`python3 LocalSearch.py SA -nodes 40 -p 0.45`

## Detailed Description


This repository contains the implementation of three Local Search Algorithms: Hill Climbing, Simulated Annealing, and Stochastic Beam Search. Each one of these three algorithms is used to solve
one of the many NP-Complete Problems in Computer Science: Graph Coloring. The main idea of the problem is to color the vertices of a graph such that no two adjacent vertices share the same color while minimizing the number of colors used. 


I ran several experiments on these algorithms to compare their performance, basically how good they are at solving any Graph Coloring Problem by varying several of their parameters. 

If interested in the findings, read the paper under the folder Paper and filename GCP.pdf or compile the GCP.tex file.

If you want to test the algorithms for yourself, you can also try them by following the insturctions below:

Before you proceed make sure that you have all the requirements outlined in the requirements.txt file using pip. You can install
all these requirments at once using PIP by following this command:
`pip install -r requirements.txt` 

Here is the pattern for providing arguments to run the code:
`python3 LocalSearch.py [Algorithm Keyword] [optional arguments]`

Use the following keywords for algorithms:
* HC for Hill Climbing
* SA for Simulated Anealing
* BS for Stochastic Beam Search

if you do not provide any of the optinal keyword, the algorithm will use a graph from the Networking Repository/Library (see citation in my paper). The algorithms use paramters from the file default_config.json by default.

You also can alter the paramters of any algorithm you want to use.
To do so, make a copy of the file: default_config.json and rename it to something else. Then play around with the parameters for each algorithm. You will have to use the flag `-config [config filename]` to provide the file to the algorithm 

The optional arguments will allow you to create a random graph and use it. Here are the optional arguments

* -nodes [number of nodes]
* -p [probability for edge creation. Must be between [0,-1]

This will use the Erdos–Rényi (ER) random graph model to generate a
random graph. 

Here is an example:
`python3 LocalSearch.py SA -nodes 40 -p 0.45`

The above key word generates a graph with 40 nodes and edges formed with a probability of 45% and use Simulated Annealing to find an optimal solutin to it using the default config file.

At the end of the the algorith, a colored graph is generated under the name coloredGraph.pdf. You might want to check it out. 
