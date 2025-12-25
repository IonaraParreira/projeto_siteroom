import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Caça à Mosca")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Variáveis da Mosca
fly_x = SCREEN_WIDTH // 2
fly_y = SCREEN_HEIGHT // 2
fly_speed = 5
fly_radius = 15
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
            if dist < fly_radius + 10: # Se o clique foi perto o suficiente
                is_alive = False # A mosca para de se mexer!

    # Só se move se estiver viva
    if is_alive:
        fly_y += fly_speed
        if fly_y <= 20 or fly_y >= SCREEN_HEIGHT - 20:
            fly_speed *= -1

    # DESENHO
    screen.fill(WHITE)
    
    # Desenha as asas (se estiver viva)
    if is_alive:
        pygame.draw.ellipse(screen, GRAY, (fly_x - 25, fly_y - 10, 20, 15)) # Asa esquerda
        pygame.draw.ellipse(screen, GRAY, (fly_x + 5, fly_y - 10, 20, 15))  # Asa direita
    
    # Desenha o corpo (Círculo central)
    pygame.draw.circle(screen, BLACK, (int(fly_x), int(fly_y)), fly_radius)
    
    # Desenha a cabeça
    pygame.draw.circle(screen, BLACK, (int(fly_x), int(fly_y - 10 if fly_speed < 0 else fly_y + 10)), 8)

    pygame.display.flip()
    clock.tick(60)