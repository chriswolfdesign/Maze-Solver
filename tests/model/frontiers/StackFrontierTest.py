import unittest

from src.model.Point import Point
from src.model.frontiers.StackFrontier import StackFrontier


class StackFrontierTest(unittest.TestCase):
    """
    StackFrontierTest.py

    Unit testing for StackFrontier.py

    Author: Chris Wolf
    Version: 1.0.0 (June 30, 2020)
    """
    # StackFrontier.remove_point() tests
    def testRemovingPointFromEmptyListShouldBeNone(self):
        frontier = StackFrontier()
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))
        point = frontier.remove_point()
        self.assertIsNone(point)
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))

    def testRemovingPointWithOnlyOnePointShouldBeOnlyPoint(self):
        frontier = StackFrontier()
        frontier.add_point(Point(1, 2))
        self.assertEqual([Point(1, 2)], frontier._points)
        self.assertEqual(1, len(frontier._points))
        point = frontier.remove_point()
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))

    def testRemovePointListWithMultiplePointsShouldBeLastPoint(self):
        frontier = StackFrontier()
        frontier.add_point(Point(1, 2))
        frontier.add_point(Point(3, 4))
        frontier.add_point(Point(5, 6))
        self.assertEqual([Point(1, 2), Point(3, 4), Point(5, 6)], frontier._points)
        self.assertEqual(3, len(frontier._points))
        point = frontier.remove_point()
        self.assertEqual(point, Point(5, 6))
        self.assertEqual([Point(1, 2), Point(3, 4)], frontier._points)
        self.assertEqual(2, len(frontier._points))


if __name__ == '__main__':
    unittest.main()
