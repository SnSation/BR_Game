class NPC():
    def __init__(self):
        self.npc_type = None

    def __repr__(self):
        return f"< NPC | Type: {self.npc_type} | >"

    def set_npc_type(self, type_name):
        self.npc_type = type_name

    def get_npc_type(self):
        return self.npc_type