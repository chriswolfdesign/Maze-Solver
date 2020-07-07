import unittest

from MazeSolver.model.point import Point
from MazeSolver.model.frontiers.queue_frontier import QueueFrontier


class QueueFrontierTest(unittest.TestCase):
    """
    QueueFrontierTest.py

    Unit testing for QueueFrontier.py

    Author: Chris Wolf
    Version: 1.0.0 (June 25, 2020)
    """

    # remove_point tests
    def testRemovePointEmptyPointListShouldBeNone(self):
        frontier = QueueFrontier()
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))
        point = frontier.remove_point()
        self.assertEqual(None, point)
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))

    def testRemovePointFromPointListLengthOneShouldBeOnlyPoint(self):
        frontier = QueueFrontier()
        frontier.add_point(Point(1, 2))
        self.assertEqual([Point(1, 2)], frontier._points)
        self.assertEqual(1, len(frontier._points))
        point = frontier.remove_point()
        self.assertEqual(Point(1, 2), point)
        self.assertEqual([], frontier._points)
        self.assertEqual(0, len(frontier._points))

    def testRemovePointFromPointListMultiplePointsShouldBeFirstPoint(self):
        frontier = QueueFrontier()
        frontier.add_point(Point(1, 2))
        frontier.add_point(Point(3, 4))
        frontier.add_point(Point(5, 6))
        self.assertEqual([Point(1, 2), Point(3, 4), Point(5, 6)], frontier._points)
        self.assertEqual(3, len(frontier._points))
        point = frontier.remove_point()
        self.assertEqual(Point(1, 2), point)
        self.assertEqual([Point(3, 4), Point(5, 6)], frontier._points)
        self.assertEqual(2, len(frontier._points))


if __name__ == '__main__':
    unittest.main()
