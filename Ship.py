import tkinter as tk
from PIL import Image, ImageTk

from Bullet import Bullet

class Ship:
    def __init__(self, canvas, max_bullets, time_bullets):
        self.canvas = canvas
        original = Image.open("images/ship.png")
        resized = original.resize((40, 50))
        self.image = ImageTk.PhotoImage(resized)
        self.ship = self.canvas.create_image(0, 0, image=self.image)

        self.speed = 4
        self.canvas.move(self.ship, 370, 770)  # Position initiale
        self.pressed_keys = set()
        self.bullets = []  # Liste pour les balles

        self.default_max_bullets = max_bullets
        self.default_time_bullets = time_bullets

        self.max_bullets = max_bullets
        self.time_bullets = time_bullets

        # Écoute des touches
        self.canvas.bind_all("<KeyPress>", self.on_key_press)
        self.canvas.bind_all("<KeyRelease>", self.on_key_release)

    def on_key_press(self, event):
        self.pressed_keys.add(event.keysym)

    def on_key_release(self, event):
        self.pressed_keys.discard(event.keysym)

    def get_coords(self):
        x, y = self.canvas.coords(self.ship)
        x1 = x - 20
        y1 = y - 25
        x2 = x1 + 40
        y2 = y1 + 50
        return x1, y1, x2, y2

    def fire(self):
        # Crée une nouvelle balle à la position actuelle du vaisseau
        x1, y1, x2, y2 = self.get_coords()

        if len(self.bullets) < self.max_bullets and not hasattr(self, 'last_fire_time'):
            bullet = Bullet(self.canvas, (x1 + x2) / 2, y1 - 5, -1)  # Position centrale du vaisseau
            self.bullets.append(bullet)
            self.last_fire_time = self.canvas.after(self.time_bullets, self.reset_fire_cooldown)  # Cooldown de 500ms

    def reset_fire_cooldown(self):
        del self.last_fire_time
            

    def delete(self):
        self.canvas.delete(self.ship)
        for bullet in self.bullets:
            bullet.delete()

    def update(self):
        # Récupère les coordonnées actuelles du vaisseau
        x1, y1, x2, y2 = self.get_coords()

        # Empêche le vaisseau de sortir des limites
        if 'Left' in self.pressed_keys and x1 > 0:
            self.canvas.move(self.ship, -self.speed, 0)
        if 'Right' in self.pressed_keys and x2 < self.canvas.winfo_width():
            self.canvas.move(self.ship, self.speed, 0)
        if 'space' in self.pressed_keys:
            self.fire()
        if 'm' in self.pressed_keys:
            self.max_bullets = 200
            self.time_bullets = 5
        if 'n' in self.pressed_keys:
            self.max_bullets = self.default_max_bullets
            self.time_bullets = self.default_time_bullets

        # Met à jour toutes les balles
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.get_coords()[1] < 0:  # Si la balle sort de l'écran
                bullet.delete()
                self.bullets.remove(bullet)
