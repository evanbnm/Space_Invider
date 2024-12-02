import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys

from LabelButton import LabelButton

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre
        self.title("Menu du jeu")
        self.after(100, lambda: self.attributes("-fullscreen", True))
        self.configure(bg="black") 
        
        # Charger l'image de fond
        self.bg_image = Image.open("images/bg.jpg")
        self.bg_image = self.bg_image.resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Créer le canvas
        self.canvas = tk.Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        self.canvas.config(highlightthickness=0)
        
        self.start = LabelButton(self, "START", self.exe)
        self.start.place(relx=0.5, rely=0.5, anchor="center")

        self.rules = LabelButton(self, "RULES", self.show_rules)
        self.rules.place(relx=0.5, rely=0.6, anchor="center")

        self.leaderboard = LabelButton(self, "LEADERBOARD", self.show_leaderboard)
        self.leaderboard.place(relx=0.5, rely=0.7, anchor="center")

        self.keybinds = LabelButton(self, "KEYBINDS", self.show_keybinds)
        self.keybinds.place(relx=0.5, rely=0.8, anchor="center")

        self.quit = LabelButton(self, "QUIT", self.destroy)
        self.quit.place(relx=0.5, rely=0.9, anchor="center")

       

        self.title_image = Image.open("images/title.png")
        self.title_image = self.title_image.resize((600, 250) , Image.LANCZOS)
        self.title_photo = ImageTk.PhotoImage(self.title_image)
        self.canvas.create_image(self.winfo_screenwidth() // 2, 250, image=self.title_photo)

        self.default_keybinds = {}
        self.default = {"Move left": "Left", "Move right": "Right", "Shoot": "space"}
        self.load_keybinds()



    def show_keybinds(self):
        keybinds = tk.Toplevel(self)
        keybinds.title("Keybinds")
        keybinds.geometry("400x400")
        keybinds.configure(bg="black")

        keybinds.focus_set()

        def reset_keybinds():
            self.default_keybinds = self.default.copy()
            self.save_keybinds()
            keybinds.destroy()
            self.show_keybinds()

        def apply_keybinds():
            self.save_keybinds()
            keybinds.destroy()
            

        left_bind = LabelButton(keybinds, f"Move left : {self.default_keybinds['Move left']}", lambda: self.edit_keybind("Move left", left_bind))
        left_bind.place(relx=0.5, rely=0.3, anchor="center") 

        right_bind = LabelButton(keybinds, f"Move right : {self.default_keybinds['Move right']}", lambda: self.edit_keybind("Move right", right_bind))
        right_bind.place(relx=0.5, rely=0.4, anchor="center")

        shoot_bind = LabelButton(keybinds, f"Shoot : {self.default_keybinds['Shoot']}", lambda: self.edit_keybind("Shoot", shoot_bind))
        shoot_bind.place(relx=0.5, rely=0.5, anchor="center")

        reset_bind = LabelButton(keybinds, "Reset", reset_keybinds)
        reset_bind.place(relx=0.5, rely=0.6, anchor="center")

        apply = LabelButton(keybinds, "Apply", apply_keybinds)
        apply.place(relx=0.5, rely=0.9, anchor="center")

        
    def edit_keybind(self, action, button):
        keybind_window = button.master  # La fenêtre actuelle contenant le bouton

        def on_key_press(event):
            # Mettre à jour la touche associée à l'action
            self.default_keybinds[action] = event.keysym
            button.update_label(f"{action} : {event.keysym}")
            keybind_window.unbind("<KeyPress>")  # Débind après la saisie
    
        # Lier uniquement à la fenêtre des keybinds
        keybind_window.bind("<KeyPress>", on_key_press)
        keybind_window.focus_set()  # Donner le focus à cette fenêtre

    def save_keybinds(self):
            with open("data/keybinds.txt", "w") as file:
                for action, key in self.default_keybinds.items():
                    file.write(f"{action} : {key}\n")

    def load_keybinds(self):
        with open("data/keybinds.txt", "r") as file:
            for line in file:
                action, key = line.strip().split(" : ")
                self.default_keybinds[action] = key
        self.save_keybinds()


    def show_leaderboard(self):
        leaderboard = tk.Toplevel(self)
        leaderboard.config(highlightthickness=0)
        leaderboard.config(borderwidth=0)
        leaderboard.title("Leaderboard")
        leaderboard.geometry("400x400")
        leaderboard.configure(bg="black")
        leaderboard_text = tk.Text(leaderboard, bg="black", fg="lime", font=("Arial", 30))
        leaderboard_text.pack(expand=True, fill="both")
        leaderboard_text.tag_configure("center", justify="center")


        scores = []
        unique_entries = set()
        with open("data/leaderboard.txt", "r") as file:
            for line in file:
                parts = line.strip().split()
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

    def show_rules(self):
        rules = tk.Toplevel(self)
        rules.title("Rules")
        rules.geometry("400x400")
        rules.configure(bg="black")
        rules_text = tk.Label(rules, text="Space Invaders\n\n"
                                         "Controls:\n"
                                         "Use the arrow keys to move the ship\n"
                                         "Press the space bar to shoot\n\n"
                                         "Objective:\n"
                                         "Destroy all the aliens before they reach the bottom\n"
                                         "of the screen\n\n"
                                         "Good luck!", font=("Arial", 14), bg="black", fg="lime")
        rules_text.pack(expand=True, fill="both")
        
        close = LabelButton(rules, "Close", rules.destroy)
        close.place(relx=0.5, rely=0.9, anchor="center")


    def exe(self):
        self.destroy()  # Fermer la fenêtre actuelle
        # Utiliser l'interpréteur Python actuel
        subprocess.Popen([sys.executable, "main.py"])

# Exécution du programme
if __name__ == "__main__":
    menu = Menu()
    menu.mainloop()
