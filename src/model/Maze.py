import os


class Maze:
    def __init__(self, file_name):
        self._maze = self._generate_maze('../../' + file_name)

    def _generate_maze(self, file_name):

        if not os.path.exists(file_name):
            print('ERROR -- Could not find {}!'.format(file_name))
            exit(1)

        file = open(file_name, 'r')

        maze = []

        for line in file.readlines():
            maze_line = []

            for letter in line:
                if not letter == '\n':
                    maze_line.append(letter)

            maze.append(maze_line)

        file.close()

        return maze

    def print_maze(self):
        if self._maze is None:
            print('No maze has been loaded.')
            return

        for line in self._maze:
            for character in line:
                print(character, end='')
            print()  # for new line

    def go(self):
        self.print_maze()
