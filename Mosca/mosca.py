import pygame
import sys
import asyncio #Necessário para rodar na web com Pygbag

async def main(): #Função principal assíncrona para compatibilidade web
    pygame.init()
    pygame.mixer.init() #Inicializa o sistema de som

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Caça à Mosca - don't let it escape")

# Carregamento de Assets
    try:
        fly_image = pygame.image.load("Mosca/mosca.png").convert_alpha()
    #Redimensiona para um tamanho legal para o jogo
        fly_image = pygame.transform.scale(fly_image, (80,60))

    #Carregando o som da mosca
        fly_sound = pygame.mixer.Sound("Mosca/mosca.mp3")
    #Inicia o som em loop (-1 sgnifica repetição infinita)
        fly_sound.play(loops=-1)

    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        return 

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
                return
        
        # LÓGICA DO CLIQUE: Se clicar com o mouse...
            if event.type == pygame.MOUSEBUTTONDOWN and is_alive:
                mouse_pos = pygame.mouse.get_pos()
            # Calcula a distância entre o mouse e a mosca
                dist = ((mouse_pos[0] - fly_x)**2 + (mouse_pos[1] - fly_y)**2)**0.5
                if dist < fly_radius: 
                    is_alive = False # A mosca para de se mexer!
                    fly_sound.stop() #Silencia a mosca ao pegá-la
    # Só se move se estiver viva
        if is_alive:
            fly_y += fly_speed
            if fly_y <= 30 or fly_y >= SCREEN_HEIGHT - 30:
                fly_speed *= -1

        # DESENHO
        screen.fill((0, 0, 0))
    
        if is_alive:
        #Desenha a imagem mosca.png centralizada
            screen.blit(fly_image, (fly_x - 40, fly_y - 30))
        
        else:
            font = pygame.font.Font("Mosca/SpecialElite-Regular.ttf",30)
            frases = [
            "Você pegou.", 
            "Na mosca!",
            "'Homem que pega mosca com palitinhos,",
            "realiza qualquer coisa.'",
            " - Sr. Miyagi"
        ]

        #Cor Verde Harcker(0,255,0)
            pos_y = SCREEN_HEIGHT // 2 - 40
            for linha in frases:
                img_texto = font.render(linha,True,(0,255,0))
                screen.blit(img_texto,(50, pos_y))
                pos_y += 40 #isso faz "pular" a linha para baixo
        pygame.display.update()
        await asyncio.sleep(0) #Necessário para o navegador não travar
        clock.tick(60)

#Para rodar localmente ou na web
asyncio.run(main())