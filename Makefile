run:
	python3 -m MazeSolver

test:
	python3 -m unittest discover tests/model

install:
	pip install -r requirements.txt
