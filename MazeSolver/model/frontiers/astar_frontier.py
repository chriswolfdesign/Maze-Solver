from MazeSolver.model.frontiers.greedy_frontier import GreedyFrontier
from MazeSolver.model.point import Point

class AStarFrontier(GreedyFrontier):
    """
    astar_frontier.py

    A frontier that removes points using the AStar algorithm

    Author: Chris Wolf
    Version: 1.0.0 (July 9, 2020)
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def remove_point(self):
        """
        Removes and returns the point that has the least sum between distance travelled and cartesan distance
        from the goal
        :return: the point that fits the above criteria, or None if there are no points in the list
        """
        if len(self._points) == 0:
            return None

        smallest_potential_index = 0
        smallest_potential_value = self._calculate_cartesan_distance_from_goal(self._points[0]) + \
            self._distance_traveled(self._points[0])

        for i in range(len(self._points)):
            potential_value = self._calculate_cartesan_distance_from_goal(self._points[i]) + \
                    self._distance_traveled(self._points[i])
                        
            if potential_value < smallest_potential_value:
                smallest_potential_value = potential_value
                smallest_potential_index = i

        return self._points.pop(smallest_potential_index)

    def _distance_traveled(self, point):
        """
        Returns how many parent-child links they are between this point and the original point
        :param point: the point we are assessing the distance traveled
        :return: number representing how far has been traveled from the initial point to the given point
        """
        distance_traveled = 0
        current_point = point.get_parent()

        while current_point is not None:
            distance_traveled = distance_traveled + 1
            current_point = current_point.get_parent()

        return distance_traveled
