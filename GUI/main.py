import pygame

pygame.init()

screen_width = 800
screen_height = 600

button_width = 200
button_height = 50


#Criando e definindo o tamanho da janela principal
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((0,0,0))        #definindo a cor como branco


#Colocando a imagem titulo
image = pygame.image.load('img/ed2.png')
position_x = 0
position_y = 0
screen.blit(image, (position_x, position_y))
pygame.display.update()

#definindo os botoes por imagem
button1 = pygame.image.load("img/b1.png")
button1_rect = button1.get_rect()
button1_rect.center = (screen_width // 2, 300)
screen.blit(button1, button1_rect)

# button2 = pygame.image.load("img/b2.png")
# button2_rect = button2.get_rect()
# button2_rect.center = (screen_width // 2, 365)
# screen.blit(button2, button2_rect)

# button3 = pygame.image.load("img/b3.png")
# button3_rect = button3.get_rect()
# button3_rect.center = (screen_width // 2, 500)
# screen.blit(button3, button3_rect)

# button4 = pygame.image.load("img/b4.png")
# button4_rect = button4.get_rect()
# button4_rect.center = (screen_width // 2, screen_height // 2 + 210)
# screen.blit(button4, button4_rect)


screen_flag = "main"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if screen_flag == "main":
                if button1_rect.collidepoint(event.pos):
                    screen.fill((0,0,0))
                    screen_flag = "first button"
                    pygame.display.update()
                
                # if button_2.collidepoint(event.pos):
                #     screen.fill((0,0,0))
                #     screen_flag = "second button"
                #     pygame.display.update()
                    
                # if button_3.collidepoint(event.pos):
                #     screen.fill((0,0,0))
                #     screen_flag = "third button"
                #     pygame.display.update()
                
                # if button_4.collidepoint(event.pos):
                #     running = False
                #     pygame.display.update()
                
        elif screen_flag == "first button":                    
            font = pygame.font.SysFont('impact', 17)
            text_surface = font.render('essa eh a primeira janela', True, (255, 255, 255))
            screen.blit(text_surface, (100, 100))
            pygame.display.flip()

        elif screen_flag == "second button":
            font = pygame.font.SysFont('impact', 17)
            text_surface = font.render('essa eh a seconda janela', True, (255, 255, 255))
            screen.blit(text_surface, (100, 100))
            pygame.display.flip()

        elif screen_flag == "third button":
            font = pygame.font.SysFont('impact', 17)
            text_surface = font.render('essa eh a third janela', True, (255, 255, 255))
            screen.blit(text_surface, (100, 100))
            pygame.display.flip()

        
        if event.type == pygame.QUIT:    #se o usuario apertar o "x"
            running = False
        
        pygame.display.update()
            
pygame.quit()


#pieces that could be useful on the code

#Define the rectangle
# button_1 = pygame.Rect(screen_width/2 - button_width/2, screen_height/10*5, button_width, button_height)
# button_2 = pygame.Rect(screen_width/2 - button_width/2, screen_height/10*6, button_width, button_height)
# button_3 = pygame.Rect(screen_width/2 - button_width/2, screen_height/10*7, button_width, button_height)
# button_4 = pygame.Rect(screen_width/2 - button_width/2, screen_height/10*8, button_width, button_height)

# button_color = (61, 89, 171)
# pygame.draw.rect(screen, button_color, button_1)
# pygame.draw.rect(screen, button_color, button_2)
# pygame.draw.rect(screen, button_color, button_3)
# pygame.draw.rect(screen, button_color, button_4)

#Adding text to the buttons
# font = pygame.font.SysFont('impact', 17)
# text_surface = font.render('LISTA SEQUENCIAL', True, (255, 255, 255))
# screen.blit(text_surface, (screen_width/2 - button_width/2 + 30, screen_height/10*5 + 15))
# text_surface = font.render('LISTA SIMPLESMENTE ', True, (255, 255, 255))
# screen.blit(text_surface, (screen_width/2 - button_width/2 + 20, screen_height/10*6 + 5))
# text_surface = font.render('ENCADEADA', True, (255, 255, 255))
# screen.blit(text_surface, (screen_width/2 - button_width/2 + 30, screen_height/10*6+20 + 5))
# text_surface = font.render('LISTA DUPLAMENTE ', True, (255, 255, 255))
# screen.blit(text_surface, (screen_width/2 - button_width/2 + 20, screen_height/10*7 + 5))
# text_surface = font.render('ENCADEADA', True, (255, 255, 255))
# screen.blit(text_surface, (screen_width/2 - button_width/2 + 20, screen_height/10*7+20 + 5))
# text_surface = font.render('SAIR', True, (255, 0, 0))
# screen.blit(text_surface, (screen_width/2 - button_width/2 + 20, screen_height/10*8 + 5))
# pygame.display.flip()