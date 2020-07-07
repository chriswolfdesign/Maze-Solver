import unittest

from MazeSolver.model.point import Point
from MazeSolver.model.frontiers.frontier import Frontier


class FrontierTest(unittest.TestCase):
    """
    FrontierTest.py

    Unit tests for Frontier.py

    Author: Chris Wolf
    Version: 1.0.0 (June 25, 2020)
    """

    # Frontier.__init__() tests
    def testFrontierInitShouldBeEmptyPointsList(self):
        frontier = Frontier()
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))
        self.assertEqual(None, frontier._starting_point)
        self.assertEqual(None, frontier._goal)

    def testFrontierInitStartingPointIsGiven(self):
        frontier = Frontier(starting_point=Point(3, 4))
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))
        self.assertEqual(Point(3, 4), frontier._starting_point)
        self.assertEqual(None, frontier._goal)

    def testFrontierInitGoalIsGiven(self):
        frontier = Frontier(goal=Point(3, 4))
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))
        self.assertEqual(None, frontier._starting_point)
        self.assertEqual(Point(3, 4), frontier._goal)

    def testFrontierInitStartingPointAndGoalAreGiven(self):
        frontier = Frontier(starting_point=Point(3, 4), goal=Point(5, 6))
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))
        self.assertEqual(Point(3, 4), frontier._starting_point)
        self.assertEqual(Point(5, 6), frontier._goal)

    # Frontier.add_point() tests
    def testFrontierAddPointToEmptyPointsListShouldBeLengthOne(self):
        frontier = Frontier()
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))
        frontier.add_point(Point(3, 4))
        self.assertEqual([Point(3, 4)], frontier._points)
        self.assertEqual(1, len(frontier._points))

    def testFrontierAddPointToPointListWithOneShouldBeLengthTwo(self):
        frontier = Frontier()
        frontier.add_point(Point(3, 4))
        self.assertEqual([Point(3, 4)], frontier._points)
        self.assertEqual(1, len(frontier._points))
        frontier.add_point(Point(5, 6))
        self.assertEqual([Point(3, 4), Point(5, 6)], frontier._points)
        self.assertEqual(2, len(frontier._points))

    # Frontier.remove_point() tests
    def testFrontierRemovePointEmptyPointListShouldBeEmpty(self):
        frontier = Frontier()
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))
        frontier.remove_point()
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))

    def testFrontierRemovePointListLengthOneShouldBeLengthOne(self):
        frontier = Frontier()
        frontier.add_point(Point(3, 4))
        self.assertEqual([Point(3, 4)], frontier._points)
        self.assertEqual(1, len(frontier._points))
        frontier.remove_point()
        self.assertEqual([Point(3, 4)], frontier._points)
        self.assertEqual(1, len(frontier._points))


if __name__ == '__main__':
    unittest.main()
