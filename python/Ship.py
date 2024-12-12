# -*- coding: utf-8 -*-
"""
Filename: Ship.py
Author: Evan et Mathis
Date: 2024-11-26
Description: This module defines the Ship class for the Space Invader game.
TODO: Add more functionalities and improve the game mechanics.
"""

from PIL import Image, ImageTk
from python.Bullet import Bullet

class Ship:
    def __init__(self, canvas, max_bullets, time_bullets):
        """
        Initialize the Ship with canvas, max bullets, and bullet cooldown time.

        :param canvas: The canvas on which the ship is drawn.
        :param max_bullets: The maximum number of bullets the ship can fire.
        :param time_bullets: The cooldown time between firing bullets.
        """
        self.canvas = canvas
        self.height = canvas.winfo_height()
        self.width = canvas.winfo_width()
        self.normalize_width = canvas.winfo_width() / 1470
        original = Image.open("images/ship.png")
        resized = original.resize((40, 50))
        self.image = ImageTk.PhotoImage(resized)
        self.ship = self.canvas.create_image(0, 0, image=self.image)

        self.life = False #  Cheat code to add a life
        self.skill = False # Cheat code to add a skill point

        self.speed = self.normalize_width * 4
        self.canvas.move(self.ship, self.width * 0.5 , self.height * 0.95)  # Initial position
        self.pressed_keys = set() # Set of currently pressed keys to have smooth movements
        self.bullets = [] 

        self.default_max_bullets = max_bullets
        self.default_time_bullets = time_bullets

        self.max_bullets = max_bullets
        self.time_bullets = time_bullets

        self.keybinds = {} 
        self.get_keybinds()

        self.canvas.bind_all("<KeyPress>", self.on_key_press) # Bind key press events
        self.canvas.bind_all("<KeyRelease>", self.on_key_release) # Bind key release events

    def get_keybinds(self):
        """Load key bindings from a file."""
        with open("data/keybinds.txt", "r") as file: # Load keybinds from a file to save them even after closing the game
            for line in file:
                action, key = line.strip().split(" : ")
                self.keybinds[action] = key

    def on_key_press(self, event): 
        """Handle key press events."""
        self.pressed_keys.add(event.keysym.upper())

    def on_key_release(self, event):
        """Handle key release events."""
        self.pressed_keys.discard(event.keysym.upper())

    def get_coords(self):
        """Get the current coordinates of the ship."""
        x, y = self.canvas.coords(self.ship)
        x1 = x - 20
        y1 = y - 25
        x2 = x1 + 40
        y2 = y1 + 50
        return x1, y1, x2, y2

    def fire(self):
        """Fire a bullet if the cooldown period has passed."""
        x1, y1, x2, y2 = self.get_coords()

        if len(self.bullets) < self.max_bullets and not hasattr(self, 'last_fire_time'): # Check if the ship can fire a bullet
            bullet = Bullet(self.canvas, (x1 + x2) / 2, y1 - 5, -1, self) # Create a bullet at the top center of the ship
            self.bullets.append(bullet)
            self.last_fire_time = self.canvas.after(self.time_bullets, self.reset_fire_cooldown) # Set the cooldown period

    def reset_fire_cooldown(self):
        """Reset the fire cooldown period."""
        del self.last_fire_time
            

    def delete(self):
        """Delete the ship and all its bullets from the canvas."""
        self.canvas.delete(self.ship)
        for bullet in self.bullets:
            bullet.delete()

    def add_life(self):
        """Add a life to the ship."""
        self.life = True

    def update(self):
        """Update the ship's position and handle key presses."""
        x1, y1, x2, y2 = self.get_coords()

        if self.keybinds['Move left'] in self.pressed_keys and x1 > 0: # Move the ship left and if it reaches the edge of the screen, stop it
            self.canvas.move(self.ship, -self.speed, 0)
        if self.keybinds['Move right'] in self.pressed_keys and x2 < self.canvas.winfo_width(): # Move the ship right and if it reaches the edge of the screen, stop it
            self.canvas.move(self.ship, self.speed, 0)
        if self.keybinds['Shoot'] in self.pressed_keys: # Shoot a bullet
            self.fire()

        # Cheat codes
        if 'M' in self.pressed_keys: # Cheat bullets
            self.max_bullets = 200
            self.time_bullets = 40
        if 'N' in self.pressed_keys: # Reset cheat bullets
            self.max_bullets = self.default_max_bullets
            self.time_bullets = self.default_time_bullets
        if 'L' in self.pressed_keys: # Cheat life
            self.add_life()
            self.pressed_keys.discard('L')
        if 'P' in self.pressed_keys: # Cheat skill point
            self.skill = True
            self.pressed_keys.discard('P')

        for bullet in self.bullets[:]: # Move all the bullets and check if they are out of the screen to delete them
            bullet.move()
            if bullet.get_coords()[1] < 0:  
                bullet.delete()
