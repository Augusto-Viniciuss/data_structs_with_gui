import pygame

pygame.init()

screen_width = 800
screen_height = 600

button_width = 200
button_height = 50


#Criando e definindo o tamanho da janela principal
screen = pygame.display.set_mode((800, 600))
screen.fill((0,0,0))


#Define the rectangle
button_1 = pygame.Rect(screen_width/2 - button_width/2, screen_height/10*5, button_width, button_height)
button_2 = pygame.Rect(screen_width/2 - button_width/2, screen_height/10*6, button_width, button_height)
button_3 = pygame.Rect(screen_width/2 - button_width/2, screen_height/10*7, button_width, button_height)
button_4 = pygame.Rect(screen_width/2 - button_width/2, screen_height/10*8, button_width, button_height)

button_color = (61, 89, 171)
pygame.draw.rect(screen, button_color, button_1)
pygame.draw.rect(screen, button_color, button_2)
pygame.draw.rect(screen, button_color, button_3)
pygame.draw.rect(screen, button_color, button_4)

#Criando texto
# font = pygame.font.SysFont('Arial', 36)
# text_surface = font.render('Estruturas de dados', True, (255, 255, 255))
# screen.blit(text_surface, (screen_width/2 - 150, 150))

#Colocando a imagem titulo
image = pygame.image.load('img/ed.png')
position_x = 0
position_y = 0
screen.blit(image, (position_x, position_y))
pygame.display.update()

#Adding text to the buttons
font = pygame.font.SysFont('freesans', 17)
text_surface = font.render('Lista Sequencial', True, (255, 255, 255))
screen.blit(text_surface, (screen_width/2 - button_width/2 + 30, screen_height/10*5 + 15))

text_surface = font.render('Lista Simplesmente ', True, (255, 255, 255))
screen.blit(text_surface, (screen_width/2 - button_width/2 + 20, screen_height/10*6 + 5))
text_surface = font.render('Encadeada', True, (255, 255, 255))
screen.blit(text_surface, (screen_width/2 - button_width/2 + 30, screen_height/10*6+20 + 5))
text_surface = font.render('Lista Duplamente ', True, (255, 255, 255))
screen.blit(text_surface, (screen_width/2 - button_width/2 + 20, screen_height/10*7 + 5))
text_surface = font.render('Encadeada', True, (255, 255, 255))
screen.blit(text_surface, (screen_width/2 - button_width/2 + 20, screen_height/10*7+20 + 5))
text_surface = font.render('Sair', True, (255, 0, 0))
screen.blit(text_surface, (screen_width/2 - button_width/2 + 20, screen_height/10*8 + 5))
pygame.display.flip()

screen_flag = "main"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if screen_flag == "main":
                if button_1.collidepoint(event.pos):
                    # código que atualiza a tela aqui
                    screen.fill((255,0,0))
                    screen_flag = "first button"
                    pygame.display.update()
                
                if button_2.collidepoint(event.pos):
                    # código que atualiza a tela aqui
                    screen.fill((0,255,0))
                    screen_flag = "second button"
                    pygame.display.update()
                    
                if button_3.collidepoint(event.pos):
                    # código que atualiza a tela aqui
                    screen.fill((0,0,255))
                    screen_flag = "third button"
                    pygame.display.update()
                
                if button_4.collidepoint(event.pos):
                    # código que atualiza a tela aqui
                    running = False
                    pygame.display.update()
                
            elif screen_flag == "first button":
                print("ok")

            elif screen_flag == "second button":
                print("ok")

            elif screen_flag == "third button":
                print("ok")

        
        if event.type == pygame.QUIT:
            running = False
        
        pygame.display.update()
            
pygame.quit()

#just see if             
    