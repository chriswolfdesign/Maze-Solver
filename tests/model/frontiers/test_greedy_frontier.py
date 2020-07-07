import unittest

from MazeSolver.model.frontiers.greedy_frontier import GreedyFrontier
from MazeSolver.model.point import Point

class GreedyFrontierTest(unittest.TestCase):
    """
    test_greedy_frontier.py

    Unit tests for greedy_frontier.py

    Author: Chris Wolf

    Version: 1.0.0 (June 7, 2020)
    """

    # GreedyFrontier.remove() tests
    def testRemovePointEmptyPointListShouldBeNone(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(1, 2))
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))
        point = frontier.remove_point()
        self.assertEqual(None, point)
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))

    def testRemovePointOnlyOnePointShouldBeOnlyPoint(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(1, 2))
        frontier.add_point(Point(1, 1))
        self.assertEqual([Point(1, 1)], frontier._points)
        self.assertEqual(1, len(frontier._points))
        point = frontier.remove_point()
        self.assertEqual(Point(1, 1), point)
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))

    def testRemovePointMultiplePointsShouldBeSecondPoint(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(2, 3))
        frontier.add_point(Point(1, 1))
        frontier.add_point(Point(3, 3))
        frontier.add_point(Point(5, 5))
        self.assertEqual([Point(1, 1), Point(3, 3), Point(5, 5)], frontier._points)
        self.assertEqual(3, len(frontier._points))
        point = frontier.remove_point()
        self.assertEqual(Point(3, 3), point)
        self.assertEqual([Point(1, 1), Point(5, 5)], frontier._points)
        self.assertEqual(2, len(frontier._points))

    # GreedyFrontier._calculate_cartesan_distance_from_goal() tests
    def testCalculateCartesanDistanceFromGoalIsGoalShouldBeZero(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(1, 2))
        self.assertEqual(0, frontier._calculate_cartesan_distance_from_goal(Point(1, 2)))

    def testCalculateCartesanDistanceFromGoalYValueIsOffByOneShouldBeOne(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(5, 5))
        self.assertEqual(1, frontier._calculate_cartesan_distance_from_goal(Point(5, 6)))

    def testCalculateCartesanDistanceFromGoalXValueIsOffByOneYValueIsOffByOneShouldBeTwo(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(5, 5))
        self.assertEqual(2, frontier._calculate_cartesan_distance_from_goal(Point(6, 6)))

    def testCalculateCartesanDistanceFromGoalXValueIsOffByOneShouldBeOne(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(5, 5))
        self.assertEqual(1, frontier._calculate_cartesan_distance_from_goal(Point(6, 5)))

    def testCalculateCartesanDistanceFromGoalXValueIsOffByOneYValueIsOffByNegativeOneShouldBeTwo(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(5, 5))
        self.assertEqual(2, frontier._calculate_cartesan_distance_from_goal(Point(6, 4)))

    def testCalculateCartesanDistanceFromGoalYValueIsOffByNegativeOneShouldBeOne(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(5, 5))
        self.assertEqual(1, frontier._calculate_cartesan_distance_from_goal(Point(5, 4)))

    def testCalculateCartesanDistanceFromGoalXValueIsOffByNegativeOneYValueIsOffByNegativeOneShouldBeTwo(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(5, 5))
        self.assertEqual(2, frontier._calculate_cartesan_distance_from_goal(Point(4, 4)))

    def testCalculateCartesanDistanceFromGoalXValueIsOffByNegativeOneShouldBeOne(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(5, 5))
        self.assertEqual(1, frontier._calculate_cartesan_distance_from_goal(Point(4, 5)))

    def testCalculateCartesanDistanceFromGoalXValueIsOffByNegativeOneYValueIsOffByOneShouldBeTwo(self):
        frontier = GreedyFrontier()
        frontier.set_goal(Point(5, 5))
        self.assertEqual(2, frontier._calculate_cartesan_distance_from_goal(Point(4, 6)))

if __name__ == '__main__':
    unittest.main()
