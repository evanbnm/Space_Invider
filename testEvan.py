import tkinter as tk
from tkinter import messagebox
import random



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
        self.loop_id = None  # Attribut pour stocker l'ID de la boucle

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
        self.running = False
        self.canvas.delete("all")
        self.ship = Ship(self.canvas)
        self.life.reset()
        self.score.reset()

        self.aliens_group = AlienGroup(self.canvas)
        self.running = True

        # Annule l'appel précédent de main_loop si il existe
        if self.loop_id:
            self.root.after_cancel(self.loop_id)

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
            
           
            if(firstLoop):
                self.alien_fire()
            # Planifie la prochaine exécution de la boucle
            self.loop_id = self.root.after(16, lambda: self.main_loop())
    
    def check_collisions(self):
        
        bullets_to_remove = []
        aliens_to_remove = []

        for bullet in self.ship.bullets:
            for row in self.aliens_group.aliens:
                for alien in row:
                    if self.is_collision(bullet, alien):
                        bullets_to_remove.append(bullet)
                        aliens_to_remove.append(alien)

        for row in self.aliens_group.aliens:
            for alien in row:
                for bullet in alien.bullets:
                    if self.is_collision(bullet, self.ship):
                        bullets_to_remove.append(bullet)
                        self.life.lose_life()
                

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

    def alien_fire(self):
        col = random.randint(0, len(self.aliens_group.aliens) - 1)
        time = random.randint(500, 2000)
        self.aliens_group.aliens[col][-1].fire()
        self.root.after(time, lambda: self.alien_fire())

    def is_collision(self, bullet, alien):
        bx1, by1, bx2, by2 = bullet.get_coords()
        ax1, ay1, ax2, ay2 = alien.get_coords()
        cx1, cy1, cx2, cy2 = self.ship.get_coords()
        return (bx1 < ax2 and bx2 > ax1 and by1 < ay2 and by2 > ay1) or (cx1 < bx2 and cx2 > bx1 and cy1 < by2 and cy2 > by1)
    
    def is_game_over(self, aliens_group, ship):
        if self.life.lives == 0:
            self.canvas.delete("all")
            self.canvas.create_text(self.screen_width / 4, self.screen_height / 2, text="Game Over", fill="red", font=("Arial", 50))
            self.running = False
        for row in aliens_group.aliens:
            for alien in row:
                if alien.get_coords()[3] >= ship.get_coords()[1]:
                    self.canvas.delete("all")
                    self.canvas.create_text(self.screen_width / 4, self.screen_height / 2, text="Game Over", fill="red", font=("Arial", 50))
                    self.running = False




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

class AlienGroup:
    def __init__(self, canvas):
        self.canvas = canvas
        self.aliens = []
        self.speed = 2
        self.direction = 1  # 1 = droite, -1 = gauche
        self.x_offset = 100
        self.y_offset = 50
        self.row = 5
        self.col = 8
        self.create_aliens()

    def create_aliens(self):
        # Crée une grille d'aliens
        for col in range(self.col):  # 3 lignes d'aliens
            l = []
            for row in range(self.row):  # 5 aliens par ligne 
                alien = Alien(self.canvas, self.x_offset + col * 60, self.y_offset + row * 60)
                l.append(alien)
            self.aliens.append(l)

    def move(self):
        # Déplace tous les aliens en même temps
        for row in self.aliens:
            for alien in row:
                alien.move(self.speed * self.direction)

    def check_edges(self):
        # Vérifie si l'un des aliens touche un bord de l'écran
        xl, xr = 100, 100
        for row in self.aliens:
            for alien in row:
                x1, y1, x2, y2 = alien.get_coords()
                xl = min(x1, xl)
                xr = max(x2, xr)

        if xl <= 0:   # Si un alien touche les bords
            self.direction *= -1  # Inverse la direction
            
            for row in self.aliens:
                for alien in row:
                    self.canvas.move(alien.alien, 0, 20)  # Descend tous les aliens d'une ligne

        if xr >= self.canvas.winfo_width():
            self.direction *= -1



    def update(self):
        self.move()
        if self.check_edges():
            pass  # Si on touche un bord, on inverse la direction et descend les aliens

    
    def delete(self):
        for row in self.aliens:
            for alien in row:
                alien.delete()

class Alien:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.alien = self.canvas.create_rectangle(x, y, x + 35, y + 25, fill="green")
        self.bullets = []
    
    def move(self, speed):
        self.canvas.move(self.alien, speed, 0)

    def destroy(self):
        self.canvas.delete(self.alien)

    def get_coords(self):
        return self.canvas.coords(self.alien)
    
    def fire(self):
        x1, y1, x2, y2 = self.get_coords()
        bullet = Bullet(self.canvas, (x1 + x2) / 2, y2 + 5, 5)
        self.bullets.append(bullet)

    def delete(self):
        self.canvas.delete(self.alien)
        for bullet in self.bullets:
            bullet.delete()

    def update(self):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.get_coords()[1] > 900:  # Si la balle sort de l'écran
                bullet.delete()
                self.bullets.remove(bullet)

class Ship:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ship = self.canvas.create_rectangle(0, 0, 50, 30, fill="blue")
        self.speed = 4
        self.canvas.move(self.ship, 275, 750)  # Position initiale
        self.moving_left = False
        self.moving_right = False
        self.bullets = []  # Liste pour les balles

        # Écoute des touches
        self.canvas.bind_all("<Left>", self.start_move_left)
        self.canvas.bind_all("<Right>", self.start_move_right)
        self.canvas.bind_all("<KeyRelease-Left>", self.stop_move)
        self.canvas.bind_all("<KeyRelease-Right>", self.stop_move)
        self.canvas.bind_all("<space>", self.fire)

    def start_move_left(self, event):
        self.moving_left = True

    def start_move_right(self, event):
        self.moving_right = True

    def stop_move(self, event):
        self.moving_left = False
        self.moving_right = False

    def get_coords(self):
        return self.canvas.coords(self.ship)

    def fire(self, event):
        # Crée une nouvelle balle à la position actuelle du vaisseau
        x1, y1, x2, y2 = self.get_coords()

        if len(self.bullets) < 3:
            bullet = Bullet(self.canvas, (x1 + x2) / 2, y1 - 5, -5)  # Position centrale du vaisseau
            self.bullets.append(bullet)

    def delete(self):
        self.canvas.delete(self.ship)
        for bullet in self.bullets:
            bullet.delete()

    def update(self):
        # Récupère les coordonnées actuelles du vaisseau
        x1, y1, x2, y2 = self.get_coords()

        # Empêche le vaisseau de sortir des limites
        if self.moving_left and x1 > 0:
            self.canvas.move(self.ship, -self.speed, 0)
        if self.moving_right and x2 < self.canvas.winfo_width():
            self.canvas.move(self.ship, self.speed, 0)

        # Met à jour toutes les balles
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.get_coords()[1] < 0:  # Si la balle sort de l'écran
                bullet.delete()
                self.bullets.remove(bullet)
class Bullet:
    def __init__(self, canvas, x, y, speed):
        self.canvas = canvas
        self.bullet = self.canvas.create_rectangle(x - 3, y - 10, x + 3, y, fill="red")
        self.speed = speed  # Vitesse vers le haut

    def move(self):
        self.canvas.move(self.bullet, 0, self.speed)

    def get_coords(self):
        return self.canvas.coords(self.bullet)

    def delete(self):
        self.canvas.delete(self.bullet)

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.title("Space Invaders")
    root.attributes("-fullscreen", True)
    root.mainloop()
