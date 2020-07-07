from MazeSolver.model.frontiers.frontier import Frontier

class GreedyFrontier(Frontier):
    """
    GreedyFrontier.py

    A frontier that will utilize the greedy algorithm to find the goal

    Author: Chris Wolf
    Version: 1.0.0 (July 7, 2020)
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def remove_point(self):
        """
        Removes the point with the smallest cartesan distance from the goal, or None if the list is empty
        :return: closed point to the goal if there are points, None otherwise
        """
        if len(self._points) == 0:
            return None

        shortest_distance_from_goal_index = 0
        shortest_distance_from_goal_distance = self._calculate_cartesan_distance_from_goal(self._points[0])

        for i in range(len(self._points)):
            current_distance = self._calculate_cartesan_distance_from_goal(self._points[i])
            if current_distance < shortest_distance_from_goal_distance:
                shortest_distance_from_goal_distance = current_distance
                shortest_distance_from_goal_index = i

        return self._points.pop(shortest_distance_from_goal_index)

    def _calculate_cartesan_distance_from_goal(self, point):
        """
        Calculates the cartesan distance from the given point to the goal
        :param point: the point we are checking the cartesan distance from the goal
        :return: the cartesan distance between the given point and the goal of the maze
        """
        return abs(point.get_x() - self._goal.get_x()) + abs(point.get_y() - self._goal.get_y())
