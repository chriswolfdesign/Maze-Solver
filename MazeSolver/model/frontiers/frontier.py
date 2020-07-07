class Frontier:
    """
    Frontier.py

    A class that represents an interface of the different ways
    we could traverse our maze searching for the goal

    Author: Chris Wolf
    Version: 1.0.0 (June 25, 2020)
    """
    def __init__(self):
        """
        Constructor
        """
        self._points = []

    def set_goal(self, goal):
        """
        Setter for the goal field
        :param goal: the goal for the frontier to reach
        """
        self._goal = goal

    def add_point(self, point):
        """
        If the point is not None, add it to the list of points
        :param point: point to be added to the list
        """
        if point is not None:
            self._points.append(point)

    def remove_point(self):
        """
        Does nothing, subclasses should inherit this method to remove and return
        a point from the list
        """
        pass
