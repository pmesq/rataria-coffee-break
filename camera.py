import pygame

class Camera:

    def __init__(self, pos: pygame.Vector2):
        self.pos = pos

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos

