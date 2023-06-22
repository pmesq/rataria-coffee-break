import pygame
from config import Config
from camera import Camera
from tilemap import Tilemap
from level_reader import LevelReader
from rat import Rat
from player import Player

from enum import Enum

# Enum utilizado para simbolizar em qual tela está o jogador 
class Tela(Enum):
    JOGO = 1
    MENU_PRINCIPAL= 2
    MENU_INICIAL = 3
    LEADERBOARD = 4

    # Setter: Define o num
    def setter(self, pos):
        self = pos

pygame.init()

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

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def menu_inicial(keys):
    # Declaro que usarei a variaǘel local telaAnual
    global telaAtual

    if keys[pygame.K_SPACE]:
        telaAtual = Tela.JOGO
        return
    
    
    screen.blit(Config.menu1_jpg, (0,0))

    pygame.draw.rect(screen, Config.COR_FONTE, (359, 432, 516, 56))
    pygame.draw.rect(screen, Config.COR_FUNDO_TEXTO, (362, 435, 510, 50))
    draw_text("Pressione ESPAÇO para iniciar", Config.font, Config.COR_FONTE, 407, 450)

    telaAtual = Tela.MENU_INICIAL
    return

def jogo(keys):
    # Declaro que usarei a variável local telaAnual
    global telaAtual

    # Caso seja pressionado a telca ESC, eu troco para o modo do menu 
    if keys[pygame.K_ESCAPE]:
        telaAtual = Tela.MENU_INICIAL
        return

    if keys[pygame.K_w]:
        player.jump()
    if keys[pygame.K_a] and not keys[pygame.K_d]:
        player.move_left()
    elif keys[pygame.K_d] and not keys[pygame.K_a]:
        player.move_right()

    tilemap.draw(screen, camera) # Desenho do tilemap na tela, levando em consideração a câmera

    # Atualização e desenho de todos os corpos presentes no jogo
    for body in bodies:
        body.update(dt)
        body.draw(screen, camera)
    
    # Atualização da posição da câmera para seguir o jogador
    camera.pos.x = min(max(0, player.pos.x - Config.SCREEN_WIDTH / 2), tilemap.m * Config.BLOCK_SIZE - Config.SCREEN_WIDTH)

    # Continuo no modo jogo
    telaAtual = Tela.JOGO

# Loop principal do jogo
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(Config.SCREEN_COLOR) # Preenchimento da tela com uma cor de fundo    
    keys = pygame.key.get_pressed() # Captura das teclas pressionadas pelo jogador
    
    # Executo a função caracteristica do modo atual
    if telaAtual == Tela.MENU_INICIAL:
        menu_inicial(keys)
    elif telaAtual == Tela.JOGO:
        jogo(keys)
    
    print(telaAtual)

    # Atualização da tela e controle de FPS
    pygame.display.flip()
    dt = clock.tick(60)

# Encerramento do pygame e finalização do jogo
pygame.quit()
