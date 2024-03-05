from gameObject import GameObject

class Player(GameObject):
    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)

        self.speed = speed
    
    def move(self, dy, max_height):
        if (self.y >= max_height - self.height and dy > 0) or (self.y == 0 and dy < 0):
            return
        self.y += (dy * self.speed)
