import pygame
import heapq
from config import Config
from evento import Evento

'''
Classe com um dicionário no qual sua chave é o nome do jogador e seu 
valor associado é o máximo de pontos que tal jogador atingiu em uma
partida
'''

class Leaderboard():
	# Em seu constructor, eu extraio o leaderboard salvo localmente em um arquivo txt,
	# que em um jogo novo começa vazio
	def __init__(self, endrecoArquivo):
		self.listaRecordes = {}

		with open(endrecoArquivo, 'r') as file:
			linhas = file.read()
			linhas = linhas.split('\n')
			for linha in linhas:
				if(linha != "FIM"):
					linha_dividida = linha.split(";")
					self.adicionarJogador(linha_dividida[0], int(linha_dividida[1]))
			file.close()
			pass

	# Retorna uma lista com os cinco melhores jogadores e seus pontos máximos
	def lisaTop5Jogadore(self):
		listaTop5 = heapq.nlargest(5, self.listaRecordes.items(), key=lambda item: item[1])
		return listaTop5

	# Adiciona um jogador no leaderboard, com seu nome e ponto em determinada
	def adicionarJogador(self, nomeJogador, ponutacaoJogador):
		if nomeJogador not in self.listaRecordes:
			self.listaRecordes[nomeJogador] = int(ponutacaoJogador)
		else:
			self.listaRecordes[nomeJogador] = max(int(self.listaRecordes[nomeJogador]), int(ponutacaoJogador))

	# Registra em um arquivo txt os cinco melhores jogadores do leaderboard
	def gravar(self, endrecoArquivo):
		listaTop5 = self.lisaTop5Jogadore()

		with open(endrecoArquivo, 'w') as File:
			for nomeJogador, pontosJogador in listaTop5:
				File.write(nomeJogador+";"+str(pontosJogador)+"\n")
			File.write("FIM")
			File.close()
			pass

	# Desenha na tela o placar do leaderboard
	def draw(self, screen):
		# Pego os cinco melhores jogadores registrados 
		lista = self.lisaTop5Jogadore()
		idx = 1

		for nomeJogador, pontosJogador in lista:
			# Desenho cada linha seperadamente
			Evento.Config(screen, str(idx)+"."+nomeJogador, Config.font2, Config.BRANCO, 245, 120+80*idx)
			Evento.Config(screen, str(pontosJogador), Config.font2, Config.AMARELO, 235+600, 120+80*idx)
			idx += 1

	'''
	def imprimir(self):
		listaTop5 = self.lisaTop5Jogadore()
		for chave, valor in listaTop5:
			print(f"{chave} {valor}")
	'''