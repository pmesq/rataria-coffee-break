import pygame

class Camera:
    """
    Classe que representa uma câmera no jogo.
    A câmera é responsável por controlar a posição da visão do jogo.
    """

    def __init__(self, pos: pygame.Vector2):
        """
        Inicializa a câmera com uma posição específica.
        Args: pos (pygame.Vector2): A posição inicial da câmera.
        """
        self.pos = pos

    @property # Getter: Obtém a posição da câmera.
    def pos(self):
        return self._pos

    @pos.setter # Setter: Define a posição da câmera.
    def pos(self, pos):
        self._pos = pos
