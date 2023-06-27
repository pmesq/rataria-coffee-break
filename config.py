import pygame
import math
import leitor
from leitor import Leitor
from math import floor
from button import Button

class Config:
    """
    Classe que armazena configurações e constantes relacionadas ao jogo.
    Contém atributos estáticos com valores específicos.
    """

    pygame.init()

    def draw_text(screen, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # Atributos do jogador que serão usados no leaderboard
    nomeJogador = ""
    pontosJogador = 0

    # Configurações da tela
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    SCREEN_COLOR = '#444444'

    # Configurações dos blocos
    BLOCK_SIZE = 80
    BLOCK_COLOR = "#222222"
    BLOCK_REBOUND = -0.5
    BLOCK_DAMAGE = 0
    BLOCK_COLLISION = {"cod_type":3, "damage":BLOCK_DAMAGE, "rebound":BLOCK_REBOUND}

    # Configuração do jogador
    PLAYER_COLOR = "purple"

    # Configuração do rato
    RAT_SIZE = BLOCK_SIZE
    RAT_COLOR = "blue"
    rato_direita = lambda color: pygame.image.load(f'imgs/ratos/{color}/right.png')
    rato_esquerda = lambda color: pygame.image.load(f'imgs/ratos/{color}/left.png')
    RAT_RIGHT = lambda color, indice: pygame.transform.scale(Leitor.get_image_by_gid(Config.rato_direita(color), floor(indice), 2, 65, 72) , (Config.BLOCK_SIZE,Config.BLOCK_SIZE))
    RAT_LEFT = lambda color, indice: pygame.transform.scale(Leitor.get_image_by_gid(Config.rato_esquerda(color), floor(indice), 2, 65, 72) , (Config.BLOCK_SIZE,Config.BLOCK_SIZE))
    RAT_DAMAGE = 1
    RAT_REBOUND = -1.5
    RAT_COLLISION = {"cod_type":3, "damage":RAT_DAMAGE, "rebound":RAT_REBOUND}

    # Configuração do contador de vida
    LIFE_WIDTH = 0.5*BLOCK_SIZE*(199/57)
    LIFE_HEIGTH = 0.5*BLOCK_SIZE
    LIFE = lambda x: pygame.transform.scale(pygame.image.load(f'imgs/lives/{x}.png'), (Config.LIFE_WIDTH, Config.LIFE_HEIGTH))

    #Configuração do queijo
    CHEESE_WIDTH = 0.5*BLOCK_SIZE*(59/38)
    CHEESE_HEIGTH = 0.5*BLOCK_SIZE
    CHEESE_IMAGE = pygame.transform.scale(pygame.image.load('imgs/cheese.png'), (CHEESE_WIDTH, CHEESE_HEIGTH))
    CHEESE_COUNTER = pygame.transform.scale(pygame.image.load('imgs/cheese.png'), (0.7*CHEESE_WIDTH, 0.7*CHEESE_HEIGTH))

    
    # Configuração da fonte
    font = pygame.font.SysFont("arialblacomicck", 40)
    font2 = pygame.font.Font("imgs/font.ttf", 50)
    font3 = pygame.font.Font("imgs/font.ttf", 40)
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)
    AMARELO = (189, 213, 28)
    CINZA = (211, 211, 211)

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

    enter_jpg = pygame.image.load("imgs/botoes/enter.png")
   
    # Botões que serão usados 
    botao_campanha = Button(254, 280, campanha_jpg, campanhaAlt_jpg, 0.5)
    botao_arcade = Button(254, 100, arcade_jpg, arcadeAlt_jpg, 0.5)
    botao_leaderboard = Button(254, 190, leaderboard_jpg, leaderboardAlt_jpg, 0.5)
    botao_sair = Button(254, 600, sair_jpg, sairAlt_jpg, 0.5)
    
    botao_esc = Button(254, 600, escKey_jpg, escKey_jpg, 0.5)
    botao_back = Button(45, 45, back_jpg, back_jpg, 0.5)
    botao_enter = Button(749, 292, enter_jpg, enter_jpg, 0.5)

    input_box = pygame.Rect(340, 300, 400, 60)
    enter_block = pygame.Rect(770, 300, 150, 60)
