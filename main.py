import tkinter as tk
import Maze
import play
import os

def NewGame(window, segment_len, starting_point):
    """
        START NEW GAME

    :window: tk.Tk()
    :segment_len: length of a side of unit cell
    :starting_point: coordinates of the starting point of maze
    """
    global path
    global vertical
    global horizontal
    global SOLUTION
    global WIDTH
    global HEIGHT
    path = [0]
    WIDTH = int(width_input.get())
    HEIGHT = int(height_input.get())
    grid = Maze.create_maze(WIDTH, HEIGHT)
    play.draw_maze(window, grid[0], grid[1], WIDTH, HEIGHT, segment_len, starting_point)
    vertical = grid[0]
    horizontal = grid[1]
    SOLUTION = grid[2]



def go(maze, direction, vertical_lines, horizontal_lines, width, height, segment_len, starting_point):
    """
                    Follow the direction

    :maze: window tk.Canvas()
    :direction: direction to go
    :paran vertical_lines: vertical walls between cells
    :paran horizontal_lines: horizontal walls between cells
    :width: width of Maze
    :height: height of Maze

    """
    global path
    cur = path[-1]
    x_starting_point = starting_point[0]
    y_starting_point = starting_point[1]

    half_of_segment = int(segment_len * 0.5)


    neighbours = Maze.get_neighbours(cur, width, height)
    if direction == "U":
        next = cur - width
        if (next in neighbours):
            index = next % width + int(cur / width) * width
            if horizontal_lines[index] == 0:
                x1 = x_starting_point + half_of_segment  + (cur % width) * segment_len
                x2 = x_starting_point + half_of_segment + (next % width) * segment_len
                y1 = y_starting_point + half_of_segment + int(cur / width) * segment_len
                y2 = y_starting_point + half_of_segment + int(next / width) * segment_len
                if next not in path:
                    maze.create_line([(x1, y1), (x2, y2)], width=2, fill='red')
                    path.append(next)
                else:
                    maze.create_line([(x1, y1), (x2, y2)], width=2, fill='white')
                    path.pop()
                maze.grid()

    if direction == "D":
        next = cur + width
        if (next in neighbours):
            index = cur % width + int(next / width) * width
            if horizontal_lines[index] == 0:
                x1 = x_starting_point + half_of_segment + (cur % width) * segment_len
                x2 = x_starting_point + half_of_segment + (next % width) * segment_len
                y1 = y_starting_point + half_of_segment + int(cur / width) * segment_len
                y2 = y_starting_point + half_of_segment + int(next / width) * segment_len
                if next not in path:
                    maze.create_line([(x1, y1), (x2, y2)], width=2, fill='red')
                    path.append(next)
                else:
                    maze.create_line([(x1, y1), (x2, y2)], width=2, fill='white')
                    path.pop()
                maze.grid()

    if direction == "L":
        next = cur - 1
        if (next in neighbours):
            index = int(next / width) + (cur % width) * height
            if vertical_lines[index] == 0:
                x1 = x_starting_point + half_of_segment + (cur % width) * segment_len
                x2 = x_starting_point + half_of_segment + (next % width) * segment_len
                y1 = y_starting_point + half_of_segment + int(cur / width) * segment_len
                y2 = y_starting_point + half_of_segment + int(next / width) * segment_len
                if next not in path:
                    maze.create_line([(x1, y1), (x2, y2)], width=2, fill='red')
                    path.append(next)
                else:
                    maze.create_line([(x1, y1), (x2, y2)], width=2, fill='white')
                    path.pop()
                maze.grid()


    if direction == "R":
        next = cur + 1
        if (next in neighbours):
            index = int(cur / width) + (next % width) * height
            if vertical_lines[index] == 0:      
                x1 = x_starting_point + half_of_segment + (cur % width) * segment_len
                x2 = x_starting_point + half_of_segment + (next % width) * segment_len
                y1 = y_starting_point + half_of_segment + int(cur / width) * segment_len
                y2 = y_starting_point + half_of_segment + int(next / width) * segment_len
                if next not in path:
                    maze.create_line([(x1, y1), (x2, y2)], width=2, fill='red')
                    path.append(next)
                else:
                    maze.create_line([(x1, y1), (x2, y2)], width=2, fill='white')
                    path.pop()
                maze.grid()
    if path[-1] == height * width - 1:
        maze.create_text(250,250,fill="darkblue",font="Times 20 italic bold",
                        text="YOU WIN!")
        maze.grid()

vertical = []
horizontal = []
SOLUTION = []
WIDTH = 0
HEIGHT = 0
segment_length = 20
starting_point = (20, 20)


if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


window = tk.Tk()
window.title("Maze Generator Game")
path = []
maze = tk.Canvas(window, height=500, width=500, bg='white')



tk.Label(window, text="Width").grid(row=0)
tk.Label(window, text="Height").grid(row=1)

width_input = tk.Entry(window)
height_input = tk.Entry(window)

width_input.grid(row=0, column=1)
height_input.grid(row=1, column=1)

# QUIT
tk.Button(window, text="Quit",  bg="black", fg="white", command=window.destroy).grid(row=2, column=2)

# NEW GAME
tk.Button(window, text="New Game",  bg="black", fg="white", command=lambda: NewGame(maze, segment_length, starting_point)).grid(row=2, column=0)

# SOLUTION
tk.Button(window, text="Solution",  bg="black", fg="white", command=lambda: play.get_solution(maze, SOLUTION, WIDTH, HEIGHT, segment_length, starting_point)).grid(row=2, column=1)

# Go UP
tk.Button(window, text="U",  bg="black", fg="white", command=lambda: go(maze, "U", vertical, horizontal, WIDTH, HEIGHT, segment_length, starting_point)).grid(row=4, column=4)

# Go LEFT
tk.Button(window, text="L",  bg="black", fg="white", command=lambda: go(maze, "L", vertical, horizontal, WIDTH, HEIGHT, segment_length, starting_point)).grid(row=5, column=3)

# Go RIGHT
tk.Button(window, text="R",  bg="black", fg="white", command=lambda: go(maze, "R", vertical, horizontal, WIDTH, HEIGHT, segment_length, starting_point)).grid(row=5, column=5)

# Go DOWN
tk.Button(window, text="D",  bg="black", fg="white", command=lambda: go(maze, "D", vertical, horizontal, WIDTH, HEIGHT, segment_length, starting_point)).grid(row=6, column=4)

window.mainloop()
