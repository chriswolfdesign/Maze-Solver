import sys

from src.model.Maze import Maze

'''
Driver.py

Entrypoint to the application

Author: Chris Wolf
Version: 1.0.0 (June 2, 2020)
'''

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python Driver.py <maze_file>')
        exit(1)

    maze = Maze(sys.argv[1])
    maze.go()
