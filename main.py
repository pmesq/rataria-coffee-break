import pygame
from config import Config
from camera import Camera
from tilemap import Tilemap
from level_reader import LevelReader
from rat import Rat
from player import Player

pygame.init()
screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0

camera = Camera(pygame.Vector2(0, 0))
tilemap, player, bodies = LevelReader.read('data/levels/1.txt')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('#444444')

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player.jump()

    if keys[pygame.K_a] and not keys[pygame.K_d]: player.move_left()
    elif keys[pygame.K_d] and not keys[pygame.K_a]: player.move_right()

    tilemap.draw(screen, camera)

    for body in bodies:
        body.update(dt)
        body.draw(screen, camera)
    
    camera.pos.x = min(max(0, player.pos.x - Config.SCREEN_WIDTH / 2), tilemap.m * Config.BLOCK_SIZE - Config.SCREEN_WIDTH)

    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()
