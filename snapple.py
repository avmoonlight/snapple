import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

VERDE = (0, 255, 127)
VERMELHO = (255, 50, 50)
AZUL = (30, 144, 255)
PRETO = (20, 20, 20)
BRANCO = (255, 255, 255)
CINZA = (40, 40, 40)
CINZA_ESCURO = (30, 30, 30)

LARGURA = 600
ALTURA = 600
TAMANHO_BLOCO = 20

fonte = pygame.font.SysFont("comicsansms", 32)
fonte_titulo = pygame.font.SysFont("comicsansms", 48, bold=True)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snapple")
relogio = pygame.time.Clock()

def desenhar_cobrinha(cobrinha):
    for bloco in cobrinha:
        pygame.draw.rect(tela, VERDE, (*bloco, TAMANHO_BLOCO, TAMANHO_BLOCO), border_radius=6)

def mostrar_pontuacao(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (10, 10))