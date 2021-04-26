import tkinter as tk


def draw_maze(
    window, vertical_lines, horizontal_lines,
        width, height, segment_len, starting_point):
    """
    Draw Maze
    :window: tk.Tk()
    :paran vertical_lines: vertical walls between cells
    :paran horizontal_lines: horizontal walls between cells
    :width: width of Maze
    :height: height of Maze
    :segment_len: length of a side of unit cell
    :starting_point: coordinates of the starting point of maze
    """

    maze = tk.Canvas(window, height=500, width=500, bg='white')
    x_start = starting_point[0]
    y_start = starting_point[1]

    for i in range(0, len(vertical_lines)):
        x1 = x_start + segment_len * int(i / height)
        x2 = x_start + segment_len * int(i / height)
        y1 = y_start + segment_len * (i % height)
        y2 = y_start + segment_len * (i % height) + segment_len
        if vertical_lines[i] == 1:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="black")
        elif vertical_lines[i] == 0:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="white")

    for i in range(0, len(horizontal_lines)):
        x1 = x_start + segment_len * (i % width)
        x2 = x_start + segment_len * (i % width) + segment_len
        y1 = y_start + segment_len * int(i / width)
        y2 = y_start + segment_len * int(i / width)
        if horizontal_lines[i] == 1:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="black")
        elif horizontal_lines[i] == 0:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="white")

    maze.grid(row=3, column=0)


def get_solution(
    window, vertical_lines, horizontal_lines,
        solution, width, height, segment_len, starting_point):
    """
    Draw Maze and Solution
    :window: tk.Tk()
    :paran vertical_lines: vertical walls between cells
    :paran horizontal_lines: horizontal walls between cells
    :param solution: list of cells, which is solution
    :width: width of Maze
    :height: height of Maze
    :segment_len: length of a side of unit cell
    :starting_point: coordinates of the starting point of maze

    """

    maze = tk.Canvas(window, height=500, width=500, bg='white')
    x_start = starting_point[0]
    y_start = starting_point[1]

    half_of_seg = int(segment_len * 0.5)

    for i in range(0, len(vertical_lines)):
        x1 = x_start + segment_len * int(i / height)
        x2 = x_start + segment_len * int(i / height)
        y1 = y_start + segment_len * (i % height)
        y2 = y_start + segment_len * (i % height) + segment_len
        if vertical_lines[i] == 1:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="black")
        elif vertical_lines[i] == 0:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="white")

    for i in range(0, len(horizontal_lines)):
        x1 = x_start + segment_len * (i % width)
        x2 = x_start + segment_len * (i % width) + segment_len
        y1 = y_start + segment_len * int(i / width)
        y2 = y_start + segment_len * int(i / width)
        if horizontal_lines[i] == 1:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="black")
        elif horizontal_lines[i] == 0:
            maze.create_line([(x1, y1), (x2, y2)], width=2, fill="white")

    x1 = x_start + half_of_seg
    x2 = x1
    y1 = y_start
    y2 = y_start + half_of_seg

    maze.create_line([(x1, y1), (x2, y2)], width=2, fill='red')

    for i in range(0, len(solution) - 1):
        x1 = x_start + half_of_seg + (solution[i] % width) * segment_len
        x2 = x_start + half_of_seg + (solution[i + 1] % width) * segment_len
        y1 = y_start + half_of_seg + int(solution[i] / width) * segment_len
        y2 = y_start + half_of_seg + int(solution[i + 1] / width) * segment_len
        maze.create_line([(x1, y1), (x2, y2)], width=2, fill='red')

    x1 = x_start + half_of_seg + (solution[-1] % width) * segment_len
    y1 = y_start + half_of_seg + int(solution[-1] / width) * segment_len
    x2 = x1
    y2 = y_start + segment_len * height
    maze.create_line([(x1, y1), (x2, y2)], width=2, fill='red')
    maze.grid(row=3, column=1)
