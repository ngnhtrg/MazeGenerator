import tkinter as tk
import Maze
import Maze_with_graphical_interface

def NewGame(window):
    """
        START NEW GAME
    """
    global vertical
    global horizontal
    global SOLUTION
    global _WIDTH
    global _HEIGHT
    _WIDTH = int(e1.get())
    _HEIGHT = int(e2.get())
    grid = Maze.create_maze(_WIDTH, _HEIGHT)
    Maze_with_graphical_interface.draw_maze(window, grid[0], grid[1], _WIDTH, _HEIGHT)
    vertical = grid[0]
    horizontal = grid[1]
    SOLUTION = grid[2]

vertical = []
horizontal = []
SOLUTION = []
_WIDTH = 0
_HEIGHT = 0
window = tk.Tk()
window.title("Maze Generator Game")


tk.Label(window, text="Width").grid(row=0)
tk.Label(window, text="Height").grid(row=1)

e1 = tk.Entry(window)
e2 = tk.Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


tk.Button(window, text="Quit",  bg="black", fg="white", command=window.destroy).grid(row=2, column=2)

tk.Button(window, text="New Game",  bg="black", fg="white", command=lambda: NewGame(window)).grid(row=2, column=0)

tk.Button(window, text="Solution",  bg="black", fg="white", command=lambda: Maze_with_graphical_interface.get_solution(window,vertical, horizontal, SOLUTION, _WIDTH, _HEIGHT)).grid(row=2, column=1)

window.mainloop()
