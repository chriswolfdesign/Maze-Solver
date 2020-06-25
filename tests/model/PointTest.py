import unittest

from src.model.Point import Point


class PointTest(unittest.TestCase):
    """
    PointTest.py

    Unit testing for Point.py

    Author: Chris Wolf
    Version: 1.0.0 (June 25, 2020)
    """

    # Point.get_x() tests
    def testGetXIsFive(self):
        point = Point(5, 5)
        self.assertEqual(5, point.get_x())

    def testGetXIsZero(self):
        point = Point(0, 5)
        self.assertEqual(0, point.get_x())

    # Point.get_y() tests
    def testGetYIsFour(self):
        point = Point(5, 4)
        self.assertEqual(4, point.get_y())

    def testGetYIsZero(self):
        point = Point(0, 0)
        self.assertEqual(0, point.get_y())

    # Point.__eq__() tests
    def testEqualsPointsAreSame(self):
        point_a = Point(3, 4)
        point_b = Point(3, 4)
        self.assertEqual(point_a, point_b)

    def testEqualsXValuesAreDifferent(self):
        point_a = Point(3, 4)
        point_b = Point(4, 4)
        self.assertNotEqual(point_a, point_b)

    def testEqualsYValuesAreDifferent(self):
        point_a = Point(3, 4)
        point_b = Point(3, 5)
        self.assertNotEqual(point_a, point_b)

    def testEqualsBothValuesAreDifferent(self):
        point_a = Point(3, 4)
        point_b = Point(5, 6)
        self.assertNotEqual(point_a, point_b)

    def testEqualsFirstPointIsNone(self):
        point = Point(3, 4)
        self.assertNotEqual(None, point)

    def testEqualsSecondPointIsNone(self):
        point = Point(3, 4)
        self.assertNotEqual(point, None)

    # Point.get_parent() tests
    def testGetParentNoParent(self):
        point = Point(3, 4)
        self.assertEqual(None, point.get_parent())

    def testGetParentHasAParent(self):
        point_a = Point(3, 4)
        point_b = Point(5, 6, point_a)
        self.assertEqual(point_a, point_b.get_parent())


if __name__ == '__main__':
    unittest.main()
