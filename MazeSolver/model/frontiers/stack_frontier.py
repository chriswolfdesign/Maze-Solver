from MazeSolver.model.frontiers.frontier import Frontier


class StackFrontier(Frontier):
    """
    StackFrontier.py

    A class to represent a frontier that uses stack philosophies
    to find the solution to the maze (FILO/Depth-First)

    Author: Chris Wolf
    Version: 1.0.0 (June 30, 2020)
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def remove_point(self):
        """
        Gets the last point in the last
        :return: the last point in the list, or None if the list is empty
        """
        if len(self._points) == 0:
            return None
        else:
            point = self._points[-1]
            self._points = self._points[:-1]
            return point
