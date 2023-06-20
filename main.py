import pygame
from config import Config
from rat import Rat
from player import Player
from camera import Camera

pygame.init()
screen = pygame.display.set_mode((Config.screen_width, Config.screen_height))
clock = pygame.time.Clock()
dt = 0

camera = Camera(pygame.Vector2(0, 0))
player = Player()
bodies = [player, Rat('yellow', pygame.Vector2(Config.screen_width / 2 + 100, 40))]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('#333333')

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player.jump()

    if keys[pygame.K_a] and not keys[pygame.K_d]: player.move_left()
    elif keys[pygame.K_d] and not keys[pygame.K_a]: player.move_right()

    for body in bodies:
        body.update(dt)
        body.draw(screen, camera)
    
    camera.pos.x = max(0, player.pos.x - Config.screen_width / 2)

    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()
