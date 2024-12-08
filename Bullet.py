import tkinter as tk
from PIL import Image, ImageTk
class Bullet:
    def __init__(self, canvas, x, y, direction, alien, isEnnemy=False):
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
        self.canvas.move(self.bullet, 0, self.direction * self.speed)

    def get_coords(self):
        x, y = self.canvas.coords(self.bullet)
        x1 = x - 6
        y1 = y - 15
        x2 = x1 + 12
        y2 = y1 + 30
        return x1, y1, x2, y2

    def delete(self):
        if self in self.alien.bullets:
            self.alien.bullets.remove(self)
        elif self.isEnnemy and self in self.alien.alien_group.bullets:
            self.alien.alien_group.bullets.remove(self)
