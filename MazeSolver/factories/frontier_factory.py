from MazeSolver.model.frontiers.queue_frontier import QueueFrontier
from MazeSolver.model.frontiers.stack_frontier import StackFrontier
from MazeSolver.model.frontiers.greedy_frontier import GreedyFrontier
from MazeSolver.enums.frontier_choices import *

"""
FrontierFactory.py

Holds the methods necessary to generate the correct frontier type

Author: Chris Wolf
Version: 1.0.0 (June 30, 2020)
"""


def generate_frontier(frontier_choice):
    if frontier_choice == STACK_FRONTIER:
        return StackFrontier()
    elif frontier_choice == QUEUE_FRONTIER:
        return QueueFrontier()
    elif frontier_choice == GREEDY_FRONTIER:
        return GreedyFrontier()
    else:
        print('ERROR -- Invalid frontier!')
        exit()
