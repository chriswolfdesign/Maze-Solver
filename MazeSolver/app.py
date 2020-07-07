import sys
import os

from MazeSolver.model.maze import Maze
from MazeSolver.enums.frontier_choices import *
from MazeSolver.factories.frontier_factory import generate_frontier

'''
app.py

Entry point to the application

Author: Chris Wolf
Version: 1.0.0 (June 2, 2020)
'''

def run():
    """
    Runs the program for the user
    """
    file_name = get_file_name()
    frontier = select_frontier()

    maze = Maze(file_name, frontier)
    maze.go()

def get_file_name():
    """
    Asks the user for the file name of the maze they want
    :return: the file name of the maze they want
    """
    file_name = input('Enter text file for maze: ')

    if not os.path.exists(file_name):
        print('ERROR -- Could not find {}!'.format(file_name))
        exit()

    return file_name

def select_frontier():
    """
    Asks the user the type of frontier they would like
    :return: the frontier the user has requested
    """
    frontier_choice = -1

    while frontier_choice < 0 or frontier_choice > NUMBER_OF_FRONTIERS:
        print('Choose your frontier:')
        print('\t 1: StackFrontier')
        print('\t 2: QueueFrontier')
        print('\t 3: GreedyFrontier')
        frontier_choice = int(input('Enter the number for the frontier you would like: '))

    return generate_frontier(frontier_choice)

