import pygame
from config import Config
from tile import Tile

class Tilemap:

    def __init__(self, grid):
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        self.tile_size = Config.BLOCK_SIZE
    
    def draw(self, screen, camera):
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == Tile.NONE: continue

                pos_x = j * Config.BLOCK_SIZE - camera.pos.x
                if pos_x <= -Config.BLOCK_SIZE: continue

                pos = pygame.Vector2(pos_x, Config.SCREEN_HEIGHT - Config.BLOCK_SIZE * (self.n - i))
                
                pygame.draw.rect(screen, '#222222', pygame.Rect(pos.x, pos.y, Config.BLOCK_SIZE, Config.BLOCK_SIZE))
