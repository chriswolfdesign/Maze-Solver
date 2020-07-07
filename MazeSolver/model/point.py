class Point:
    """
    Point.py

    A class to represent a point in our maze

    Author: Chris Wolf
    Version: 1.0.0 (June 25, 2020)
    """

    def __init__(self, x, y, parent=None):
        """
        Constructor
        :param x: the x coordinate for the point
        :param y: the y coordinate for the point
        :param parent: the point that the mouse came from to this point (if any)
        """
        self._x = x
        self._y = y
        self._parent = parent

    def get_x(self):
        """
        Getter for x-coordinate
        :return: the point's x-coordinate
        """
        return self._x

    def get_y(self):
        """
        Getter for the y-coordinate
        :return: the point's y-coordinate
        """
        return self._y

    def get_parent(self):
        """
        Getter for the parent
        :return: the point the maze came to this point from
        """
        return self._parent

    def __eq__(self, other):
        """
        Determines if this point and the other have the same x and y coordinates
        :param other: the other coordinate we are comparing to
        :return: True if they have the same x and y coordinates, False otherwise
        """
        if self is None or other is None:
            return False
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()
