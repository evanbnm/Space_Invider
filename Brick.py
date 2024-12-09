# -*- coding: utf-8 -*-
"""
Filename: Brick.py
Author: Your Name
Date: YYYY-MM-DD
Description: This module defines the Brick class used in the Space Invader game.
TODO: - Change the skin of the bricks when they are hit.
        - Add a sound effect when the bricks are hit.
"""

from PIL import Image, ImageTk

class Brick:
    def __init__(self, canvas, x, y, wall):
        """
        Initialize a Brick object.

        :param canvas: The canvas on which the brick is drawn.
        :param x: The x-coordinate of the brick.
        :param y: The y-coordinate of the brick.
        :param wall: The wall object to which the brick belongs.
        """
        self.canvas = canvas
        self.wall = wall
        original = Image.open("images/brick.png")
        resized = original.resize((36, 36))
        self.image = ImageTk.PhotoImage(resized)
        self.brick = self.canvas.create_image(x, y, image=self.image)

    def delete(self):
        """
        Delete the brick from the wall.
        """
        self.wall.brick.remove(self)

    def get_coords(self):
        """
        Get the coordinates of the brick.

        :return: A tuple containing the coordinates (x1, y1, x2, y2) of the brick.
        """
        x, y = self.canvas.coords(self.brick)
        x1 = x - 18
        y1 = y - 18
        x2 = x1 + 36
        y2 = y1 + 36
        return x1, y1, x2, y2
