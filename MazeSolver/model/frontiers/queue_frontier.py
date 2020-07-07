from MazeSolver.model.frontiers.frontier import Frontier


class QueueFrontier(Frontier):
    """
    QueueFrontier.py

    A class that represents the queue based algorithm (FIFO) for searching
    a maze.

    Author: Chris Wolf
    Version: 1.0.0 (June 25, 2020)
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def remove_point(self):
        """
        Returns the first point in the list, or None if the list is empty
        :return: the first point in the list
        """
        if len(self._points) == 0:
            return None
        else:
            point = self._points[0]
            self._points = self._points[1:]
            return point
