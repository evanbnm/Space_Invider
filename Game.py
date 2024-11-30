import tkinter as tk
from tkinter import messagebox
import random
import subprocess
import sys
from PIL import Image, ImageTk

from AlienGroup import AlienGroup
from Ship import Ship
from Life import Life
from Score import Score
from Button import Button
from Wall import Wall
from BonusAlien import BonusAlien

class Game:
    def __init__(self, root):
        self.root = root

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()


        self.canvas = tk.Canvas(self.root, bg="black")
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
        self.file_menu.add_command(label="Menu", command=self.quit_game)
        self.file_menu.add_command(label="About", command=self.show_about)
        
        self.running = True
        self.loop_id = None  # Attribut pour stocker l'ID de la boucle
        self.bonus_exist = False
        self.end = False

        self.buttonQuit = Button(self.frame, "Menu", self.exe, 'right')
        self.buttonStart = Button(self.frame, "Restart", self.start_game, 'left')

        self.score = Score(self.frame)  

        self.life = Life(self.frame)

        self.title = self.canvas.create_text(self.screen_width / 4, self.screen_height / 2, text="SPACE INVADERS", fill="lime", font=("Arial", 50))


        self.root.after(2000,self.start_game)

    

    def show_about(self):
        messagebox.showinfo("About", "Space Invaders Game\nCreated by Evan and Mathis")

    def quit_game(self):
        self.running = False
        self.root.destroy()

    def exe(self):
        self.running = False
        try:
            self.root.destroy()  # Fermer la fenêtre actuelle
            # Utiliser l'interpréteur Python actuel
            subprocess.Popen([sys.executable, "menu.py"])
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution : {e}")
        except FileNotFoundError:
            print("Le fichier 'autre_script.py' est introuvable.")

    def start_game(self):
        self.running = False
        self.bonus_exist = False
        self.canvas.delete("all")
        self.ship = Ship(self.canvas)
        self.life.reset()
        self.score.reset()

        self.aliens_group = AlienGroup(self.canvas)
        self.wall_right = Wall(self.canvas, 450, 600)
        self.wall_left = Wall(self.canvas, 100, 600)
        
        self.running = True

        # Annule l'appel précédent de main_loop si il existe
        if self.loop_id:
            if not self.end:
                self.root.after_cancel(self.root.after(1))
            self.root.after_cancel(self.loop_id)
            self.loop_id = None
            self.end = False

        # Relance la boucle principale
        self.main_loop(True)
        

    def main_loop(self, firstLoop = False):
        if self.running:

            self.ship.update()   # Mets à jour le vaisseau
            self.aliens_group.update()  # Mise à jour du groupe d'aliens
            for row in self.aliens_group.aliens:
                for alien in row:
                    alien.update()
            self.check_collisions()
            self.is_game_over(self.aliens_group, self.ship)
            self.is_win(self.aliens_group)
            if self.bonus_exist:
                self.bonus.update()
                self.check_collision_bonus()
            
            self.score.update()
            
            
           
            if(firstLoop):
                self.alien_fire()
                self.bonus_alien()
            # Planifie la prochaine exécution de la boucle
            self.loop_id = self.root.after(16, lambda: self.main_loop())
            
    
    def check_collisions(self):
        
        bullets_to_remove = []
        aliens_to_remove = []
        bricks_to_remove = []
        bonus_to_remove = []

        for bullet in self.ship.bullets:
            for row in self.aliens_group.aliens:
                for alien in row:
                    if self.is_collision(bullet, alien):
                        bullets_to_remove.append(bullet)
                        aliens_to_remove.append(alien)
                        self.score.add(25)
            for brick in self.wall_right.brick:
                if self.is_collision(bullet, brick):
                    bullets_to_remove.append(bullet)
                    bricks_to_remove.append(brick)
                    self.score.add(-100)
            for brick in self.wall_left.brick:
                if self.is_collision(bullet, brick):
                    bullets_to_remove.append(bullet)
                    bricks_to_remove.append(brick)
                    self.score.add(-100)
            if self.bonus_exist:
                if self.is_collision(bullet, self.bonus):
                    bullets_to_remove.append(bullet)
                    self.bonus.delete()
                    self.bonus_exist = False
                    self.score.add(150)

        for row in self.aliens_group.aliens:
            for alien in row:
                for bullet in alien.bullets:
                    if self.is_collision(bullet, self.ship):
                        bullets_to_remove.append(bullet)
                        self.life.lose_life()
                        break
                    for brick in self.wall_right.brick:
                        if self.is_collision(bullet, brick):
                            bullets_to_remove.append(bullet)
                            bricks_to_remove.append(brick)
    
                    for brick in self.wall_left.brick:
                        if self.is_collision(bullet, brick):
                            bullets_to_remove.append(bullet)
                            bricks_to_remove.append(brick)
                        
                for brick in self.wall_right.brick:
                    if self.is_collision(alien, brick):
                        if brick not in bricks_to_remove:
                            bricks_to_remove.append(brick)
                        
                for brick in self.wall_left.brick:
                    if self.is_collision(alien, brick):
                        if brick not in bricks_to_remove:
                            bricks_to_remove.append(brick)

            
        # Supprime les balles et aliens marqués
        for bullet in bullets_to_remove:
            bullet.delete()
            if bullet in self.ship.bullets:
                self.ship.bullets.remove(bullet)
            else:
                for row in self.aliens_group.aliens:
                    for alien in row:
                        if bullet in alien.bullets:
                            alien.bullets.remove(bullet)


        for alien in aliens_to_remove:
            alien.delete()
            for row in self.aliens_group.aliens:
                if alien in row:
                    row.remove(alien)

        for brick in bricks_to_remove:
            brick.delete()
            if brick in self.wall_right.brick:
                self.wall_right.brick.remove(brick)
            else:
                self.wall_left.brick.remove(brick)

        

    def alien_fire(self):
        if self.running:
            col = random.choice(self.aliens_group.aliens)
            time = random.randint(500, 1500)
            col[-1].fire()
            self.root.after(time, lambda: self.alien_fire())

    def bonus_alien(self):
        if self.running:
            self.bonus_exist = True
            direction = random.choice([-1,1])
            if direction == 1:
                self.bonus = BonusAlien(self.canvas, 0, 30, direction)
            else:
                self.bonus = BonusAlien(self.canvas, 700, 30, direction)
            time = random.randint(15000, 20000)
            self.root.after(time, lambda: self.bonus_alien())
    
    def check_collision_bonus(self):
        if self.running:
            x1, y1, x2, y2 = self.bonus.get_coords()
            if x1 >= self.canvas.winfo_width() or x2 <= 0:
                self.bonus.delete()
                self.bonus_exist = False

    def is_collision(self, object1, object2):
        bx1, by1, bx2, by2 = object1.get_coords()
        ax1, ay1, ax2, ay2 = object2.get_coords()
        return (bx1 < ax2 and by1 < ay2 and bx2 > ax1 and by2 > ay1)
    
    def is_game_over(self, aliens_group, ship):
        if self.life.lives == 0:
            self.running = False
            self.end = True
            self.canvas.delete("all")
            self.canvas.create_text(self.screen_width / 4, self.screen_height / 2, text="GAME OVER", fill="red", font=("Arial", 50))
        for row in aliens_group.aliens:
            for alien in row:
                if alien.get_coords()[3] >= ship.get_coords()[1]:
                    self.running = False
                    self.end = True
                    self.canvas.delete("all")
                    self.canvas.create_text(self.screen_width / 4, self.screen_height / 2, text="GAME OVER", fill="red", font=("Arial", 50))
                    

    def is_win(self, aliens_group):
        for row in aliens_group.aliens:
            if len(row):
                return 
        self.running = False
        self.end = True
        self.score.add(300 + 200 * self.life.lives)
        self.canvas.delete("all")
        self.canvas.create_text(self.screen_width / 4, self.screen_height / 2, text="YOU WIN", fill="lime", font=("Arial", 50))

        

        
        
            
        
