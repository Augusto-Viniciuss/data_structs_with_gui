import pygame
from windowManager import WindowManager
from inputBox import InputBox
     
class LinkedList():
    def __init__(self):
        self.wm = WindowManager()
        self.id = "Linked List"
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
        self.box_x, self.box_y = 170, 420      #need to define as parameter the x and y of the firstbox
        self.spacing = 75
        self.wm.blit_screen()
        self.flag_input = None
        self.input_box1 = InputBox(self.box_x, self.box_y+50)       #box inserir-elemento
        self.input_box2= InputBox(self.box_x, self.box_y)          
        self.input_box3 = InputBox(self.box_x*2+30, self.box_y)     
        self.input_box4 = InputBox(self.box_x*3+60, self.box_y)
        self.input_box5 = InputBox(self.box_x*3+60, self.box_y+50)
        self.node_positions = [[self.mid_w - 280, self.mid_h], [self.mid_w - 220, self.mid_h], [self.mid_w - 160, self.mid_h], [self.mid_w - 100, self.mid_h], [self.mid_w - 40, self.mid_h], [self.mid_w + 20, self.mid_h], [self.mid_w + 80, self.mid_h], [self.mid_w + 140, self.mid_h], [self.mid_w + 200, self.mid_h], [self.mid_w + 260, self.mid_h]]
    
    def show_display(self):
        
        running = True
        while running: 
            self.flag_input = self.check_input()
            if self.flag_input != None: 
                return self.flag_input

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

            for x in range(10):
                self.create_node(self.node_positions[x][0], self.node_positions[x][1], x + 1, x)
            
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
        
    def create_node(self, posx, posy, text, node_index):
        self.wm.draw_circle_with_text(posx, posy, 20, self.wm.WHITE, 1, str(text), 15)
        if node_index < 9:
            self.wm.draw_arrow(pygame.Vector2(posx + 20, posy), pygame.Vector2(posx + 40, posy), self.wm.WHITE, 2, 8, 6)