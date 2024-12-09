# -*- coding: utf-8 -*-
"""
Filename: Keybinds.py
Author: Your Name
Date: YYYY-MM-DD
Description:
Keybinds module for managing key bindings in the Space Invader game.
This module allows users to view, edit, reset, and save key bindings for game actions.

TODO:
- Add more key bindings for additional actions.
- Improve error handling for file operations.
"""

import tkinter as tk
from LabelButton import LabelButton

class Keybinds:
    """Class to manage key bindings for the Space Invader game."""

    def __init__(self, parent):
        """
        Initialize the Keybinds class.

        Args:
            parent (tk.Tk): The parent Tkinter window.
        """
        self.parent = parent
        self.default_keybinds = {}
        self.default = {"Move left": "LEFT ARROW", "Move right": "RIGHT ARROW", "Shoot": "SPACE BAR"}
        self.load_keybinds()

    def show_keybinds(self):
        """Display the key bindings window."""
        keybinds = tk.Toplevel(self.parent)
        keybinds.title("Keybinds")
        keybinds.attributes("-fullscreen", True)
        keybinds.configure(bg="black")

        keybinds.focus_set()

        def reset_keybinds():
            """Reset key bindings to default values."""
            self.default_keybinds = self.default.copy()
            self.save_keybinds()
            keybinds.destroy()
            self.show_keybinds()

        def apply_keybinds():
            """Apply the current key bindings."""
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
        """
        Edit a specific key binding.

        Args:
            action (str): The action to bind a key to.
            button (LabelButton): The button to update with the new key binding.
        """
        keybind_window = button.master  # The current window containing the button

        def on_key_press(event):
            """
            Handle key press event to update the key binding.

            Args:
                event (tk.Event): The key press event.
            """
            # Update the key associated with the action
            ecriture = self.name_binds(event.keysym.upper())
            if ecriture in self.default_keybinds.values() or ecriture in ["M", "N", "P", "L"]:
                error_label = tk.Label(keybind_window, text="Key already in use!", fg="red", bg="black", font=("Arial", 30))
                error_label.place(relx=0.5, rely=0.2, anchor="center")
                keybind_window.after(1000, error_label.destroy)
                return

            self.default_keybinds[action] = event.keysym
            button.update_label(f"{action} : {ecriture}")
            keybind_window.unbind("<KeyPress>")  # Unbind after input

        # Bind only to the keybinds window
        keybind_window.bind("<KeyPress>", on_key_press)
        keybind_window.focus_set()  # Give focus to this window
        self.save_keybinds()
        self.load_keybinds()

    def save_keybinds(self):
        """Save the current key bindings to a file."""
        with open("data/keybinds.txt", "w") as file:
            for action, key in self.default_keybinds.items():
                key = self.name_binds_inverse(key)
                file.write(f"{action} : {key}\n")

    def load_keybinds(self):
        """Load key bindings from a file."""
        with open("data/keybinds.txt", "r") as file:
            for line in file:
                action, key = line.strip().split(" : ")
                key = self.name_binds(key)
                self.default_keybinds[action] = key
        self.save_keybinds()

    def name_binds(self, name):
        """
        Convert key names to a more readable format.

        Args:
            name (str): The key name to convert.

        Returns:
            str: The converted key name.
        """
        if name == "SPACE":
            return "SPACE BAR"
        if name == "LEFT":
            return "LEFT ARROW"
        if name == "RIGHT":
            return "RIGHT ARROW"
        return name.upper()
    
    def name_binds_inverse(self, name):
        """
        Convert readable key names back to their original format.

        Args:
            name (str): The readable key name to convert.

        Returns:
            str: The original key name.
        """
        if name == "SPACE BAR":
            return "SPACE"
        if name == "LEFT ARROW":
            return "LEFT"
        if name == "RIGHT ARROW":
            return "RIGHT"
        return name.upper()

