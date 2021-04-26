import tkinter as tk
import Maze


def draw_maze(maze, vertical_lines, horizontal_lines, width, height, segment_len, starting_point):
    """
    Draw Maze
    :maze: window tk.Canvas()
    :paran vertical_lines: vertical walls between cells
    :paran horizontal_lines: horizontal walls between cells
    :width: width of Maze
    :height: height of Maze
    :segment_len: length of a side of unit cell
    :starting_point: coordinates of the starting point to draw maze
    """
    maze.delete("all")

    x_starting_point = starting_point[0]
    y_starting_point = starting_point[1]
    
    half_of_segment =  int(segment_len * 0.5)
    
    x1 = x_starting_point + half_of_segment
    y1 = y_starting_point
    x2 = x1
    y2 = y_starting_point + half_of_segment

    maze.create_line([(x1, y1),(x2, y2)], width=2, fill='red')
    
    for i in range(0, len(vertical_lines)):
        x1 = x_starting_point + segment_len * int(i / height)
        x2 = x1
        y1 = y_starting_point + segment_len * (i % height)
        y2 = y_starting_point + segment_len * (i  % height) + segment_len
        if vertical_lines[i] == 1:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="black")
        elif vertical_lines[i] == 0:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="white")

    for i in range(0, len(horizontal_lines)):
        x1 = x_starting_point + segment_len * (i % width)
        x2 = x_starting_point + segment_len * (i % width) + segment_len
        y1 = y_starting_point + segment_len * int(i / width)
        y2 = y1
        if horizontal_lines[i] == 1:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="black")
        elif horizontal_lines[i] == 0:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="white")

    maze.grid(row=3, column=0)


def get_solution(maze, solution, width, height, segment_len, starting_point):
    """
    Draw Maze and Solution
    :maze: window tk.Canvas()
    :param solution: list of cells, which is solution
    :width: width of Maze
    :height: height of Maze
    :segment_len: length of a side of unit cell
    :starting_point: coordinates of the starting point of maze
    """
    x_starting_point = starting_point[0]
    y_starting_point = starting_point[1]
        
    half_of_segment =  int(segment_len * 0.5)
    # Draw the first segment
    x1 = x_starting_point + half_of_segment
    x2 = x1
    y1 = y_starting_point
    y2 = y_starting_point + half_of_segment

    maze.create_line([(x1, y1),(x2, y2)], width=2, fill='green')

    # Draw solution
    for i in range(0, len(solution) - 1):
        x1 = x_starting_point + half_of_segment + (solution[i] % width) * segment_len
        x2 = x_starting_point + half_of_segment + (solution[i + 1] % width) * segment_len
        y1 = y_starting_point + half_of_segment + int(solution[i] / width) * segment_len
        y2 = y_starting_point + half_of_segment + int(solution[i + 1] / width) * segment_len
        maze.create_line([(x1, y1), (x2, y2)], width=2, fill='green')

    # Draw the last segment
    x1 = x_starting_point + half_of_segment + (solution[-1] % width) * segment_len
    y1 = y_starting_point + half_of_segment + int(solution[-1] / width) * segment_len
    x2 = x1
    y2 = y_starting_point + segment_len * height
    
    maze.create_line([(x1, y1),(x2, y2)], width=2, fill='green')
    maze.grid(row=3, column=0)

