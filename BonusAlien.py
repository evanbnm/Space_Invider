# -*- coding: utf-8 -*-
"""
Filename: BonusAlien.py
Author: Your Name
Date: 2023-10-10
Description: This module defines the BonusAlien class for the Space Invader game.

TODO: - Add the capacity for the alien to move in the y-direction.
      - Add the capacity for the alien to shoot bullets.
"""
from PIL import Image, ImageTk

class BonusAlien:
    def __init__(self, canvas, x, y, direction):
        """
        Initialize the BonusAlien object.

        :param canvas: The canvas on which the alien is drawn.
        :param x: The initial x-coordinate of the alien.
        :param y: The initial y-coordinate of the alien.
        :param direction: The direction in which the alien moves.
        """
        self.canvas = canvas
        self.normalize_width = canvas.winfo_width() / 1470
        original = Image.open("images/bonus.png")
        resized = original.resize((50, 30))
        self.image = ImageTk.PhotoImage(resized)
        self.alien = self.canvas.create_image(x, y, image=self.image)

        self.score = 150
        self.direction = direction
        self.speed = self.normalize_width * 6 * self.direction

    def move(self):
        """
        Move the alien on the canvas.
        """
        self.canvas.move(self.alien, self.speed, 0)

    def delete(self):
        """
        Delete the alien from the canvas.
        """
        self.canvas.delete(self.alien)

    def get_coords(self):
        """
        Get the coordinates of the alien.

        :return: A tuple containing the coordinates (x1, y1, x2, y2) of the alien.
        """
        x, y = self.canvas.coords(self.alien)
        x1 = x - 25
        y1 = y - 15
        x2 = x1 + 50
        y2 = y1 + 30
        return x1, y1, x2, y2

    def update(self):
        """
        Update the position of the alien.
        """
        self.move()


