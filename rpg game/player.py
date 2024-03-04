from gameObject import GameObject

class Player(GameObject):
    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)

        self.speed = speed
    
    def move(self, dy):
        self.y += (dy * self.speed)
