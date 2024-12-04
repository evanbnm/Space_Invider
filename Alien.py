from PIL import Image, ImageTk
import tkinter as tk

from Bullet import Bullet

class Alien:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.is_visible = True
        original = Image.open("images/alien.png")
        resized = original.resize((40, 30))
        self.image = ImageTk.PhotoImage(resized)
        self.alien = self.canvas.create_image(x, y, image=self.image)
        self.bullets = []
    def move(self, speed):
        self.canvas.move(self.alien, speed, 0)

    def destroy(self):
        self.canvas.delete(self.alien)

    def get_coords(self):
        x, y = self.canvas.coords(self.alien)
        x1 = x - 20
        y1 = y - 15
        x2 = x1 + 40
        y2 = y1 + 30
        return x1, y1, x2, y2
    
    def fire(self):
        x1, y1, x2, y2 = self.get_coords()
        bullet = Bullet(self.canvas, (x1 + x2) / 2, y2 + 5, 1)
        self.bullets.append(bullet)

    def delete(self):
        self.canvas.delete(self.alien)
        # for bullet in self.bullets:
        #     bullet.delete()
    
    def schedule_delete(self):
        # Supprime complètement l'alien après un délai
        self.canvas.after(5000, self.delete)

    def hide(self):
        """Masque l'alien visuellement."""
        self.canvas.itemconfigure(self.alien, state="hidden")
        self.is_visible = False
        

    def update(self):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.get_coords()[1] > 900:  # Si la balle sort de l'écran
                bullet.delete()
                self.bullets.remove(bullet)