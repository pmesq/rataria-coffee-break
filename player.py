import pygame
from rat import Rat
from config import Config

class Player(Rat):

    def __init__(self, pos):
        super().__init__('purple', pos)
    