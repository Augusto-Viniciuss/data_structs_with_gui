import pygame
from windowManager import WindowManager



class SequentialList():
    def __init__(self):
        self.wm = WindowManager()
        self.id = "Sequential list"
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
        self.wm.blit_screen()
        self.flag_input = None
        
    def show_display(self):
        
        inputbox_fake = self.wm.draw_inputbox(self.mid_w, self.mid_h, self.wm.GRAY) #getting the dimensions of the first input box
        self.wm.blit_screen()       #updating the screen
        
        return_function = self.wm.logic_inputbox(inputbox_fake)
        
        if return_function == 1 or return_function == -1:
            return -1     
    
        
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
            
    # 