# -*- coding: utf-8 -*-
"""
Filename: Life.py
Author: Evan et Mathis
Date: 2024-11-26
Description: This module defines the Life class for managing player lives in a game.
TODO: Implement additional features such as saving and loading lives.
"""

import tkinter as tk

class Life:
    def __init__(self, root):
        """
        Initialize the Life class with the root window and set up the label.
        
        Args:
            root (tk.Tk): The root window of the Tkinter application.
        """
        self.root = root
        self.lives = 3
        self.label = tk.Label(root, text="Lives: " + str(self.lives), bg="black", fg="lime")
        self.label.config(font=("Arial", 25))
        self.label.pack(side="top")

    def update(self):
        """
        Update the label to display the current number of lives.
        """
        self.label.config(text="Lives: " + str(self.lives))

    def lose_life(self):
        """
        Decrease the number of lives by one and update the label.
        """
        self.lives -= 1
        self.update()

    def gain_life(self):
        """
        Increase the number of lives by one and update the label.
        """
        self.lives += 1
        self.update()

    def reset(self):
        """
        Reset the number of lives to the initial value and update the label.
        """
        self.lives = 3
        self.update()