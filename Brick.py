import tkinter as tk
from PIL import Image, ImageTk

class Brick:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        original = Image.open("images/brick.png")
        resized = original.resize((26, 26))
        self.image = ImageTk.PhotoImage(resized)
        self.brick = self.canvas.create_image(x, y, image=self.image)

    def delete(self):
        self.canvas.delete(self.brick)

    def get_coords(self):
        x, y = self.canvas.coords(self.brick)
        x1 = x - 13
        y1 = y - 13
        x2 = x1 + 26
        y2 = y1 + 26
        return x1, y1, x2, y2
    