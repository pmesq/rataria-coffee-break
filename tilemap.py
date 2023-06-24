import pygame
from config import Config
from tile import Tile

class Tilemap:

    def __init__(self, grid):
        # Inicializa a classe Tilemap com a grade (grid) fornecida
        self.n = len(grid)  # Número de linhas da grade
        self.m = len(grid[0])  # Número de colunas da grade
        self.grid = grid  # Armazena a grade fornecida
        self.tile_size = Config.BLOCK_SIZE  # Tamanho dos blocos em pixels, obtido da classe Config
        self.block_texture = pygame.transform.scale(pygame.image.load(f'imgs/tile.jpeg'), (self.tile_size,self.tile_size))

    def draw(self, screen, camera):
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == Tile.NONE:
                    continue  # Pula para a próxima iteração se o bloco atual for do tipo Tile.NONE (nenhum bloco)

                # Calcula a posição x do bloco na tela
                pos_x = j * Config.BLOCK_SIZE - camera.pos.x

                if pos_x <= -Config.BLOCK_SIZE:
                    continue  # Pula para a próxima iteração se o bloco estiver completamente fora da tela

                # Calcula a posição do bloco na tela
                pos = pygame.Vector2(pos_x, Config.SCREEN_HEIGHT - Config.BLOCK_SIZE * (self.n - i))
                
                # Desenha um retângulo na tela representando o bloco
                screen.blit(self.block_texture, pos)
