import pygame
from windowManager import WindowManager
from inputBox import InputBox



class SequentialList():
    def __init__(self):
        self.wm = WindowManager()
        self.id = "Sequential list"
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
        self.wm.blit_screen()
        self.flag_input = None
        self.input_box = InputBox(100, 100, 140, 32)
        self.input_box2 = InputBox(100, 300, 140, 32)
        
    def show_display(self):
        running = True
        while running: 
            
            self.flag_input = self.check_input()
            if self.flag_input != None: 
                return self.flag_input

            self.wm.window.fill(self.wm.WHITE)
            self.input_box.draw(self.wm.window)
            self.input_box2.draw(self.wm.window)
            pygame.display.flip()   
        
    def check_input(self):
        
        for event in pygame.event.get():    
            
            if event.type == pygame.QUIT:
                return -1
            
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    return 1
                    
            self.input_box.handle_event(event)
            self.input_box2.handle_event(event)