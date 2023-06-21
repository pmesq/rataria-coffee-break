import pygame
from config import Config
from body import Body

class Rat(Body):
    def __init__(self, color, pos):
        super().__init__(pos)
        self.color = color
        self.falling = True

    def draw(self, screen, camera):
        pos_x = self.pos.x - camera.pos.x #Calcula a posição inicial
        if pos_x < -40 or pos_x > Config.SCREEN_WIDTH + 40: return #Verifica se o rato está fora da tela

        pos = pygame.Vector2(pos_x, self.pos.y)

        S = Config.BLOCK_SIZE

        # Desenha o corpo
        pygame.draw.rect(screen, self.color, pygame.Rect(pos.x, pos.y, S, S))

        # Desenha as orelhas
        pygame.draw.circle(screen, self.color, pos + (0, 0), S / 4)
        pygame.draw.circle(screen, self.color, pos + (S, 0), S / 4)

        # Desenha os olhos
        pygame.draw.circle(screen, 'black', pos + (S / 4, S * 3 / 8), S / 16)
        pygame.draw.circle(screen, 'black', pos + (S * 3 / 4, S * 3 / 8), S / 16)

        # Desenha o nariz
        pygame.draw.circle(screen, 'black', pos + (S / 2, S / 2), S / 16)

        # Desenha a boca
        pygame.draw.line(screen, 'red', pos + (S * 3 / 8, S * 55 / 80), pos + (S * 5 / 8, S * 55 / 80), width=int(S / 16))

        # Desenha os bigodes
        pygame.draw.line(screen, 'black', pos + (S * 25 / 80, S * 45 / 80), pos + (S * 10 / 80, S * 40 / 80), width=int(S / 20))
        pygame.draw.line(screen, 'black', pos + (S * 25 / 80, S * 48 / 80), pos + (S * 10 / 80, S * 48 / 80), width=int(S / 20))
        pygame.draw.line(screen, 'black', pos + (S * 25 / 80, S * 51 / 80), pos + (S * 10 / 80, S * 56 / 80), width=int(S / 20))
        pygame.draw.line(screen, 'black', pos + (S * 55 / 80, S * 45 / 80), pos + (S * 70 / 80, S * 40 / 80), width=int(S / 20))
        pygame.draw.line(screen, 'black', pos + (S * 55 / 80, S * 48 / 80), pos + (S * 70 / 80, S * 48 / 80), width=int(S / 20))
        pygame.draw.line(screen, 'black', pos + (S * 55 / 80, S * 51 / 80), pos + (S * 70 / 80, S * 56 / 80), width=int(S / 20))

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
        # Verifica se a velocidade horizontal é maior que zero
        if self.velocity.x > 0:
            # Reduz gradualmente a velocidade horizontal com um limite mínimo de 0
            self.velocity.x = max(self.velocity.x - 0.1, 0) 
        elif self.velocity.x < 0:
            self.velocity.x = min(self.velocity.x + 0.1, 0)

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