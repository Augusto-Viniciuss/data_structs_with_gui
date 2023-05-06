import pygame
from windowManager import WindowManager
from inputBox import InputBox


class Tree_():
    def __init__(self):
        self.wm = WindowManager()
        self.wm.blit_screen()
        self.flag_input = None
    
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
                    
   