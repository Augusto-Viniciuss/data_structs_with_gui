import pygame
from windowManager import WindowManager
from inputBox import InputBox
from utils.Stack import Stack


class Stack_():
    def __init__(self):
       self.wm = WindowManager()
       self.list = Stack()
       self.wm.blit_screen()
       self.id = "Stack"
       self.flag_input = None
       self.add = None
       self.remove = None
       self.buscar = None
       self.wm.display = pygame.Surface((800, 900))
       self.wm.window = pygame.display.set_mode(((800, 900)))
       self.box_x, self.box_y = 140.5, 775.5
       self.input_box1 = InputBox(self.box_x, self.box_y)
       self.spacing = 10
       self.error_add, self.error_remove, self.error_search = False, False, False
       #usei as definições acima
       self.mid_w, self.mid_h = self.wm.DISPLAY_W /2 , self.wm.DISPLAY_H/2 + 20
       self.square_w,self.square_h = 200, 50
       self.square_side, self.square_border = 70, 1
       self.node_positions = [[self.mid_w, self.mid_h - 180],[self.mid_w, self.mid_h - 110],[self.mid_w, self.mid_h - 40],[self.mid_w, self.mid_h + 30],[self.mid_w, self.mid_h + 100],[self.mid_w, self.mid_h + 170],[self.mid_w, self.mid_h + 240],[self.mid_w, self.mid_h + 310],[self.mid_w, self.mid_h + 380],[self.mid_w, self.mid_h + 450]]

    def show_display(self):
      
        running = True
        while running:
            self.flag_input = self.check_input()

            if self.flag_input == "menu" or self.flag_input == "quit":
                return self.flag_input
          
            if self.flag_input == "add":
                self.wm.draw_circle_with_text(self.node_positions[self.add[0]-1][0], self.node_positions[self.add[0]-1][1] - 50, 24, self.wm.PURPLE, 1, str(self.add[1]), 20)

                if self.add[0] != 1:
                    self.wm.draw_arrow(pygame.Vector2(self.node_positions[self.add[0]-1][0], self.node_positions[self.add[0]-1][1]- 24), pygame.Vector2(self.node_positions[self.add[0]-1][0], self.node_positions[self.add[0]-1][1]), self.wm.YELLOW, 4, 10, 8)

                self.wm.blit_screen()
                pygame.time.delay(700)
              
            self.print_static_imgs()
           
            for i in range(self.list.qtd_elements):
                text = self.list.get_element(i)
                self.create_node(self.node_positions[i][0], self.node_positions[i][1]+100, str(text), self.wm.PURPLE, i)
            
            self.wm.blit_screen()
        
           
            if self.error_add:  #error treatment
                self.wm.draw_text("Erro ao inserir!", 16, 400, 150, self.wm.YELLOW)
            if self.error_remove:
                self.wm.draw_text("Erro ao remover! Posição inválida.", 16, 400, 150, self.wm.YELLOW)
            if self.error_search:
                self.wm.draw_text("Erro ao buscar! Posição ou elemento inválido.", 16, 400, 150, self.wm.YELLOW)
              
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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos() 
                    
                    #this is referent to the "send" button of "INSERIR" 
                    if self.wm.collide_point("imgs/enviar2.png", 200, 840, mouse_position):
                        if self.input_box1.text != '':   #if the user filled the box with element
                            if self.list.qtd_elements < 9:    #if the queue didnt have 10 elem yet
                                if self.list.push(int(self.input_box1.text)) == True:
                                    self.error_add = False
                                    self.add = self.list.get_size(), int(self.input_box1.text)
                                    return "add"
                                else:
                                    self.error_add = True
                                    return None     
                            else:
                                self.error_add = True   
                    
                    #this is referent to the "send" button of "REMOVER" 
                    elif self.wm.collide_point("imgs/enviar2.png",400, 800, mouse_position):
                            removed_value = self.list.pop()                          
                            if removed_value == None:     #if the position to be removed is invalid
                                self.error_remove = True
                                return None
                            else:                               #if the remove is valid 
                                self.error_remove = False
                                self.remove = 1, self.list.get_top()
                                return "remove"                        
                    #this is referent to the "send" button of "BUSCA"    
                    elif self.wm.collide_point("imgs/enviar2.png",600, 800, mouse_position):
                        element = self.list.get_top()
                        print(element)
                        if element == None:
                            self.error_search = True
                
                        else:
                            self.error_search = False
                            return "busca"
                     
    def create_node(self, posx, posy, text, color_text, node_index):
        self.wm.draw_circle_with_text(posx, posy, 24, color_text, 1, str(text), 20)

        if node_index < self.list.qtd_elements-1:
            self.wm.draw_arrow(pygame.Vector2(posx, posy - 48), pygame.Vector2(posx, posy - 24), self.wm.WHITE, 4, 10, 8)

    def print_static_imgs(self):
       self.wm.display.fill(self.wm.BLACK)
       self.wm.add_img("imgs/stack.png", 400, 70)  # title
       self.wm.add_img("imgs/inserir.png", 200, 750)  
       self.wm.add_img("imgs/remover.png", 400, 750)  
       self.wm.add_img("imgs/buscar.png", 600, 750) 
       self.wm.add_img("imgs/elemento.png", 75, 775.5) 
      
       self.wm.add_img("imgs/enviar2.png", 200, 840)  #inserir button
       self.wm.add_img("imgs/enviar2.png", 400, 800)  #remover button
       self.wm.add_img("imgs/enviar2.png", 600, 800)  #consultar button
      
       self.input_box1.draw(self.wm.display)
      

