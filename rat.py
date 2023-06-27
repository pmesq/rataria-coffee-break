import pygame
from config import Config
from body import Body
from collision import Collision

class Rat(Body):
    def __init__(self, color, pos):
        super().__init__(pos)
        Body.bodies.append(self)
        self.color = color
        self.indice = 0
        self.falling = False
        self.image = Config.RAT_RIGHT(color, self.indice)
        self.last_direction = "right"
        self.lives = 3
        self.dead = False

    @property # Getter: Retorna se o rato está morto.
    def dead(self):
        return self._dead
        # Espaço para uma eventual animação de morte do rato

    @dead.setter # Setter: Define se o rato está morto.
    def dead(self, dead):
        self._dead = dead
        # Espaço para uma eventual animação de morte do rato
        if dead:
            Body.bodies[0].velocity.y = -1
            Body.bodies.remove(self)

    @property # Getter: Retorna a quantidade de vidas do rato.
    def lives(self):
        return self._lives
    
    @lives.setter # Setter: Define a quantidade de vidas do rato.
    def lives(self, lives):
        self._lives = max(lives,0)
        if lives == 0:
            self.dead = True

    def __contains__(self, hitbox): #Sobscreve o operador in para verificar se um ponto está dentro da hitbox do rato
        sup_esq = hitbox[0].x >= self.pos.x and hitbox[0].x <= self.pos.x + Config.RAT_SIZE and hitbox[0].y >= self.pos.y and hitbox[0].y <= self.pos.y + Config.RAT_SIZE
        sup_dir = hitbox[1].x >= self.pos.x and hitbox[1].x <= self.pos.x + Config.RAT_SIZE and hitbox[1].y >= self.pos.y and hitbox[1].y <= self.pos.y + Config.RAT_SIZE
        inf_esq = hitbox[2].x >= self.pos.x and hitbox[2].x <= self.pos.x + Config.RAT_SIZE and hitbox[2].y >= self.pos.y and hitbox[2].y <= self.pos.y + Config.RAT_SIZE
        inf_dir = hitbox[3].x >= self.pos.x and hitbox[3].x <= self.pos.x + Config.RAT_SIZE and hitbox[3].y >= self.pos.y and hitbox[3].y <= self.pos.y + Config.RAT_SIZE

        collision_side = (sup_esq and inf_esq) or (sup_dir and inf_dir)
        collision_bellow = (inf_esq and not sup_esq) or (inf_dir and not sup_dir)
        if collision_side:
            raise Collision(**Config.RAT_COLLISION)
        if collision_bellow:
            self.dead = True
        return False

    def draw(self, screen, camera):
        if not self.dead:
            pos_x = self.pos.x - camera.pos.x #Calcula a posição inicial
            if pos_x < -40 or pos_x > Config.SCREEN_WIDTH + 40 or self.dead: return #Verifica se o rato está fora da tela ou morto
            pos = pygame.Vector2(pos_x, self.pos.y)

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
            self.falling = True

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
            self.image = Config.RAT_RIGHT(self.color, self.indice)
            self.indice += 0.125
            if self.indice >= 2:
                self.indice = 0
            self.last_direction = "right"
        elif self.velocity.x < 0:
            self.velocity.x = min(self.velocity.x + 0.1, 0)
            self.image = Config.RAT_LEFT(self.color, self.indice)
            self.indice += 0.125
            if self.indice >= 2:
                self.indice = 0
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