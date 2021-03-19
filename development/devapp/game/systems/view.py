class View:
    def __init__(self):
        self.width = None
        self.height = None
        self.sprites = None

    def __repr__(self):
        return f'< View >'

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    

    