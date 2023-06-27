import pygame
from config import Config
from body import Body
from collision import Collision

class Cheese(Body):
    many_collected = 0

    def __init__(self, pos):
        super().__init__(pos)
        Body.bodies.append(self)
        self.image = Config.CHEESE_IMAGE
        self.collected = False

    @property # Getter: Retorna se o queijo foi coletado.
    def collected(self):
        return self._collected
    
    @collected.setter # Setter: Define se o queijo foi coletado.
    def collected(self, collected):
        self._collected = collected
        if collected:
            Body.bodies.remove(self)

    def __contains__(self, hitbox): #Sobscreve o operador in para verificar se um ponto está dentro da hitbox do queijo
        for point in hitbox:
            if point.x >= self.pos.x and point.x <= self.pos.x + Config.BLOCK_SIZE and point.y >= self.pos.y and point.y <= self.pos.y + Config.BLOCK_SIZE:
                self.collected = True
                Cheese.many_collected += 1
        return False

    def draw(self, screen, camera):
        pos_x = self.pos.x - camera.pos.x #Calcula a posição inicial
        if pos_x < -40 or pos_x > Config.SCREEN_WIDTH + 40 or self.collected: return #Verifica se o queijo está fora da tela ou já foi coletado

        pos = pygame.Vector2(pos_x, self.pos.y)
        screen.blit(self.image, (pos.x, pos.y))

       