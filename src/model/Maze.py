import os


class Maze:
    """
    Maze.py

    The object that stores the different tiles in our maze.

    Author: Chris Wolf
    Version: 1.0.0 (June 2, 2020)
    """

    def __init__(self, file_name):
        """
        Constructor

        :param file_name: the text file we are reading the maze from
        """
        self._maze = self._generate_maze('../../' + file_name)

    def _generate_maze(self, file_name):
        """
        Reads the given text file and converts it to a 2D array

        :param file_name: the text file we are reading the maze from

        :return: the 2D array representation of the maze
        """

        # if we cannot find the file, give up
        if not os.path.exists(file_name):
            print('ERROR -- Could not find {}!'.format(file_name))
            exit(1)

        file = open(file_name, 'r')

        maze = []

        # create the 2D array
        for line in file.readlines():
            maze_line = []

            for letter in line:
                if not letter == '\n':
                    maze_line.append(letter)

            maze.append(maze_line)

        # close the file
        file.close()

        return maze

    def print_maze(self):
        """
        Prints the maze to the terminal
        """
        if self._maze is None:
            print('No maze has been loaded.')
            return

        for line in self._maze:
            for character in line:
                print(character, end='')
            print()  # for new line

    def go(self):
        """
        Starts the behavior of the maze
        """

        self.print_maze()
