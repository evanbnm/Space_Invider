import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys

from LabelButton import LabelButton
from Keybinds import Keybinds
from Leaderboard import Leaderboard

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

    def show_keybinds(self):
        keybinds_manager = Keybinds(self)
        keybinds_manager.show_keybinds()

    def show_leaderboard(self):
        leaderboard = Leaderboard(None, None, self)
        leaderboard.show_leaderboard()


    def show_rules(self):
        rules = tk.Toplevel(self)
        rules.title("Rules")
        rules.attributes("-fullscreen", True)
        rules.configure(bg="black")
        rules_text = tk.Label(rules, text="Space Invaders\n\n"
                                         "Objective:\n"
                                         "Destroy all the aliens before they reach the bottom\n"
                                         "of the screen\n\n"
                                        "Skills:\n"
                                        "When you destroy an bonus alien you get a skill point\n"
                                        "You also get a skill point when you beat a level\n"
                                        "You can use your skill points to buy upgrades\n"
                                        "at the end of each level\n\n"
                                         "Good luck!", font=("Arial", 30), bg="black", fg="lime")
        rules_text.pack(expand=True, fill="both")
        
        close = LabelButton(rules, "Close", rules.destroy)
        close.place(relx=0.5, rely=0.9, anchor="center")


    def exe(self):
        subprocess.Popen([sys.executable, "main_game.py"])        # Utiliser l'interpréteur Python actuel
        self.destroy()
 