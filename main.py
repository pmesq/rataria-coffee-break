import pygame
from config import Config
from camera import Camera
from tilemap import Tilemap
from level_reader import LevelReader
from rat import Rat
from player import Player
from button import Button
from tela import Tela
from evento import Evento

from enum import Enum

pygame.init()

def main():
    # Configuração da tela do jogo
    screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

    # Inicialização do relógio para controle de FPS
    clock = pygame.time.Clock()

    # Variável para armazenar o tempo transcorrido entre cada frame
    dt = 0

    # Criação da câmera do jogo
    camera = Camera(pygame.Vector2(0, 0))

    # Leitura do nível do jogo utilizando a classe LevelReader
    tilemap, player, bodies = LevelReader.read('data/levels/1.txt')

    # Variável de controle do loop principal do jogo
    running = True

    # Variável que controla em qual tela o jogo esta 
    telaAtual = Tela.MENU_INICIAL

    # Loop principal 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(Config.SCREEN_COLOR) # Preenchimento da tela com uma cor de fundo    
        keys = pygame.key.get_pressed() # Captura das teclas pressionadas pelo jogador
        
        # Executo a função caracteristica do modo atual
        if telaAtual ==  Tela.MENU_INICIAL:
            telaAtual = Evento.menu_inicial(keys, screen)
        elif telaAtual ==  Tela.MENU_PRINCIPAL:
            telaAtual = Evento.menu_principal(keys, screen)
        elif telaAtual ==  Tela.ARCADE:
            telaAtual = Evento.arcade(keys, screen, player, tilemap, camera, bodies, dt)
        elif telaAtual ==  Tela.CAMPANHA:
            telaAtual = Evento.campanha(keys, screen)
        elif telaAtual ==  Tela.LEADERBOARD:
            telaAtual = Evento.leaderboard(keys, screen)

        # Atualização da tela e controle de FPS
        pygame.display.flip()
        dt = clock.tick(60)

        if telaAtual == Tela.SAIR:
            running = False

main()

# Encerramento do pygame e finalização do jogo
pygame.quit()

# Testando push
