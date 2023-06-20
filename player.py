import pygame
from rat import Rat
from config import Config

class Player(Rat):

    def __init__(self):
        super().__init__('purple', pygame.Vector2(Config.screen_width / 2, Config.screen_height / 2))
    