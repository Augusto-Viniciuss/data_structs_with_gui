import pygame
from windowManager import WindowManager
     
class LinkedList():
    def __init__(self):
        self.wm = WindowManager()
        self.id = "Linked List"
        self.mid_w, self.mid_h = self.wm.DISPLAY_W / 2, self.wm.DISPLAY_H / 2
        self.wm.blit_screen()
        self.flag_input = None
        self.node_positions = [[self.mid_w - 280, self.mid_h], [self.mid_w - 220, self.mid_h], [self.mid_w - 160, self.mid_h], [self.mid_w - 100, self.mid_h], [self.mid_w - 40, self.mid_h], [self.mid_w + 20, self.mid_h], [self.mid_w + 80, self.mid_h], [self.mid_w + 140, self.mid_h], [self.mid_w + 200, self.mid_h], [self.mid_w + 260, self.mid_h]]
    
    def show_display(self):
        while True:
            self.wm.check_events()
            self.flag_input = self.check_input()
            if self.flag_input != None:
                return self.flag_input
            self.wm.display.fill(self.wm.BLACK)
            for x in range(10):
                self.create_node(self.node_positions[x][0], self.node_positions[x][1], x + 1, x)
            self.wm.blit_screen()
            self.wm.reset_keys()
            
    def check_input(self):
        if self.wm.MOUSE1:
            mouse_position = pygame.mouse.get_pos() 
        
        elif self.wm.BACK_KEY:
            return 1
        
    def create_node(self, posx, posy, text, node_index):
        self.wm.draw_circle_with_text(posx, posy, 20, self.wm.WHITE, 1, str(text), 15)
        if node_index < 9:
            self.wm.draw_arrow(pygame.Vector2(posx + 20, posy), pygame.Vector2(posx + 40, posy), self.wm.WHITE, 2, 8, 6)