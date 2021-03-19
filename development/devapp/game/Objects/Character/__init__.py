from .Base import Base
from .NPC_Standalone import NPC

def new_character(class_object):
    new_character = Base()
    new_character.set_class(class_object)
    return new_character

def new_NPC():
    new_NPC = NPC()
    return new_NPC