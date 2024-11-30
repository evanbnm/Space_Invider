import tkinter as tk

class LabelButton:
    def __init__(self, master, text, command):
        self.master = master
        self.text = text
        self.command = command
        self.label = tk.Label(self.master, text=self.text, font=("Arial", 24), bg="black", fg="lime", width=20, height=2, relief="raised", borderwidth=0)
       
        self.label.bind("<Enter>", lambda e: self.label.config(bg="lime", fg="black"))
        self.label.bind("<Leave>", lambda e: self.label.config(bg="black", fg="lime"))
        self.label.bind("<Button-1>", self.action)

    def action(self, event):
        self.label.config(bg="#00CC00", fg="#000000")
        self.master.after(150, lambda: self.label.config(bg="lime", fg="black"))
        self.master.after(300, self.command)

    def place(self, **kwargs):
        self.label.place(**kwargs)

    def config(self, **kwargs):
        self.label.config(**kwargs)
    
    def destroy(self):
        self.label.destroy()

    