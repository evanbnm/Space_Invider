# -*- coding: utf-8 -*-
"""
Filename: Alien.py
Author: Evan et Mathis
Date: 2024-11-26
Description: 

TODO: 
-Change the color of the alien when it is hit by a bullet.
"""

from PIL import Image, ImageTk
from Bullet import Bullet

class Alien:
    def __init__(self, canvas, x, y, alien_group):
        """
        Initialize an Alien instance.

        Parameters:
        canvas (Canvas): The canvas on which the alien is drawn.
        x (int): The x-coordinate of the alien.
        y (int): The y-coordinate of the alien.
        alien_group (AlienGroup): The group to which this alien belongs.
        """
        self.canvas = canvas
        self.height = canvas.winfo_height()
        self.alien_group = alien_group
        original = Image.open("images/alien.png")
        resized = original.resize((40, 30))
        self.image = ImageTk.PhotoImage(resized)
        self.alien = self.canvas.create_image(x, y, image=self.image)
        self.bullets = [] 

    def move(self, speed):
        """
        Move the alien horizontally.

        Parameters:
        speed (int): The speed at which the alien moves.
        """
        self.canvas.move(self.alien, speed, 0)

    def get_coords(self):
        """
        Get the coordinates of the alien.

        Returns:
        tuple: The coordinates (x1, y1, x2, y2) of the alien.
        """
        x, y = self.canvas.coords(self.alien)
        x1 = x - 20
        y1 = y - 15
        x2 = x1 + 40
        y2 = y1 + 30
        return x1, y1, x2, y2
    
    def fire(self):
        """
        Fire a bullet from the alien.
        """
        x1, y1, x2, y2 = self.get_coords()
        bullet = Bullet(self.canvas, (x1 + x2) / 2, y2 + 5, 1, self, True)
        self.alien_group.bullets.append(bullet)

    def delete(self):
        """
        Delete the alien from the canvas.
        """
        self.canvas.delete(self.alien)
        
    def update(self):
        """
        Update the state of the alien, including moving bullets and removing
        bullets that have left the screen.
        """
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.get_coords()[1] > self.height:  # Si la balle sort de l'écran
                bullet.delete()
                self.bullets.remove(bullet)