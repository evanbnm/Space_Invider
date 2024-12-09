# -*- coding: utf-8 -*-
"""
Filename: Game.py
Author: Evan and Mathis
Date: 2023-10-10
Description: This module contains the Game class for the Space Invaders game.

TODO:
- Improve collision detection
- Add more levels
- Optimize performance
"""

import tkinter as tk
from tkinter import messagebox
import random
import subprocess
import sys

from AlienGroup import AlienGroup
from Ship import Ship
from Life import Life
from Score import Score
from Wall import Wall
from BonusAlien import BonusAlien
from LabelButton import LabelButton
from SkillPoint import SkillPoint
from Leaderboard import Leaderboard

class Game:
    def __init__(self, root):
        """Initialize the game with the given root window."""
        self.root = root
        self.root.attributes("-fullscreen", True)
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.normalize_width = self.screen_width / 1470   # Normalize the width and height of the game to fit all screen sizes
        self.normalize_height = self.screen_height / 956  # 1470 and 956 are the dimensions of the screen where the game was developed

        self.canvas = tk.Canvas(self.root, bg="black") # Creation of the canvas
        self.canvas.config(width=self.screen_width  , height=self.screen_height * 0.85)
        self.canvas.config(highlightthickness=0)
        self.canvas.pack()

        self.frame = tk.Frame(root) # Creation of the frame where the buttons, the score and all the infomations are displayed
        self.frame.config(width=self.screen_width  , height=self.screen_height * 0.15)
        self.frame.config(bg="black")
        self.frame.pack_propagate(False)
        self.frame.pack(side="bottom")

        self.menu = tk.Menu(self.root) # Creation of the menu bar at the top of the window
        self.root.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Menu", menu=self.file_menu)
        self.file_menu.add_command(label="New Game", command=self.restart_game)
        self.file_menu.add_command(label="Quit", command=self.quit_game)
        self.file_menu.add_command(label="About", command=self.show_about)
        
        self.running = True  # To check if the game is running
        self.loop_id = None  # Initialize the loop id for avoiding multiple loops bug
        self.bonus_exist = False # Initialize the bonus alien existence
        self.bonus_id = None # Initialize the bonus alien id for avoiding multiple bonus aliens bug
        self.end = False # To check if the game is over
        self.stage = 1 # Initialize the stage of the game
        self.win = False # To check if the player has won
        self.lose = False # To check if the player has lost

        self.buttonQuit = LabelButton(self.frame, "Menu", self.exe)
        self.buttonQuit.config(width=10, height=2)
        self.buttonQuit.place(relx=0.8, rely=0.5, anchor="center")
        self.buttonStart = LabelButton(self.frame, "Restart", self.restart_game)
        self.buttonStart.config(width=10, height=2)
        self.buttonStart.place(relx=0.2, rely=0.5, anchor="center")

        self.life = Life(self.frame) 
        self.score = Score(self.frame)  
        self.skill = SkillPoint(self.frame, self.canvas)
        self.leaderboard = Leaderboard(self.canvas, self.frame, None)

        self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="STAGE " + str(self.stage), fill="lime", font=("Arial", 50))
        self.root.after(1000, lambda: self.start_game())
        
    def show_about(self):
        """Show the 'About' message box."""
        messagebox.showinfo("About", "Space Invaders Game\nCreated by Evan and Mathis")

    def quit_game(self):
        """Quit the game and close the window."""
        self.running = False
        self.root.destroy()

    def exe(self):
        """Execute the main.py script and close the current game window."""
        self.running = False
        subprocess.Popen([sys.executable, "main.py"]) # Use the current Python interpreter
        self.root.destroy()

    def start_game(self):
        """Start the game by initializing all game components."""
        if self.bonus_id: # Cancel the bonus alien loop if it exists for avoiding multiple bonus aliens bug
            self.root.after_cancel(self.bonus_id)
            self.bonus_id = None
        self.win = False
        self.lose = False
        self.running = False
        self.bonus_exist = False
        self.canvas.delete("all")
        self.title = self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="STAGE " + str(self.stage), fill="lime", font=("Arial", 50))
        self.root.after(1000, lambda: self.canvas.delete(self.title))
        self.ship = Ship(self.canvas, self.skill.max_bullets, self.skill.time_bullets)

        if self.stage < 10:  # Create the alien group based on the stage to increase difficulty
            self.aliens_group = AlienGroup(self.canvas, self.normalize_width * (self.stage / 4 + 1.25), self.normalize_height * (self.stage * 5 + 10))
        if self.stage >= 10:
            self.aliens_group = AlienGroup(self.canvas, self.normalize_width * (self.stage / 4 + 1.25), self.normalize_height * 60)

        self.wall_right = Wall(self.canvas, self.screen_width * 0.7, self.screen_height * 0.64)
        self.wall_left = Wall(self.canvas, self.screen_width * 0.15, self.screen_height * 0.64)
        self.wall_middle = Wall(self.canvas, self.screen_width * 0.44, self.screen_height * 0.64)
        
        self.running = True

        # Cancel the previous loop if it exists for avoiding multiple loops bug
        if self.loop_id:  
            if not self.end:
                self.root.after_cancel(self.root.after(1))
            self.root.after_cancel(self.loop_id)
            self.loop_id = None
            self.end = False

        self.main_loop(True)

    def restart_game(self):
        """Restart the game by resetting all game components."""
        self.running = False
        self.end = True
        if self.lose: 
            self.leaderboard.destroy()
        if self.win: 
            self.continueButton.destroy()
            self.rate_button.destroy()
            self.bullet_button.destroy()
        self.canvas.delete("all")
        self.score.reset()
        self.life.reset()
        self.skill.reset()
        self.stage = 1
        self.title = self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="STAGE " + str(self.stage), fill="lime", font=("Arial", 50))
        self.root.after(1000, lambda: self.start_game())
        
    def main_loop(self, firstLoop = False):
        """Main game loop to update game state and check for collisions."""
        if self.running:
            self.ship.update()
            self.aliens_group.update() 
            for row in self.aliens_group.aliens:
                for alien in row:
                    alien.update()
            self.check_collisions()
            self.is_game_over(self.aliens_group, self.ship) 
            self.is_win(self.aliens_group)

            if self.bonus_exist:
                self.bonus.update()
                self.check_collision_bonus()

            if self.ship.life: # Cheat code to gain a life
                self.life.gain_life()
                self.ship.life = False

            if self.ship.skill: # Cheat code to gain a skill point
                self.skill.add_point()
                self.ship.skill = False

            self.life.update()
            self.score.update()
           
            if(firstLoop): # First loop to start the alien fire and bonus alien
                self.alien_fire()
                self.bonus_alien()

            self.loop_id = self.root.after(16, lambda: self.main_loop())
            
    
    def check_collisions(self):
        """Check for collisions between bullets, aliens, walls, and the ship."""
        for bullet in self.ship.bullets:
            for row in self.aliens_group.aliens: # Check if the bullet has hit an alien
                for alien in row:
                    if self.is_collision(bullet, alien): 
                        bullet.delete()
                        alien.delete()
                        row.remove(alien)
                        self.score.add(25)

            for brick in self.wall_right.brick: # Check if the bullet has hit a brick
                if self.is_collision(bullet, brick): 
                    bullet.delete()
                    brick.delete()
                    self.score.add(-100)
            for brick in self.wall_left.brick:
                if self.is_collision(bullet, brick): 
                    bullet.delete()
                    brick.delete()
                    self.score.add(-100)
            for brick in self.wall_middle.brick:
                if self.is_collision(bullet, brick):
                    bullet.delete()
                    brick.delete()
                    self.score.add(-100)

            if self.bonus_exist: # Check if the bullet has hit the bonus alien
                if self.is_collision(bullet, self.bonus): 
                    bullet.delete()
                    self.bonus.delete()
                    self.bonus_exist = False
                    self.score.add(150)
                    self.skill.add_point() # Gain a skill point when the bonus alien is hit

        for bullet in self.aliens_group.bullets:
            if self.is_collision(bullet, self.ship): # Check if the bullet has hit the ship
                bullet.delete()
                self.life.lose_life()
                break
            
            for brick in self.wall_right.brick: # Check if the bullet has hit a brick
                if self.is_collision(bullet, brick):
                    bullet.delete()
                    brick.delete()
            for brick in self.wall_left.brick:
                if self.is_collision(bullet, brick):
                    bullet.delete()
                    brick.delete()
            for brick in self.wall_middle.brick:
                if self.is_collision(bullet, brick):
                    bullet.delete()
                    brick.delete()
        
    def alien_fire(self):
        """Make a random alien fire a bullet."""
        if self.running:
            col = random.choice(self.aliens_group.aliens) # Choose a random column
            if self.stage < 10: # Change the fire rate based on the stage to increase difficulty
                time = random.randint(516 - self.stage * 50, 1516 - self.stage * 100)
            if self.stage >= 10 and self.stage < 20:
                time = random.randint(16, 516 - self.stage * 20)
            if self.stage >= 20: # After stage 20, the aliens fire at a constant rate.
                time = 16        # This stage might be impossible to beat.
            col[-1].fire() # Fire the bullet from the alien the lowest in the column
            self.root.after(time, lambda: self.alien_fire()) 

    def bonus_alien(self):
        """Create a bonus alien at random intervals."""
        if not self.bonus_exist and self.running: # To avoid multiple bonus aliens bug
            self.bonus_exist = True 
            direction = random.choice([-1,1]) # Choose a random direction for the bonus alien
            if direction == 1:
                self.bonus = BonusAlien(self.canvas, 0, 30, direction)
            else:
                self.bonus = BonusAlien(self.canvas, self.screen_width, 30, direction)
        time_bonus = random.randint(15000, 20000) # Choose a random time interval for the bonus alien
        self.bonus_id = self.root.after(time_bonus, self.bonus_alien)

    
    def check_collision_bonus(self):
        """Check for collisions edges and the bonus alien."""
        if self.running:
            x1, y1, x2, y2 = self.bonus.get_coords()
            if x1 >= self.canvas.winfo_width() or x2 <= 0:
                self.bonus.delete()
                self.bonus_exist = False

    def is_collision(self, object1, object2):
        """Check if two objects have collided."""
        bx1, by1, bx2, by2 = object1.get_coords()
        ax1, ay1, ax2, ay2 = object2.get_coords()
        return (bx1 < ax2 and by1 < ay2 and bx2 > ax1 and by2 > ay1)
    
    def is_game_over(self, aliens_group, ship):
        """Check if the game is over by verifying lives and alien positions."""
        if self.life.lives == 0: # Check if the player has no more lives
            self.lose_game()
        for row in aliens_group.aliens: # Check if the aliens have reached the ship
            for alien in row:
                if alien.get_coords()[3] >= ship.get_coords()[1]:
                    self.lose_game()
                    
    def lose_game(self):
        """Handle the game over scenario."""
        self.lose = True
        self.running = False
        self.end = True
        self.canvas.delete("all")
        self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="GAME OVER", fill="red", font=("Arial", 50))
        final_score = self.score.get_score() # Get the final score of the player
        self.canvas.create_text(self.screen_width / 2, self.screen_height / 2 + self.normalize_height * 50, text="Score: " + str(final_score), fill="red", font=("Arial", 30))
        self.canvas.create_text(self.screen_width / 2, self.screen_height / 2 + self.normalize_height * 150, text="Enter your pseudo", fill="red", font=("Arial", 30))
        self.leaderboard.enter_pseudo(final_score) # Enter the pseudo of the player in the leaderboard

    def is_win(self, aliens_group):
        """Check if the player has won by clearing all aliens and allows him to continue."""
        for row in aliens_group.aliens: # Check if all aliens have been destroyed
            if len(row):
                return 
        self.win = True
        self.bonus.delete()
        self.bonus_exist = False
        self.running = False
        self.end = True
        self.skill.add_point()
        self.score.add(300 + 200 * self.life.lives) # Add a bonus score based on the remaining lives
        self.canvas.delete("all")

        self.win_label = self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="YOU WIN", fill="lime", font=("Arial", 50))
        
        self.continueButton = LabelButton(self.canvas, "Continue", self.next_stage) # Button to continue to the next stage
        self.continueButton.place(relx=0.5, rely=0.8, anchor="center")
        self.continueButton.config(width=10, height=3)

        self.rate_button = LabelButton(self.canvas, "Upgrade rate\nLevel " + str(self.skill.level_rate), self.upgrade_rate) # Button to upgrade the ship's firing rate with skill points
        self.rate_button.place(relx=0.2, rely=0.8, anchor="center")
        self.rate_button.config(width=15, height=3)

        self.bullet_button = LabelButton(self.canvas, "Upgrade bullets\nLevel " + str(self.skill.level_bullets), self.upgrade_bullets) # Button to upgrade the number of bullets the ship can fire with skill points
        self.bullet_button.place(relx=0.8, rely=0.8, anchor="center")
        self.bullet_button.config(width=15, height=3)


    def upgrade_rate(self):
        """Upgrade the firing rate of the ship."""
        self.skill.upgrade_rate()
        self.rate_button.config(text="Upgrade rate\nLevel " + str(self.skill.level_rate))

    def upgrade_bullets(self):
        """Upgrade the number of bullets the ship can fire."""
        self.skill.upgrade_bullets()
        self.bullet_button.config(text="Upgrade bullets\nLevel " + str(self.skill.level_bullets))

    def next_stage(self):
        """Proceed to the next stage of the game."""
        self.continueButton.destroy()
        self.rate_button.destroy()
        self.bullet_button.destroy()
        self.canvas.delete("all")
        self.stage += 1
        self.canvas.create_text(self.screen_width / 2, self.screen_height / 2, text="STAGE " + str(self.stage), fill="lime", font=("Arial", 50))
        self.root.after(1000, lambda: self.start_game())








