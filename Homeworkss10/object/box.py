
class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def check_win(self, dest):
        if self.x == dest.x and self.y == dest.y:
            return True
        return False

