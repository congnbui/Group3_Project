class Pusher:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def collide(self, box, dx, dy):
        if self.x + dx == box.x and self.y + dy == box.y:
            return True
        return False

    def move(self, dx, dy):
        self.x += dx
        self.y += dy