from math import exp
#from numpy.random import choice, multinomial 
import numpy as np
from GCP import *


def generate_props(neighbors_cost, temp):
    """ A helper function to generate probabilities used in beam search.
    See Beam Search below"""
    res = []
    for cost in neighbors_cost:
            res.append(exp(-cost/temp))
    total = sum(res)
    result = [res[i]/total for i in range(len(res))]
    return result


def stochastic_beam_search(problem, pop_size, steps, init_temp,
                           temp_decay, max_neighbors):
        """Implementes the stochastic beam search local search algorithm.
        Inputs:
                - problem: A GCP instance.
                - pop_size: Number of candidates tracked.
                - steps: The number of moves to make in a given run.
                - init_temp: Initial temperature. Note that temperature has a
                        slightly different interpretation here than in simulated
                        annealing.
                - temp_decay: Multiplicative factor by which temperature is reduced
                        on each step. Temperature parameters should be chosen such
                        that e^(-cost / temp) never reaches 0.
                - max_neighbors: Number of neighbors generated each round for each
                        candidate in the population.
        Returns: best_candidate, best_cost
                The best candidate identified by the search and its cost.
        """
        best_state, best_cost = None, float("inf")
        candidates = [problem.randomCandidate() for _ in range(pop_size)]

        temp = init_temp
        for step in range(steps):
                
                neighbors = [] #population
                neighbors_cost = []
                for candidate in candidates: 
                        for i in range(max_neighbors):
                                tour, cost = problem.randomNeighbor(candidate)
                                neighbors.append(tour)
                                neighbors_cost.append(cost)
                
                best_near_cost = min(neighbors_cost)
                best_neigh_state = neighbors[neighbors_cost.index(best_near_cost)]
                
                if best_near_cost < best_cost:
                        best_cost = best_near_cost
                        best_state = best_neigh_state
                        print("Best Cost: %.1f" % (best_cost))
                try:

                        probs_list = generate_props(neighbors_cost, temp)
                except ZeroDivisionError:
                        print("Algorithm Ending Early...")
                        return best_state, best_cost

                
                indices = list(range(len(probs_list)))
                choices = np.random.choice(indices, pop_size, p= probs_list)
              
                new_neighbors = [neighbors[index] for index in choices]
                candidates = new_neighbors #update population for next iteration

                temp *=temp_decay
        return best_state, best_cost
