from pygame import image, transform
class GameObject:

    def __init__(self, x, y, width, height, image_path):
        # image
        image_file = image.load(image_path)
        self.image = transform.scale(image_file, (width, height))

        # position and size
        self.x = x
        self.y = y
        self.width = width
        self.height = height
