import tkinter as tk


class Game:
    def __init__(self, root):
        self.root = root

        self.canvas = tk.Canvas(root, bg="black")
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight() 
        self.canvas.config(width=self.screen_width * 0.5 , height=self.screen_height * 0.85)
        self.canvas.config(highlightthickness=0)
        self.canvas.pack()

        self.frame = tk.Frame(root)
        self.frame.config(width=self.screen_width * 0.5 , height=self.screen_height * 0.15)
        self.frame.config(bg="black")
        self.frame.pack_propagate(False)
        self.frame.pack(side="bottom")

        self.menubar=tk.Menu(self.root)
        self.root.config(menu=self.menubar)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="New Game", command=self.start_game)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Quit", command=self.quit_game)


        self.running = True

        self.buttonQuit = Button(self.frame, "Quit", self.quit_game, 'right')
        self.buttonStart = Button(self.frame, "Start", self.start_game, 'left')

        self.score = Score(self.frame)  

        self.life = Life(self.frame)

    def quit_game(self):
        self.running = False
        self.root.destroy()

    def start_game(self):
        self.main_loop()

    def main_loop(self):
        pass

    def update(self):
        pass

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

class Score:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.label = tk.Label(root, text="Score: " + str(self.score), bg="black", fg="green")
        self.label.config(font=("Arial", 30))
        self.label.pack(side="bottom")

    def update(self):
        self.label.config(text="Score: " + str(self.score))

    def add(self, points):
        self.score += points
        self.update()

    def reset(self):
        self.score = 0
        self.update()

class Life:
    def __init__(self, root):
        self.root = root
        self.lives = 3
        self.label = tk.Label(root, text="Lives: " + str(self.lives), bg="black", fg="green")
        self.label.config(font=("Arial", 30))
        self.label.pack(side="top")

    def update(self):
        self.label.config(text="Lives: " + str(self.lives))

    def lose_life(self):
        self.lives -= 1
        self.update()

    def reset(self):
        self.lives = 3
        self.update()



if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.title("Space Invaders")
    root.attributes("-fullscreen", True)
    root.mainloop()
