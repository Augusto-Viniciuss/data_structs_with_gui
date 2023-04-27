import pygame
from windowManager import WindowManager
from inputBox import InputBox
from utils.Sequential_list import Sequential_list


class SequentialList():
    def __init__(self):
        self.wm = WindowManager()
        self.list = Sequential_list()
        self.box_x, self.box_y = 170, 420      #need to define as parameter the x and y of the firstbox
        self.spacing = 75
        self.id = "Sequential list"
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
        self.wm.blit_screen()
        self.fetch = None
        self.add = None
        self.remove = None
        self.flag_input = None
        self.input_box1 = InputBox(self.box_x, self.box_y+50)       #box inserir-elemento
        self.input_box2= InputBox(self.box_x, self.box_y)          
        self.input_box3 = InputBox(self.box_x*2+30, self.box_y)     
        self.input_box4 = InputBox(self.box_x*3+60, self.box_y)
        self.input_box5 = InputBox(self.box_x*3+60, self.box_y+50)
        self.error_add, self.error_remove, self.error_search = False, False, False
        self.square_w,self.square_h = -20, 200
        self.square_side, self.square_border = 70, 1
        self.square_number_w, self.square_number_h= self.square_w+self.square_side/2, self.square_h+self.square_side/2 
        
    def show_display(self):
        
        running = True
        while running: 
            self.flag_input = self.check_input()
            
            if self.flag_input == "menu" or self.flag_input == "quit": 
                return self.flag_input
            elif self.flag_input == "busca":
                if(self.fetch[0] == "element"):
                    for x in range(self.fetch[1]):
                        if(x == 0 and x != self.fetch[1] - 1):
                            self.wm.draw_rect(self.square_w+(x+1)*self.square_side+self.square_border , self.square_h, self.square_side, self.square_side, self.wm.YELLOW, self.square_border)
                        elif(x != self.fetch[1] - 1):
                            self.wm.draw_rect(self.square_w+(x+1)*self.square_side+self.square_border , self.square_h, self.square_side, self.square_side, self.wm.YELLOW, self.square_border)
                            self.wm.draw_rect(self.square_w+(x)*self.square_side+self.square_border , self.square_h, self.square_side, self.square_side, self.wm.WHITE, self.square_border)
                        elif(x == 0 and x == self.fetch[1] - 1):
                            self.wm.draw_rect(self.square_w+(x+1)*self.square_side+self.square_border , self.square_h, self.square_side, self.square_side, self.wm.BLUE, self.square_border)
                        elif(x == self.fetch[1] - 1):
                            self.wm.draw_rect(self.square_w+(x+1)*self.square_side+self.square_border , self.square_h, self.square_side, self.square_side, self.wm.BLUE, self.square_border)
                            self.wm.draw_rect(self.square_w+(x)*self.square_side+self.square_border , self.square_h, self.square_side, self.square_side, self.wm.WHITE, self.square_border)
                        
                        self.wm.blit_screen()
                        pygame.time.delay(700)
                elif(self.fetch[0] == "position"):
                    self.wm.draw_rect(self.square_w+(self.fetch[1])*self.square_side+self.square_border + 5, self.square_h + 5, self.square_side - 10, self.square_side - 10, self.wm.BLACK)
                    self.wm.draw_text(str(self.fetch[2]), 31, self.square_number_w+(self.fetch[1])*self.square_side+self.square_border , self.square_number_h, self.wm.BLUE)
                    
                    self.wm.blit_screen()
                    pygame.time.delay(700)
            elif (self.flag_input == "add"): 
                if(self.add[0] == 1 and self.list.get_size() == 1):
                    self.wm.draw_text(str(self.add[1]), 30, self.square_number_w+(self.add[0])*self.square_side+self.square_border , self.square_number_h, self.wm.BLUE)
                    self.wm.blit_screen()
                    pygame.time.delay(700)
                elif(self.add[0] == self.list.get_size()):
                    self.wm.draw_text(str(self.add[1]), 30, self.square_number_w+(self.add[0])*self.square_side+self.square_border , self.square_number_h, self.wm.BLUE)
                    self.wm.blit_screen()
                    pygame.time.delay(700)
                else:
                    for x in range(self.list.get_size(), self.add[0], -1):
                        self.wm.draw_text(str(self.list.get_element(x)), 30, self.square_number_w+(x)*self.square_side+self.square_border , self.square_number_h, self.wm.PURPLE)
                        self.wm.draw_rect(self.square_w+(x - 1)*self.square_side+self.square_border + 5, self.square_h + 5, self.square_side - 10, self.square_side - 10, self.wm.BLACK)
                        self.wm.blit_screen()
                        pygame.time.delay(700)

                    self.wm.draw_text(str(self.list.get_element(self.add[0])), 30, self.square_number_w+(self.add[0])*self.square_side+self.square_border , self.square_number_h, self.wm.BLUE)
                    self.wm.blit_screen()
                    pygame.time.delay(700)
            elif self.flag_input == "remove":
                    self.wm.draw_text(str(self.remove[1]), 30, self.square_number_w+(self.remove[0])*self.square_side+self.square_border , self.square_number_h, self.wm.RED)
                    self.wm.blit_screen()
                    pygame.time.delay(700)
                    
                    for x in range(self.remove[0], self.list.get_size()):
                        self.wm.draw_rect(self.square_w+(x)*self.square_side+self.square_border + 5, self.square_h + 5, self.square_side - 10, self.square_side - 10, self.wm.BLACK)
                        self.wm.draw_text(str(self.list.get_element(x)), 30, self.square_number_w+(x)*self.square_side+self.square_border , self.square_number_h, self.wm.PURPLE)                        
                        self.wm.draw_rect(self.square_w+(x + 1)*self.square_side+self.square_border + 5, self.square_h + 5, self.square_side - 10, self.square_side - 10, self.wm.BLACK)

                        self.wm.blit_screen()
                        pygame.time.delay(700)
    

            self.print_static_imgs()      #printing the images on screen

    
            if self.error_add:         #error treatment
                self.wm.draw_text("ERROR", 18, self.box_x+55, self.box_y-55, self.wm.RED)
            if self.error_remove:
                self.wm.draw_text("ERROR", 18, self.box_x*2+85, self.box_y-55, self.wm.RED)
            if self.error_search:
                self.wm.draw_text("ERROR", 18, self.box_x*3+115, self.box_y-55, self.wm.RED)
            
            
            for i in range(10):
                if self.list.get_element(i+1) == None:
                    element = ''
                else:
                    element = str(self.list.get_element(i+1))
                self.wm.draw_rect(self.square_w+(i+1)*self.square_side+self.square_border , self.square_h, self.square_side, self.square_side, self.wm.WHITE, self.square_border)
                self.wm.draw_text(element, 30, self.square_number_w+(i+1)*self.square_side+self.square_border , self.square_number_h, self.wm.PURPLE)
            
            self.wm.blit_screen()
            
            if self.error_add != False or self.error_remove != False or self.error_search != False:
                pygame.time.delay(500)
                self.error_add, self.error_remove, self.error_search = False, False, False
        
    def check_input(self):
        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return "quit"
            
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    return "menu"
                    
            self.input_box1.handle_event(event)
            self.input_box2.handle_event(event)
            self.input_box3.handle_event(event)
            self.input_box4.handle_event(event)
            self.input_box5.handle_event(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos() 
                if self.wm.collide_point("imgs/enviar.png",self.box_x+55, self.box_y+self.spacing+40, mouse_position):
                    if self.input_box1.text != '' and self.input_box2.text != '':
                        if self.list.is_full() == False:
                            if self.list.insert(int(self.input_box1.text), int(self.input_box2.text)) == False:
                                self.error_add = True
                                return None
                            else:
                                self.add = (int(self.input_box2.text), int(self.input_box1.text))
                                self.error_add = False
                                return "add"
                        else:
                            self.error_add = True
                    elif self.input_box1.text == '' or self.input_box2.text == '':
                        self.error_add = True
                
                elif self.wm.collide_point("imgs/enviar.png",self.box_x*2+85, self.box_y+self.spacing+40, mouse_position):
                    if self.input_box3.text != '':
                        removed_element = self.list.remove(int(self.input_box3.text))
                        if removed_element == None:
                            self.error_remove = True
                            return None
                        else:
                            self.remove = (int(self.input_box3.text), removed_element)
                            self.error_remove = False
                            return "remove"
                            
                elif self.wm.collide_point("imgs/enviar.png",self.box_x*3+115, self.box_y+self.spacing+40, mouse_position):
                    element = ''
                    if self.input_box4.text != '' and self.input_box5.text != '':
                        self.error_search = True
                    elif self.input_box4.text != '' and self.input_box5.text == '':
                        element = self.list.get_element(int(self.input_box4.text))
                        if  element == None:
                            self.error_search = True
                            return None
                        else:
                            self.fetch = ("position", int(self.input_box4.text), element)
                            self.error_search = False
                            return "busca"
                    elif self.input_box5.text != '' and self.input_box4.text == '':
                        position = self.list.get_position(int(self.input_box5.text))
                        if  position == None:
                            self.error_search = True
                            return None
                        else:
                            self.error_search = False
                            self.fetch = ("element", position)
                            return "busca"


    def print_static_imgs(self):
    
        self.wm.display.fill(self.wm.BLACK)
        self.wm.add_img("imgs/ls.png", 400, 70)     #title
        self.wm.add_img("imgs/inserir.png", self.box_x+55, self.box_y-30)  #in the top of first column
        self.wm.add_img("imgs/remover.png", self.box_x*2+85, self.box_y-30)  #in the top of second column
        self.wm.add_img("imgs/buscar.png", self.box_x*3+115, self.box_y-30)  #in the top of third column
        self.wm.add_img("imgs/posicao.png", self.box_x-self.spacing, self.box_y+15)  #in the left of first line
        self.wm.add_img("imgs/elemento.png", self.box_x-self.spacing, self.box_y+50+15)  #in the left of second line
        
        self.wm.add_img("imgs/enviar2.png", self.box_x+55, self.box_y+self.spacing+40)
        self.wm.add_img("imgs/enviar2.png", self.box_x*2+85, self.box_y+self.spacing+40)
        self.wm.add_img("imgs/enviar2.png", self.box_x*3+115, self.box_y+self.spacing+40)

        self.input_box1.draw(self.wm.display)
        self.input_box2.draw(self.wm.display)
        self.input_box3.draw(self.wm.display)
        self.input_box4.draw(self.wm.display)
        self.input_box5.draw(self.wm.display)