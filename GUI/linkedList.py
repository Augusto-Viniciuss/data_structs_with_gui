import pygame
from windowManager import WindowManager
from inputBox import InputBox
from utils.Linked_list import Linked_list
     
class LinkedList():
    def __init__(self):
        self.wm = WindowManager()
        self.id = "Linked List"
        self.list = Linked_list()
        self.mid_w, self.mid_h = self.wm.DISPLAY_W /2 , self.wm.DISPLAY_H / 2
        self.box_x, self.box_y = 170, 420      #need to define as parameter the x and y of the firstbox
        self.spacing = 75
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
        self.wm.blit_screen()
        self.fetch = None
        self.add = None
        self.flag_input = None
        self.input_box1 = InputBox(self.box_x, self.box_y+50)       #box inserir-elemento
        self.input_box2= InputBox(self.box_x, self.box_y)          
        self.input_box3 = InputBox(self.box_x*2+30, self.box_y)     
        self.input_box4 = InputBox(self.box_x*3+60, self.box_y)
        self.input_box5 = InputBox(self.box_x*3+60, self.box_y+50)
        self.error_add, self.error_remove, self.error_search = False, False, False
        self.node_positions = [[self.mid_w - 280, self.mid_h], [self.mid_w - 220, self.mid_h], [self.mid_w - 160, self.mid_h], [self.mid_w - 100, self.mid_h], [self.mid_w - 40, self.mid_h], [self.mid_w + 20, self.mid_h], [self.mid_w + 80, self.mid_h], [self.mid_w + 140, self.mid_h], [self.mid_w + 200, self.mid_h], [self.mid_w + 260, self.mid_h]]
    
    def show_display(self):
        
        running = True
        while running: 
            self.flag_input = self.check_input()

            if self.flag_input == "menu" or self.flag_input == "quit": 
                return self.flag_input
            # elif self.flag_input == "busca":
            #     if(self.fetch[0] == "element"):
            #         continue
            
            #     elif(self.fetch[0] == "position"):
            #         self.wm.blit_screen()
            #         pygame.time.delay(700)

            # elif (self.flag_input == "add"):
                
                    
            self.wm.display.fill(self.wm.BLACK)
            self.wm.add_img("imgs/lse.png", 400, 70)     #title
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

            for i in range(self.list.qtd_elements):
                text = self.list.get_element(i+1)
                #print(text)
                self.create_node(self.node_positions[i][0], self.node_positions[i][1]-50, str(text) , i)

            
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
                        if self.list.qtd_elements<10:
                            if self.list.insert(int(self.input_box1.text), int(self.input_box2.text)) == True:
                                self.error_add = False
                            else:
                                self.error_add = True
                        else:
                            self.error_add = True    
                            
                            
                    elif self.input_box1.text == '' or self.input_box2.text == '':
                        self.error_add = True
                
                elif self.wm.collide_point("imgs/enviar.png",self.box_x*2+85, self.box_y+self.spacing+40, mouse_position):
                    if self.input_box3.text == '':
                        self.error_remove = True
                    else:
                        if self.list.remove(int(self.input_box3.text)) == None:
                            self.error_remove = True
                        else:
                            self.error_remove = False
                        
                            
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
            
        
    def create_node(self, posx, posy, text, node_index):
        self.wm.draw_circle_with_text(posx, posy, 20, self.wm.WHITE, 1, str(text), 15)
        if node_index < 9:
            self.wm.draw_arrow(pygame.Vector2(posx + 20, posy), pygame.Vector2(posx + 40, posy), self.wm.WHITE, 2, 8, 6)