import tkinter as tk
from tkinter import messagebox


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

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Menu", menu=self.file_menu)
        self.file_menu.add_command(label="New Game", command=self.start_game)
        self.file_menu.add_command(label="Quit", command=self.quit_game)
        self.file_menu.add_command(label="About", command=self.show_about)
        
        self.running = True

        self.buttonQuit = Button(self.frame, "Quit", self.quit_game, 'right')
        self.buttonStart = Button(self.frame, "Start", self.start_game, 'left')

        self.score = Score(self.frame)  

        self.life = Life(self.frame)

        

    def show_about(self):
        messagebox.showinfo("About", "Space Invaders Game\nCreated by Evan and Mathis")

    def quit_game(self):
        self.running = False
        self.root.destroy()

    def start_game(self):
        self.canvas.delete("all")
        self.alien = Alien(self.canvas, 0, 0)
        self.ship = Ship(self.canvas)
        self.life.reset()
        self.score.reset()
        self.main_loop()

    def main_loop(self):
        while self.running:
            self.alien.update()
            self.root.update()
            # self.ship.update()
        

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

class Alien:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.alien = self.canvas.create_rectangle(x, y, x + 50, y + 30, fill="green")
        self.speed = 2
        self.move()
    
    def move(self):
        self.canvas.move(self.alien, self.speed, 0)
        x1, y1, x2, y2 = self.canvas.coords(self.alien)
        if x2 > self.canvas.winfo_width() or x1 < 0:
            self.speed *= -1

    def update(self):
        self.move()

class Ship:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ship = self.canvas.create_rectangle(0, 0, 50, 30, fill="blue")
        self.speed = 0.3
        self.canvas.move(self.ship, 275, 400)
        self.canvas.bind_all("<Left>", self.start_move_left)
        self.canvas.bind_all("<Right>", self.start_move_right)
        self.canvas.bind_all("<KeyRelease-Left>", self.stop_move)
        self.canvas.bind_all("<KeyRelease-Right>", self.stop_move)
        self.moving_left = False
        self.moving_right = False
        self.update()

    def start_move_left(self, event):
        self.moving_left = True

    def start_move_right(self, event):
        self.moving_right = True

    def stop_move(self, event):
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left:
            self.canvas.move(self.ship, -self.speed, 0)
        if self.moving_right:
            self.canvas.move(self.ship, self.speed, 0)
        self.canvas.after(1, self.update)



if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.title("Space Invaders")
    root.attributes("-fullscreen", True)
    root.mainloop()
