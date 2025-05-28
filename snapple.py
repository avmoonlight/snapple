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
