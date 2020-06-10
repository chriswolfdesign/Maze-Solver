import os

from PIL import Image, ImageDraw

STARTING_POINT = 'A'
GOAL = 'B'
WALL = '#'
BLANK_TILE = ' '


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
        self._file_name = file_name
        self._generate_maze()

    def _get_width(self):
        """
        Gets the width of the maze

        :return: the width of the maze
        """
        return len(self._maze[0])

    def _get_height(self):
        """
        Gets the height of the maze

        :return: the height of the maze
        """
        return len(self._maze)

    def _generate_maze(self):
        """
        Reads the given text file and converts it to a 2D array

        :return: the 2D array representation of the maze
        """
        # if we cannot find the file, give up
        if not os.path.exists('../../' + self._file_name):
            print('ERROR -- Could not find {}!'.format(self._file_name))
            exit(1)

        file = open('../../' + self._file_name, 'r')

        # If there are incorrect number of starting or ending points, quit
        characters = file.read()

        # Ensure that the maze is valid
        self._validate_maze(characters)
        characters = characters.splitlines()
        self._create_maze_array(characters)

        # close the file
        file.close()

    def _create_maze_array(self, characters):
        """
        Generates the maze based on the characters array passed in
        :param characters: the array of characters to convert into a maze
        """
        maze = []
        # create the 2D array
        for line in characters:
            maze_line = []

            for letter in line:
                maze_line.append(letter)

            maze.append(maze_line)
        self._maze = maze

    def _validate_maze(self, characters):
        """
        Checks that the characters represents a valid maze
        If it does not, the user is informed and the program exits
        :param characters: the array of characters to check are a valid maze
        """
        if characters.count('A') != 1:
            print('ERROR -- File must have exactly one starting point!')
            exit(1)
        if characters.count('B') != 1:
            print('ERROR -- File must have exactly one goal!')
            exit(1)

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

    def draw_image(self):
        """
        Draws the maze to a png file to ease of viewing
        """
        cell_size = 50
        cell_border = 2

        image = Image.new('RGBA', (self._get_width() * cell_size, self._get_height() * cell_size),
                          'black')
        draw = ImageDraw.Draw(image)

        for i in range(self._get_height()):
            for j in range(self._get_width()):
                fill = self._get_tile_color(self._maze[i][j])

                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        file_name_without_path = self._file_name.split('/')[-1]
        image_file_name = '../../maze_images/' + file_name_without_path[:-4] + '.png'
        image.save(image_file_name)

    def _get_tile_color(self, character):
        """
        Determines what color a tile should be based on what the file represents in the maze

        :param character: the type of file the character is
        :return: a tuple containing the RGB information for the tile
        """
        if character == STARTING_POINT:
            return 255, 0, 0  # red
        elif character == GOAL:
            return 0, 255, 0  # green
        elif character == WALL:
            return 211, 211, 211  # gray
        else:
            return 0, 0, 0  # black

    def go(self):
        """
        Starts the behavior of the maze
        """
        self.draw_image()
        self.print_maze()
