class Library:
    def __init__(self):
        self.name = None
        self.game_object = None
        self.system = None
        self.view = None
        self.event = None
        self.data = None

    def __repr__(self):
        return f'< Library >'

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def to_dict(self):
        attribute_dict = {
            "name": self.name,
            "game_object": self.game_object,
            "system": self.system,
            "view": self.view,
            "event": self.event,
            "data": self.data
        }

        return attribute_dict

    def set_attribute(self, data_dict):
        for attribute in ["name", "game_object", "system", "view", "event", "data"]:
            if attribute in data_dict:
                setattr(self, attribute, data_dict[attribute])

    def get_attribute(self, property_name):
        library_data = self.to_dict()
        for attribute in library_data.items():
            if property_name == attribute:

                return library_data[attribute]

    def set_item(self, property_name, item_category, item):
        library_data = self.to_dict()
        library_data[property_name][item_category][item.get_name()] = item
        self.set_attribute(library_data)

    def get_item(self, property_name, item_category, item_name):
        library_data = self.to_dict()
        return library_data[property_name][item_category][item_name]

    ##### File Manipulation #####

    



    
