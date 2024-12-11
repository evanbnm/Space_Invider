# -*- coding: utf-8 -*-
"""
Filename: Score.py
Author: Your Name
Date: YYYY-MM-DD
Description: This module defines the Score class for managing the game score in a tkinter application.
TODO: 
- Add more functionalities to handle high scores.
"""

import tkinter as tk

class Score:
    def __init__(self, root):
        """
        Initialize the Score class with the root tkinter window.
        
        Args:
            root (tk.Tk): The root tkinter window.
        """
        self.root = root
        self.score = 0
        self.label = tk.Label(root, text="Score: " + str(self.score), bg="black", fg="lime")
        self.label.config(font=("Arial", 25))
        self.label.pack(side="top")

    def update(self):
        """
        Update the score label with the current score.
        """
        self.label.config(text="Score: " + str(self.score))

    def add(self, points):
        """
        Add points to the current score and update the label.
        
        Args:
            points (int): The number of points to add to the score.
        """
        self.score += points
        self.update()

    def get_score(self):
        """
        Get the current score.
        
        Returns:
            int: The current score.
        """
        return self.score

    def reset(self):
        """
        Reset the score to zero and update the label.
        """
        self.score = 0
        self.update()