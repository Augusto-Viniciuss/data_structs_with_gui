import pygame
from windowManager import WindowManager
from inputBox import InputBox


class Tree_():
    def __init__(self):
        self.wm = WindowManager()
        self.wm.blit_screen()
        self.flag_input = None
        self.wm.display = pygame.Surface((800, 800))
        self.wm.window = pygame.display.set_mode(((800, 800)))
        self.node_positions = [[400, 200], [225, 275], [575, 275], [150, 350], [300, 350], 
                               [500, 350], [650, 350], [115, 425], [185, 425], [265, 425],
                               [335, 425], [465, 425], [535, 425], [615, 425], [685,425]]

        self.input_box1 = InputBox(140, 660)
        self.input_box2 = InputBox(315, 660)
        self.box_side = 50

    def show_display(self):

        running = True
        while running:

            self.flag_input = self.check_input()

            if self.flag_input == "menu" or self.flag_input == "quit":
                return self.flag_input

            self.print_static_imgs()

            self.wm.draw_circle_with_text(self.node_positions[0][0],self.node_positions[0][1] , 24, self.wm.WHITE, 1, "1", 20)  
            self.wm.draw_circle_with_text(self.node_positions[1][0],self.node_positions[1][1] , 24, self.wm.WHITE, 1, "2", 20)
            self.wm.draw_circle_with_text(self.node_positions[2][0],self.node_positions[2][1] , 24, self.wm.WHITE, 1, "3", 20)
            self.wm.draw_circle_with_text(self.node_positions[3][0],self.node_positions[3][1] , 24, self.wm.WHITE, 1, "4", 20)
            self.wm.draw_circle_with_text(self.node_positions[4][0],self.node_positions[4][1] , 24, self.wm.WHITE, 1, "5", 20)
            self.wm.draw_circle_with_text(self.node_positions[5][0],self.node_positions[5][1] , 24, self.wm.WHITE, 1, "6", 20)
            self.wm.draw_circle_with_text(self.node_positions[6][0],self.node_positions[6][1] , 24, self.wm.WHITE, 1, "7", 20)
            self.wm.draw_circle_with_text(self.node_positions[7][0],self.node_positions[7][1] , 24, self.wm.WHITE, 1, "8", 20)
            self.wm.draw_circle_with_text(self.node_positions[8][0],self.node_positions[8][1] , 24, self.wm.WHITE, 1, "9", 20)
            self.wm.draw_circle_with_text(self.node_positions[9][0],self.node_positions[9][1] , 24, self.wm.WHITE, 1, "10", 20)
            self.wm.draw_circle_with_text(self.node_positions[10][0],self.node_positions[10][1] , 24, self.wm.WHITE, 1, "11", 20)
            self.wm.draw_circle_with_text(self.node_positions[11][0],self.node_positions[11][1] , 24, self.wm.WHITE, 1, "12", 20)
            self.wm.draw_circle_with_text(self.node_positions[12][0],self.node_positions[12][1] , 24, self.wm.WHITE, 1, "13", 20)
            self.wm.draw_circle_with_text(self.node_positions[13][0],self.node_positions[13][1] , 24, self.wm.WHITE, 1, "14", 20)
            self.wm.draw_circle_with_text(self.node_positions[14][0],self.node_positions[14][1] , 24, self.wm.WHITE, 1, "15", 20)
            
            
            self.wm.blit_screen()

    def check_input(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos() 
                
                #this is referent to the "send" button of "INSERIR" 
                if self.wm.collide_point("imgs/enviar.png", 200, 725, mouse_position):
                    
                    if self.input_box1.text != '':   #if the user filled the box with element
                        print("inserir")
                
                #this is referent to the "send" button of "BUSCA" 
                elif self.wm.collide_point("imgs/enviar.png",375, 725, mouse_position):
                    
                    if self.input_box2.text != '':   #if the user filled the box with element
                        print("busca")
                                               
                #this is referent to the "send" button of "CAMINHAMENTO"    
                elif self.wm.collide_point("imgs/inordem.png",600, 675, mouse_position):
                    print("caminhamento")
            
            self.input_box1.handle_event(event)
            self.input_box2.handle_event(event)

    def print_static_imgs(self):
        self.wm.display.fill(self.wm.BLACK)
        self.wm.add_img("imgs/arvore.png", 400, 70)  # title
        self.wm.add_img("imgs/inserir.png", 200, 630)  #in the top of first column
        self.wm.add_img("imgs/buscar.png", 375, 630)  #in the top of second column
        self.wm.add_img("imgs/caminhamento.png", 600, 630)  
        self.wm.add_img("imgs/elemento.png", 75, 675)  
        
        self.wm.add_img("imgs/enviar2.png", 200, 725)  #inserir button
        self.wm.add_img("imgs/enviar2.png", 375, 725)  #busca button
        self.wm.add_img("imgs/inordem.png", 600, 675)  #caminhamento button
        
        self.input_box1.draw(self.wm.display)
        self.input_box2.draw(self.wm.display)


        for i in range(15):
            self.wm.draw_rect(25+(i*50), 525, self.box_side, self.box_side, self.wm.WHITE, 1)
