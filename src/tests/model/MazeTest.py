import unittest

from src.model.Maze import Maze


class MazeTest(unittest.TestCase):
    """
    MazeTest.py

    Unit testing for model.Maze.py

    Author: Chris Wolf
    Version: 1.0.0 (June 2, 2020)
    """

    # Maze._get_height() tests
    def testGetHeightMazeIsNone(self):
        maze = Maze('../../mazes/linear_maze.txt')
        maze._maze = None
        self.assertEqual(0, maze._get_height())

    def testGetHeightMazeIsEmptyList(self):
        maze = Maze('../../mazes/linear_maze.txt')
        maze._maze = []
        self.assertEqual(0, maze._get_height())

    def testGetHeightLinearMazeShouldBeSeven(self):
        maze = Maze('../../mazes/linear_maze.txt')
        self.assertEqual(7, maze._get_height())

    def testGetHeightMazeWithCycleShouldBeNine(self):
        maze = Maze('../../mazes/maze_with_cycle.txt')
        self.assertEqual(9, maze._get_height())

    def testGetHeightMazeWithDeadEndShouldBeEight(self):
        maze = Maze('../../mazes/maze_with_dead_end.txt')
        self.assertEqual(8, maze._get_height())

    def testGetHeightMazeWithMultipleSolutionsShouldBeEight(self):
        maze = Maze('../../mazes/maze_with_multiple_solutions.txt')
        self.assertEqual(8, maze._get_height())

    def testGetHeightMazeWithTurnShouldBeNine(self):
        maze = Maze('../../mazes/maze_with_turn.txt')
        self.assertEqual(9, maze._get_height())

    def testGetHeightShortestPossibleMazeShouldBeFour(self):
        maze = Maze('../../mazes/shortest_possible_maze.txt')
        self.assertEqual(4, maze._get_height())

    def testGetHeightVeryShortMazeShouldBeFive(self):
        maze = Maze('../../mazes/very_short_maze.txt')
        self.assertEqual(5, maze._get_height())

    # Maze._generate_maze() tests
    def testGenerateMazeShortestPossibleMaze(self):
        expected_result = [['#', '#', '#'], ['#', 'B', '#'], ['#', 'A', '#'], ['#', '#', '#']]
        maze = Maze('../../mazes/shortest_possible_maze.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeVeryShortMaze(self):
        expected_result = [['#', '#', '#'], ['#', 'B', '#'], ['#', ' ', '#'], ['#', 'A', '#'], ['#', '#', '#']]
        maze = Maze('../../mazes/very_short_maze.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeLinearMaze(self):
        expected_result = [['#', '#', '#'], ['#', 'B', '#'], ['#', ' ', '#'], ['#', ' ', '#'], ['#', ' ', '#'],
                           ['#', 'A', '#'], ['#', '#', '#']]
        maze = Maze('../../mazes/linear_maze.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeMazeWithTurn(self):
        expected_result = [['#', '#', '#', '#', '#'], ['#', '#', '#', 'B', '#'], ['#', '#', '#', ' ', '#'],
                           ['#', '#', '#', ' ', '#'], ['#', ' ', ' ', ' ', '#'], ['#', ' ', '#', '#', '#'],
                           ['#', ' ', '#', '#', '#'], ['#', 'A', '#', '#', '#'], ['#', '#', '#', '#', '#']]
        maze = Maze('../../mazes/maze_with_turn.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeMazeWithDeadEnd(self):
        expected_result = [['#', '#', '#', '#', '#'], ['#', ' ', '#', 'B', '#'], ['#', ' ', '#', ' ', '#'],
                           ['#', ' ', ' ', ' ', '#'], ['#', '#', ' ', '#', '#'], ['#', '#', ' ', '#', '#'],
                           ['#', '#', 'A', '#', '#'], ['#', '#', '#', '#', '#']]
        maze = Maze('../../mazes/maze_with_dead_end.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeMazeWithMultipleSolutions(self):
        expected_result = [['#', '#', '#', '#', '#'], ['#', ' ', ' ', ' ', '#'], ['#', ' ', '#', 'B', '#'],
                           ['#', ' ', '#', ' ', '#'], ['#', ' ', ' ', ' ', '#'], ['#', '#', ' ', '#', '#'],
                           ['#', '#', 'A', '#', '#'], ['#', '#', '#', '#', '#']]
        maze = Maze('../../mazes/maze_with_multiple_solutions.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeMazeWithCycle(self):
        expected_result = [['#', '#', '#', '#', '#'], ['#', '#', 'B', '#', '#'], ['#', '#', ' ', '#', '#'],
                           ['#', ' ', ' ', ' ', '#'], ['#', ' ', '#', ' ', '#'], ['#', ' ', ' ', ' ', '#'],
                           ['#', '#', ' ', '#', '#'], ['#', '#', 'A', '#', '#'], ['#', '#', '#', '#', '#']]
        maze = Maze('../../mazes/maze_with_cycle.txt')
        self.assertEqual(expected_result, maze._maze)


if __name__ == '__main__':
    unittest.main()
