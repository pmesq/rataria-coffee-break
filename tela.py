from enum import Enum

# Enum usado para diferenciar em qual modo o jogo está
class Tela(Enum):    
    MENU_INICIAL = 1
    MENU_PRINCIPAL= 2
    ARCADE = 3
    LEADERBOARD = 4
    CAMPANHA = 5
    NOME_JOGADOR = 6
    SAIR = 0

    def setter(self, pos):
        self = pos