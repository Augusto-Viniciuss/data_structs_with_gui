import pygame

class WindowManager:
    def __init__(self, font = pygame.font.get_default_font()):
        self.MOUSE1, self.BACK_KEY, self.ENTER, self.BACKSPACE = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = font
        self.BLACK, self.WHITE, self.RED, self.GREEN, self.GRAY = (0,0,0), (255,255,255), (255,0,0), (0,255,0), pygame.Color('gray15')
        self.GRAY, self.LIGHTBLUE = pygame.Color('gray15'), pygame.Color('lightskyblue3')
        self.quit = False
        self.BOX_W, self.BOX_H = 150, 30
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                elif event.key == pygame.K_RETURN:
                    self.ENTER = True
                elif event.key == pygame.K_BACKSPACE:
                    self.BACKSPACE = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.MOUSE1 = True

    def reset_keys(self):
        self.MOUSE1, self.BACK_KEY, self.ENTER, self.BACKSPACE = False, False, False, False

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
        
    def blit_screen(self):
        self.window.blit(self.display, (0,0))
        pygame.display.update()
        self.reset_keys()
        
    def draw_rect(self, posx, posy, rect_w, rect_h, color, rectborder):
        rect = pygame.Rect(posx, posy, rect_w, rect_h)
        pygame.draw.rect(self.display, color, rect, rectborder)
        
    def draw_inputbox(self, posx, posy, color):
    
        rectborder = 2        #defining the boarder of the input box
        
        rect = pygame.Rect(posx- self.BOX_W, posy - self.BOX_H, self.BOX_W, self.BOX_H)        #defining the retangle
        pygame.draw.rect(self.display, color, rect, rectborder)  #drawing the retangle in the screen
        
        return rect

    
    def logic_inputbox(self, input_box):
      
        clock = pygame.time.Clock()
        font_text = pygame.font.Font(None, 25)
        user_text = ''
    
        active = False
        while True:
            
            for event in pygame.event.get():
            
                if event.type == pygame.K_ESCAPE:     #if ESC is pressed
                    return 1 
                elif event.type == pygame.QUIT:      #if QUIT is pressed
                    return -1
                
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #if the mouse is pressed
                    if input_box.collidepoint(event.pos):         
                        active = True
                    else:
                        active = False
                    
                if event.type == pygame.KEYDOWN:    #if the keyboard is pressed
                        
                    if active: 
                        if event.key == pygame.K_RETURN:      #if the enter is pressed
                            active = False
                            pygame.time.delay(500)  #just adding a delay to erase all
                            user_text = ''
                        
                        elif event.key == pygame.K_BACKSPACE:  #the button to erase
                            user_text = user_text[:-1]
                                        
                        elif event.unicode.isnumeric():      #any number is added
                            user_text += event.unicode
                                    
                if active:
                    current_color = self.LIGHTBLUE
                else:
                    current_color = self.GRAY
                
            self.window.fill(self.BLACK)
            pygame.draw.rect(self.window, current_color, input_box, 2) 
            text_surface = font_text.render(user_text, True, self.WHITE)
            self.window.blit(text_surface, (input_box.x + 5, input_box.y + 5))     #just a spacing to the text in the box
            input_box.w = max(150, text_surface.get_width() + 15)
            pygame.display.flip()
            clock.tick(60)
                        
  # def text_input_box(self):
    #     text , return_text= '', ''
    #     active = True
    #     text_size = 32
    #     base_font = pygame.font.Font(None, text_size)
    #     posx, posy = 200, 200
    #     rectx, recty = 140, 32
        
    #     input_rect = pygame.Rect(posx, posy, rectx, recty)
    #     back_rect = pygame.Rect(posx, posy, rectx+5, recty+5)

        
    #     while active:
    #         for event in pygame.event.get():            
    #             if event.type == pygame.QUIT:
    #                 self.quit = True
    #                 active = False
    #             if event.type == pygame.KEYDOWN:           #if any button is pressed 
    #                 if event.key == pygame.K_RETURN:      #if the enter is pressed
    #                     print(text)
    #                     active = False
    #                     text = ''
    #                     return return_text
    #                 elif event.key == pygame.K_BACKSPACE:
    #                     text = text[:-1]
    #                 elif event.key == pygame.K_ESCAPE:
    #                     active = False
    #                 else:
    #                     text += event.unicode

    #         pygame.draw.rect(self.window, self.BLACK, back_rect)
    #         if active:
    #             pygame.draw.rect(self.window, self.LIGHTBLUE, input_rect, 2)
    #         else:
    #             pygame.draw.rect(self.window, self.GRAY, input_rect, 2)
    #         text_surface = base_font.render(text, True, self.WHITE)     
    #         self.window.blit(text_surface, (input_rect.x + 5, input_rect.y +5))
            
    #         input_rect.w = max(rectx , text_surface.get_width() + 10)
    #         if back_rect.w < (input_rect.w+5):
    #             back_rect.w += text_size

    #         pygame.display.update()

    #         self.reset_keys()