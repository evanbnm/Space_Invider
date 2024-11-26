import tkinter as tk

class Score:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.label = tk.Label(root, text="Score: " + str(self.score), bg="black", fg="lime")
        self.label.config(font=("Arial", 30))
        self.label.pack(side="bottom")

    def update(self):
        self.label.config(text="Score: " + str(self.score))

    def add(self, points):
        self.score += points
        self.update()

    def reset(self):
        self.score = 0
        self.update()