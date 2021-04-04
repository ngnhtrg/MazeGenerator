import tkinter as tk
import random


def get_neighbours(cell, width, height):
    """
        Find neighbour cells of current cell
        Width of the maze: width
        Height of the maze: height
        cell - non-negative integer number represented for the cell
            ._._._._._.
            |0.1.2.3.4|
            |5.6.7.8.9|
        Return: list of neighbour cells

    """
    neighbours = []
    if ((cell % width) != 0) :
        neighbours.append(cell - 1)
    if ((cell % width) != width - 1):
        neighbours.append(cell + 1)
    if (cell >= width):
        neighbours.append(cell - width)
    if (cell < height * width - width):
        neighbours.append(cell + width)		
    return neighbours

def create_maze(WIDTH, HEIGHT):
    """
    Create the maze using horizontal walls and vertical walls and find the solution
    Algorithm: Randomized depth-first search --> https://en.wikipedia.org/wiki/Maze_generation_algorithm
    Return: (vertical_wall, horizontal_wall, solution)
    """

    horizontal_wall = [1 for x in range(WIDTH * HEIGHT + WIDTH)]
    vertical_wall = [1 for x in range(WIDTH * HEIGHT + HEIGHT)]

    solution = []

    visited = set()
    stack = []
    initial_cell = 0
    visited.add(initial_cell)
    stack.append(initial_cell)

    while stack:
        current_cell = stack[-1]
        stack.pop()
        neighbours_of_current_cell = get_neighbours(current_cell, WIDTH, HEIGHT)
        unvisited_neighbours = [x for x in neighbours_of_current_cell if x not in visited]
        if unvisited_neighbours:
            stack.append(current_cell)
            random_index = random.randrange(len(unvisited_neighbours))
            chosen_cell = unvisited_neighbours[random_index]

            if chosen_cell - current_cell == 1:
                index = int(current_cell / WIDTH) + (chosen_cell % WIDTH) * HEIGHT
                vertical_wall[index] = 0

            elif current_cell - chosen_cell == 1:
                index = int(chosen_cell / WIDTH) + (current_cell % WIDTH) * HEIGHT
                vertical_wall[index] = 0

            elif chosen_cell - current_cell == WIDTH:
                index = current_cell % WIDTH + int(chosen_cell / WIDTH) * WIDTH
                horizontal_wall[index] = 0

            else: 
                index = chosen_cell % WIDTH + int(current_cell / WIDTH) * WIDTH
                horizontal_wall[index] = 0

            visited.add(chosen_cell)
            stack.append(chosen_cell)

            if stack[-1] == (HEIGHT * WIDTH - 1):
                solution = stack.copy()

    horizontal_wall[0] = 0
    horizontal_wall[-1] = 0
    return vertical_wall, horizontal_wall, solution
