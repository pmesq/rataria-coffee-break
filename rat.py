import pygame
from config import Config
from body import Body

class Rat(Body):
    def __init__(self, color, pos):
        super().__init__(pos)
        self.color = color
        self.falling = True
        self.image = pygame.image.load('imgs/ratin_right.png').convert_alpha()
        self.last_direction = "right"


    def draw(self, screen, camera):
        pos_x = self.pos.x - camera.pos.x #Calcula a posição inicial
        if pos_x < -40 or pos_x > Config.SCREEN_WIDTH + 40: return #Verifica se o rato está fora da tela
        
        pos = pygame.Vector2(pos_x, self.pos.y)

        S = Config.BLOCK_SIZE


        screen.blit(self.image, (pos.x, pos.y))


    @property # Getter: Retorna a cor atual do rato.
    def color(self):
        return self._color

    @color.setter # Setter: Define a cor do rato.
    def color(self, color):
        self._color = color

    def move_left(self): # Move o rato para a esquerda com base na sua velocidade atual.
        if self.falling:
            self.velocity.x = max(self.velocity.x - 0.2, -1)
        else:
            self.velocity.x = max(self.velocity.x - 0.3, -1) 

    def move_right(self): # Move o rato para a direita com base na sua velocidade atual.
        if self.falling:
            self.velocity.x = min(self.velocity.x + 0.2, 1)
        else:
            self.velocity.x = min(self.velocity.x + 0.3, 1)

    def jump(self):
        # Faz o rato pular se não estiver caindo.
        if not self.falling:
            self.velocity.y += -1.5

    def update(self, dt):
        """
        Atualiza o estado do objeto Rat com base no tempo decorrido desde a última atualização.
        Args: dt (float): Tempo decorrido desde a última atualização em segundos.
        """
        S = Config.BLOCK_SIZE
        # Verifica se a velocidade horizontal é maior que zero
        if self.velocity.x > 0:
            # Reduz gradualmente a velocidade horizontal com um limite mínimo de 0
            self.velocity.x = max(self.velocity.x - 0.1, 0) 
            self.image = Config.RAT_RIGHT
            self.last_direction = "right"
        elif self.velocity.x < 0:
            self.velocity.x = min(self.velocity.x + 0.1, 0)
            self.image = Config.RAT_LEFT
            self.last_direction = "left"

        #Verifica se o rato parou o movimento e atualiza sua imagem conforme ultima direção
        if self.last_direction == "left":
            self.image = Config.RAT_LEFT
        elif self.last_direction == "right":
            self.image = Config.RAT_RIGHT

        # Verifica se o rato está caindo
        if self.falling:
            # Aumenta a velocidade vertical para simular a aceleração da gravidade
            self.velocity.y += 0.1

        # Atualiza a posição horizontal e vertical do rato com base na velocidade horizontal e no tempo decorrido
        self.pos.x += self.velocity.x * dt
        self.pos.y = min(Config.SCREEN_HEIGHT - Config.BLOCK_SIZE, self.pos.y + self.velocity.y * dt)

        # Verifica se o rato atingiu ou ultrapassou o chão
        if self.pos.y >= Config.SCREEN_HEIGHT - Config.BLOCK_SIZE:
            # Define que o rato não está mais caindo e zera a velocidade vertical
            self.falling = False
            self.velocity.y = 0
        else:
            # Caso contrário, o rato está no ar e ainda está caindo
            self.falling = True