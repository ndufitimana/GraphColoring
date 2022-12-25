import json
from argparse import ArgumentParser
import networkx as nx

from GCP import *
from HillClimbing import hill_climbing
from SimulatedAnnealing import simulated_annealing
from BeamSearch import stochastic_beam_search

def parse_input():
    parser = ArgumentParser()
    parser.add_argument("search", choices=["HC","SA","BS"],\
                        help="Local search algorithm to use: HC, SA, or BS")
    parser.add_argument("-config", type=str, default="default_config.json",\
                        help="JSON file with search parameters.")
    parser.add_argument("-plot", type=str, default="coloredGraph.pdf",\
                         help="Filename for graph output.")
    parser.add_argument("-nodes", type=int, required=False, \
                        help="the number of nodes for you graph")
    parser.add_argument("-p", type=float, required=False, \
                        help="Probability for edge creation")
    args = parser.parse_args()
    with open(args.config) as f:
        config = json.load(f)
    args.search_args = config[args.search]
    return args


def generateGraph(nodes = None, prob=None):
    
       
    adjList = {}
    
    if nodes and prob:
        G = nx.erdos_renyi_graph(n=nodes, p=prob)
    else:
        #use a graph from the the Network Repository
        path = "fb-pages-tvshow/fb-pages-tvshow.edges"
        edges = []
        # Read the graph from the Network Repository
        with open(path, 'r') as f:
            for line in f:
                # Split the line on the comma to get the nodes
                nodes = line.strip().split(',')
                edges.append((nodes[0], nodes[1]))
            # Create the graph object based on the edges
            G = nx.Graph()
            G.add_edges_from(edges)
        f.close()
    for node in G.nodes():
        adjList[node] = list(G.neighbors(node))
    chromaticNum = nx.greedy_color(G, strategy='largest_first')
    print("Graph Details: ", end=" ")
    print(f'Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}, chromatic number: {len(set(chromaticNum.values()))} ')


    return adjList, len(set(chromaticNum.values()))

def main():
    args = parse_input()
    # adjList, chromNum = generateGraph(45, 0.35)
    adjList, chromNum = generateGraph(args.nodes, args.p)
    problem = Graph(adjList, chromNum)
    if args.search == "HC":
        search_alg = hill_climbing
    if args.search == "SA":
        search_alg = simulated_annealing
    if args.search == "BS":
        search_alg = stochastic_beam_search
    solution, cost = search_alg(problem, **args.search_args)
    print("coloring:")
    print(solution)
    print(f"colors used: {chromNum}, adj vert with same color: {cost}")
    problem.plot(solution, args.plot) 
    

if __name__ == "__main__":
    main()