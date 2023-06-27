
import pygame
from config import Config
from camera import Camera
from tela import Tela

from enum import Enum

'''
Classe que coleciona 
'''

class Evento:
    pygame.init()

    def menu_inicial(keys, screen):
        # Exibo a tela de título
        screen.blit(Config.menu1_jpg, (0,0))

        # Exibo a mensagem par apressionar espaço
        pygame.draw.rect(screen, Config.CINZA, (359, 432+20, 516, 56))
        pygame.draw.rect(screen, Config.PRETO, (362, 435+20, 510, 50))
        Config.draw_text(screen, "Pressione ESPAÇO para iniciar", Config.font, Config.CINZA, 410, 450+20)

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
            Config.nomeJogador = ""
            return Tela.NOME_JOGADOR
        elif Config.botao_leaderboard.draw(screen):
            return Tela.LEADERBOARD
        elif Config.botao_sair.draw(screen):
            return Tela.SAIR
        
        return Tela.MENU_PRINCIPAL

    '''
    TODO AQUI FICA O MODO INFINITO
    '''

    def arcade(keys, screen, player, tilemap, camera, bodies, dt):
        # Caso seja pressionado a telca ESC, a tela volta ao menu
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

        # Desenha o contador de vidas
        screen.blit(Config.LIFE(player.lives), (15,10))

        #Desenha o contador de queijos
        from cheese import Cheese
        screen.blit(Config.CHEESE_COUNTER, (15, 20+Config.LIFE_HEIGTH))
        Config.draw_text(screen, f"{Cheese.many_collected}", Config.font, Config.BRANCO, 15+0.7*Config.CHEESE_WIDTH+10, 20+Config.LIFE_HEIGTH)


        if player.dead:
            # Leitura do nível do jogo utilizando a classe LevelReader
            return Tela.MORTE
        # Continuo no modo arcade
        return Tela.ARCADE
    '''
    TODO AQUI FICA O MODO ONDE TEM AS FASES
    '''
    def morte(keys, screen):
        pygame.draw.rect(screen, Config.BRANCO, (359, 432, 516, 56))
        pygame.draw.rect(screen, Config.PRETO, (362, 435, 510, 50))
        Config.draw_text(screen, "Pressione ESPAÇO para reiniciar", Config.font, Config.CINZA, 362, 435+20)

        # Caso o usuaŕio pressione espaço o programa segue para o menu principal
        if keys[pygame.K_SPACE]:
            
            return Tela.ARCADE

        return Tela.MORTE

    def campanha(keys, screen):
        pygame.draw.rect(screen, Config.BRANCO, (359, 432, 516, 56))
        pygame.draw.rect(screen, Config.PRETO, (362, 435, 510, 50))
        Config.draw_text(screen, "JANELA DE CAMPANHA", Config.font, Config.BRANCO, 410, 450)

        if Config.botao_sair.draw(screen):
            return Tela.SAIR

        return Tela.CAMPANHA
    
    
    def leaderboard(keys, screen, leaderboard):
        # Exibo o plano de fundo
        screen.blit(Config.leaderboardFUNDO_jpg, (0,0))

        # Caso seja pressionado a tecla ESC ou clicado o botão de volar na tela
        # a tela é direcionada para o menu principal
        if Config.botao_back.draw(screen):
            return Tela.MENU_PRINCIPAL
        elif keys[pygame.K_ESCAPE]:
            return Tela.MENU_PRINCIPAL
        
        leaderboard.draw(screen)

        return Tela.LEADERBOARD
    
    def inserirNome(keys, screen, charLido):
        if any(keys):
            # Caso seja pressionada a tecla ENTER com algum input escrito a tela é
            # transferida para o modo arcade
            if keys[pygame.K_RETURN] and len(Config.nomeJogador) > 0:
                return Tela.ARCADE
            # Caso seja pressionada a tecla de BACKSPACE é retirado um caratere do input
            elif keys[pygame.K_BACKSPACE] and len(Config.nomeJogador) > 0:
                Config.nomeJogador = Config.nomeJogador[:-1]
            elif charLido != '$' and len(Config.nomeJogador) < 7:
                Config.nomeJogador += charLido

        # Preencho tela de preto
        screen.fill(Config.PRETO)

        # Fazer o texto que pede para inserir o nome
        text_surface = pygame.font.Font(None, 60).render("Insira seu nome:", True, Config.BRANCO)
        screen.blit(text_surface, (340, 250))

        # Fazer a caixa de texto
        pygame.draw.rect(screen, Config.BRANCO, Config.input_box, 2)

        # Inserir dentro da caixa de texto o input do nome do jogador
        input_text = pygame.font.Font(None, 60).render(Config.nomeJogador, True, Config.BRANCO)
        screen.blit(input_text, (Config.input_box.x + 10, Config.input_box.y + 10))

        # Caso clicado o botão enter da tela o nome é lido e a tela é 
        # transferida para o modo arcade
        if Config.botao_enter.draw(screen) and len(Config.nomeJogador) > 0:
            return Tela.ARCADE
        else:
            return Tela.NOME_JOGADOR