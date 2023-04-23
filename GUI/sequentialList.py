import pygame
from windowManager import WindowManager
from inputBox import InputBox



class SequentialList():
    def __init__(self):
        self.wm = WindowManager()
        self.box_x, self.box_y = 150, 200      #need to define as parameter the x and y of the firstbox
        self.spacing = 100
        self.id = "Sequential list"
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
        self.wm.blit_screen()
        self.flag_input = None
        self.input_box1= InputBox(self.box_x, self.box_y)
        self.input_box2 = InputBox(self.box_x, self.box_y+75)
        self.input_box3 = InputBox(self.box_x*3, self.box_y)
        self.input_box4 = InputBox(self.box_x*3, self.box_y+75)
        self.input_box5 = InputBox(self.box_x*4, self.box_y)
        self.input_box6 = InputBox(self.box_x*4, self.box_y+75)
        
    def show_display(self):
        
        font_name = pygame.font.get_default_font()
        font = pygame.font.Font(font_name, 15)
        
        running = True
        while running: 
            
            self.flag_input = self.check_input()
            if self.flag_input != None: 
                return self.flag_input

            self.wm.window.fill(self.wm.BLACK)
            text_surface = font.render("posição:", True, self.wm.PURPLE)
            self.wm.window.blit(text_surface, (self.box_x-self.spacing, self.box_y+5))  #in the left of the firstbox
            
            text_surface = font.render("o elemento:", True, self.wm.PURPLE)
            self.wm.window.blit(text_surface, (self.box_x-self.spacing, self.box_y+75+5))  #in the left of the second box

            text_surface = font.render("INSERÇÃO", True, self.wm.PURPLE)       #in the top of first column
            self.wm.window.blit(text_surface, (self.box_x+15, self.box_y-30))  
            self.input_box1.draw(self.wm.window)
            self.input_box2.draw(self.wm.window)
            
            
            text_surface = font.render("por posição:", True, self.wm.PURPLE)
            self.wm.window.blit(text_surface, (self.box_x*3-self.spacing, self.box_y+5))  #in the left of the firstbox
            text_surface = font.render("por elemento:", True, self.wm.PURPLE)
            self.wm.window.blit(text_surface, (self.box_x*3-self.spacing-10, self.box_y+75+5))  #in the left of the second box
            
            text_surface = font.render("REMOÇÃO", True, self.wm.PURPLE)
            self.wm.window.blit(text_surface, (self.box_x*3+15, self.box_y-30))  #in the top of second column
            self.input_box3.draw(self.wm.window)
            self.input_box4.draw(self.wm.window)
            
            text_surface = font.render("BUSCA", True, self.wm.PURPLE)
            self.wm.window.blit(text_surface, (self.box_x*4+30, self.box_y-30))  #in the top of third column
            self.input_box5.draw(self.wm.window)
            self.input_box6.draw(self.wm.window)
            pygame.display.flip()   
        
    def check_input(self):
        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return -1
            
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    return 1
                    
            self.input_box1.handle_event(event)
            self.input_box2.handle_event(event)
            self.input_box3.handle_event(event)
            self.input_box4.handle_event(event)
            self.input_box5.handle_event(event)
            self.input_box6.handle_event(event)
            
            