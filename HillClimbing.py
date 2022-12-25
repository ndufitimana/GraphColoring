from random import random
from GCP import *

def hill_climbing(problem, runs, steps, rand_move_prob):
    """Implementes the hill climbing local search algorithm.
    Inputs:
        - problem: A GCP instance.
        - runs: Number of times to start from a random initial candidate.
        - steps: Number of moves to make in a given run.
        - rand_move_prob: prob of a random neighbor on any given step.
    Returns: best_candidate, best_cost
        The best candidate identified by the search and its cost.
     When doing a random move we use random_neighbor(), we otherwise use
        best_neighbor(). 
    """
    best_state = None
    best_cost = float("inf")
    for run in range(runs):
        current_state = problem.randomCandidate()
        current_cost = problem.cost(current_state)
        for step in range(steps):
            if random() < rand_move_prob:
                current_state, current_cost = problem.randomNeighbor(current_state)
            else:
                neighbor_state, neighbor_cost = problem.bestNeighbor(current_state)
                if neighbor_cost < current_cost:
                    current_state = neighbor_state
                    current_cost = neighbor_cost
            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost 
                print("The Best cost is:", best_cost)
    return best_state, best_cost
if __name__ == "__main__":
    #playground
    problem = Graph("Graphs/6v.json")
    
    # random = g.randomCandidate()
    # print(random)
    # print(f"{random.cost()}")
    # print(f"near: {random.random_neighbor(random)}")
    print(f"res: {hill_climbing(problem, 10, 700, 0.25)}")