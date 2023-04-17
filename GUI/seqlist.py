import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()
        
class Seqlist(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.blit_screen()
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.WHITE)
            self.blit_screen()
            
    def check_input(self):
        if self.game.MOUSE1:
            mouse_position = pygame.mouse.get_pos() 
        
        elif self.game.BACK_KEY:
            self.game.curr_menu = self.game.MainMenu(self.game)