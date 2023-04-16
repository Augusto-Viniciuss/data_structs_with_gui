import pygame

pygame.init()

#some parameters being defined 
screen_width = 800
screen_height = 600
button_width = 200
button_height = 50
button_spacing = 65     
BLACK = (0,0,0)
WHITE = (255,255,255)

#creating and defining the main window
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(BLACK)        


#image of the main title
image = pygame.image.load('imgs/ed2.png')
position_x = 0
position_y = 0
screen.blit(image, (position_x, position_y))
pygame.display.update()

#defining the buttons using image
button1 = pygame.image.load("imgs/b1.png")
button1_rect = button1.get_rect()
button1_rect.center = (screen_width // 2, screen_height/2)
screen.blit(button1, button1_rect)

button2 = pygame.image.load("imgs/b2.png")
button2_rect = button2.get_rect()
button2_rect.center = (screen_width // 2, screen_height/2 + button_spacing)
screen.blit(button2, button2_rect)

button3 = pygame.image.load("imgs/b3.png")
button3_rect = button3.get_rect()
button3_rect.center = (screen_width // 2, screen_height/2 + (button_spacing*2))
screen.blit(button3, button3_rect)

button4 = pygame.image.load("imgs/b4.png")
button4_rect = button4.get_rect()
button4_rect.center = (screen_width // 2, screen_height/2 + (button_spacing*3))
screen.blit(button4, button4_rect)

button_color = (61, 89, 171)
button_1 = pygame.Rect(screen_width/2 - button_width/2, screen_height/10*5, button_width, button_height)


screen_flag = "main"           #this flag indicates in which window the user is placed

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if screen_flag == "main":
                if button1_rect.collidepoint(event.pos):
                    screen.fill(BLACK)
                    screen_flag = "lista sequencial"
                    pygame.display.update()
                
                if button2_rect.collidepoint(event.pos):
                    screen.fill(BLACK)
                    screen_flag = "second button"
                    pygame.display.update()
                    
                if button3_rect.collidepoint(event.pos):
                    screen.fill(BLACK)
                    screen_flag = "third button"
                    pygame.display.update()
                
                if button4_rect.collidepoint(event.pos):
                    running = False
                    pygame.display.update()
            
        elif screen_flag == "lista sequencial":    
                
            font = pygame.font.SysFont('Courier New', 24)             #just to fill the window (must be removed)
            text_surface = font.render('Lista Sequencial', True, (255, 255, 255))
            screen.blit(text_surface, (300, 100))
            pygame.draw.rect(screen, button_color, button_1)
            pygame.display.flip()

            # elif screen_flag == "second button":
            #     font = pygame.font.SysFont('impact', 17)            #just to fill the window (must be removed)
            #     text_surface = font.render('essa eh a seconda janela', True, (255, 255, 255))
            #     screen.blit(text_surface, (100, 100))
            #     pygame.display.flip()

            # elif screen_flag == "third button":
            #     font = pygame.font.SysFont('impact', 17)            #just to fill the window (must be removed)
            #     text_surface = font.render('essa eh a third janela', True, (255, 255, 255))
            #     screen.blit(text_surface, (100, 100))
            #     pygame.display.flip()

            
        if event.type == pygame.QUIT:    #if the user press the "x"
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