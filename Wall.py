from Brick import Brick

class Wall:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.brick = []
        self.x = x
        self.y = y
        self.create()
    
    def create(self):
        for i in range(6):
            for j in range(4):
                brick = Brick(self.canvas, self.x + i * 36, self.y + j * 36, self)
                self.brick.append(brick)






