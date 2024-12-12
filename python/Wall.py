# -*- coding: utf-8 -*-
"""
Filename: Wall.py
Author: Evan et Mathis
Date: 2024-11-26
Description: This module defines the Wall class which creates a wall of bricks in a canvas.

TODO:
- Allow an alien to destroy all the wall in one super bullet.
"""

from python.Brick import Brick

class Wall:
    def __init__(self, canvas, x, y):
        """
        Initialize the Wall with a canvas, and starting x and y coordinates.
        
        Args:
            canvas: The canvas on which the wall is drawn.
            x (int): The starting x-coordinate of the wall.
            y (int): The starting y-coordinate of the wall.
        """
        self.canvas = canvas
        self.brick = []
        self.x = x
        self.y = y
        self.create()
    
    def create(self):
        """
        Create a wall of bricks on the canvas.
        
        The wall consists of 6 columns and 4 rows of bricks.
        """
        for i in range(6):
            for j in range(4):
                brick = Brick(self.canvas, self.x + i * 36, self.y + j * 36, self)
                self.brick.append(brick)






