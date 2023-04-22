import pygame
from windowManager import WindowManager
     
class DoubleChainList():
    def __init__(self):
        self.wm = WindowManager()
        self.id = "Double chain list"
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
        self.wm.blit_screen()
        self.flag_input = None
    
    def show_display(self):
        while True:
            self.wm.check_events()
            self.flag_input = self.check_input()
            if self.flag_input != None:
                return self.flag_input
            self.wm.display.fill(self.wm.WHITE)
            self.wm.blit_screen()
            self.wm.reset_keys()
            
    def check_input(self):
        if self.wm.MOUSE1:
            mouse_position = pygame.mouse.get_pos() 
        
        elif self.wm.BACK_KEY:
            return -1