# -*- coding: utf-8 -*-
"""
Filename: LabelButton.py
Author: Evan et Mathis
Date: 2024-12-01
Description: This module defines the LabelButton class which creates a custom label button using tkinter.

TODO: 
- Add more customization options for the LabelButton class.
"""

import tkinter as tk

class LabelButton:
    def __init__(self, master, text, command):
        """
        Initialize the LabelButton with the given master, text, and command.
        
        Args:
            master (tk.Widget): The parent widget.
            text (str): The text to display on the label.
            command (callable): The function to call when the label is clicked.
        """
        self.master = master
        self.text = text
        self.command = command
        self.label = tk.Label(self.master, text=self.text, font=("Arial", 24), bg="black", fg="lime", width=20, height=2, relief="raised", borderwidth=0)
       
        self.label.bind("<Enter>", lambda e: self.label.config(bg="lime", fg="black"))
        self.label.bind("<Leave>", lambda e: self.label.config(bg="black", fg="lime"))
        self.label.bind("<Button-1>", self.action)

    def action(self, event):
        """
        Handle the click event on the label.
        
        Args:
            event (tk.Event): The event object.
        """
        self.label.config(bg="#00CC00", fg="#000000")
        self.master.after(150, lambda: self.label.config(bg="lime", fg="black"))
        self.master.after(300, self.command)

    def place(self, **kwargs):
        """
        Place the label widget in the parent widget using the given options.
        
        Args:
            **kwargs: The options to pass to the place method.
        """
        self.label.place(**kwargs)

    def config(self, **kwargs):
        """
        Configure the label widget with the given options.
        
        Args:
            **kwargs: The options to pass to the config method.
        """
        self.label.config(**kwargs)
    
    def destroy(self):
        """
        Destroy the label widget.
        """
        self.label.destroy()
    
    def update_label(self, new_text):
        """
        Update the text displayed on the label.
        
        Args:
            new_text (str): The new text to display on the label.
        """
        self.label.config(text=new_text)

