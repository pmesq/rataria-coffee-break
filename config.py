import pygame
import leitor
from leitor import Leitor
from button import Button

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

    # Configuração do rato
    RAT_COLOR = "blue"
    rato_direita = lambda color: pygame.image.load(f'imgs/ratos/{color}/ratin_right.png')
    rato_esquerda = lambda color: pygame.image.load(f'imgs/ratos/{color}/ratin_left.png')
    RAT_LEFT = lambda color, indice=0: pygame.transform.scale(Leitor.get_image_by_gid(Config.rato_esquerda(color), indice, 2, 65, 72) , (Config.BLOCK_SIZE,Config.BLOCK_SIZE))
    RAT_RIGHT = lambda color, indice=0: pygame.transform.scale(Leitor.get_image_by_gid(Config.rato_direita(color), indice, 2, 65, 72) , (Config.BLOCK_SIZE,Config.BLOCK_SIZE))

    # Configuração da fonte
    font = pygame.font.SysFont("arialblacomicck", 40)
    COR_FONTE = (255, 255, 255)
    COR_FUNDO_TEXTO = (0, 0, 0)

    # imagens que serão usadas durante o jogo
    menu1_jpg = pygame.image.load("imgs/menu1.jpg")
    menu2_jpg = pygame.image.load("imgs/menu2.jpg")
    leaderboardFUNDO_jpg = pygame.image.load("imgs/leaderboard2.jpg")
    
    campanha_jpg = pygame.image.load("imgs/botoes/campanha.png")
    arcade_jpg = pygame.image.load("imgs/botoes/arcade.png")
    leaderboard_jpg = pygame.image.load("imgs/botoes/leaderboard.png")
    sair_jpg = pygame.image.load("imgs/botoes/sair.png")
    escKey_jpg = pygame.image.load("imgs/botoes/escKey.png")
    back_jpg = pygame.image.load("imgs/botoes/back.png")

    campanhaAlt_jpg = pygame.image.load("imgs/botoes/campanhaAlt.png")
    arcadeAlt_jpg = pygame.image.load("imgs/botoes/arcadeAlt.png")
    leaderboardAlt_jpg = pygame.image.load("imgs/botoes/leaderboardAlt.png")
    sairAlt_jpg = pygame.image.load("imgs/botoes/sairAlt.png")

    # Botões que serão usados 
    botao_campanha = Button(254, 280, campanha_jpg, campanhaAlt_jpg, 0.5)
    botao_arcade = Button(254, 100, arcade_jpg, arcadeAlt_jpg, 0.5)
    botao_leaderboard = Button(254, 190, leaderboard_jpg, leaderboardAlt_jpg, 0.5)
    botao_sair = Button(254, 600, sair_jpg, sairAlt_jpg, 0.5)
    
    botao_esc = Button(254, 600, escKey_jpg, escKey_jpg, 0.5)
    botao_back = Button(45, 45, back_jpg, back_jpg, 0.5)
