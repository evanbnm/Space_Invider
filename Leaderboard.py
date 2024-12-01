import tkinter as tk
from Score import Score

class Leaderboard:
    def __init__(self, canvas, frame):
        self.canvas = canvas
        self.frame = frame

    def enter_pseudo(self, score):
        self.pseudo = tk.Entry(self.canvas, bg="black", fg="lime", font=("Arial", 24))
        self.pseudo.place(relx=0.5, rely=0.71, anchor="center")
        self.pseudo.bind("<Return>", lambda event: self.add_score(event, score))

    def add_score(self, event, score):
        pseudo = self.pseudo.get()
        with open("data/leaderboard.txt", "a") as file:
            file.write(f"{pseudo} {score}\n")
        self.pseudo.delete(0, tk.END)
        self.pseudo.destroy()



