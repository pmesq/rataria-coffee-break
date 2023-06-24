import pygame
from rat import Rat
from config import Config

class Player(Rat):
    """
    Classe que representa o jogador no jogo.

    É uma classe concreta que herda da classe Rat, que por sua vez herda da classe Body.
    """

    def __init__(self, pos):
        super().__init__(Config.PLAYER_COLOR, pos)
        self.lives = 3

    
    