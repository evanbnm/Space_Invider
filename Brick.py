from PIL import Image, ImageTk

class Brick:
    def __init__(self, canvas, x, y, wall):
        self.canvas = canvas
        self.wall = wall
        original = Image.open("images/brick.png")
        resized = original.resize((36, 36))
        self.image = ImageTk.PhotoImage(resized)
        self.brick = self.canvas.create_image(x, y, image=self.image)

    def delete(self):
        self.wall.brick.remove(self)

    def get_coords(self):
        x, y = self.canvas.coords(self.brick)
        x1 = x - 18
        y1 = y - 18
        x2 = x1 + 36
        y2 = y1 + 36
        return x1, y1, x2, y2
    