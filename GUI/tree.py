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
                
        self.arrow_positions = [[pygame.Vector2(365, 215), pygame.Vector2(255, 260)], [pygame.Vector2(435, 215), pygame.Vector2(545, 260)],
                                [pygame.Vector2(200, 300), pygame.Vector2(175, 325)], [pygame.Vector2(250, 300), pygame.Vector2(275, 325)],
                                [pygame.Vector2(550, 300), pygame.Vector2(525, 325)], [pygame.Vector2(600, 300), pygame.Vector2(625, 325)],
                                [pygame.Vector2(130, 375), pygame.Vector2(120, 395)], [pygame.Vector2(170, 375), pygame.Vector2(180, 395)],
                                [pygame.Vector2(280, 375), pygame.Vector2(270, 395)], [pygame.Vector2(320, 375), pygame.Vector2(330, 395)],
                                [pygame.Vector2(480, 375), pygame.Vector2(470, 395)], [pygame.Vector2(520, 375), pygame.Vector2(530, 395)],
                                [pygame.Vector2(630, 375), pygame.Vector2(620, 395)], [pygame.Vector2(670, 375), pygame.Vector2(680, 395)]]
        self.add = [None, 0]
        self.fetch = [None, 0]
        self.walk = [None] 
        self.array_fetch = []
        self.array_walk = None
        self.active = [[False,0], [False,0], [False,0], [False,0], [False,0], [False,0], [False,0],
                       [False,0], [False,0], [False,0], [False,0], [False,0], [False,0], [False,0],
                       [False,0]]         
        self.input_box1 = InputBox(140, 660)
        self.input_box2 = InputBox(315, 660)
        self.radius = 24
        
        

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
                self.define_flags_fetch()
                self.fetch[0] = None
                
                for i in range(len(self.array_fetch)):
                
                    if i == len(self.array_fetch)-1:      #if is the last element
                        self.wm.draw_circle(self.node_positions[self.array_fetch[i]][0],self.node_positions[self.array_fetch[i]][1] , 24, self.wm.BLUE, 1)
                    else:
                        self.wm.draw_circle(self.node_positions[self.array_fetch[i]][0],self.node_positions[self.array_fetch[i]][1] , 24, self.wm.YELLOW, 1)
                        
                    self.wm.blit_screen()
                    pygame.time.delay(500)
                    
                self.array_fetch = []    #restarting the arrayfetch
                
                        
            elif self.walk == "walk":
                for i in range(15):                              #printing the walking by the tree
                    if(self.array_walk[i]!= None):
                        if i != 0:      #if it isnt the first element to print the "-"
                            self.wm.draw_text("-", 20, 22+(i*50), 550, self.wm.WHITE)
                            
                        self.wm.draw_text(str(self.array_walk[i]), 20, 50+(i*50), 550, self.wm.WHITE) #printing the number of the walk
                
                self.wm.blit_screen()
                pygame.time.delay(2100)
                self.walk = None
            
            self.print_static_imgs()
            
            for i in range(len(self.active)):       #printing the tree
                if self.active[i][0] == True: 
                    if i != 0:
                        self.wm.draw_arrow(self.arrow_positions[i-1][0], self.arrow_positions[i-1][1], self.wm.WHITE, 4, 10, 8)
                        
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
                if self.wm.collide_point("imgs/enviar.png", 200, 725, mouse_position):
    
                    if self.input_box1.text != '':   #if the user filled the box with element
                        self.tree.insert(int(self.input_box1.text))        #inserindo elemento
                        self.add = ["add", int(self.input_box1.text)]
                        
                #this is referent to the "send" button of "BUSCA" 
                elif self.wm.collide_point("imgs/enviar.png",375, 725, mouse_position):

                    if self.input_box2.text != '':   #if the user filled the box with element
                                                
                        if self.tree.search_element(int(self.input_box2.text)) == True:      #if the element was founded
                            self.fetch = ["fetch", int(self.input_box2.text)]
                        else:         
                            print("deu erro total")       
                                               
                #this is referent to the "send" button of "CAMINHAMENTO"    
                elif self.wm.collide_point("imgs/preordem.png",600, 675, mouse_position):     #first button (pre ordem)
                    self.array_walk = self.tree.get_walkin_array("prefix")
                    self.walk = "walk"


                elif self.wm.collide_point("imgs/inordem.png",600, 715, mouse_position):      #second button (in ordem)
                    self.array_walk = self.tree.get_walkin_array("infix")
                    self.walk = "walk"
                
                elif self.wm.collide_point("imgs/posordem.png",600, 755, mouse_position):     #third button (pos ordem)
                    self.array_walk = self.tree.get_walkin_array("suffix")
                    self.walk = "walk"
            
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
        self.wm.draw_rect(25, 525, 750, 50, self.wm.WHITE, 1)
        
            
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
            
    def define_flags_fetch(self):
        
        self.array_fetch.append(0)            #pushing in the array the position
        if self.active[0][0] == True and self.active[0][1] == self.fetch[1]:        #se o nó raiz nao tiver valor ainda
            return 0                                                                #node founded
        else:                                 
            if self.fetch[1] < self.active[0][1]:

                self.array_fetch.append(1)    #pushing the position
                if self.active[1][0] == True and self.active[1][1] == self.fetch[1]:
                    return 0                                                        #node founded
                else:
                    if self.fetch[1] < self.active[1][1]: 
                        
                        self.array_fetch.append(3)    #pushing the position  
                        if self.active[3][0] == True and self.active[3][1] == self.fetch[1]:       
                            return 0
                        else:                                
                            if self.fetch[1] < self.active[3][1]:  
                                
                                self.array_fetch.append(7)    #pushing the position  
                                if self.active[7][0] == True and self.active[7][1] == self.fetch[1]:
                                    return 0
                                else:
                                    print("deu erro busca")
                            else:                              
                                self.array_fetch.append(8)    #pushing the position  
                                if self.active[8][0] == True and self.active[8][1] == self.fetch[1]:       
                                    return 0
                                else: 
                                    print("deu erro busca")
                                        
                    else:     
                        self.array_fetch.append(4)    #pushing the position  
                        if self.active[4][0] == True and self.active[4][1] == self.fetch[1]:
                            return 0 
                        else:
                            if self.fetch[1] < self.active[4][1]:
                                
                                self.array_fetch.append(9)    #pushing the position  
                                if self.active[9][0] == True and self.active[9][1] == self.fetch[1]:       
                                    return 0;
                                else:
                                    print("deu erro busca")
                            else: 
                                self.array_fetch.append(10)    #pushing the position  
                                if self.active[10][0] == True and self.active[10][1] == self.fetch[1]:
                                    return 0;
                                else:
                                    print("deu erro busca")
                        
            else:                #valor inserido maior que a raiz
                self.array_fetch.append(2)    #pushing the position  
                if self.active[2][0] == True and self.active[2][1] == self.fetch[1]:
                    return 0
                else:
                    if self.fetch[1] < self.active[2][1]:       #valor é menor que o primeiro nó a direita
                        
                        self.array_fetch.append(5)    #pushing the position  
                        if self.active[5][0] == True and self.active[5][1] == self.fetch[1]:
                            return 0
                        else:                                 # nó a esquerda do 2 nó ja existe
                            if self.fetch[1] < self.active[5][1]:
                                self.array_fetch.append(11)    #pushing the position  
                                if self.active[11][0] == True and self.active[11][1] == self.fetch[1]:
                                    return 0;
                                else:
                                    print("deu erro busca")
                            else:
                                self.array_fetch.append(12)    #pushing the position  
                                if self.active[12][0] == True and self.active[12][1] == self.fetch[1]:
                                    return 0;
                                else:
                                    print("deu erro busca")
                        
                    else:     #valor é maior que o 1 nó a esquerda   
                        self.array_fetch.append(6)    #pushing the position      
                        if self.active[6][0] == True and self.active[6][1] == self.fetch[1]:
                            return 0
                        
                        else:
                            if self.fetch[1] < self.active[6][1]:
                                self.array_fetch.append(13)    #pushing the position  
                                if self.active[13][0] == True and self.active[13][1] == self.fetch[1]:
                                    return 0
                                else:
                                    print("deu erro busca!")
                            else:
                                self.array_fetch.append(14)    #pushing the position  
                                if self.active[14][0] == True and self.active[14][1] == self.fetch[1]:
                                    return 0
                                else:
                                    print("deu erro busca!")              
                
          
