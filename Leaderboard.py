# -*- coding: utf-8 -*-
"""
Leaderboard.py
Author: Evan et Mathis
Date: YYYY-MM-DD
Description: This module handles the leaderboard functionality for the Space Invader game.
             It allows users to enter their pseudonyms and scores, and displays the leaderboard.
TODO: 
- Add error handling for file operations.
- Improve the UI for the leaderboard display.
"""

import tkinter as tk
from LabelButton import LabelButton

class Leaderboard:
    def __init__(self, canvas, frame, parent):
        """
        Initialize the Leaderboard class with canvas, frame, and parent.
        
        :param canvas: The canvas on which the leaderboard is displayed.
        :param frame: The frame containing the leaderboard.
        :param parent: The parent widget.
        """
        self.canvas = canvas
        self.frame = frame
        self.parent = parent

    def enter_pseudo(self, score):
        """
        Create an entry widget for the user to enter their pseudonym.
        
        :param score: The score to be associated with the pseudonym.
        """
        self.pseudo = tk.Entry(self.canvas, bg="black", fg="lime", font=("Arial", 24)) 
        self.pseudo.place(relx=0.5, rely=0.71, anchor="center")
        self.pseudo.bind("<Return>", lambda event: self.add_score(event, score))
        self.pseudo.focus_set() 

    def add_score(self, event, score):
        """
        Add the user's pseudonym and score to the leaderboard file.
        
        :param event: The event that triggered this function.
        :param score: The score to be added to the leaderboard.
        """
        pseudo = self.pseudo.get() # Get the pseudonym entered by the user
        with open("data/leaderboard.txt", "a", encoding="utf-8") as file: # Save the pseudonym and score to the file
            file.write(f"{pseudo} : {score}\n")
        self.pseudo.delete(0, tk.END)
        self.pseudo.destroy()

    def destroy(self):
        """
        Destroy the pseudonym entry widget.
        """
        self.pseudo.destroy()

    def show_leaderboard(self):
        """
        Display the leaderboard in a new window.
        """
        leaderboard = tk.Toplevel(self.parent)
        leaderboard.config(highlightthickness=0)
        leaderboard.config(borderwidth=0)
        leaderboard.title("Leaderboard")
        leaderboard.attributes("-fullscreen", True)
        leaderboard.configure(bg="black")
        leaderboard_text = tk.Text(leaderboard, bg="black", fg="lime", font=("Arial", 30))
        leaderboard_text.pack(expand=True, fill="both")
        leaderboard_text.tag_configure("center", justify="center")

        scores = {}
        with open("data/leaderboard.txt", "r", encoding="utf-8") as file: # Read the leaderboard file
            for line in file:
                parts = line.strip().split(" : ") # Split the line into pseudonym and score
                if len(parts) == 2:
                    pseudo, score = parts
                    score = int(score)
                    if pseudo in scores:
                        if score > scores[pseudo]: # Check if the new score is higher
                            scores[pseudo] = score
                    else:
                        scores[pseudo] = score
        
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True) # Sort scores in descending order
        
        leaderboard_text.insert(tk.END, "\n\n\n\n", "center") # Add space to center the text
        # Display the scores        
        for index, (pseudo, score) in enumerate(sorted_scores, start=1): # Show the rank, pseudonym, and score
            leaderboard_text.insert(tk.END, f"{index}. {pseudo} : {score}\n", "center")

        leaderboard_text.insert(tk.END, "\n\n\n\n", "center") # Add space to center the text
        
        # To remove all the borders
        black_band_bottom = tk.Frame(leaderboard, bg="black")
        black_band_bottom.place(relx=0.5, rely=0.93, anchor="center", relwidth=1, relheight=0.15)
        black_band_top = tk.Frame(leaderboard, bg="black")
        black_band_top.place(relx=0.5, rely=0.07, anchor="center", relwidth=1, relheight=0.15)
        black_band_right = tk.Frame(leaderboard, bg="black")
        black_band_right.place(relx=0.93, rely=0.5, anchor="center", relwidth=0.15, relheight=1)
        black_band_left = tk.Frame(leaderboard, bg="black")
        black_band_left.place(relx=0.07, rely=0.5, anchor="center", relwidth=0.15, relheight=1)

        close = LabelButton(black_band_bottom, "Close", leaderboard.destroy)
        close.place(relx=0.5, rely=0.5, anchor="center")







