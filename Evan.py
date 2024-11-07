import tkinter as tk


class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, bg="black")
        self.screen_width = root.winfo_screenwidth() * 0.5
        self.screen_height = root.winfo_screenheight()
        self.canvas.config(width=self.screen_width, height=self.screen_height)
        self.canvas.pack()
        self.running = True
        self.main_loop()

    def main_loop(self):
        pass

    def update(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.title("Space Invaders")
    root.attributes("-fullscreen", True)
    root.mainloop()
