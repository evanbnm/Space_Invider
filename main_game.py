# -*- coding: utf-8 -*-
"""
Filename: main_game.py
Author: Evan et Mathis
Date: 2024-12-09
Description: Main script to run the Space Invaders game using tkinter.
"""

import tkinter as tk
from python.Game import Game

def main():
    """
    Initialize the main window and start the Space Invaders game.
    """
    root = tk.Tk()
    game = Game(root)
    root.title("Space Invaders")
    root.after(100, lambda: root.attributes("-fullscreen", True))
    root.mainloop()

if __name__ == "__main__":
    main()