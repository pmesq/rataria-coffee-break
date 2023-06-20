import pygame

class Body:

    def __init__(self, pos: pygame.Vector2):
        self.pos = pos
        self.velocity = pygame.Vector2(0, 0)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos
    
    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        self._velocity = velocity

    def draw(self, screen, camera):
       pass
