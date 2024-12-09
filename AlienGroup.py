# -*- coding: utf-8 -*-
"""
Filename: AlienGroup.py
Author: Your Name
Date: YYYY-MM-DD
Description: This module defines the AlienGroup class which manages a group of alien objects in the Space Invader game.
TODO: -
"""

from Alien import Alien

class AlienGroup:
    def __init__(self, canvas, speed, down):
        """
        Initialize the AlienGroup with a canvas, speed, and downward movement.
        
        :param canvas: The canvas on which the aliens are drawn.
        :param speed: The speed at which the aliens move.
        :param down: The distance the aliens move down when they hit the edge.
        """
        self.canvas = canvas
        self.height = canvas.winfo_height()
        self.aliens = []
        self.speed = speed
        self.down = down
        self.direction = 1 
        self.x_offset = 100
        self.y_offset = 80
        self.row = 5
        self.col = 8
        self.bullets = []
        self.create_aliens()

    def create_aliens(self):
        """
        Create a grid of aliens.
        """
        for col in range(self.col): 
            list = []
            for row in range(self.row): 
                alien = Alien(self.canvas, self.x_offset + col * 60, self.y_offset + row * 60, self)
                list.append(alien)
            self.aliens.append(list)

    def move(self):
        """
        Move all the aliens simultaneously.
        """
        for row in self.aliens:
            for alien in row:
                alien.move(self.speed * self.direction)

    def check_edges(self):
        """
        Check if any alien has touched the edge of the screen and reverse direction if so.
        """
        xl, xr = 100, 100
        for row in self.aliens:
            for alien in row:
                x1, y1, x2, y2 = alien.get_coords()
                xl = min(x1, xl)
                xr = max(x2, xr) # Find the leftmost and rightmost aliens

        if xl <= 0: 
            self.direction *= -1 
            
            for row in self.aliens:
                for alien in row:
                    self.canvas.move(alien.alien, 0, self.down)  

        if xr >= self.canvas.winfo_width():
            self.direction *= -1

    def update_bullets(self):
        """
        Update the position of bullets and remove them if they go off-screen.
        """
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.get_coords()[1] > self.height + 30:  
                self.bullets.remove(bullet)

    def update(self):
        """
        Update the position of aliens and bullets, and check for edge collisions.
        """
        self.move()
        self.check_edges()
        for row in self.aliens:
            if len(row) == 0:
                self.aliens.remove(row)
        self.update_bullets()
        
    
    def delete(self):
        """
        Delete all aliens from the canvas.
        """
        for row in self.aliens:
            for alien in row:
                alien.delete()