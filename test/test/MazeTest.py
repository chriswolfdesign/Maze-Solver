import unittest

from src.model.Maze import Maze


class MazeTest(unittest.TestCase):
    """
    MazeTest.py

    Unit testing for model.Maze.py

    Author: Chris Wolf
    Version: 1.0.0 (June 2, 2020)
    """

    def testGenerateMazeShortestPossibleMaze(self):
        expected_result = [['#', '#', '#'], ['#', 'B', '#'], ['#', 'A', '#'], ['#', '#', '#']]
        maze = Maze('mazes/shortest_possible_maze.txt')
        self.assertEqual(expected_result, maze._generate_maze('../../mazes/shortest_possible_maze.txt'))

    def testGenerateMazeVeryShortMaze(self):
        expected_result = [['#', '#', '#'], ['#', 'B', '#'], ['#', ' ', '#'], ['#', 'A', '#'], ['#', '#', '#']]
        maze = Maze('mazes/very_short_maze.txt')
        self.assertEqual(expected_result, maze._generate_maze('../../mazes/very_short_maze.txt'))

    def testGenerateMazeLinearMaze(self):
        expected_result = [['#', '#', '#'], ['#', 'B', '#'], ['#', ' ', '#'], ['#', ' ', '#'], ['#', ' ', '#'],
                           ['#', 'A', '#'], ['#', '#', '#']]
        maze = Maze('mazes/linear_maze.txt')
        self.assertEqual(expected_result, maze._generate_maze('../../mazes/linear_maze.txt'))

    def testGenerateMazeMazeWithTurn(self):
        expected_result = [['#', '#', '#', '#', '#'], ['#', '#', '#', 'B', '#'], ['#', '#', '#', ' ', '#'],
                           ['#', '#', '#', ' ', '#'], ['#', ' ', ' ', ' ', '#'], ['#', ' ', '#', '#', '#'],
                           ['#', ' ', '#', '#', '#'], ['#', 'A', '#', '#', '#'], ['#', '#', '#', '#', '#']]
        maze = Maze('mazes/maze_with_turn.txt')
        self.assertEqual(expected_result, maze._generate_maze('../../mazes/maze_with_turn.txt'))

    def testGenerateMazeMazeWithDeadEnd(self):
        expected_result = [['#', '#', '#', '#', '#'], ['#', ' ', '#', 'B', '#'], ['#', ' ', '#', ' ', '#'],
                           ['#', ' ', ' ', ' ', '#'], ['#', '#', ' ', '#', '#'], ['#', '#', ' ', '#', '#'],
                           ['#', '#', 'A', '#', '#'], ['#', '#', '#', '#', '#']]
        maze = Maze('mazes/maze_with_dead_end.txt')
        self.assertEqual(expected_result, maze._generate_maze('../../mazes/maze_with_dead_end.txt'))

    def testGenerateMazeMazeWithMultipleSolutions(self):
        expected_result = [['#', '#', '#', '#', '#'], ['#', ' ', ' ', ' ', '#'], ['#', ' ', '#', 'B', '#'],
                           ['#', ' ', '#', ' ', '#'], ['#', ' ', ' ', ' ', '#'], ['#', '#', ' ', '#', '#'],
                           ['#', '#', 'A', '#', '#'], ['#', '#', '#', '#', '#']]
        maze = Maze('mazes/maze_with_multiple_solutions.txt')
        self.assertEqual(expected_result, maze._generate_maze('../../mazes/maze_with_multiple_solutions.txt'))

if __name__ == '__main__':
    unittest.main()
