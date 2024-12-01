import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys

from LabelButton import LabelButton

class MenuJeu(tk.Tk):
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
        
        self.start = LabelButton(self, "START", self.exe)
        self.start.place(relx=0.5, rely=0.5, anchor="center")

        self.rules = LabelButton(self, "RULES", self.show_rules)
        self.rules.place(relx=0.5, rely=0.6, anchor="center")

        self.leaderboard = LabelButton(self, "LEADERBOARD", self.show_leaderboard)
        self.leaderboard.place(relx=0.5, rely=0.7, anchor="center")

        self.quit = LabelButton(self, "QUIT", self.destroy)
        self.quit.place(relx=0.5, rely=0.8, anchor="center")

        self.title_image = Image.open("images/title.png")
        self.title_image = self.title_image.resize((600, 250) , Image.LANCZOS)
        self.title_photo = ImageTk.PhotoImage(self.title_image)
        self.canvas.create_image(self.winfo_screenwidth() // 2, 250, image=self.title_photo)

    def show_leaderboard(self):
        leaderboard = tk.Toplevel(self)
        leaderboard.title("Leaderboard")
        leaderboard.geometry("400x400")
        leaderboard.configure(bg="black")
        leaderboard_text = tk.Label(leaderboard, text="Leaderboard\n\n"
                                         "1. 1000\n"
                                         "2. 900\n"
                                         "3. 800\n"
                                         "4. 700\n"
                                         "5. 600\n"
                                         "6. 500\n"
                                         "7. 400\n"
                                         "8. 300\n"
                                         "9. 200\n"
                                         "10. 100", font=("Arial", 14), bg="black", fg="lime")
        leaderboard_text.pack(expand=True, fill="both")
        
        close = LabelButton(leaderboard, "Close", leaderboard.destroy)
        close.place(relx=0.5, rely=0.9, anchor="center")

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
        try:
            self.destroy()  # Fermer la fenêtre actuelle
            # Utiliser l'interpréteur Python actuel
            subprocess.Popen([sys.executable, "main.py"])
            
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution : {e}")
        except FileNotFoundError:
            print("Le fichier 'autre_script.py' est introuvable.")

# Exécution du programme
if __name__ == "__main__":
    menu = MenuJeu()
    menu.mainloop()
