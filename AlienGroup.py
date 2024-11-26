from Alien import Alien

class AlienGroup:
    def __init__(self, canvas):
        self.canvas = canvas
        self.aliens = []
        self.speed = 2
        self.direction = 1  # 1 = droite, -1 = gauche
        self.x_offset = 100
        self.y_offset = 80
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
        for row in self.aliens:
            if len(row) == 0:
                self.aliens.remove(row)
    
    def delete(self):
        for row in self.aliens:
            for alien in row:
                alien.delete()