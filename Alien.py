from PIL import Image, ImageTk
import tkinter as tk

from Bullet import Bullet

class Alien:
    def __init__(self, canvas, x, y, alien_group):
        self.canvas = canvas
        self.height = canvas.winfo_height()
        self.alien_group = alien_group
        original = Image.open("images/alien.png")
        resized = original.resize((40, 30))
        self.image = ImageTk.PhotoImage(resized)
        self.alien = self.canvas.create_image(x, y, image=self.image)
        self.bullets = [] 

    def move(self, speed):
        self.canvas.move(self.alien, speed, 0)

    def get_coords(self):
        x, y = self.canvas.coords(self.alien)
        x1 = x - 20
        y1 = y - 15
        x2 = x1 + 40
        y2 = y1 + 30
        return x1, y1, x2, y2
    
    def fire(self):
        x1, y1, x2, y2 = self.get_coords()
        bullet = Bullet(self.canvas, (x1 + x2) / 2, y2 + 5, 1, self, True)
        self.alien_group.bullets.append(bullet)

    def delete(self):
        self.canvas.delete(self.alien)
        
    def update(self):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.get_coords()[1] > self.height:  # Si la balle sort de l'écran
                bullet.delete()
                self.bullets.remove(bullet)