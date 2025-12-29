import pygame
import sys
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Caça à Mosca - don't let it escape")

# Cores
WHITE = (255, 255, 255)

try:
    fly_image = pygame.image.load("mosca.png").convert_alpha()
    #Redimensiona para um tamanho legal para o jogo
    fly_image = pygame.transform.scale(fly_image,(80,60))
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
    pygame.quit()
    sys.exit()

# Variáveis da Mosca
fly_x = SCREEN_WIDTH // 2
fly_y = SCREEN_HEIGHT // 2
fly_speed = 5
fly_radius = 30
is_alive = True  # Nova variável para saber se ela está voando

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # LÓGICA DO CLIQUE: Se clicar com o mouse...
        if event.type == pygame.MOUSEBUTTONDOWN and is_alive:
            mouse_pos = pygame.mouse.get_pos()
            # Calcula a distância entre o mouse e a mosca
            dist = ((mouse_pos[0] - fly_x)**2 + (mouse_pos[1] - fly_y)**2)**0.5
            if dist < fly_radius: 
                is_alive = False # A mosca para de se mexer!

    # Só se move se estiver viva
    if is_alive:
        fly_y += fly_speed
        if fly_y <= 30 or fly_y >= SCREEN_HEIGHT - 30:
            fly_speed *= -1

    # DESENHO
    screen.fill(WHITE)
    
    if is_alive:
        #Desenha a imagem mosca.png centralizada
        screen.blit(fly_image, (fly_x - 40, fly_y - 30))

    else:
        font = pygame.font.SysFont(None, 48)
        img_texto = font.render('Você pegou a mosca!',True, (0,150,0))
        screen.blit(img_texto,(200, SCREEN_HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)
