import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys

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
        
        # Ajouter un label agissant comme un bouton
        self.start = tk.Label(self, text="PLAY NEW GAME", font=("Arial", 24), bg="black", fg="lime", width=20, height=2, relief="raised", borderwidth=0)
        self.start.place(relx=0.5, rely=0.5, anchor="center")

        #Utiliser les options de style de tkinter pour changer l'apparence au survol
        self.start.bind("<Enter>", lambda e: self.start.config(bg="lime", fg="black"))
        self.start.bind("<Leave>", lambda e: self.start.config(bg="black", fg="lime"))
        self.start.bind("<Button-1>", self.start_game)  # Simule un clic sur le bouton

        # Ajouter un label agissant comme un bouton
        self.quit = tk.Label(self, text="QUIT", font=("Arial", 24), bg="black", fg="lime", width=20, height=2, relief="raised", borderwidth=0)
        self.quit.place(relx=0.5, rely=0.6, anchor="center")

        #Utiliser les options de style de tkinter pour changer l'apparence au survol
        self.quit.bind("<Enter>", lambda e: self.quit.config(bg="lime", fg="black"))
        self.quit.bind("<Leave>", lambda e: self.quit.config(bg="black", fg="lime"))
        self.quit.bind("<Button-1>", self.quit_game)

        
        
    def start_game(self, event):
        self.start.config(bg="#00CC00", fg="#000000")
        self.after(150, lambda: self.start.config(bg="lime", fg="black"))
        self.after(300, self.exe)

    def quit_game(self, event):
        self.quit.config(bg="#00CC00", fg="#000000")
        self.after(150, lambda: self.quit.config(bg="lime", fg="black"))
        self.after(300, self.destroy)

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
