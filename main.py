import pygame
from config import Config
from tela import Tela
from leaderboard import Leaderboard
from level import Level

def main():
    # Inicia a tela do jogo
    tela = Tela()
    tela.menu_inicial()

main()

# Encerramento do pygame e finalização do jogo
pygame.quit()