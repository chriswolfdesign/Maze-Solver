import unittest

from MazeSolver.model.frontiers.astar_frontier import AStarFrontier
from MazeSolver.model.point import Point

class AStarFrontierTest(unittest.TestCase):
    """
    test_astar_frontier.py

    Unit testing for astar_frontier.py

    Author: Chris Wolf
    Version: 1.0.0 (July 9, 2020)
    """
    # AStarFrontier.remove_point() tests
    def testRemovePointEmptyPointListShouldBeNone(self):
        frontier = AStarFrontier()
        frontier.set_goal(Point(1, 2))
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))
        point = frontier.remove_point()
        self.assertEqual(None, point)
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))

    def testRemovePointListHasOnePointShouldBeThatPoint(self):
        frontier = AStarFrontier()
        frontier.set_goal(Point(2, 2))
        frontier.add_point(Point(1, 2))
        self.assertEqual([Point(1, 2)], frontier._points)
        self.assertEqual(1, len(frontier._points))
        point = frontier.remove_point()
        self.assertEqual(point, Point(1, 2))
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))

    def testRemovePointListHasMultiplePointsShouldBeSecondPoint(self):
        frontier = AStarFrontier()
        frontier.set_goal(Point(3, 3))
        point1 = Point(1, 1)
        point2 = Point(2, 3, point1)
        point3 = Point(5, 5, point2)
        frontier.add_point(point1)
        frontier.add_point(point2)
        frontier.add_point(point3)
        self.assertEqual([point1, point2, point3], frontier._points)
        self.assertEqual(3, len(frontier._points))
        point = frontier.remove_point()
        self.assertEqual(point2, point)
        self.assertEqual([point1, point3], frontier._points)
        self.assertEqual(2, len(frontier._points))

    # AStarFrontier._distance_traveled() tests
    def testDistanceTraveledNoParentsShouldBeZero(self):
        frontier = AStarFrontier()
        frontier.set_goal(Point(1, 1))
        point = Point(2, 2)
        self.assertEqual(0, frontier._distance_traveled(point))

    def testDistanceTraveledOneParentShouldBeOne(self):
        frontier = AStarFrontier()
        frontier.set_goal(Point(1, 1))
        point = Point(2, 2, Point(3, 3))
        self.assertEqual(1, frontier._distance_traveled(point))

    def testDistanceTraveledMultipleParentsShouldBeTwo(self):
        frontier = AStarFrontier()
        frontier.set_goal(Point(1, 1))
        point1 = Point(2, 2)
        point2 = Point(3, 3, point1)
        point3 = Point(4, 4, point2)
        self.assertEqual(2, frontier._distance_traveled(point3))

if __name__ == '__main__':
    unittest.main()
