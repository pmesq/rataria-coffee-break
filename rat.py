import pygame
from config import Config
from body import Body

class Rat(Body):
    def __init__(self, color, pos):
        super().__init__(pos)
        self.color = color
        self.falling = True

    def draw(self, screen, camera):
        pos_x = self.pos.x - camera.pos.x
        if pos_x < -40 or pos_x > Config.SCREEN_WIDTH + 40: return

        pos = pygame.Vector2(pos_x, self.pos.y)

        S = Config.BLOCK_SIZE

        # body
        pygame.draw.rect(screen, self.color, pygame.Rect(pos.x, pos.y, S, S))

        # ears
        pygame.draw.circle(screen, self.color, pos + (0, 0), S / 4)
        pygame.draw.circle(screen, self.color, pos + (S, 0), S / 4)

        # eyes
        pygame.draw.circle(screen, 'black', pos + (S / 4, S * 3 / 8), S / 16)
        pygame.draw.circle(screen, 'black', pos + (S * 3 / 4, S * 3 / 8), S / 16)

        # nose
        pygame.draw.circle(screen, 'black', pos + (S / 2, S / 2), S / 16)

        # mouth
        pygame.draw.line(screen, 'black', pos + (S * 3 / 8, S * 55 / 80), pos + (S * 5 / 8, S * 55 / 80), width = int(S / 16))

        # moustache
        pygame.draw.line(screen, 'black', pos + (S * 25 / 80, S * 45 / 80), pos + (S * 10 / 80, S * 40 / 80), width = int(S / 20))
        pygame.draw.line(screen, 'black', pos + (S * 25 / 80, S * 48 / 80), pos + (S * 10 / 80, S * 48 / 80), width = int(S / 20))
        pygame.draw.line(screen, 'black', pos + (S * 25 / 80, S * 51 / 80), pos + (S * 10 / 80, S * 56 / 80), width = int(S / 20))
        pygame.draw.line(screen, 'black', pos + (S * 55 / 80, S * 45 / 80), pos + (S * 70 / 80, S * 40 / 80), width = int(S / 20))
        pygame.draw.line(screen, 'black', pos + (S * 55 / 80, S * 48 / 80), pos + (S * 70 / 80, S * 48 / 80), width = int(S / 20))
        pygame.draw.line(screen, 'black', pos + (S * 55 / 80, S * 51 / 80), pos + (S * 70 / 80, S * 56 / 80), width = int(S / 20))

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def move_left(self):
        if self.falling:
            self.velocity.x = max(self.velocity.x - 0.2, -1)
        else:
            self.velocity.x = max(self.velocity.x - 0.3, -1)

    def move_right(self):
        if self.falling:
            self.velocity.x = min(self.velocity.x + 0.2, 1)
        else:
            self.velocity.x = min(self.velocity.x + 0.3, 1)

    def jump(self):
        if not self.falling:
            self.velocity.y += -1.5

    def update(self, dt):
        if self.velocity.x > 0:
            self.velocity.x = max(self.velocity.x - 0.1, 0)
        elif self.velocity.x < 0:
            self.velocity.x = min(self.velocity.x + 0.1, 0)
        
        if self.falling:
            self.velocity.y += 0.1

        self.pos.x += self.velocity.x * dt
        self.pos.y = min(Config.SCREEN_HEIGHT - Config.BLOCK_SIZE, self.pos.y + self.velocity.y * dt)

        if self.pos.y >= Config.SCREEN_HEIGHT - Config.BLOCK_SIZE:
            self.falling = False
            self.velocity.y = 0
        else:
            self.falling = True
