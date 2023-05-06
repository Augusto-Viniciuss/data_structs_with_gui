import pygame
from windowManager import WindowManager

class Menu():
    def __init__(self):
        self.wm = WindowManager()
        self.id = "menu"
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
        
        self.seqlistx, self.seqlisty = self.mid_w-110, self.mid_h            #parameters button sequencial list
        self.chainlistx, self.chainlisty = self.mid_w-110, self.mid_h + 65   #parameters button linked list
        self.doublechainlistx, self.doublechainlisty = self.mid_w-110, self.mid_h + (65*2) #parameters button double list
        self.stackx, self.stacky = self.mid_w+110, self.mid_h            #parameters button stack
        self.queuex, self.queuey = self.mid_w+110, self.mid_h + 65     #parameters button queue
        self.treex, self.treey = self.mid_w+110, self.mid_h + (65*2)  #parameters button tree
        self.exitx, self.exity = self.mid_w, self.mid_h + (65*3)   #parameters button exit
        
        self.flag_input = None

    def show_display(self):
        while True:
            self.wm.check_events()
            self.flag_input = self.check_input()
            if self.flag_input != None:
                return self.flag_input
            self.wm.display.fill(self.wm.BLACK)
            self.wm.add_img("imgs/ed2.png",self.mid_w,100)
            self.wm.add_img("imgs/b1.png",self.seqlistx,self.seqlisty)
            self.wm.add_img("imgs/b2.png",self.chainlistx,self.chainlisty)
            self.wm.add_img("imgs/b3.png",self.doublechainlistx,self.doublechainlisty)
            self.wm.add_img("imgs/b4.png",self.exitx,self.exity)
            self.wm.add_img("imgs/b5_p.png",self.stackx,self.stacky)
            self.wm.add_img("imgs/b6_f.png",self.queuex,self.queuey)
            self.wm.add_img("imgs/b7_a.png",self.treex,self.treey)
            
            self.wm.blit_screen()
            self.wm.reset_keys()

    def check_input(self):
        if self.wm.MOUSE1:
            mouse_position = pygame.mouse.get_pos() 
            if self.wm.collide_point("imgs/b1.png",self.seqlistx,self.seqlisty, mouse_position):
                return 2
            elif self.wm.collide_point("imgs/b2.png", self.chainlistx, self.chainlisty, mouse_position):
                return 3
            elif self.wm.collide_point("imgs/b3.png", self.doublechainlistx, self.doublechainlisty, mouse_position):
                return 4
            elif self.wm.collide_point("imgs/b5_p.png", self.stackx, self.stacky, mouse_position):
                return 5
            elif self.wm.collide_point("imgs/b6_f.png", self.queuex, self.queuey, mouse_position):
                return 6
            elif self.wm.collide_point("imgs/b7_a.png", self.treex, self.treey, mouse_position):
                return 7
            elif self.wm.collide_point("imgs/b4.png", self.exitx,self.exity, mouse_position):
                return "quit"
        elif self.wm.BACK_KEY:
            return "quit"
        elif self.wm.quit == True:
            return "quit"