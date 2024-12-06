import tkinter as tk

from LabelButton import LabelButton

class Keybinds:
    def __init__(self, parent):
        self.parent = parent
        self.default_keybinds = {}
        self.default = {"Move left": "LEFT ARROW", "Move right": "RIGHT ARROW", "Shoot": "SPACE BAR"}
        self.load_keybinds()

    def show_keybinds(self):
        keybinds = tk.Toplevel(self.parent)
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
            self.load_keybinds()
            keybinds.destroy()
            

        left_bind = LabelButton(keybinds, f"Move left : {self.default_keybinds['Move left']}", lambda: self.edit_keybind("Move left", left_bind))
        left_bind.config(width=25)
        left_bind.place(relx=0.5, rely=0.3, anchor="center") 

        right_bind = LabelButton(keybinds, f"Move right : {self.default_keybinds['Move right']}", lambda: self.edit_keybind("Move right", right_bind))
        right_bind.config(width=25)
        right_bind.place(relx=0.5, rely=0.4, anchor="center")

        shoot_bind = LabelButton(keybinds, f"Shoot : {self.default_keybinds['Shoot']}", lambda: self.edit_keybind("Shoot", shoot_bind))
        shoot_bind.config(width=25)
        shoot_bind.place(relx=0.5, rely=0.5, anchor="center")

        reset_bind = LabelButton(keybinds, "Reset", reset_keybinds)
        reset_bind.config(width=25)
        reset_bind.place(relx=0.5, rely=0.6, anchor="center")

        apply = LabelButton(keybinds, "Apply", apply_keybinds)
        apply.config(width=25)
        apply.place(relx=0.5, rely=0.9, anchor="center")



        
    def edit_keybind(self, action, button):
        keybind_window = button.master  # La fenêtre actuelle contenant le bouton

        def on_key_press(event):
            # Mettre à jour la touche associée à l'action
            ecriture = self.name_binds(event.keysym.upper())
            if ecriture in self.default_keybinds.values() or ecriture == "M" or ecriture == "N" or ecriture == "P" or ecriture == "L":
                error_label = tk.Label(keybind_window, text="Key already in use!", fg="red", bg="black", font=("Arial", 30))
                error_label.place(relx=0.5, rely=0.2, anchor="center")
                keybind_window.after(1000, error_label.destroy)
                return
                
            self.default_keybinds[action] = event.keysym
            button.update_label(f"{action} : {ecriture}")
            keybind_window.unbind("<KeyPress>")  # Débind après la saisie
    
        # Lier uniquement à la fenêtre des keybinds
        keybind_window.bind("<KeyPress>", on_key_press)
        keybind_window.focus_set()  # Donner le focus à cette fenêtre
        self.save_keybinds()
        self.load_keybinds()


    def save_keybinds(self):
            with open("data/keybinds.txt", "w") as file:
                for action, key in self.default_keybinds.items():
                    key = self.name_binds_inverse(key)
                    file.write(f"{action} : {key}\n")

    def load_keybinds(self):
        with open("data/keybinds.txt", "r") as file:
            for line in file:
                action, key = line.strip().split(" : ")
                key = self.name_binds(key)
                self.default_keybinds[action] = key
        self.save_keybinds()


    def name_binds(self, name):
        if name == "SPACE":
            return "SPACE BAR"
        if name == "LEFT":
            return "LEFT ARROW"
        if name == "RIGHT":
            return "RIGHT ARROW"
        return name.upper()
    
    def name_binds_inverse(self, name):
        if name == "SPACE BAR":
            return "SPACE"
        if name == "LEFT ARROW":
            return "LEFT"
        if name == "RIGHT ARROW":
            return "RIGHT"
        return name.upper()

