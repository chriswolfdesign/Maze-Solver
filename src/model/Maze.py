import os

from PIL import Image, ImageDraw


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

        self._maze = maze

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
        if character == 'A':
            return 255, 0, 0  # red
        elif character == 'B':
            return 0, 255, 0  # green
        elif character == '#':
            return 211, 211, 211  # gray
        else:
            return 0, 0, 0  # black

    def go(self):
        """
        Starts the behavior of the maze
        """

        self.draw_image()
        self.print_maze()
