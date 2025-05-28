import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

# Cores
VERDE = (0, 255, 127)
VERMELHO = (255, 50, 50)
AZUL = (30, 144, 255)
PRETO = (20, 20, 20)
BRANCO = (255, 255, 255)
CINZA = (40, 40, 40)
CINZA_ESCURO = (30, 30, 30)

# Tamanho da tela
LARGURA = 600
ALTURA = 600
TAMANHO_BLOCO = 20

# Fonte
fonte = pygame.font.SysFont("comicsansms", 32)
fonte_titulo = pygame.font.SysFont("comicsansms", 48, bold=True)

# Tela e relógio
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("🐍 Snake Estilizado 🐍")
relogio = pygame.time.Clock()

# Função para desenhar a cobrinha
def desenhar_cobrinha(cobrinha):
    for bloco in cobrinha:
        pygame.draw.rect(tela, VERDE, (*bloco, TAMANHO_BLOCO, TAMANHO_BLOCO), border_radius=6)

# Função para mostrar pontuação
def mostrar_pontuacao(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (10, 10))

# Função: Tela Inicial com Botão
def tela_inicial():
    while True:
        tela.fill(CINZA_ESCURO)

        titulo = fonte_titulo.render("Snake Estilizado", True, VERDE)
        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 100))

        # Botão
        botao = pygame.Rect(LARGURA // 2 - 100, ALTURA // 2 - 30, 200, 60)
        pygame.draw.rect(tela, AZUL, botao, border_radius=12)
        texto_botao = fonte.render("JOGAR", True, BRANCO)
        tela.blit(texto_botao, (botao.x + 50, botao.y + 10))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao.collidepoint(evento.pos):
                    return  # Sai da tela inicial e inicia o jogo

# Função principal do jogo
def jogo():
    x = LARGURA // 2
    y = ALTURA // 2
    dx = TAMANHO_BLOCO  # começa andando para direita
    dy = 0
    cobrinha = []
    comprimento = 3

    fruta_x = random.randrange(0, LARGURA, TAMANHO_BLOCO)
    fruta_y = random.randrange(0, ALTURA, TAMANHO_BLOCO)

    rodando = True
    pontos = 0

    while rodando:
        tela.fill(CINZA)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -TAMANHO_BLOCO
                elif evento.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, TAMANHO_BLOCO
                elif evento.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -TAMANHO_BLOCO, 0
                elif evento.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = TAMANHO_BLOCO, 0

        # Atualiza posição
        x += dx
        y += dy

        # Colisão com bordas
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            break

        # Atualiza corpo da cobrinha
        cobrinha.append((x, y))
        if len(cobrinha) > comprimento:
            del cobrinha[0]

        # Colisão com si mesma
        if len(cobrinha) != len(set(cobrinha)):
            break

        # Colisão com fruta
        if x == fruta_x and y == fruta_y:
            fruta_x = random.randrange(0, LARGURA, TAMANHO_BLOCO)
            fruta_y = random.randrange(0, ALTURA, TAMANHO_BLOCO)
            comprimento += 1
            pontos += 1

        # Desenha elementos
        pygame.draw.rect(tela, VERMELHO, (fruta_x, fruta_y, TAMANHO_BLOCO, TAMANHO_BLOCO), border_radius=8)
        desenhar_cobrinha(cobrinha)
        mostrar_pontuacao(pontos)

        pygame.display.update()

        # Ajuste de velocidade com limite máximo
        relogio.tick(min(6 + pontos // 3, 20))

    # Tela de Game Over
    tela.fill(PRETO)
    texto_game_over = fonte.render("Game Over!", True, BRANCO)
    tela.blit(texto_game_over, (LARGURA // 2 - texto_game_over.get_width() // 2, ALTURA // 2 - 20))
    pygame.display.update()

    pygame.time.delay(1000)  # Delay para o jogador ver o "Game Over"

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                esperando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    esperando = False
                elif evento.key == pygame.K_r:
                    jogo()
                    return
    pygame.quit()
    sys.exit()

# Início do programa
if __name__ == "__main__":
    tela_inicial()
    jogo()
