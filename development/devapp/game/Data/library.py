class Library:
    def __init__(self):
        self.name = None
        self.objects = None
        self.systems = None
        self.views = None
        self.events = None

    def __repr__(self):
        return f'< Library >'

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def to_dict(self):
        attribute_dict = {
            "name": self.name,
            "objects": self.objects,
            "systems": self.systems,
            "views": self.views,
            "events": self.events,
        }

        return attribute_dict

    def set_attribute(self, data_dict):
        for attribute in ["name", "objects", "systems", "views", "events"]:
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


    ##### Start Methods #####


    



    
