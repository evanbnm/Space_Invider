import tkinter as tk
from PIL import Image, ImageTk

class Bullet:
    def __init__(self, canvas, x, y, direction):
        self.canvas = canvas
        self.speed = 7
        self.direction = direction
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
        self.canvas.delete(self.bullet)
