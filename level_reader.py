import pygame
from config import Config
from rat import Rat
from player import Player
from tile import Tile
from tilemap import Tilemap

class LevelReader:
    """
    Classe responsável por ler e interpretar os dados de um nível do jogo.
    """

    def read(filename: str):
        # Abrir o arquivo para leitura, ler as linhas do arquivo e separá-las em uma lista
        f = open(filename, 'r')
        lines = f.read().split('\n')

        # Extrair as dimensões do nível (número de linhas e colunas)
        n, m = [int(x) for x in lines[0].split()]
        lines.pop(0)

        # Inicializar listas vazias para armazenar os corpos e a grade do nível
        bodies = []
        grid = []

        # Percorrer cada linha do nível
        for i in range(n):
            grid.append([])

            # Percorrer cada caractere da linha
            for j in range(m):
                ch = lines[i][j]

                # Verificar o caractere e adicionar o tipo correspondente à grade
                if ch == '#':
                    grid[i].append(Tile.GROUND)
                else:
                    grid[i].append(Tile.NONE)

                # Verificar o caractere e adicionar um corpo correspondente
                if ch == 'E':
                    bodies.append(Rat(Config.RAT_COLOR, pygame.Vector2(j * Config.BLOCK_SIZE, Config.SCREEN_HEIGHT - (n - i) * Config.BLOCK_SIZE)))
                elif ch == 'S':
                    player = Player(pygame.Vector2(j * Config.BLOCK_SIZE, Config.SCREEN_HEIGHT - (n - i) * Config.BLOCK_SIZE))

        # Criar um objeto Tilemap a partir da grade lida
        tilemap = Tilemap(grid)

        # Adicionar o corpo do jogador à lista de corpos
        bodies.append(player)

        # Retornar o Tilemap, o objeto Player e a lista de corpos
        return tilemap, player, bodies
