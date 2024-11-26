import tkinter as tk
from Game import Game

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.title("Space Invaders")
    root.attributes("-fullscreen", True)
    root.mainloop()