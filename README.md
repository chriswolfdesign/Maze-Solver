# Maze-Solver

This is a program that will read in a maze as a text file and use different
searching algorithms to solve it.  

Contact: chriswolfdesign@gmail.com

## Credits

I borrowed the visualization code that generates the PNG files from Harvard's Intro to Machine Learning
course.  However, the algorithms, CLI, and logic was written by me.

## Usage instructions

It is recommended to use a virtual environment of your choosing when working with this application.

Once you have your virtual environment running you can run the following commands:

make install: will install all of the necessary requirements \
make run: will run the application \
make test: will run all unit tests for the application

After you run a maze through the application, a png image representing that maze traversal
will be added into the maze_images directory.  The colors mean the following:

Gray: wall tile \
Orange: starting tile \
Green: goal tile \
Blue: tile that was traversed and is part of the path to the goal \
Red: tile that was traversed but is not part of the path to the goal \
Black: tile that was not traversed

Academic note: As I was working on this practice project, I realized it may prove
to be a useful teaching tool for an undergraduate Data Structures and Algorithms course.
Please feel free to use this project as an educational tool with your students.