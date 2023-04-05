import pygame

from menu import MainMenu

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.MOUSE1, self.BACK_KEY = False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0,0,0), (255,255,255)
        self.curr_menu = MainMenu(self)

    def game_loop(self):
        while self.playing:
            self.check_events()
            
            if self.BACK_KEY:
                self.playing = False

            self.display.fill(self.BLACK)
            
            self.draw_text('Thanks for working!!', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)

            self.window.blit(self.display, (0,0))
            
            pygame.display.update()
            
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.MOUSE1 = True
    
    def reset_keys(self):
        self.MOUSE1, self.BACK_KEY = False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)

    def add_img(self, icon, x, y):
        image = pygame.image.load(icon)
        image_rect = image.get_rect()
        image_rect.center = (x,y)
        self.display.blit(image, image_rect)

    def collide_point(self, icon, x, y, mouse_position):
        image = pygame.image.load(icon)
        image_rect = image.get_rect()
        image_rect.center = (x,y)
        if (image_rect.collidepoint(mouse_position) ):
            return True