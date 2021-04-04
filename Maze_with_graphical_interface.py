import tkinter as tk
import Maze


def draw_maze(window, vertical_lines, horizontal_lines, width, height):
    """
    Draw Maze
    :window: tk.Tk()
    :paran vertical_lines: vertical walls between cells
    :paran horizontal_lines: horizontal walls between cells
    :width: width of Maze
    :height: height of Maze
    """

    maze = tk.Canvas(window, height=500, width=500, bg='white')
    segment_len = 20
    for i in range(0, len(vertical_lines)):
        x1 = segment_len + segment_len * int(i / height)
        x2 = segment_len + segment_len * int(i / height)
        y1 = segment_len + segment_len * (i % height)
        y2 = segment_len + segment_len * (i  % height) + segment_len
        if vertical_lines[i] == 1:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="black")
        elif vertical_lines[i] == 0:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="white")

    for i in range(0, len(horizontal_lines)):
        x1 = segment_len + segment_len * (i % width)
        x2 = segment_len + segment_len * (i % width) + segment_len
        y1 = segment_len + segment_len * int(i / width)
        y2 = segment_len + segment_len * int(i / width)
        if horizontal_lines[i] == 1:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="black")
        elif horizontal_lines[i] == 0:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="white")

    maze.grid(row=3, column=0)

def get_solution(window, vertical_lines, horizontal_lines, solution, width, height):
    """
    Draw Maze and Solution
    :window: tk.Tk()
    :paran vertical_lines: vertical walls between cells
    :paran horizontal_lines: horizontal walls between cells
    :param solution: list of cells, which is solution
    :width: width of Maze
    :height: height of Maze
    """


    maze = tk.Canvas(window, height=500, width=500, bg='white')
    segment_len = 20

    for i in range(0, len(vertical_lines)):
        x1 = segment_len + segment_len * int(i / height)
        x2 = segment_len + segment_len * int(i / height)
        y1 = segment_len + segment_len * (i % height)
        y2 = segment_len + segment_len * (i  % height) + segment_len
        if vertical_lines[i] == 1:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="black")
        elif vertical_lines[i] == 0:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="white")

    for i in range(0, len(horizontal_lines)):
        x1 = segment_len + segment_len * (i % width)
        x2 = segment_len + segment_len * (i % width) + segment_len
        y1 = segment_len + segment_len * int(i / width)
        y2 = segment_len + segment_len * int(i / width)
        if horizontal_lines[i] == 1:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="black")
        elif horizontal_lines[i] == 0:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="white")

    x1 = int(segment_len * 1.5)
    y1 = segment_len
    x2 = int(segment_len * 1.5)
    y2 = int(segment_len * 1.5)

    maze.create_line([(x1, y1),(x2, y2)], width=2, fill='red')

    for i in range(0, len(solution) - 1):
        x1 = int(segment_len * 1.5) + (solution[i] % width) * segment_len
        x2 = int(segment_len * 1.5) + (solution[i + 1] % width) * segment_len
        y1 = int(segment_len * 1.5) + int(solution[i] / width) * segment_len
        y2 = int(segment_len * 1.5) + int(solution[i + 1] / width) * segment_len
        maze.create_line([(x1, y1), (x2, y2)], width=2, fill='red')

    x1 = int(segment_len * 1.5) + (solution[-1] % width) * segment_len
    y1 = int(segment_len * 1.5) + int(solution[-1] / width) * segment_len
    x2 = int(segment_len * (width + 0.5))
    y2 = segment_len * (height + 1)
    maze.create_line([(x1, y1),(x2, y2)], width=2, fill='red')
    maze.grid(row=3, column=1)
