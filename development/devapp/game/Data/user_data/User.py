class User:
    def __init__(self):
        self.id = 0
        self.name = "Default"

    def __repr__(self):
        return f'< User | ID: {self.id} | Name: {self.name} >'