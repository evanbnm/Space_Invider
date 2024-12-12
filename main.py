# -*- coding: utf-8 -*-
"""
Filename: main.py
Author: Evan et Mathis
Date: 2024-11-26
Description: This script initializes and runs the main menu for the Space Invader game.
"""

from python.Menu import Menu

def main():
    """
    Initialize and run the main menu.
    """
    menu = Menu()
    menu.mainloop()

if __name__ == "__main__":
    main()