'''
Czernecki Mathis
07/11/2024
tests tkinter pour space invaders
'''

import tkinter as tk


fenetre = tk.Tk()
fenetre.title('Space invaders')

toile = tk.Canvas(fenetre,
                  height=700,
                  width = 700,
                  bg='black')
toile.grid(row = 1, column = 0, rowspan = 10, columnspan = 10)


button_jouer = tk.Button(fenetre,
                         text = 'JOUER',
                         fg = 'black',
                         ).grid(row = 4, column = 11)


button_quit = tk.Button(fenetre,
                        text = 'QUITTER',
                        fg = 'black',
                        command = fenetre.destroy).grid(row = 8, column = 11)

texte_score = tk.Label(fenetre,
                 text = 'Score :',
                 fg = 'black',
                 ).grid(row = 0, column = 0)


class


fenetre.mainloop()