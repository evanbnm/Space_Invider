
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, bg="black")
screen_width = root.winfo_screenwidth() * 0.5
screen_height = root.winfo_screenheight()
canvas.config(width=screen_width, height=screen_height)
canvas.pack()

root.title("Space Invaders")
root.attributes("-fullscreen", True)
root.mainloop()