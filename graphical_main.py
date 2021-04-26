import tkinter as tk
import Maze
import Maze_with_graphical_interface


def NewGame(window, segment_length, starting_point):
    """
        START NEW GAME
    """
    global vertical
    global horizontal
    global SOLUTION
    global WIDTH
    global HEIGHT
    WIDTH = int(width_input.get())
    HEIGHT = int(height_input.get())
    grid = Maze.create_maze(WIDTH, HEIGHT)
    Maze_with_graphical_interface.draw_maze(
        window, grid[0], grid[1],
        WIDTH, HEIGHT, segment_length, starting_point)
    vertical = grid[0]
    horizontal = grid[1]
    SOLUTION = grid[2]


vertical = []
horizontal = []
SOLUTION = []
WIDTH = 0
HEIGHT = 0
segment_length = 20
starting_point = (20, 20)

window = tk.Tk()
window.title("Maze Generator Game")


tk.Label(window, text="Width").grid(row=0)
tk.Label(window, text="Height").grid(row=1)

width_input = tk.Entry(window)
height_input = tk.Entry(window)

width_input.grid(row=0, column=1)
height_input.grid(row=1, column=1)


tk.Button(
    window, text="Quit", bg="black", fg="white",
    command=window.destroy
    ).grid(row=2, column=2)

tk.Button(
    window,
    text="New Game", bg="black", fg="white",
    command=lambda: NewGame(window, segment_length, starting_point)
    ).grid(row=2, column=0)

tk.Button(
    window,
    text="Solution", bg="black", fg="white",
    command=lambda: Maze_with_graphical_interface.get_solution(
        window, vertical, horizontal,
        SOLUTION, WIDTH, HEIGHT, segment_length, starting_point)
    ).grid(row=2, column=1)

window.mainloop()
