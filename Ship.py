import tkinter as tk
from PIL import Image, ImageTk

from Bullet import Bullet

class Ship:
    def __init__(self, canvas):
        self.canvas = canvas
        #self.ship = self.canvas.create_rectangle(0, 0, 50, 30, fill="blue")
        original = Image.open("images/ship.png")
        resized = original.resize((50, 60))
        self.image = ImageTk.PhotoImage(resized)
        self.ship = self.canvas.create_image(0, 0, image=self.image)

        self.speed = 4
        self.canvas.move(self.ship, 275, 770)  # Position initiale
        self.moving_left = False
        self.moving_right = False
        self.bullets = []  # Liste pour les balles

        # Écoute des touches
        self.canvas.bind_all("<Left>", self.start_move_left)
        self.canvas.bind_all("<Right>", self.start_move_right)
        self.canvas.bind_all("<KeyRelease-Left>", self.stop_move)
        self.canvas.bind_all("<KeyRelease-Right>", self.stop_move)
        self.canvas.bind_all("<space>", self.fire)

    def start_move_left(self, event):
        self.moving_left = True

    def start_move_right(self, event):
        self.moving_right = True

    def stop_move(self, event):
        self.moving_left = False
        self.moving_right = False

    def get_coords(self):
        x, y = self.canvas.coords(self.ship)
        x1 = x - 25
        y1 = y - 30
        x2 = x1 + 50
        y2 = y1 + 60
        return x1, y1, x2, y2

    def fire(self, event):
        # Crée une nouvelle balle à la position actuelle du vaisseau
        x1, y1, x2, y2 = self.get_coords()

        if len(self.bullets) < 1:
            bullet = Bullet(self.canvas, (x1 + x2) / 2, y1 - 5, -1)  # Position centrale du vaisseau
            self.bullets.append(bullet)

    def delete(self):
        self.canvas.delete(self.ship)
        for bullet in self.bullets:
            bullet.delete()

    def update(self):
        # Récupère les coordonnées actuelles du vaisseau
        x1, y1, x2, y2 = self.get_coords()

        # Empêche le vaisseau de sortir des limites
        if self.moving_left and x1 > 0:
            self.canvas.move(self.ship, -self.speed, 0)
        if self.moving_right and x2 < self.canvas.winfo_width():
            self.canvas.move(self.ship, self.speed, 0)

        # Met à jour toutes les balles
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.get_coords()[1] < 0:  # Si la balle sort de l'écran
                bullet.delete()
                self.bullets.remove(bullet)