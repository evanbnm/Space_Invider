import tkinter as tk

class Life:
    def __init__(self, root):
        self.root = root
        self.lives = 3
        self.label = tk.Label(root, text="Lives: " + str(self.lives), bg="black", fg="lime")
        self.label.config(font=("Arial", 25))
        self.label.pack(side="top")

    def update(self):
        self.label.config(text="Lives: " + str(self.lives))

    def lose_life(self):
        self.lives -= 1
        self.update()

    def reset(self):
        self.lives = 3
        self.update()