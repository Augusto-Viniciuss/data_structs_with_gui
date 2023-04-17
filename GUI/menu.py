import pygame
from seqlist import Seqlist
from chainlist import Chainlist
from doublechainlist import Doublechainlist

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.seqlistx, self.seqlisty = self.mid_w, self.mid_h
        self.chainlistx, self.chainlisty = self.mid_w, self.mid_h + 65
        self.doublechainlistx, self.doublechainlisty = self.mid_w, self.mid_h + (65*2)
        self.exitx, self.exity = self.mid_w, self.mid_h + (65*3)

    def show_display(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.flag_input = self.check_input()
            if self.flag_input != None:
                return self.flag_input
            self.game.display.fill(self.game.BLACK)
            self.game.add_img("imgs/ed2.png",self.mid_w,100)
            self.game.add_img("imgs/b1.png",self.seqlistx,self.seqlisty)
            self.game.add_img("imgs/b2.png",self.chainlistx,self.chainlisty)
            self.game.add_img("imgs/b3.png",self.doublechainlistx,self.doublechainlisty)
            self.game.add_img("imgs/b4.png",self.exitx,self.exity)
            self.blit_screen()
        
        return 0

    def check_input(self):
        if self.game.MOUSE1:
            mouse_position = pygame.mouse.get_pos() 
            if self.game.collide_point("imgs/b1.png",self.seqlistx,self.seqlisty, mouse_position):
                self.run_display = False
                self.game.curr_menu = Seqlist(self.game)

            elif self.game.collide_point("imgs/b2.png", self.chainlistx, self.chainlisty, mouse_position):
                self.run_display = False
                self.game.curr_menu = Chainlist(self.game)
                
            elif self.game.collide_point("imgs/b3.png", self.doublechainlistx, self.doublechainlisty, mouse_position):
                self.run_display = False
                self.game.curr_menu = Doublechainlist(self.game)
                
            elif self.game.collide_point("imgs/b4.png", self.exitx,self.exity, mouse_position):
                self.run_display = False
                self.game.running = False
                self.run_display = False
                
        elif self.game.BACK_KEY:
            self.run_display = False
            self.game.running = False
            self.run_display = False