from game.assets import Character, Environment
from game.data import Library, State, User
from game.systems import View

import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.name = "A Few to Many"
        self.library = None
        self.state = None
        self.view = None
        self.objects = None

    def __repr__(self):
        return f"< Game >"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_library(self, library_object):
        self.library = library_object

    def get_library(self):
        return self.library

    def set_state(self, state_object):
        self.state = state_object

    def get_state(self):
        return self.state

    def set_view(self, view_object):
        self.view = view_object

    def get_view(self):
        return self.view
    
    def set_objects(self, object_dict):
        self.objects = object_dict

    def get_objects(self, object_dict):
        return self.objects
    
    ##### Initialization Methods #####

    def create_library(self):
        lib = Library()
        self.set_library(lib)

