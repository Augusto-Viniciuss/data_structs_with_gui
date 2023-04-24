import pygame
from windowManager import WindowManager
from inputBox import InputBox
from Sequential_list import Sequential_list



class SequentialList():
    def __init__(self):
        self.wm = WindowManager()
        self.list = Sequential_list()
        self.box_x, self.box_y = 170, 420      #need to define as parameter the x and y of the firstbox
        self.spacing = 75
        self.id = "Sequential list"
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
        self.wm.blit_screen()
        self.flag_input = None
        self.input_box1 = InputBox(self.box_x, self.box_y+50)       #box inserir-elemento
        self.input_box2= InputBox(self.box_x, self.box_y)          
        self.input_box3 = InputBox(self.box_x*2+30, self.box_y)     
        self.input_box4 = InputBox(self.box_x*3+60, self.box_y)
        self.input_box5 = InputBox(self.box_x*3+60, self.box_y+50)
        self.error_add, self.error_remove, self.error_search = False, False, False
        self.square_w,self.square_h = -20, 200
        self.square_side, self.square_border = 70, 2
        self.square_number_w, self.square_number_h= self.square_w+self.square_side/2, self.square_h+self.square_side/2 
        
    def show_display(self):
        
        running = True
        while running: 
            self.flag_input = self.check_input()
            if self.flag_input != None: 
                return self.flag_input

            self.wm.display.fill(self.wm.BLACK)
            
            self.wm.add_img("imgs/ls.png", 400, 70)     #title
            self.wm.add_img("imgs/inserir.png", self.box_x+55, self.box_y-30)  #in the top of first column
            self.wm.add_img("imgs/remover.png", self.box_x*2+85, self.box_y-30)  #in the top of second column
            self.wm.add_img("imgs/buscar.png", self.box_x*3+115, self.box_y-30)  #in the top of third column
            
            self.wm.add_img("imgs/posicao.png", self.box_x-self.spacing, self.box_y+15)  #in the left of first line
            self.wm.add_img("imgs/elemento.png", self.box_x-self.spacing, self.box_y+50+15)  #in the left of second line
            
        
            
            if self.error_add:
                self.wm.draw_text("ERROR", 18, self.box_x+55, self.box_y-55, self.wm.RED)
            if self.error_remove:
                self.wm.draw_text("ERROR", 18, self.box_x*2+85, self.box_y-55, self.wm.RED)
            if self.error_search:
                self.wm.draw_text("ERROR", 18, self.box_x*3+115, self.box_y-55, self.wm.RED)

            self.wm.add_img("imgs/enviar.png", self.box_x+55, self.box_y+self.spacing+40)
            self.wm.add_img("imgs/enviar.png", self.box_x*2+85, self.box_y+self.spacing+40)
            self.wm.add_img("imgs/enviar.png", self.box_x*3+115, self.box_y+self.spacing+40)

            self.input_box1.draw(self.wm.display)
            self.input_box2.draw(self.wm.display)
            self.input_box3.draw(self.wm.display)
            self.input_box4.draw(self.wm.display)
            self.input_box5.draw(self.wm.display)
            
            for i in range(10):
                if self.list.get_element(i+1) == None:
                    element = ''
                else:
                    element = str(self.list.get_element(i+1))
                self.wm.draw_rect(self.square_w+(i+1)*self.square_side+self.square_border , self.square_h, self.square_side, self.square_side, self.wm.WHITE, self.square_border)
                self.wm.draw_text(element, 30, self.square_number_w+(i+1)*self.square_side+self.square_border , self.square_number_h, self.wm.PURPLE)
            
            self.wm.blit_screen()
        
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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos() 
                if self.wm.collide_point("imgs/enviar.png",self.box_x+55, self.box_y+self.spacing+40, mouse_position):
                    if self.input_box1.text != '' and self.input_box2.text != '':
                        if self.list.insert(int(self.input_box1.text), int(self.input_box2.text)) == False:
                            self.error_add = True
                        else:
                            self.error_add = False
                    elif self.input_box1.text == '' or self.input_box2.text == '':
                        self.error_add = True
                
                elif self.wm.collide_point("imgs/enviar.png",self.box_x*2+85, self.box_y+self.spacing+40, mouse_position):
                    if self.input_box3.text != '':
                        if self.list.remove(int(self.input_box3.text)) == None:
                            self.error_remove = True
                        else:
                            self.error_remove = False
                            
                elif self.wm.collide_point("imgs/enviar.png",self.box_x*3+115, self.box_y+self.spacing+40, mouse_position):
                    found = ''
                    if self.input_box4.text != '' and self.input_box5.text != '':
                        self.error_search = True
                    elif self.input_box4.text != '' and self.input_box5.text == '':
                        found = self.list.get_element(int(self.input_box4.text))
                        if  found == None:
                            self.error_search = True
                        else:
                            self.error_search = False
                            print (found)
                    elif self.input_box5.text != '' and self.input_box4.text == '':
                        found = self.list.get_position(int(self.input_box5.text))
                        if  found == None:
                            self.error_search = True
                        else:
                            self.error_search = False
                            print(found)
            