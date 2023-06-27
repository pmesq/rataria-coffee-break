import pygame
from config import Config
from rat import Rat
from player import Player
from cheese import Cheese
from tile import Tile
from tilemap import Tilemap
from camera import Camera

class Level:
    """
    Classe responsável por ler e interpretar os dados de um nível do jogo.
    """
    def __init__(self, filepath):
        self.tilemap = []
        self.player = None
        self.bodies = []
        self.dt = 0
        self.camera = Camera(pygame.Vector2(0, 0))
        self.read(filepath)

    def new_random_rat(self, pos, rightOrleft):

        self.bodies.append(Rat(Config.RAT_COLOR, pygame.Vector2(80, 560), True))   

    def read(self, filename: str):
        # Abrir o arquivo para leitura, ler as linhas do arquivo e separá-las em uma lista
        f = open(filename, 'r')
        lines = f.read().split('\n')
        # Extrair as dimensões do nível (número de linhas e colunas)
        n, m = [int(x) for x in lines[0].split()]
        lines.pop(0)
        grid = [] # Inicializar listas vazias para armazenar os corpos e a grade do nível

        for i in range(n): # Percorrer cada linha do nível
            grid.append([])
            for j in range(m): # Percorrer cada caractere da linha
                ch = lines[i][j]
                # Verificar o caractere e adicionar o tipo correspondente à grade
                if ch == '#':
                    grid[i].append(Tile.GROUND)
                else:
                    grid[i].append(Tile.NONE)
                # Verificar o caractere e adicionar um corpo correspondente
                if ch == 'E':
                    self.bodies.append(Rat(Config.RAT_COLOR, pygame.Vector2(j * Config.BLOCK_SIZE, Config.SCREEN_HEIGHT - (n - i) * Config.BLOCK_SIZE)))
                elif ch == 'S':
                    self.player = Player(pygame.Vector2(j * Config.BLOCK_SIZE, Config.SCREEN_HEIGHT - (n - i) * Config.BLOCK_SIZE))
                elif ch == 'C':
                    self.bodies.append(Cheese(pygame.Vector2(j * Config.BLOCK_SIZE+ 0.1118*Config.BLOCK_SIZE , Config.SCREEN_HEIGHT - (n - i) * Config.BLOCK_SIZE+0.5*Config.BLOCK_SIZE )))
        # Criar um objeto Tilemap a partir da grade lida
        self.tilemap = Tilemap(grid)

        # Adicionar o corpo do jogador e o tilemap à lista de corpos
        self.bodies.append(self.player)
        self.bodies.append(self.tilemap)
        Cheese.many_collected = 0  
