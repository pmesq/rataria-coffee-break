import pygame
import heapq
from config import Config
from evento import Evento

class Leaderboard():
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

	def imprimir(self):
		listaTop5 = self.lisaTop5Jogadore()
		for chave, valor in listaTop5:
			print(f"{chave} {valor}")

	def lisaTop5Jogadore(self):
		listaTop5 = heapq.nlargest(5, self.listaRecordes.items(), key=lambda item: item[1])
		return listaTop5
		

	def adicionarJogador(self, nomeJogador, ponutacaoJogador):
		if nomeJogador not in self.listaRecordes:
			self.listaRecordes[nomeJogador] = int(ponutacaoJogador)
		else:
			self.listaRecordes[nomeJogador] = max(int(self.listaRecordes[nomeJogador]), int(ponutacaoJogador))

	def gravar(self, endrecoArquivo):
		listaTop5 = self.lisaTop5Jogadore()
		with open(endrecoArquivo, 'w') as File:
			for nomeJogador, pontosJogador in listaTop5:
				File.write(nomeJogador+";"+str(pontosJogador)+"\n")
			File.write("FIM")
			File.close()
			pass
	
	def draw(self, screen):
		lista = self.lisaTop5Jogadore()
		idx = 1

		for nomeJogador, pontosJogador in lista:
			Evento.draw_text(screen, str(idx)+"."+nomeJogador, Config.font2, Config.COR_FONTE, 245, 120+80*idx)
			Evento.draw_text(screen, str(pontosJogador), Config.font2, Config.COR_FONTE2, 235+600, 120+80*idx)
			idx += 1

