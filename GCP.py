

from random import choice, sample, shuffle, randint
import json
from itertools import permutations
import copy
from GCPState import GCPState
import networkx as nx
try:
    import matplotlib
    matplotlib.use('Agg') #don't try to create a display window
    from matplotlib import pyplot
    _mpl_available = True
except:
    _mpl_available = False

class Graph():
    """Represents a GCP given an adjacency list.
    Local search candidates are is a graph with random colors assigned. Colors cannot be over four.
    cities. Neighbors are generated by randomly changing one color assigned to a vertex to a different color   in the ordering. The cost of a tour is the Euclidean distance traveled.
    Local search functions will call the following methods:
    random_candidate() to get an initial state
    best_neighbor() to get a best neighbor state -> state with min overlapping colors
    random_neighbor() to get a random neighbor state of a given state
    cost(state) to determine the total number of adjacent vertices that share a similar color
    """
    def __init__(self, adjList, colorNum):
        self.adjacencyList = adjList
        self.colorNum = colorNum
        self.colors = self._generateColorList()  
    def __repr__(self):
        return f"{str(self.adjacencyList)}"
    def randomCandidate(self):
        """ generates random key-value pairing that forms a state based on the given vertices """
        vertices = list(self.adjacencyList.keys())
        shuffle(vertices)
        return GCPState(vertices, self.colors)
        
    def cost(self, state):
        """ given a state, this method returns the total number of adjacent vertices
        that share the same color"""
        totalCost = 0
        for vertex in state.coloring.keys():
            res = self._getColorsofNear(vertex, state)
            if state.coloring[vertex] in res:
                totalCost +=1
        return totalCost
    def _getColorsofNear(self, vertex, state):
        """ given a vertex and a state, it returns the colors of
        vertices adjacent to this vertex using the adjacency list. 
        This private method is used to get the cost"""
        res = []
        for dest in self.adjacencyList[vertex]:
            res.append(state.coloring[dest])
        return res
    def randomNeighbor(self, state):
        """ returns a random state that's near the given state and its cost. 
        The near state is obtained by flipping one color of the current state"""
        near = state.flipColor()
        cost = self.cost(near)
        return near, cost
    
    def _getAllNeigbhors(self, state):
        """ 'private' method to get all possible neigbhors of a current sate
        given a graph of n vertices colored with c colors, there n*(c-1) sucessors 
        that are obtained by changing the color of each vertice"""
        successors = []
        for vertex, color in state.coloring.items():
            for c in state.colors:
                if c != state.coloring[vertex]:
                    successor = state.coloring.copy()
                    successor[vertex] = c
                    new_state = GCPState(state.coloring.keys(), self.colors)
                    new_state.coloring = successor
                    successors.append(new_state)     
        return successors

    def bestNeighbor(self, state):
        """Returns the best possible state that can be made out of the random coloring that we started with.
        the best possible state is one with the lowest state
        Returns: best_tour, best_cost
        """
        minCost = float("inf")
        minState = []
        allNeighbors = self._getAllNeigbhors(state)
        for state in allNeighbors:
            cost = self.cost(state)
            if cost < minCost:
                minCost =cost
                minState = state
        return minState, minCost
    def _getEdgesVertices(self):
        """ get edges and vertices to plot the graph """
        edges = []
        vertices = []
        for key, values in self.adjacencyList.items():
            vertices.append(int(key))
            for value in values:
                edges.append((int(key), value))
        return vertices, edges
    def _generateColorList(self):
        """ This private methods generates a list of colors(rgb) that
        will be used to color graphs. It generates it based on the
        chromatic number of the given graph problem
        returns: list of turples of RGB values as floats between 0 and 1 
        to be used in the networkx draw function"""
        rgbValues = []
        # Generate random RGB values
        for i in range(self.colorNum):
            r = randint(0, 255)/255.0
            g = randint(0, 255)/255.0
            b = randint(0, 255)/255.0
            rgbValues.append((r, g, b))

        return rgbValues
    
    def plot(self, solution, filename):
        """ this function will provide a picture of the optimal solution found 
        by the local search algorithm"""
        
        colors = []
        nodes, edges = self._getEdgesVertices()
        for node in nodes:
            colors.append(solution.coloring[node]) 
        
        # Create a undirectedgraph
        G = nx.MultiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        # Draw the graph using the default spring layout
        nx.draw(G, with_labels=True, node_color = colors, alpha=0.3, width=1)
        
        #save plot with the userprovided name
        pyplot.savefig(filename)



          
if __name__ == "__main__":
    g = Graph("Graphs/chrom3/octahedron.json", 3)
    print(g)
    randomCand = g.randomCandidate()
    # print(f"random candidate: {randomCand}, random candiate cost: {g.cost(randomCand)}")
    # print(f"random near: {g.randomNeighbor(randomCand)[0]}, cost: {g.randomNeighbor(randomCand)[1]}")
    # print((g._getAllNeigbhors(randomCand)))
    # print(g.bestNeighbor(randomCand))
    #g.plot()