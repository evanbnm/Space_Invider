import tkinter as tk

win = tk.Tk()
win.title("test")
win.attributes("-fullscreen", True)

BG = tk.Canvas(win, bg="black", height=win.winfo_screenheight(), width=win.winfo_screenwidth())
BG.pack()


win.mainloop()