from .Base import Base
class NPC(Base):
    def __init__(self):
        self.npc_type = "Merchant"

    def __repr__(self):
        return f"< NPC | Type: {self.npc_type} | Name: {self.first_name} {self.last_name} >"

    def set_npc_type(self, type_name):
        self.npc_type = type_name

    def get_npc_type(self):
        return self.npc_type