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
        if pos_x < -40 or pos_x > Config.screen_width + 40:
            return

        pos = pygame.Vector2(pos_x, self.pos.y)

        # body
        pygame.draw.circle(screen, self.color, pos, 40)

        # ears
        pygame.draw.circle(screen, self.color, pos + (-30, -30), 10)
        pygame.draw.circle(screen, self.color, pos + (30, -30), 10)

        # eyes
        pygame.draw.circle(screen, 'black', pos + (-20, -10), 5)
        pygame.draw.circle(screen, 'black', pos + (20, -10), 5)

        # nose
        pygame.draw.circle(screen, 'black', pos + (0, 0), 5)

        # mouth
        pygame.draw.line(screen, 'black', pos + (-10, 15), pos + (10, 15), width = 5)

        # moustache
        pygame.draw.line(screen, 'black', pos + (-15, 5), pos + (-30, 0), width = 3)
        pygame.draw.line(screen, 'black', pos + (-15, 8), pos + (-30, 8), width = 3)
        pygame.draw.line(screen, 'black', pos + (-15, 11), pos + (-30, 16), width = 3)
        pygame.draw.line(screen, 'black', pos + (15, 5), pos + (30, 0), width = 3)
        pygame.draw.line(screen, 'black', pos + (15, 8), pos + (30, 8), width = 3)
        pygame.draw.line(screen, 'black', pos + (15, 11), pos + (30, 16), width = 3)

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
        self.pos.y = min(Config.screen_height - 40, self.pos.y + self.velocity.y * dt)

        if self.pos.y >= Config.screen_height - 40:
            self.falling = False
            self.velocity.y = 0
        else:
            self.falling = True
