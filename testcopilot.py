import tkinter as tk
import random

class SpaceInvaders:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Invaders")
        self.canvas = tk.Canvas(root, width=600, height=400, bg="black")
        self.canvas.pack()
        
        self.ship = self.canvas.create_rectangle(270, 350, 330, 370, fill="white")
        self.aliens = []
        self.bullets = []
        
        self.create_aliens()
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)
        
        self.update_game()
    
    def create_aliens(self):
        for i in range(5):
            for j in range(3):
                alien = self.canvas.create_rectangle(100 + i*80, 50 + j*40, 150 + i*80, 80 + j*40, fill="green")
                self.aliens.append(alien)
    
    def move_left(self, event):
        self.canvas.move(self.ship, -20, 0)
    
    def move_right(self, event):
        self.canvas.move(self.ship, 20, 0)
    
    def shoot(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.ship)
        bullet = self.canvas.create_rectangle(x1 + 25, y1 - 10, x2 - 25, y1, fill="red")
        self.bullets.append(bullet)
    
    def update_game(self):
        for bullet in self.bullets:
            self.canvas.move(bullet, 0, -10)
            if self.canvas.coords(bullet)[1] < 0:
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)
        
        for alien in self.aliens:
            for bullet in self.bullets:
                if self.check_collision(alien, bullet):
                    self.canvas.delete(alien)
                    self.canvas.delete(bullet)
                    self.aliens.remove(alien)
                    self.bullets.remove(bullet)
                    break
        
        self.root.after(50, self.update_game)
    
    def check_collision(self, alien, bullet):
        x1, y1, x2, y2 = self.canvas.coords(alien)
        bx1, by1, bx2, by2 = self.canvas.coords(bullet)
        return x1 < bx2 and x2 > bx1 and y1 < by2 and y2 > by1

if __name__ == "__main__":
    root = tk.Tk()
    game = SpaceInvaders(root)
    root.mainloop()
    class Ship:
        def __init__(self, canvas):
            self.canvas = canvas
            self.id = self.canvas.create_rectangle(270, 350, 330, 370, fill="white")
        
        def move_left(self, event):
            self.canvas.move(self.id, -20, 0)
        
        def move_right(self, event):
            self.canvas.move(self.id, 20, 0)

    class Alien:
        def __init__(self, canvas, x, y):
            self.canvas = canvas
            self.id = self.canvas.create_rectangle(x, y, x + 50, y + 30, fill="green")

    class Bullet:
        def __init__(self, canvas, x, y):
            self.canvas = canvas
            self.id = self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="red")
        
        def move(self):
            self.canvas.move(self.id, 0, -10)
        
        def out_of_bounds(self):
            return self.canvas.coords(self.id)[1] < 0

    # Update the SpaceInvaders class to use the new classes
    class SpaceInvaders:
        def __init__(self, root):
            self.root = root
            self.root.title("Space Invaders")
            self.canvas = tk.Canvas(root, width=600, height=400, bg="black")
            self.canvas.pack()
            
            self.ship = Ship(self.canvas)
            self.aliens = []
            self.bullets = []
            
            self.create_aliens()
            self.root.bind("<Left>", self.ship.move_left)
            self.root.bind("<Right>", self.ship.move_right)
            self.root.bind("<space>", self.shoot)
            
            self.update_game()
        
        def create_aliens(self):
            for i in range(5):
                for j in range(3):
                    alien = Alien(self.canvas, 100 + i*80, 50 + j*40)
                    self.aliens.append(alien)
        
        def shoot(self, event):
            x1, y1, x2, y2 = self.canvas.coords(self.ship.id)
            bullet = Bullet(self.canvas, x1 + 25, y1 - 10)
            self.bullets.append(bullet)
        
        def update_game(self):
            for bullet in self.bullets:
                bullet.move()
                if bullet.out_of_bounds():
                    self.canvas.delete(bullet.id)
                    self.bullets.remove(bullet)
            
            for alien in self.aliens:
                for bullet in self.bullets:
                    if self.check_collision(alien.id, bullet.id):
                        self.canvas.delete(alien.id)
                        self.canvas.delete(bullet.id)
                        self.aliens.remove(alien)
                        self.bullets.remove(bullet)
                        break
            
            self.root.after(50, self.update_game)
        
        def check_collision(self, alien_id, bullet_id):
            x1, y1, x2, y2 = self.canvas.coords(alien_id)
            bx1, by1, bx2, by2 = self.canvas.coords(bullet_id)
            return x1 < bx2 and x2 > bx1 and y1 < by2 and y2 > by1

    if __name__ == "__main__":
        root = tk.Tk()
        game = SpaceInvaders(root)
        root.mainloop()