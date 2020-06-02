import os


class Maze:
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
