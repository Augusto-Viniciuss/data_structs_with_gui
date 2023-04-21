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
        
        color_inactive = pygame.Color('gray15')
        
        while True:
            
            self.wm.display.fill(self.wm.BLACK)
            self.wm.draw_text("LISTA SEQUENCIAL", 14, self.mid_w, 30)
            self.input_rect = pygame.Rect(200, 200, 140, 32)
            pygame.draw.rect(self.wm.window, color_inactive, self.input_rect, 2)    #draw the retangle of the text box
            self.wm.display.blit(self.wm.window, self.input_rect)
            self.wm.blit_screen()
            
            self.wm.check_events()
            self.flag_input = self.check_input()
            if self.flag_input != None:
                return self.flag_input
            
            #self.wm.add_img("imgs/b1.png", self.mid_w, self.mid_h)
            self.wm.blit_screen()
            
    def check_input(self):
        
        if self.wm.MOUSE1:
            mouse_position = pygame.mouse.get_pos()
            if self.input_rect.collidepoint(mouse_position):
                self.wm.check_text()

        elif self.wm.BACK_KEY:
            return 1
        elif self.wm.quit == True:
            return -1