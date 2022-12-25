""" A representation of a state in the GCP 
A state is a dictionary that maps vertices to a specific color
it takes in the number of colors which represent the expected chromatic
number of the problem that is being solved. As a user, you should not have to worry
about this class because it is only used by the actual GCP class"""
from random import choice

class GCPState:
    def __init__(self, vertices, colorList):
        self.vertices = vertices
        # if self.colorNum == 3: 
        #     self.colors = ["red",  "blue", "yellow"] 
        # elif self.colorNum == 4:
        #     self.colors = ["red", "green", "blue", "yellow"]
        self.colors = colorList
        self.coloring = self.setColors() 
    def __repr__(self):
        return f"{self.coloring}"
    
    def setColors(self):
        """ This function assigns random colors to vertices from a list of
        the available colors. this is how we get the the first candidate.
        it is only called during initialization of the class.
        return: returns in GCP object representing the initial state."""
        coloring = {}
        for vertex in self.vertices:
            coloring[vertex] = choice(self.colors)
        return coloring 
    def flipColor(self):
        """ This function flips a color of a vertex at random to generate
        the next state. It is useful when getting a successor of a state
        return: returns a new state where one color has been flipped"""
        state = GCPState(self.vertices, self.colors)
        old_colors = self.coloring.copy()
        while True:
            key = choice(list(self.vertices))
            color = choice(self.colors)
            if color != self.coloring[key]:
                old_colors[key] = color
                state.coloring = old_colors
                break
        return state

         
if __name__ == "__main__":
    state = GCPState(["1", "2", "3", "4", "5"])
    print(state)
    print(state.flipColor())
   
        