import tkinter as tk
from PIL import Image, ImageTk

class BonusAlien:
    def __init__(self, canvas, x, y, direction):
        self.canvas = canvas

        original = Image.open("images/bonus.png")
        resized = original.resize((50, 30))
        self.image = ImageTk.PhotoImage(resized)
        self.alien = self.canvas.create_image(x, y, image=self.image)

        self.score = 150
        self.direction = direction
        self.speed = 3 * self.direction


    
    def move(self, speed):
        self.canvas.move(self.alien, self.speed, 0)

    def delete(self):
        self.canvas.delete(self.alien)

    def get_coords(self):
        x, y = self.canvas.coords(self.alien)
        x1 = x - 25
        y1 = y - 15
        x2 = x1 + 50
        y2 = y1 + 30
        return x1, y1, x2, y2

    
    def update(self):
        
        self.move(self.speed)
            
        
