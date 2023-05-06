import pygame
from windowManager import WindowManager
from inputBox import InputBox
from utils.Sequential_list import Sequential_list


class Stack_():
    def __init__(self):
        self.wm = WindowManager()
        self.wm.blit_screen()
        self.id = "Stack"
        self.flag_input = None
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
    
    def show_display(self):
        
        running = True
        while running: 
            self.flag_input = self.check_input()

            if self.flag_input == "menu" or self.flag_input == "quit": 
                return self.flag_input
            
            self.wm.display.fill(self.wm.BLACK)
            self.wm.blit_screen()
    

    def check_input(self):
        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return "quit"
            
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    return "menu"
                    
   