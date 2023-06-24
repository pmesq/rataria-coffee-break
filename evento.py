
import pygame
from config import Config
from camera import Camera
from tela import Tela

from enum import Enum

class Evento:
    pygame.init()

    def draw_text(screen, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def menu_inicial(keys, screen):
        # Exibo a tela de título
        screen.blit(Config.menu1_jpg, (0,0))

        # Exibo a mensagem par apressionar espaço
        pygame.draw.rect(screen, Config.COR_FONTE, (359, 432, 516, 56))
        pygame.draw.rect(screen, Config.COR_FUNDO_TEXTO, (362, 435, 510, 50))
        Evento.draw_text(screen, "Pressione ESPAÇO para iniciar", Config.font, Config.COR_FONTE, 410, 450)

        # Caso o usuaŕio pressione espaço o programa segue para o menu principal
        if keys[pygame.K_SPACE]:
            return Tela.MENU_PRINCIPAL

        return Tela.MENU_INICIAL

    def menu_principal(keys, screen):
        # Exibo o plano de fundo
        screen.blit(Config.menu2_jpg, (0,0))

        # Botões exibidos na tela
        if Config.botao_campanha.draw(screen):
            return Tela.CAMPANHA
        elif Config.botao_arcade.draw(screen):
            return Tela.ARCADE
        elif Config.botao_leaderboard.draw(screen):
            return Tela.LEADERBOARD
        elif Config.botao_sair.draw(screen):
            return Tela.SAIR
        
        return Tela.MENU_PRINCIPAL

    def arcade(keys, screen, player, tilemap, camera, bodies, dt):
        # Caso seja pressionado a telca ESC, eu troco para o modo do menu 
        if keys[pygame.K_ESCAPE]:
            return Tela.MENU_PRINCIPAL

        # Captura do input do jogador
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
        screen.blit(Config.LIFE(player.lives), (15,10))

        # Continuo no modo arcade
        return Tela.ARCADE

    def campanha(keys, screen):
        pygame.draw.rect(screen, Config.COR_FONTE, (359, 432, 516, 56))
        pygame.draw.rect(screen, Config.COR_FUNDO_TEXTO, (362, 435, 510, 50))
        Evento.draw_text(screen, "JADELA DE CAMPANHA", Config.font, Config.COR_FONTE, 410, 450)

        if Config.botao_sair.draw(screen):
            return Tela.SAIR

        return Tela.CAMPANHA
    
    
    def leaderboard(keys, screen, leaderboard):
        # Exibo o plano de fundo
        screen.blit(Config.leaderboardFUNDO_jpg, (0,0))

        if Config.botao_back.draw(screen):
            return Tela.MENU_PRINCIPAL
        
        leaderboard.draw(screen)

        return Tela.LEADERBOARD