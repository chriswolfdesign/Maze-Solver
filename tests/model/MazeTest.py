import unittest

from src.model.Maze import Maze
from src.model.Point import Point


class MazeTest(unittest.TestCase):
    """
    MazeTest.py

    Unit testing for model.Maze.py

    Author: Chris Wolf
    Version: 1.0.0 (June 2, 2020)
    """

    # Maze.__init__() tests
    def testMazeInitShouldHaveFrontierAndPointsExploredShouldBeEmpty(self):
        maze = Maze('../mazes/linear_maze.txt')
        self.assertNotEqual(None, maze._frontier)
        self.assertEqual([], maze._points_explored)
        self.assertEqual(0, len(maze._points_explored))

    # Maze._get_height() tests
    def testGetHeightMazeIsNone(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = None
        self.assertEqual(0, maze._get_height())

    def testGetHeightMazeIsEmptyList(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        self.assertEqual(0, maze._get_height())

    def testGetHeightLinearMazeShouldBeSeven(self):
        maze = Maze('../mazes/linear_maze.txt')
        self.assertEqual(7, maze._get_height())

    def testGetHeightMazeWithCycleShouldBeNine(self):
        maze = Maze('../mazes/maze_with_cycle.txt')
        self.assertEqual(9, maze._get_height())

    def testGetHeightMazeWithDeadEndShouldBeEight(self):
        maze = Maze('../mazes/maze_with_dead_end.txt')
        self.assertEqual(8, maze._get_height())

    def testGetHeightMazeWithMultipleSolutionsShouldBeEight(self):
        maze = Maze('../mazes/maze_with_multiple_solutions.txt')
        self.assertEqual(8, maze._get_height())

    def testGetHeightMazeWithTurnShouldBeNine(self):
        maze = Maze('../mazes/maze_with_turn.txt')
        self.assertEqual(9, maze._get_height())

    def testGetHeightShortestPossibleMazeShouldBeFour(self):
        maze = Maze('../mazes/shortest_possible_maze.txt')
        self.assertEqual(4, maze._get_height())

    def testGetHeightVeryShortMazeShouldBeFive(self):
        maze = Maze('../mazes/very_short_maze.txt')
        self.assertEqual(5, maze._get_height())

    # Maze._get_width() tests
    def testGetWidthEmptyMazeShouldBeZero(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = None
        self.assertEqual(0, maze._get_width())

    def testGetWidthFirstRowEmptyShouldBeZero(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        self.assertEqual(0, maze._get_width())

    def testGetWidthFromOneByOneShouldBeOne(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = [['#']]
        self.assertEqual(1, maze._get_width())

    def testGetWidthLinearMazeShouldBeThree(self):
        maze = Maze('../mazes/linear_maze.txt')
        self.assertEqual(3, maze._get_width())

    def testGetWidthMazeWithCycleShouldBeFive(self):
        maze = Maze('../mazes/maze_with_cycle.txt')
        self.assertEqual(5, maze._get_width())

    def testGetWidthMazeWithDeadEndShouldBeFive(self):
        maze = Maze('../mazes/maze_with_dead_end.txt')
        self.assertEqual(5, maze._get_width())

    def testGetWidthMazeWithMultipleSolutionsShouldBeFive(self):
        maze = Maze('../mazes/maze_with_multiple_solutions.txt')
        self.assertEqual(5, maze._get_width())

    def testGetWidthMazeWithTurnShouldBeFive(self):
        maze = Maze('../mazes/maze_with_turn.txt')
        self.assertEqual(5, maze._get_width())

    def testGetWidthShortestPossibleMazeShouldBeThree(self):
        maze = Maze('../mazes/shortest_possible_maze.txt')
        self.assertEqual(3, maze._get_width())

    def testGetWidthVeryShortMazeShouldBeThree(self):
        maze = Maze('../mazes/very_short_maze.txt')
        self.assertEqual(3, maze._get_width())

    # Maze._generate_maze() tests
    def testGenerateMazeShortestPossibleMaze(self):
        expected_result = [['#', '#', '#'], ['#', 'B', '#'], ['#', 'A', '#'], ['#', '#', '#']]
        maze = Maze('../mazes/shortest_possible_maze.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeVeryShortMaze(self):
        expected_result = [['#', '#', '#'], ['#', 'B', '#'], ['#', ' ', '#'], ['#', 'A', '#'], ['#', '#', '#']]
        maze = Maze('../mazes/very_short_maze.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeLinearMaze(self):
        expected_result = [['#', '#', '#'], ['#', 'B', '#'], ['#', ' ', '#'], ['#', ' ', '#'], ['#', ' ', '#'],
                           ['#', 'A', '#'], ['#', '#', '#']]
        maze = Maze('../mazes/linear_maze.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeMazeWithTurn(self):
        expected_result = [['#', '#', '#', '#', '#'], ['#', '#', '#', 'B', '#'], ['#', '#', '#', ' ', '#'],
                           ['#', '#', '#', ' ', '#'], ['#', ' ', ' ', ' ', '#'], ['#', ' ', '#', '#', '#'],
                           ['#', ' ', '#', '#', '#'], ['#', 'A', '#', '#', '#'], ['#', '#', '#', '#', '#']]
        maze = Maze('../mazes/maze_with_turn.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeMazeWithDeadEnd(self):
        expected_result = [['#', '#', '#', '#', '#'], ['#', ' ', '#', 'B', '#'], ['#', ' ', '#', ' ', '#'],
                           ['#', ' ', ' ', ' ', '#'], ['#', '#', ' ', '#', '#'], ['#', '#', ' ', '#', '#'],
                           ['#', '#', 'A', '#', '#'], ['#', '#', '#', '#', '#']]
        maze = Maze('../mazes/maze_with_dead_end.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeMazeWithMultipleSolutions(self):
        expected_result = [['#', '#', '#', '#', '#'], ['#', ' ', ' ', ' ', '#'], ['#', ' ', '#', 'B', '#'],
                           ['#', ' ', '#', ' ', '#'], ['#', ' ', ' ', ' ', '#'], ['#', '#', ' ', '#', '#'],
                           ['#', '#', 'A', '#', '#'], ['#', '#', '#', '#', '#']]
        maze = Maze('../mazes/maze_with_multiple_solutions.txt')
        self.assertEqual(expected_result, maze._maze)

    def testGenerateMazeMazeWithCycle(self):
        expected_result = [['#', '#', '#', '#', '#'], ['#', '#', 'B', '#', '#'], ['#', '#', ' ', '#', '#'],
                           ['#', ' ', ' ', ' ', '#'], ['#', ' ', '#', ' ', '#'], ['#', ' ', ' ', ' ', '#'],
                           ['#', '#', ' ', '#', '#'], ['#', '#', 'A', '#', '#'], ['#', '#', '#', '#', '#']]
        maze = Maze('../mazes/maze_with_cycle.txt')
        self.assertEqual(expected_result, maze._maze)

    # is_maze_complete_rectangle tests
    def testIsMazeCompleteRectangleMazeIsNoneShouldBeFalse(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = None
        self.assertFalse(maze._is_maze_complete_rectangle())

    def testIsMazeCompleteRectangleMazeIsEmptyShouldBeFalse(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        self.assertFalse(maze._is_maze_complete_rectangle())

    def testIsMazeCompleteRectangleMazeIsSingleHashShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = [['#']]
        self.assertTrue(maze._is_maze_complete_rectangle())

    def testIsMazeCompleteRectangleMazeIsSingleSpaceShouldBeFalse(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = [[' ']]
        self.assertFalse(maze._is_maze_complete_rectangle())

    def testIsMazeCompleteRectangleLinearMazeShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        self.assertTrue(maze._is_maze_complete_rectangle())

    def testIsMazeCompleteRectangleMazeWithCycleShouldBeTrue(self):
        maze = Maze('../mazes/maze_with_cycle.txt')
        self.assertTrue(maze._is_maze_complete_rectangle())

    def testIsMazeCompleteRectangleMazeWithDeadEndShouldBeTrue(self):
        maze = Maze('../mazes/maze_with_dead_end.txt')
        self.assertTrue(maze._is_maze_complete_rectangle())

    def testIsMazeCompleteRectangleMazeWithMultipleSolutionsShouldBeTrue(self):
        maze = Maze('../mazes/maze_with_multiple_solutions.txt')
        self.assertTrue(maze._is_maze_complete_rectangle())

    def testIsMazeCompleteRectangleMazeWithTurnShouldBeTrue(self):
        maze = Maze('../mazes/maze_with_turn.txt')
        self.assertTrue(maze._is_maze_complete_rectangle())

    def testIsMazeCompleteRectangleShortestPossibleMazeShouldBeTrue(self):
        maze = Maze('../mazes/shortest_possible_maze.txt')
        self.assertTrue(maze._is_maze_complete_rectangle())

    def testIsMazeCompleteRectangleVeryShortMazeShouldBeTrue(self):
        maze = Maze('../mazes/very_short_maze.txt')
        self.assertTrue(maze._is_maze_complete_rectangle())

    # does_maze_left_wall_have_gaps tests
    def testDoesMazeLeftWallHaveGapsFirstTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append([' ', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertTrue(maze._does_maze_left_wall_have_gaps())

    def testDoesMazeLeftWallHaveGapsMiddleTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append([' ', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertTrue(maze._does_maze_left_wall_have_gaps())

    def testDoesMazeLeftWallHaveGapsLastTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append([' ', '#', '#'])
        self.assertTrue(maze._does_maze_left_wall_have_gaps())

    def testDoesMazeLeftWallHaveGapsNoGapsShouldBeFalse(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertFalse(maze._does_maze_left_wall_have_gaps())

    # does_maze_right_wall_have_gaps tests
    def testDoesMazeRightWallHaveGapsFirstTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', ' '])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertTrue(maze._does_maze_right_wall_have_gaps())

    def testDoesMazeRightWallHaveGapsMiddleTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', ' '])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertTrue(maze._does_maze_right_wall_have_gaps())

    def testDoesMazeRightWallHaveGapsLastTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', ' '])
        self.assertTrue(maze._does_maze_right_wall_have_gaps())

    def testDoesMazeRightWallHaveGapsNoGapsShouldBeFalse(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertFalse(maze._does_maze_right_wall_have_gaps())

    # does_maze_top_wall_have_gaps tests
    def testDoesMazeTopWallHaveGapsFirstTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append([' ', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertTrue(maze._does_maze_top_wall_have_gaps())

    def testDoesMazeTopWallHaveGapsMiddleTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertTrue(maze._does_maze_top_wall_have_gaps())

    def testDoesMazeTopWallHaveGapsLastTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', ' '])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertTrue(maze._does_maze_top_wall_have_gaps())

    def testDoesMazeTopWallHaveGapsNoGapsShouldBeFalse(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertFalse(maze._does_maze_top_wall_have_gaps())

    # does_maze_bottom_wall_have_gaps tests
    def testDoesMazeBottomWallHaveGapsFirstTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append([' ', '#', '#'])
        self.assertTrue(maze._does_maze_bottom_wall_have_gaps())

    def testDoesBottomWallHaveGapsMiddleTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', ' ', '#'])
        self.assertTrue(maze._does_maze_bottom_wall_have_gaps())

    def testDoesBottomWallHaveGapsLastTileIsGapShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', ' '])
        self.assertTrue(maze._does_maze_bottom_wall_have_gaps())

    def testDoesBottomWallHaveGapsNoGapsShouldBeFalse(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertFalse(maze._does_maze_bottom_wall_have_gaps())

    # are_all_maze_rows_equal_length tests
    def testAreAllMazeRowsEqualLengthTopRowHasExtraTileShouldBeFalse(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertFalse(maze._are_all_maze_rows_equal_length())

    def testAreAllMazeRowsEqualLengthMiddleRowHasExtraFileShouldBeFalse(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertFalse(maze._are_all_maze_rows_equal_length())

    def testAreAllMazeRowsEqualLengthBottomRowHasExtraFileShouldBeFalse(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#', '#'])
        self.assertFalse(maze._are_all_maze_rows_equal_length())

    def testAreAllMazeRowsEqualLengthAllAreEqualLengthShouldBeTrue(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._maze = []
        maze._maze.append(['#', '#', '#'])
        maze._maze.append(['#', 'B', '#'])
        maze._maze.append(['#', ' ', '#'])
        maze._maze.append(['#', 'A', '#'])
        maze._maze.append(['#', '#', '#'])
        self.assertTrue(maze._are_all_maze_rows_equal_length())

    # Maze._find_starting_point() tests
    def testFindStartingPointLinearMazeShouldBeOneFive(self):
        maze = Maze('../mazes/linear_maze.txt')
        self.assertEqual(Point(1, 5), maze._find_starting_point())

    def testFindStartingPointMazeWithCycleShouldBeTwoSeven(self):
        maze = Maze('../mazes/maze_with_cycle.txt')
        self.assertEqual(Point(2, 7), maze._find_starting_point())

    def testFindStartingPointMazeWithDeadEndShouldBeTwoSix(self):
        maze = Maze('../mazes/maze_with_dead_end.txt')
        self.assertEqual(Point(2, 6), maze._find_starting_point())

    def testFindStartingPointMazeWithTurnShouldBeOneSeven(self):
        maze = Maze('../mazes/maze_with_turn.txt')
        self.assertEqual(Point(1, 7), maze._find_starting_point())

    def testFindStartingPointMazeShortestPossibleMazeShouldBeOneTwo(self):
        maze = Maze('../mazes/shortest_possible_maze.txt')
        self.assertEqual(Point(1, 2), maze._find_starting_point())

    def testFindStartingPointVeryShortMazeShouldOneThree(self):
        maze = Maze('../mazes/very_short_maze.txt')
        self.assertEqual(Point(1, 3), maze._find_starting_point())

    # Maze._find_goal() tests
    def testFindGoalLinearMazeShouldBeOneOne(self):
        maze = Maze('../mazes/linear_maze.txt')
        self.assertEqual(Point(1, 1), maze._find_goal())

    def testFindGoalMazeWithCycleShouldBeTwoOne(self):
        maze = Maze('../mazes/maze_with_cycle.txt')
        self.assertEqual(Point(2, 1), maze._find_goal())

    def testFindGoalMazeWithDeadEndShouldBeThreeOne(self):
        maze = Maze('../mazes/maze_with_dead_end.txt')
        self.assertEqual(Point(3, 1), maze._find_goal())

    def testFindGoalMazeWithTurnShouldBeThreeOne(self):
        maze = Maze('../mazes/maze_with_turn.txt')
        self.assertEqual(Point(3, 1), maze._find_goal())

    def testFindGoalMazeShortestPossibleMazeShouldBeOneOne(self):
        maze = Maze('../mazes/shortest_possible_maze.txt')
        self.assertEqual(Point(1, 1), maze._find_goal())

    def testFindGoalVeryShortMazeShouldBeOneOne(self):
        maze = Maze('../mazes/very_short_maze.txt')
        self.assertEqual(Point(1, 1), maze._find_goal())

    # Maze._add_point() tests
    def testAddPointAddingNoneShouldNotBeAdded(self):
        maze = Maze('../mazes/linear_maze.txt')
        self.assertNotEqual(None, maze._frontier)
        self.assertEqual([], maze._frontier._points)
        self.assertEqual(0, len(maze._frontier._points))
        self.assertEqual([], maze._points_explored)
        self.assertEqual(0, len(maze._points_explored))
        maze._add_point(None)
        self.assertEqual([], maze._frontier._points)
        self.assertEqual(0, len(maze._frontier._points))
        self.assertEqual([], maze._points_explored)
        self.assertEqual(0, len(maze._points_explored))

    def testAddPointAddWallTileShouldNotBeAdded(self):
        maze = Maze('../mazes/linear_maze.txt')
        self.assertNotEqual(None, maze._frontier)
        self.assertEqual([], maze._frontier._points)
        self.assertEqual(0, len(maze._frontier._points))
        self.assertEqual([], maze._points_explored)
        self.assertEqual(0, len(maze._points_explored))
        maze._add_point(Point(0, 0))
        self.assertEqual([], maze._frontier._points)
        self.assertEqual(0, len(maze._frontier._points))
        self.assertEqual([], maze._points_explored)
        self.assertEqual(0, len(maze._points_explored))

    def testAddPointAddingValidPointShouldBeAdded(self):
        maze = Maze('../mazes/linear_maze.txt')
        self.assertEqual([], maze._frontier._points)
        self.assertEqual(0, len(maze._frontier._points))
        self.assertEqual([], maze._points_explored)
        self.assertEqual(0, len(maze._points_explored))
        maze._add_point(Point(1, 3))
        self.assertEqual([Point(1, 3)], maze._frontier._points)
        self.assertEqual(1, len(maze._frontier._points))
        self.assertEqual([Point(1, 3)], maze._points_explored)
        self.assertEqual([Point(1, 3)], maze._points_explored)

    def testAddPointAddingPointAlreadyThereShouldNotBeAdded(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._add_point(Point(1, 3))
        self.assertEqual([Point(1, 3)], maze._frontier._points)
        self.assertEqual(1, len(maze._frontier._points))
        self.assertEqual([Point(1, 3)], maze._points_explored)
        self.assertEqual([Point(1, 3)], maze._points_explored)
        maze._add_point(Point(1, 3))
        self.assertEqual([Point(1, 3)], maze._frontier._points)
        self.assertEqual(1, len(maze._frontier._points))
        self.assertEqual([Point(1, 3)], maze._points_explored)
        self.assertEqual([Point(1, 3)], maze._points_explored)

    def testAddPointAddingValidPointToNonEmptyListShouldBeAdded(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._add_point(Point(1, 3))
        self.assertEqual([Point(1, 3)], maze._frontier._points)
        self.assertEqual(1, len(maze._frontier._points))
        self.assertEqual([Point(1, 3)], maze._points_explored)
        self.assertEqual([Point(1, 3)], maze._points_explored)
        maze._add_point(Point(1, 4))
        self.assertEqual([Point(1, 3), Point(1, 4)], maze._frontier._points)
        self.assertEqual(2, len(maze._frontier._points))
        self.assertEqual([Point(1, 3), Point(1, 4)], maze._points_explored)
        self.assertEqual(2, len(maze._points_explored))

    # Maze._solve_maze() tests
    def testSolveMazeMazeWithCycleShouldHaveTwelveExploredTiles(self):
        maze = Maze('../mazes/maze_with_cycle.txt')
        maze._solve_maze()
        expected_maze = [['#', '#', '#', '#', '#'], ['#', '#', 'B', '#', '#'], ['#', '#', 'O', '#', '#'],
                         ['#', 'O', 'O', 'X', '#'], ['#', 'O', '#', 'X', '#'], ['#', 'O', 'O', 'X', '#'],
                         ['#', '#', 'O', '#', '#'], ['#', '#', 'A', '#', '#'], ['#', '#', '#', '#', '#']]
        self.assertEqual(expected_maze, maze._maze)
        self.assertEqual(12, maze._number_explored_tiles)

    def testSolveMazeLinearMazeShouldHaveFiveExploredTiles(self):
        maze = Maze('../mazes/linear_maze.txt')
        maze._solve_maze()
        expected_maze = [['#', '#', '#'], ['#', 'B', '#'], ['#', 'O', '#'], ['#', 'O', '#'], ['#', 'O', '#'],
                         ['#', 'A', '#'], ['#', '#', '#']]
        self.assertEqual(expected_maze, maze._maze)
        self.assertEqual(5, maze._number_explored_tiles)

    def testSolveMazeMazeWithDeadEndShouldHaveTenExploredTiles(self):
        maze = Maze('../mazes/maze_with_dead_end.txt')
        maze._solve_maze()
        expected_maze = [['#', '#', '#', '#', '#'], ['#', 'X', '#', 'B', '#'], ['#', 'X', '#', 'O', '#'],
                         ['#', 'X', 'O', 'O', '#'], ['#', '#', 'O', '#', '#'], ['#', '#', 'O', '#', '#'],
                         ['#', '#', 'A', '#', '#'], ['#', '#', '#', '#', '#']]
        self.assertEqual(expected_maze, maze._maze)
        self.assertEqual(10, maze._number_explored_tiles)

    def testSolveMazeMazeWithMultipleSolutionsShouldHaveNineExploredTiles(self):
        maze = Maze('../mazes/maze_with_multiple_solutions.txt')
        maze._solve_maze()
        expected_maze = [['#', '#', '#', '#', '#'], ['#', ' ', ' ', ' ', '#'], ['#', 'X', '#', 'B', '#'],
                         ['#', 'X', '#', 'O', '#'], ['#', 'X', 'O', 'O', '#'], ['#', '#', 'O', '#', '#'],
                         ['#', '#', 'A', '#', '#'], ['#', '#', '#', '#', '#']]
        self.assertEqual(expected_maze, maze._maze)
        self.assertEqual(9, maze._number_explored_tiles)

    def testSolveMazeVeryShortMazeShouldHaveTwoExploredTiles(self):
        maze = Maze('../mazes/very_short_maze.txt')
        maze._solve_maze()
        expected_maze = [['#', '#', '#'], ['#', 'B', '#'], ['#', 'O', '#'], ['#', 'A', '#'], ['#', '#', '#']]
        self.assertEqual(expected_maze, maze._maze)
        self.assertEqual(2, maze._number_explored_tiles)

    def testSolveMazeShortestPossibleMazeShouldHaveOneExploredTile(self):
        maze = Maze('../mazes/shortest_possible_maze.txt')
        maze._solve_maze()
        expected_maze = [['#', '#', '#'], ['#', 'B', '#'], ['#', 'A', '#'], ['#', '#', '#']]
        self.assertEqual(expected_maze, maze._maze)
        self.assertEqual(1, maze._number_explored_tiles)

    def testSolveMazeMazeWithTurnShouldHaveNineExploredTiles(self):
        maze = Maze('../mazes/maze_with_turn.txt')
        maze._solve_maze()
        expected_maze = [['#', '#', '#', '#', '#'], ['#', '#', '#', 'B', '#'], ['#', '#', '#', 'O', '#'],
                         ['#', '#', '#', 'O', '#'], ['#', 'O', 'O', 'O', '#'], ['#', 'O', '#', '#', '#'],
                         ['#', 'O', '#', '#', '#'], ['#', 'A', '#', '#', '#'], ['#', '#', '#', '#', '#']]
        self.assertEqual(expected_maze, maze._maze)
        self.assertEqual(9, maze._number_explored_tiles)


if __name__ == '__main__':
    unittest.main()
