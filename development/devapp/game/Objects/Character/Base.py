class Base:
    def __init__(self):
        self.id = 0
        self.first_name = "First"
        self.last_name = "Last"
        self.character_class = None
        self.kind = None

    def __repr__(self):
        return f"< Character | ID: {self.id} | Name: {self.first_name} {self.last_name} >"

    def set_id(self, idno):
        self.id = idno

    def get_id(self):
        return self.id

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return f'{self.first_name}_{self.last_name}'

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def set_class(self, class_object):
        self.character_class = class_object

    def get_class(self):
        return self.character_class

    def set_kind(self):
        self.kind = self.character_class.get_name()

    def get_kind(self):
        return self.kind