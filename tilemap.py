import pygame
from config import Config
from tile import Tile
from body import Body
from math import floor, ceil
from collision import Collision

class Tilemap:
    pos_map = lambda self, pos: pygame.Vector2(pos.x/self.tile_size, ((pos.y-Config.SCREEN_HEIGHT)/self.tile_size)+self.n)    

    def __init__(self, grid):
        # Inicializa a classe Tilemap com a grade (grid) fornecida
        self.n = len(grid)  # Número de linhas da grade
        self.m = len(grid[0])  # Número de colunas da grade
        self.grid = grid  # Armazena a grade fornecida
        self.tile_size = Config.BLOCK_SIZE  # Tamanho dos blocos em pixels, obtido da classe Config
        self.block_texture = pygame.transform.scale(pygame.image.load(f'imgs/tile.jpeg'), (self.tile_size,self.tile_size))
        Body.bodies.append(self)

    def __contains__(self, hitbox):
        #Verifica se o corpo está dentro do tilemap
        pos = hitbox[0] #A posição 0 da hitbox é referente a parte superior esquerda
        pos = self.pos_map(pos) #Converte a posição do corpo para a posição na grade
        i = floor(pos.y)

        if i in range(self.n):
            j_floor = floor(pos.x)
            j_ceil = ceil(pos.x)
            if j_floor < 0 or j_ceil >= self.m:
                raise Collision(Collision.Side,rebound=-0.5)
            block_inside = self.grid[i][j_floor] != Tile.NONE or self.grid[i][j_ceil] != Tile.NONE
            if block_inside:
                raise Collision(**Config.BLOCK_COLLISION)
        
        #Verifica se o bloco abaixo é um Tile.GROUND
        pos_bellow = hitbox[2] #A posição 2 da hitbox é referente a parte inferior esquerda
        pos_bellow = self.pos_map(pos_bellow) #Converte a posição para o bloco abaixo
        i = floor(pos_bellow.y)
        j_floor = floor(pos_bellow.x)
        j_ceil = ceil(pos_bellow.x)
        if j_floor < 0 or j_ceil >= self.m:
            raise Collision(**Config.BLOCK_COLLISION)
        
        if i in range(self.n):
            block_bellow = self.grid[i][j_floor] == Tile.GROUND or self.grid[i][j_ceil] == Tile.GROUND
            j = j_floor if self.grid[i][j_floor] == Tile.GROUND else j_ceil
            if block_bellow:
                height = self.ground(j)
                raise Collision(Collision.Ground, height)
            if not block_bellow:
                raise Collision(Collision.Flying)    
        return False
        
        
        

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

    def ground(self, j):
        count = 1
        for i in range(self.n):
            if self.grid[i][j] == Tile.GROUND:
                count += 1
        return Config.SCREEN_HEIGHT - (count)*Config.BLOCK_SIZE
        
