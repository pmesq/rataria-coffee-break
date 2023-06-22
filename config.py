import pygame

class Config:
    """
    Classe que armazena configurações e constantes relacionadas ao jogo.
    Contém atributos estáticos com valores específicos.
    """

    pygame.init()

    # Configurações da tela
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    SCREEN_COLOR = '#444444'

    # Configurações dos blocos
    BLOCK_SIZE = 80
    BLOCK_COLOR = "#222222"
    # Configuração do jogador
    PLAYER_COLOR = "purple"

    # Configuração da fonte
    font = pygame.font.SysFont("arialblacomicck", 40)
    COR_FONTE = (255, 255, 255)
    COR_FUNDO_TEXTO = (0, 0, 0)

    # imagens que serão usadas durante o jogo
    menu1_jpg = pygame.image.load("imgs/menu1.jpg")
