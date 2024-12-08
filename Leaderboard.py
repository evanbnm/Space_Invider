import tkinter as tk
from LabelButton import LabelButton

class Leaderboard:
    def __init__(self, canvas, frame, parent):
        self.canvas = canvas
        self.frame = frame
        self.parent = parent

    def enter_pseudo(self, score):
        self.pseudo = tk.Entry(self.canvas, bg="black", fg="lime", font=("Arial", 24))
        self.pseudo.place(relx=0.5, rely=0.71, anchor="center")
        self.pseudo.bind("<Return>", lambda event: self.add_score(event, score))
        self.pseudo.focus_set()

    def add_score(self, event, score):
        pseudo = self.pseudo.get()
        with open("data/leaderboard.txt", "a", encoding="utf-8") as file:
            file.write(f"{pseudo} : {score}\n")
        self.pseudo.delete(0, tk.END)
        self.pseudo.destroy()
        

    def destroy(self):
        self.pseudo.destroy()

    def show_leaderboard(self):
        leaderboard = tk.Toplevel(self.parent)
        leaderboard.config(highlightthickness=0)
        leaderboard.config(borderwidth=0)
        leaderboard.title("Leaderboard")
        leaderboard.attributes("-fullscreen", True)
        leaderboard.configure(bg="black")
        leaderboard_text = tk.Text(leaderboard, bg="black", fg="lime", font=("Arial", 30))
        leaderboard_text.pack(expand=True, fill="both")
        leaderboard_text.tag_configure("center", justify="center")


        scores = []
        unique_entries = set()
        with open("data/leaderboard.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(" : ")
                if len(parts) == 2:
                    pseudo, score = parts
                    if pseudo not in unique_entries:
                        scores.append((pseudo, int(score)))
                        unique_entries.add(pseudo)

        # Trier les scores par ordre décroissant
        scores.sort(key=lambda x: x[1], reverse=True)

        # Ajouter de l'espace pour centrer le texte
        leaderboard_text.insert(tk.END, "\n\n\n\n", "center")

        # Afficher les scores        
        for index, (pseudo, score) in enumerate(scores, start=1):
            leaderboard_text.insert(tk.END, f"{index}. {pseudo} : {score}\n", "center")

        leaderboard_text.insert(tk.END, "\n\n\n\n", "center")


        black_band_bottom = tk.Frame(leaderboard, bg="black")

        black_band_bottom.place(relx=0.5, rely=0.93, anchor="center", relwidth=1, relheight=0.15)

        black_band_top = tk.Frame(leaderboard, bg="black")
        black_band_top.place(relx=0.5, rely=0.07, anchor="center", relwidth=1, relheight=0.15)

        black_band_right = tk.Frame(leaderboard, bg="black")
        black_band_right.place(relx=0.93, rely=0.5, anchor="center", relwidth=0.15, relheight=1)

        black_band_left = tk.Frame(leaderboard, bg="black")
        black_band_left.place(relx=0.07, rely=0.5, anchor="center", relwidth=0.15, relheight=1)

        

        close = LabelButton(black_band_bottom, "Close", leaderboard.destroy)
        close.place(relx=0.5, rely=0.5, anchor="center")
    






