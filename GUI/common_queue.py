import pygame
from windowManager import WindowManager
from inputBox import InputBox
from utils.Queue import Queue


class Common_Queue():
    def __init__(self):
        self.wm = WindowManager()
        self.queue = Queue()
        self.box_x, self.box_y = 170, 420      #need to define as parameter the x and y of the firstbox
        self.spacing = 75
        self.id = "Queue"
        self.mid_w, self.mid_h = self.wm.DISPLAY_W /2 , self.wm.DISPLAY_H / 2
        self.wm.blit_screen()
        self.fetch = None
        self.add = None
        self.remove = None
        self.flag_input = None
        self.input_box1 = InputBox(self.box_x-50, self.box_y+5)       #box inserir-elemento     
        self.input_box4 = InputBox(self.box_x*3+85, self.box_y)     #box busca- posicao
        self.input_box5 = InputBox(self.box_x*3+85, self.box_y+50)  #box busca- elemento
        
        self.error_add, self.error_remove, self.error_search = False, False, False
        self.node_positions = [[self.mid_w - 324, self.mid_h], [self.mid_w - 252, self.mid_h], [self.mid_w - 180, self.mid_h], [self.mid_w - 108, self.mid_h], [self.mid_w - 36, self.mid_h], [self.mid_w + 36, self.mid_h], [self.mid_w + 108, self.mid_h], [self.mid_w + 180, self.mid_h], [self.mid_w + 252, self.mid_h], [self.mid_w + 324, self.mid_h]]
        self.square_w,self.square_h = 59.8, 250
        self.square_side, self.circle_border = 60, 1
        self.square_number_w, self.square_number_h= self.square_w+self.square_side/2, self.square_h+self.square_side/2
    
    def show_display(self):
        running = True
        while running: 
            self.flag_input = self.check_input()
            if self.flag_input == "menu" or self.flag_input == "quit": 
                return self.flag_input
            if self.flag_input == "menu" or self.flag_input == "quit": 
                return self.flag_input
            # elif self.flag_input == "busca":
            #     if(self.fetch[0] == "element"):
            #         for x in range(self.fetch[1]+1):
                            
            #             if(x == self.fetch[1]):
            #                 if(x == 0): 
            #                     self.wm.draw_circle(self.node_positions[0][0], self.node_positions[x - 1][1]-50, 24, self.wm.BLUE, self.circle_border)
            #                 else: 
            #                     self.wm.draw_circle(self.node_positions[x - 1][0], self.node_positions[x - 1][1]-50, 24, self.wm.BLUE, self.circle_border)
            #             else:
            #                 if(x == 0): 
            #                     self.wm.draw_circle(self.node_positions[0][0], self.node_positions[x - 1][1]-50, 24, self.wm.YELLOW, self.circle_border)
            #                 else:
            #                     self.wm.draw_circle(self.node_positions[x-1][0], self.node_positions[x - 1][1]-50, 24, self.wm.YELLOW, self.circle_border)
                        
            #             self.wm.blit_screen()   
            #             pygame.time.delay(500)     

            #     elif(self.fetch[0] == "position"):
            #         for x in range(self.fetch[1]+1):
                        
            #             if(x == self.fetch[1]):
            #                 if(x == 0): 
            #                     self.wm.draw_circle(self.node_positions[0][0], self.node_positions[x - 1][1]-50, 24, self.wm.BLUE, self.circle_border)
            #                 else: 
            #                     self.wm.draw_circle(self.node_positions[x - 1][0], self.node_positions[x - 1][1]-50, 24, self.wm.BLUE, self.circle_border)
            #             else:
            #                 if(x == 0): 
            #                     self.wm.draw_circle(self.node_positions[0][0], self.node_positions[x - 1][1]-50, 24, self.wm.YELLOW, self.circle_border)
            #                 else:
            #                     self.wm.draw_circle(self.node_positions[x-1][0], self.node_positions[x - 1][1]-50, 24, self.wm.YELLOW, self.circle_border)
                        
            #             self.wm.blit_screen()
            #             pygame.time.delay(700)  

            # if(self.flag_input == "add"):
            #     if(self.list.get_size() == 1):
            #         self.wm.draw_circle_with_text(self.node_positions[self.add[0] - 1][0], self.node_positions[self.add[0] - 1][1] - 50, 24, self.wm.PURPLE, 1, str(self.list.get_element(self.add[0])), 20)
            #         self.wm.blit_screen()
            #         pygame.time.delay(700)
            #     elif(self.add[0] == self.list.get_size()):
            #         self.wm.draw_circle_with_text(self.node_positions[self.add[0] - 1][0], self.node_positions[self.add[0] - 1][1] - 50, 24, self.wm.PURPLE, 1, str(self.list.get_element(self.add[0])), 20)
            #         self.wm.draw_arrow(pygame.Vector2(self.node_positions[self.add[0] - 2][0] + 24, self.node_positions[self.add[0] - 2][1] - 50), pygame.Vector2(self.node_positions[self.add[0] - 1][0] - 24, self.node_positions[self.add[0] - 1][1] - 50), self.wm.YELLOW, 4, 10, 8)
            #         self.wm.blit_screen()
            #         pygame.time.delay(700)
                

            # elif(self.flag_input == "remove"):
            #     if(self.queue.get_size() > 0):
            #         self.wm.draw_arrow(pygame.Vector2(self.node_positions[0][0] + 24, self.node_positions[0][1] - 50), pygame.Vector2(self.node_positions[1][0] - 24, self.node_positions[1][1] - 50), self.wm.RED, 4, 10, 8)
            #         self.wm.blit_screen()
            #         pygame.time.delay(700)
            #         self.wm.draw_rect(self.node_positions[0][0] - 48, self.node_positions[0][1] - 100, self.square_side + 36, self.square_side + 40, self.wm.BLACK)
            #         self.wm.blit_screen()
            #         pygame.time.delay(700)
            #         self.queue.remove()

            self.print_static_imgs()     #function where the images and the input boxes are printed
            
            for i in range(self.queue.qtd_elements):
                text = self.queue.get_begin_element()
                self.create_node(self.node_positions[i][0], self.node_positions[i][1]-50, str(text), self.wm.PURPLE, i)
            
            if self.error_add:  #error treatment
                self.wm.draw_text("Erro ao inserir!", 16, 400, 150, self.wm.YELLOW)
            if self.error_remove:
                self.wm.draw_text("Erro ao remover! Posição inválida.", 16, 400, 150, self.wm.YELLOW)
            if self.error_search:
                self.wm.draw_text("Erro ao buscar! Posição ou elemento inválido.", 16, 400, 150, self.wm.YELLOW)
            
            self.wm.blit_screen()        #update the screen
            
            if self.error_add != False or self.error_remove != False or self.error_search != False:     #if exist some error
                pygame.time.delay(1700)                                                                 
                self.error_add, self.error_remove, self.error_search = False, False, False              #give some delay and reset variables
            

    def check_input(self):

        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return "quit"
            
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    return "menu"
                    
            self.input_box1.handle_event(event)
            self.input_box4.handle_event(event)
            self.input_box5.handle_event(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos() 
                
                #this is referent to the "send" button of "INSERIR" 
                if self.wm.collide_point("imgs/enviar.png",self.box_x+10, self.box_y+self.spacing, mouse_position):
                    print("cheguei")
                    if self.input_box1.text != '':   #if the user filled the box with element
                        if self.queue.qtd_elements < 10:    #if the queue didnt have 10 elem yet
                            if self.queue.insert(int(self.input_box1.text)) == True:
                                self.error_add = False
                                self.add = (self.queue.get_size(), int(self.input_box1.text))    #the position is always the last one
                                return "add"
                            else:
                                self.error_add = True
                                return None     
                        else:
                            self.error_add = True   
                
                #this is referent to the "send" button of "REMOVER" 
                elif self.wm.collide_point("imgs/enviar.png",self.box_x*2+85, self.box_y+self.spacing+40, mouse_position):
                        removed_value = self.queue.remove()                          
                        if removed_value == None:     #if the position to be removed is invalid
                            self.error_remove = True
                            return None
                        else:                               #if the remove is valid 
                            self.error_remove = False
                            self.remove = ()
                            return "remove"                        
                #this is referent to the "send" button of "BUSCA"    
                elif self.wm.collide_point("imgs/enviar.png",self.box_x*3+115, self.box_y+self.spacing+40, mouse_position):
                    element = ''
                    
                    if self.input_box4.text != '' and self.input_box5.text != '':        #if the user typed in the two boxes
                        self.error_search = True
                        
                    elif self.input_box4.text != '' and self.input_box5.text == '':    #if the box by position is filled
                        element = self.queue.get_element(int(self.input_box4.text))
                        if  element == None:       #the position does not exist
                            self.error_search = True
                            return None
                        else:                      #the position exists
                            self.fetch = ("position", int(self.input_box4.text), element)
                            self.error_search = False
                            return "busca"
                        
                    elif self.input_box5.text != '' and self.input_box4.text == '':    #if the search by element is filled
                        position = self.queue.get_position(int(self.input_box5.text))
                        
                        if  position == None:       #if the element does not exist
                            self.error_search = True
                            return None
                        else:      
                            self.error_search = False
                            self.fetch = ("element", position)
                            return "busca"
    
    def create_node(self, posx, posy, text, color_text, node_index):
        self.wm.draw_circle_with_text(posx, posy, 24, color_text, 1, str(text), 20)

        if node_index < self.queue.qtd_elements-1:
            self.wm.draw_arrow(pygame.Vector2(posx + 24, posy), pygame.Vector2(posx + 48, posy), self.wm.WHITE, 4, 10, 8)


    def print_static_imgs(self):
    
        self.wm.display.fill(self.wm.BLACK)
        self.wm.add_img("imgs/queue.png", 400, 70)     #title
        
        #inserir column 
        self.wm.add_img("imgs/inserir.png", self.box_x+10, self.box_y-30)  #in the top of first column
        self.wm.add_img("imgs/elemento.png", self.box_x-self.spacing-30, self.box_y+20)  #below "inserir"
        self.wm.add_img("imgs/enviar2.png", self.box_x+10, self.box_y+self.spacing)
        
        #remove column
        self.wm.add_img("imgs/remover.png", self.box_x*2+5, self.box_y-30)  #in the top of second column
        self.wm.add_img("imgs/enviar2.png", self.box_x*2+5, self.box_y+self.spacing)
        
        #search column
        self.wm.add_img("imgs/buscar.png", self.box_x*3+140, self.box_y-30)  #in the top of third column
        self.wm.add_img("imgs/posicao.png", self.box_x*3+30, self.box_y+15)  #in the left of first line
        self.wm.add_img("imgs/elemento.png", self.box_x*3+30, self.box_y+50+15)  #in the left of second line
        self.wm.add_img("imgs/enviar2.png", self.box_x*3+140, self.box_y+self.spacing+40)

        self.input_box1.draw(self.wm.display)
        self.input_box4.draw(self.wm.display)
        self.input_box5.draw(self.wm.display)
   