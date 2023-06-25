import pygame
from config import Config
from body import Body


class Cheese(Body):

    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.transform.scale(pygame.image.load('imgs/cheese.png'), (0.5*Config.BLOCK_SIZE*(59/38),0.5*Config.BLOCK_SIZE))

    def draw(self, screen, camera):
        pos_x = self.pos.x - camera.pos.x #Calcula a posição inicial
        if pos_x < -40 or pos_x > Config.SCREEN_WIDTH + 40: return #Verifica se o queijo está fora da tela

        pos = pygame.Vector2(pos_x, self.pos.y)
        screen.blit(self.image, (pos.x, pos.y))

       