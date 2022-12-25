from math import exp, e
from random import random
from GCP import *
def simulated_annealing(problem, runs, steps, init_temp, temp_decay):
    """Implementes the simulated annealing local search algorithm.
    Inputs:
        - problem: A GCP instance.
        - runs: Number of times to start from a random initial candidate.
        - steps: Number of moves to make in a given run.
        - init_temp: Initial temperature for the start of each run.
                This should scale linearly relative to the cost of a
                typical candidate.
        - temp_decay: Multiplicative factor by which temperature is reduced
                on each step.
    Returns: best_candidate, best_cost
        The best candidate identified by the search and its cost
        Simulated anealing will always use random neighbor rather that best neighbor.
    """
    best_state = None
    best_cost = float("inf")
    for run in range(runs):
        temp = init_temp
        currrent_state = problem.randomCandidate()
        currrent_cost = problem.cost(currrent_state)
        for step in range(steps):
            near_state, near_cost = problem.randomNeighbor(currrent_state)
            delta = currrent_cost - near_cost
            if delta > 0 or random() < exp(delta/temp):
                currrent_state = near_state
                currrent_cost = near_cost
            if currrent_cost < best_cost:
                best_state = currrent_state
                best_cost = currrent_cost
                print("Best Cost: " , best_cost)
            temp *=temp_decay
    return best_state, best_cost
   