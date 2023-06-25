import pygame

class Body:
    """
    Classe abstrata que representa um objeto com posição e velocidade.
    Essa classe é projetada para ser herdada por outros objetos do jogo.
    """

    def __init__(self, pos: pygame.Vector2):
        self.pos = pos
        self.velocity = pygame.Vector2(0, 0) # Velocidade inicial zero

    @property #Getter: Retorna a posição atual do objeto.
    def pos(self):
        return self._pos

    @pos.setter #Setter: Define a posição do objeto.
    def pos(self, pos):
        self._pos = pos
    
    @property #Getter: Retorna a velocidade atual do objeto.
    def velocity(self):
        return self._velocity

    @velocity.setter #Setter: Define a velocidade do objeto.
    def velocity(self, velocity):
        self._velocity = velocity


    def draw(self, screen, camera):
        """
        Método responsável por desenhar o objeto na tela.
        Esse método deve ser implementado nas classes filhas.
        """
        pass

    def update(self, dt):
        """
        Método responsável por atualizar o objeto na tela.
        Esse método deve ser implementado nas classes filhas.
        """
        pass