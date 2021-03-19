from Game import Data, Object, View
from Game import View
import pygame
from pygame.locals import *

class Game():
    def __init__(self):
        self.name = "A Few to Many"
        self.user = None
        self.library = None
        self.state = None
        self.screen = None
        self.view = None
        self.objects = None
        self.clock = None

    def __repr__(self):
        return f"< Game >"

    def set_user(self, user_object):
        self.user = user_object

    def get_user(self):
        return self.user

    def set_library(self, library_object):
        self.library = library_object

    def get_library(self):
        return self.library

    def set_state(self, state_object):
        self.state = state_object

    def get_state(self):
        return self.state

    def set_screen(self, surface_object):
        self.screen = surface_object

    def get_screen(self):
        return self.screen

    def set_view(self, view_object):
        self.view = view_object

    def get_view(self):
        return self.view
    
    def set_objects(self, object_dict):
        self.objects = object_dict

    def get_objects(self, object_dict):
        return self.objects

    def set_clock(self, clock_object):
        self.clock = clock_object

    def get_clock(self):
        return self.clock
    
    ##### Initialization Methods #####

    def start_library(self):
        pass

    def start_game(self):
        pass

    ##########

    def main(self):
        pygame.init()
        self.start_game()

