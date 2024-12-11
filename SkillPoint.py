# -*- coding: utf-8 -*-
"""
Filename: SkillPoint.py
Author: Evan et Mathis
Date: 2024-12-01
Description: This module manages skill points for a game, allowing upgrades to bullet rate and count.

TODO: 
- Add more upgrade options.
"""

import tkinter as tk

class SkillPoint:
    def __init__(self, root, canvas):
        """
        Initialize the SkillPoint class with the root window and canvas.
        
        Args:
            root (tk.Tk): The root window.
            canvas (tk.Canvas): The canvas widget.
        """
        self.root = root
        self.canvas = canvas
        self.screen_width = self.canvas.winfo_screenwidth()
        self.screen_height = self.canvas.winfo_screenheight()
        self.points = 0
        self.label = tk.Label(root, text="Skill Points : " + str(self.points), bg="black", fg="lime")
        self.label.config(font=("Arial", 25))
        self.label.pack(side="top")
        
        self.max_bullets = 2
        self.time_bullets = 1050

        self.level_bullets = 1
        self.level_rate = 1

    def add_point(self):
        """
        Add a skill point and update the display.
        """
        self.points += 1
        self.update()

    def upgrade_rate(self):
        """
        Upgrade the bullet rate if enough points are available.
        Display an error message if the maximum level is reached or not enough points.
        """
        if self.level_rate == "max":
            self.canvas.delete("all")
            self.error = self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="MAX LEVEL REACHED", fill="red", font=("Arial", 50))
            self.canvas.after(1500, lambda: self.canvas.delete("all"))
            return
        if self.points > 0:
            self.time_bullets -= 100
            self.points -= 1
            self.level_rate += 1
            if self.level_rate == 10:
                self.level_rate = "max"
            self.update()
        else:
            self.canvas.delete("all")
            self.error = self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="NOT ENOUGH POINTS", fill="red", font=("Arial", 50))
            self.canvas.after(1500, lambda: self.canvas.delete("all"))

    def upgrade_bullets(self):
        """
        Upgrade the maximum number of bullets on the screen in same time if enough points are available.
        Display an error message if the maximum level is reached or not enough points.
        """
        if self.level_bullets == "max":
            self.canvas.delete("all")
            self.error = self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="MAX LEVEL REACHED", fill="red", font=("Arial", 50))
            self.canvas.after(1500, lambda: self.canvas.delete("all"))
            return
        if self.points > 0:
            self.max_bullets += 1
            self.points -= 1
            self.level_bullets += 1
            if self.level_bullets == 10:
                self.level_bullets = "max"
            self.update()
        else:
            self.canvas.delete("all")
            self.error = self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="NOT ENOUGH POINTS", fill="red", font=("Arial", 50))
            self.canvas.after(1500, lambda: self.canvas.delete(self.error))

    def reset(self):
        """
        Reset all skill levels and points to their initial values.
        """
        self.level_bullets = 1
        self.level_rate = 1
        self.points = 0
        self.max_bullets = 2
        self.time_bullets = 1050
        self.update()

    def update(self):
        """
        Update the skill points display label.
        """
        self.label.config(text="Skill Points : " + str(self.points))

