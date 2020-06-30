"""
FrontierFactory.py

Holds the methods necessary to generate the correct frontier type

Author: Chris Wolf
Version: 1.0.0 (June 30, 2020)
"""
from src.model.frontiers.QueueFrontier import QueueFrontier
from src.model.frontiers.StackFrontier import StackFrontier


def generate_frontier(frontier_type):
    if frontier_type == '-q':
        return QueueFrontier()
    elif frontier_type == '-s':
        return StackFrontier()
    else:
        print('Invalid Frontier')
        exit()
