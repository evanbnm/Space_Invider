# -*- coding: utf-8 -*-
"""
Filename: Bullet.py
Author: [Your Name]
Date: [Current Date]
Description: This module defines the Bullet class for the Space Invader game.

TODO: - Add collision between bullets.
"""

from PIL import Image, ImageTk

class Bullet:
    def __init__(self, canvas, x, y, direction, alien, isEnnemy=False):
        """
        Initialize a Bullet object.

        :param canvas: The canvas on which the bullet is drawn.
        :param x: The x-coordinate of the bullet.
        :param y: The y-coordinate of the bullet.
        :param direction: The direction of the bullet (1 for down, -1 for up).
        :param alien: The alien object associated with the bullet.
        :param isEnnemy: Boolean indicating if the bullet is from an enemy.
        """
        self.isEnnemy = isEnnemy
        self.canvas = canvas
        self.speed = 7
        self.direction = direction
        self.alien = alien
        original = Image.open("images/bullet.png")
        resized = original.resize((12, 30))
        if self.direction == 1:
            resized = resized.rotate(180)
        self.image = ImageTk.PhotoImage(resized)
        self.bullet = self.canvas.create_image(x, y, image=self.image)
        

    def move(self):
        """
        Move the bullet in the specified direction.
        """
        self.canvas.move(self.bullet, 0, self.direction * self.speed)

    def get_coords(self):
        """
        Get the coordinates of the bullet.

        :return: A tuple containing the coordinates (x1, y1, x2, y2) of the bullet.
        """
        x, y = self.canvas.coords(self.bullet)
        x1 = x - 6
        y1 = y - 15
        x2 = x1 + 12
        y2 = y1 + 30
        return x1, y1, x2, y2

    def delete(self):
        """
        Delete the bullet from the canvas and remove it from the alien's bullet list.
        """
        if self in self.alien.bullets:
            self.alien.bullets.remove(self)
        elif self.isEnnemy and self in self.alien.alien_group.bullets:
            self.alien.alien_group.bullets.remove(self)
