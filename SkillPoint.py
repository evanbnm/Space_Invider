import tkinter as tk

class SkillPoint:
    def __init__(self,root, canvas):
        self.root = root
        self.canvas = canvas
        self.screen_width = self.canvas.winfo_screenwidth()
        self.screen_height = self.canvas.winfo_screenheight()
        self.points = 0
        self.label = tk.Label(root, text="Skill Points : " + str(self.points), bg="black", fg="lime")
        self.label.config(font=("Arial", 25))
        self.label.pack(side="top")
        
        self.max_bullets = 2
        self.time_bullets = 1050

        self.level_bullets = 1
        self.level_rate = 1

    def add_point(self):
        self.points += 1
        self.update()

    def upgrade_rate(self):
        if self.level_rate == "max":
            self.canvas.delete("all")
            self.error = self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="MAX LEVEL REACHED", fill="red", font=("Arial", 50))
            self.canvas.after(1500, lambda: self.canvas.delete("all"))
            return
        if self.points > 0:
            self.time_bullets -= 100
            self.points -= 1
            self.level_rate += 1
            if self.level_rate == 10:
                self.level_rate = "max"
            self.update()
        else:
            self.canvas.delete("all")
            self.error = self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="NOT ENOUGH POINTS", fill="red", font=("Arial", 50))
            self.canvas.after(1500, lambda: self.canvas.delete("all"))

    def upgrade_bullets(self):
        if self.level_bullets == "max":
            self.canvas.delete("all")
            self.error = self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="MAX LEVEL REACHED", fill="red", font=("Arial", 50))
            self.canvas.after(1500, lambda: self.canvas.delete("all"))
            return
        if self.points > 0:
            self.max_bullets += 1
            self.points -= 1
            self.level_bullets += 1
            if self.level_bullets == 10:
                self.level_bullets = "max"
            self.update()
        else:
            self.canvas.delete("all")
            self.error = self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="NOT ENOUGH POINTS", fill="red", font=("Arial", 50))
            self.canvas.after(1500, lambda: self.canvas.delete(self.error))

        
    def reset(self):
        self.level_bullets = 1
        self.level_rate = 1
        self.points = 0
        self.max_bullets = 2
        self.time_bullets = 1050
        self.update()

    def update(self):
        self.label.config(text="Skill Points : " + str(self.points))
    
