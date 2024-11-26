import tkinter as tk

class Button:
    def __init__(self, root, text, command, pos):
        self.root = root
        self.text = text
        self.command = command
        self.pos = pos
        self.button = tk.Button(root, text=self.text, command=self.command, relief='flat')
        self.button.pack(side=self.pos)
        self.button.config(highlightbackground='black')
        self.button.config(width=10, height=2)