import pygame
from windowManager import WindowManager



class Seqlist():
    def __init__(self):
        self.wm = WindowManager()
        self.id = "Sequential list"
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
        self.wm.blit_screen()
        self.flag_input = None
        
    def show_display(self):
        
        font_text = pygame.font.Font(None, 32)
        user_text = ''
    
        while True:
            self.wm.check_events()
            
            if self.wm.BACK_KEY:           #if ESC is pressed
                return 1 
            elif self.wm.quit == True:      #if QUIT is pressed
                return -1
            
            elif self.wm.MOUSE1 == True:          #if the mouse is pressed
                #mouse_position = pygame.mouse.get_pos()
                
                while True: 
                    for event in pygame.event.get():
                        
                        if event.type == pygame.KEYDOWN:    #if the keyboard is pressed
                            
                            if event.type == pygame.K_BACKSPACE: #the button to erase a letter
                                print("entered here")
                                user_text = user_text[:-1]
                                
                            else:                           #any other button is added
                                user_text += event.unicode
                            
                    self.wm.window.fill(self.wm.BLACK)
                    text_surface = font_text.render(user_text, True, self.wm.WHITE)
                    self.wm.window.blit(text_surface, (0,0))
                    pygame.display.flip()
    
            
            
    # def show_display(self):
        
    #     color_inactive = pygame.Color('gray15')
    #     self.wm.display.fill(self.wm.BLACK)
    #     self.wm.draw_text("LISTA SEQUENCIAL", 14, self.mid_w, self.mid_h/2)
    #     self.wm.blit_screen()
        
    #     while True:
    #         self.input_rect = pygame.Rect(200, 200, 140, 32)
    #         pygame.draw.rect(self.wm.window, color_inactive, self.input_rect, 2)    #draw the retangle of the text box
            
    #         self.wm.display.blit(self.wm.display, self.input_rect)
            
    #         self.wm.check_events()
    #         self.flag_input = self.check_input()
    #         if self.flag_input != None:
    #             return self.flag_input
        
    #         self.wm.blit_screen()
            
    # def check_input(self):
        
    #     if self.wm.MOUSE1:
    #         mouse_position = pygame.mouse.get_pos()
    #         if self.input_rect.collidepoint(mouse_position):
    #             self.wm.check_text()

    #     elif self.wm.BACK_KEY:
    #         return 1
    #     elif self.wm.quit == True:
    #         return -1