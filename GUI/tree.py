import pygame
from windowManager import WindowManager
from inputBox import InputBox
from utils.Binary_search_tree import Binary_search_tree

class Tree_():
    def __init__(self):
        self.wm = WindowManager()
        self.wm.blit_screen()
        self.tree = Binary_search_tree()
        self.quantity_nodes = 15
        self.flag_input = None
        self.wm.display = pygame.Surface((800, 800))
        self.wm.window = pygame.display.set_mode(((800, 800)))
        self.node_positions = [[400, 200], [225, 275], [575, 275], [150, 350], [300, 350], 
                               [500, 350], [650, 350], [115, 425], [185, 425], [265, 425],
                               [335, 425], [465, 425], [535, 425], [615, 425], [685,425]]
        self.add = [None, 0]
        self.fetch = [None, 0]
        self.entered_first = 0
        self.active = [[False,0], [False,0], [False,0], [False,0], [False,0], [False,0], [False,0],
                       [False,0], [False,0], [False,0], [False,0], [False,0], [False,0], [False,0],
                       [False,0]]         
        self.input_box1 = InputBox(140, 660)
        self.input_box2 = InputBox(315, 660)
        self.box_side = 50

    def show_display(self):

        running = True
        while running:

            self.flag_input = self.check_input()

            if self.flag_input == "menu" or self.flag_input == "quit":
                return self.flag_input

        
            elif self.add[0] == "add":
                self.define_flags_add()
                self.add[0] = None
                        
            elif self.fetch[0] == "fetch":
                for i in range(len(self.active)):
                    if self.active[i][0] == True:
                        if self.active[i][1] == self.fetch[1]:      #if the element is equal to the searched
                            self.wm.draw_circle_with_text(self.node_positions[i][0],self.node_positions[i][1] , 24, self.wm.BLUE, 1, str(self.active[i][1]), 20)
                        else:
                            self.wm.draw_circle_with_text(self.node_positions[i][0],self.node_positions[i][1] , 24, self.wm.YELLOW, 1, str(self.active[i][1]), 20)
                

            # self.wm.draw_circle_with_text(self.node_positions[0][0],self.node_positions[0][1] , 24, self.wm.WHITE, 1, "1", 20)  
            # self.wm.draw_circle_with_text(self.node_positions[1][0],self.node_positions[1][1] , 24, self.wm.WHITE, 1, "2", 20)
            # self.wm.draw_circle_with_text(self.node_positions[2][0],self.node_positions[2][1] , 24, self.wm.WHITE, 1, "3", 20)
            # self.wm.draw_circle_with_text(self.node_positions[3][0],self.node_positions[3][1] , 24, self.wm.WHITE, 1, "4", 20)
            # self.wm.draw_circle_with_text(self.node_positions[4][0],self.node_positions[4][1] , 24, self.wm.WHITE, 1, "5", 20)
            # self.wm.draw_circle_with_text(self.node_positions[5][0],self.node_positions[5][1] , 24, self.wm.WHITE, 1, "6", 20)
            # self.wm.draw_circle_with_text(self.node_positions[6][0],self.node_positions[6][1] , 24, self.wm.WHITE, 1, "7", 20)
            # self.wm.draw_circle_with_text(self.node_positions[7][0],self.node_positions[7][1] , 24, self.wm.WHITE, 1, "8", 20)
            # self.wm.draw_circle_with_text(self.node_positions[8][0],self.node_positions[8][1] , 24, self.wm.WHITE, 1, "9", 20)
            # self.wm.draw_circle_with_text(self.node_positions[9][0],self.node_positions[9][1] , 24, self.wm.WHITE, 1, "10", 20)
            # self.wm.draw_circle_with_text(self.node_positions[10][0],self.node_positions[10][1] , 24, self.wm.WHITE, 1, "11", 20)
            # self.wm.draw_circle_with_text(self.node_positions[11][0],self.node_positions[11][1] , 24, self.wm.WHITE, 1, "12", 20)
            # self.wm.draw_circle_with_text(self.node_positions[12][0],self.node_positions[12][1] , 24, self.wm.WHITE, 1, "13", 20)
            # self.wm.draw_circle_with_text(self.node_positions[13][0],self.node_positions[13][1] , 24, self.wm.WHITE, 1, "14", 20)
            # self.wm.draw_circle_with_text(self.node_positions[14][0],self.node_positions[14][1] , 24, self.wm.WHITE, 1, "15", 20)
            self.print_static_imgs()
            
            for i in range(len(self.active)):
                if self.active[i][0] == True: 
                    self.wm.draw_circle_with_text(self.node_positions[i][0],self.node_positions[i][1] , 24, self.wm.WHITE, 1, str(self.active[i][1]), 20)  
            
            
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
                if self.wm.collide_point("imgs/enviar.png", 200, 500, mouse_position):
    
                    if self.input_box1.text != '':   #if the user filled the box with element
                        self.tree.insert(int(self.input_box1.text))        #inserindo elemento
                        self.add = ["add", int(self.input_box1.text)]
                        
                #this is referent to the "send" button of "BUSCA" 
                elif self.wm.collide_point("imgs/enviar.png",375, 500, mouse_position):

                    if self.input_box2.text != '':   #if the user filled the box with element
                                                
                        if self.tree.search_element(int(self.input_box2.text)) == True:      #if the element was founded
                            self.fetch = ["fetch", int(self.input_box2.text)]
                        else:         
                            print("deu erro total")       
                                               
                #this is referent to the "send" button of "CAMINHAMENTO"    
                elif self.wm.collide_point("imgs/preordem.png",600, 675, mouse_position):     #first button (pre ordem)
                    print("caminhamento1")

                elif self.wm.collide_point("imgs/inordem.png",600, 715, mouse_position):      #second button (in ordem)
                    print("caminhamento2")
                
                elif self.wm.collide_point("imgs/posordem.png",600, 755, mouse_position):     #third button (pos ordem)
                    print("caminhamento3")
            
            self.input_box1.handle_event(event)
            self.input_box2.handle_event(event)

    def print_static_imgs(self):
        self.wm.display.fill(self.wm.BLACK)
        self.wm.add_img("imgs/arvore.png", 400, 70)  # title
        self.wm.add_img("imgs/inserir.png", 200, 630)  #in the top of first column
        self.wm.add_img("imgs/buscar.png", 375, 630)  #in the top of second column
        self.wm.add_img("imgs/caminhamento.png", 600, 630)  
        self.wm.add_img("imgs/elemento.png", 75, 675)  
        
        self.wm.add_img("imgs/enviar2.png", 200, 725)  #inserir button          **************ycerto= 725
        self.wm.add_img("imgs/enviar2.png", 375, 725)  #busca button
        self.wm.add_img("imgs/preordem.png", 600, 675)  #caminhamento button
        self.wm.add_img("imgs/inordem.png", 600, 715)  #caminhamento button
        self.wm.add_img("imgs/posordem.png", 600, 755)  #caminhamento button
        
        self.input_box1.draw(self.wm.display)
        self.input_box2.draw(self.wm.display)

        #tem que trocar por circulozinhos!!!!
        #for i in range(15):
            #self.wm.draw_rect(25+(i*50), 525, self.box_side, self.box_side, self.wm.WHITE, 1)
            
    def define_flags_add(self):
        
        if self.active[0][0] == False:        #se o nó raiz nao tiver valor ainda
            self.active[0] = True, self.add[1]
        else:                                 
            if self.add[1] < self.active[0][1]:      #raiz existe e o valor a ser inserido é menor que o nó raiz
                if self.active[1][0] == False:
                    self.active[1] = True, self.add[1]
                else:
                    if self.add[1] < self.active[1][1]:      #1º nó a esquerda ja existe e o valor inserido é menor
                        if self.active[3][0] == False:       
                            self.active[3] = True, self.add[1]
                        else:                                #2 nó a esquerda ja existe
                            if self.add[1] < self.active[3][1]:  #valor é menor que o 2 nó
                                if self.active[7][0] == False:       
                                        self.active[7] = True, self.add[1]
                                else:
                                        print("deu erro arvore cheia")
                            else:                              #valor é maior que 2 nó
                                if self.active[8][0] == False:       
                                    self.active[8] = True, self.add[1]
                                else: 
                                    print("deu erro arvore cheia")
                                        
                    else:             #1º nó a esquerda ja existe e o valor inserido é maior
                        if self.active[4][0] == False: 
                            self.active[4] = True, self.add[1]    
                        else:
                            if self.add[1] < self.active[4][1]:
                                if self.active[9][0] == False:       
                                    self.active[9] = True, self.add[1]
                                else:
                                    print("deu erro arvore cheia")
                            else: 
                                if self.active[10][0] == False:       
                                    self.active[10] = True, self.add[1]
                                else:
                                    print("deu erro arvore cheia")
                        
            else:                #valor inserido maior que a raiz
                if self.active[2][0] == False:
                    self.active[2]= True, self.add[1]
                else:
                    if self.add[1] < self.active[2][1]:       #valor é menor que o primeiro nó a direita
                        if self.active[5][0] == False:      
                            self.active[5]= True, self.add[1]
                            
                        else:                                 # nó a esquerda do 2 nó ja existe
                            if self.add[1] < self.active[5][1]:
                                if self.active[11][0] == False:
                                    self.active[11] = True, self.add[1]
                                else:
                                    print("deu erro  tree cheia!")
                            else:
                                if self.active[12][0] == False:
                                    self.active[12] = True, self.add[1]
                                else:
                                    print("deu erro  tree cheia!")
                        
                    else:     #valor é maior que o 1 nó a esquerda       
                        if self.active[6][0] == False:      
                            self.active[6] = True, self.add[1]
                            
                        else:
                            if self.add[1] < self.active[6][1]:
                                if self.active[13][0] == False:
                                    self.active[13] = True, self.add[1]
                                else:
                                    print("deu erro  tree cheia!")
                            else:
                                if self.active[14][0] == False:
                                    self.active[14] = True, self.add[1]
                                else:
                                    print("deu erro  tree cheia!")
            
