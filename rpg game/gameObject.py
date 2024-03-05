from pygame import image, transform
class GameObject:

    def __init__(self, x, y, width, height, image_path):
        # image
        self.image = transform.scale(image.load(image_path), (width, height))

        # position and size
        self.x = x
        self.y = y
        self.width = width
        self.height = height
