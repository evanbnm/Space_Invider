import tkinter as tk


class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, bg="black")
        self.screen_width = root.winfo_screenwidth() * 0.5
        self.screen_height = root.winfo_screenheight() * 0.85
        self.canvas.config(width=self.screen_width, height=self.screen_height)
        self.canvas.pack(side="top")

        

        self.running = True
        self.main_loop()

        self.button = Button(self.canvas, "Quit", self.quit_game, 0, 0, 100, 50)

    def quit_game(self):
        self.button.destroy()

    def main_loop(self):
        pass

    def update(self):
        pass


class Button:
    def __init__(self, root, text, command, x, y, width, height):
        self.root = root
        self.text = text
        self.command = command
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button = tk.Button(root, text=self.text, command=self.command)
        self.button.place(x=self.x, y=self.y, width=self.width, height=self.height)

    def destroy(self):
        self.button.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.title("Space Invaders")
    root.attributes("-fullscreen", True)
    root.mainloop()
