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

    # Frontier.set_goal() tests
    def testFrontierSetGoalHadNoGoalGivenGoal(self):
        frontier = Frontier()
        frontier.set_goal(Point(1, 2))
        self.assertEqual(Point(1, 2), frontier._goal)

    def testFrontierSetGoalHadGoalHasNewGoal(self):
        frontier = Frontier()
        frontier.set_goal(Point(1, 2))
        self.assertEqual(Point(1, 2), frontier._goal)
        frontier.set_goal(Point(3, 4))
        self.assertEqual(Point(3, 4), frontier._goal)

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
