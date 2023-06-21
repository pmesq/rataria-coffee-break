import pygame
from config import Config
from rat import Rat
from player import Player
from tile import Tile
from tilemap import Tilemap

class LevelReader:

    def read(filename: str):
        f = open(filename, 'r')
        lines = f.read().split('\n')
        n, m = [int(x) for x in lines[0].split()]
        lines.pop(0)

        bodies = []
        grid = []
        for i in range(n):
            grid.append([])
            for j in range(m):
                ch = lines[i][j]

                if ch == '#': grid[i].append(Tile.GROUND)
                else: grid[i].append(Tile.NONE)

                if ch == 'E':
                    bodies.append(Rat('yellow', pygame.Vector2(j * Config.BLOCK_SIZE, Config.SCREEN_HEIGHT - (n - i) * Config.BLOCK_SIZE)))
                elif ch == 'S':
                    player = Player(pygame.Vector2(j * Config.BLOCK_SIZE, Config.SCREEN_HEIGHT - (n - i) * Config.BLOCK_SIZE))

        tilemap = Tilemap(grid)
        bodies.append(player)

        return tilemap, player, bodies
