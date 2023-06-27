import pygame
from body import Body
from rat import Rat
from config import Config
from collision import Collision

class Enemy(Rat):
    """
    Classe abstrata que define propriedades comuns a todos inimigos
    """
    def __init__(self, color, pos, leftOrRight):
        super().__init__(color, pos)
        self.leftOrRight = leftOrRight


    def update(self, dt):
            """
            Atualiza o estado do objeto Rat com base no tempo decorrido desde a última atualização.
            Args: dt (float): Tempo decorrido desde a última atualização em segundos.
            """
            S = Config.BLOCK_SIZE

            # Movimnta apenas para um lado
            if self.leftOrRight == True:
                self.velocity.x = 0.5
                self.last_direction = "right"
            else:
                self.velocity.x = -0.5
                self.last_direction = "left"

            #Verifica se o rato parou o movimento e atualiza sua imagem conforme ultima direção
            if self.last_direction == "left":
                self.image = Config.RAT_LEFT(self.color, self.indice)
                self.indice += 0.0625
                if self.indice >= 2:
                    self.indice = 0
            elif self.last_direction == "right":
                self.image = Config.RAT_RIGHT(self.color, self.indice)
                self.indice += 0.0625
                if self.indice >= 2:
                    self.indice = 0

            # Verifica se o rato está caindo
            if self.falling:
                # Aumenta a velocidade vertical para simular a aceleração da gravidade            
                self.velocity.y += 0.1

            # Atualiza a posição horizontal e vertical do rato com base na velocidade horizontal e no tempo decorrido
            new_pos = pygame.Vector2(self.pos.x + self.velocity.x * dt, self.pos.y + self.velocity.y * dt)
            if new_pos != self.pos:
                try:
                    canto_sup_esq = pygame.Vector2(new_pos.x, new_pos.y)
                    canto_sup_dir = pygame.Vector2(new_pos.x + S, new_pos.y)
                    canto_inf_esq = pygame.Vector2(new_pos.x, new_pos.y + S)
                    canto_inf_dir = pygame.Vector2(new_pos.x + S, new_pos.y + S)
                    hitbox = [canto_sup_esq, canto_sup_dir,canto_inf_esq, canto_inf_dir]
                    
                    for body in Body.bodies:
                        if body != self and hitbox in body: raise Exception("Colisão")
                    self.pos = new_pos
                except Collision as C:
                    if C.type == Collision.Ground:
                        if self.falling:
                            self.falling = False
                            self.velocity.y = 0
                            self.pos.y = C.height
                            self.pos.x = new_pos.x
                        else: self.pos = new_pos
                    elif C.type == Collision.Flying:
                        self.falling = True
                        self.pos.x = new_pos.x        
                        self.pos.y = new_pos.y
                    elif C.type == Collision.Side:
                        self.velocity.x *= C.rebound
                        self.pos.x += self.velocity.x * dt
                        self.pos.y = min(new_pos.y,C.height)
                        self.lives -= C.damage
                except Exception as e:
                    print(e)