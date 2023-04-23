import pygame

class InputBox:
    def __init__(self, xpos, ypos, width = 115, height = 32, text = ''):
        self.X_POS, self.Y_POS, self.BOX_W, self.BOX_H = xpos, ypos, 115, 32
        self.rect = pygame.Rect(xpos, ypos, width, height)
        self.color = pygame.Color('grey15')
        self.text = text
        self.txt_surface = pygame.font.Font(None, 32).render(text, True, self.color)
        self.active = False
        

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the color of the input box.
            self.color = pygame.Color('lightskyblue3') if self.active else pygame.Color('gray15')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # If the user pressed Return, clear the input box and print the input.
                    #print(self.text)
                    #self.text = ''
                    self.active = False
                    self.color = pygame.Color('gray15')
                elif event.key == pygame.K_BACKSPACE:
                    # If the user pressed Backspace, remove the last character from the input.
                    self.text = self.text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    self.active = False
                elif event.unicode.isnumeric():           # if the user typed a number, add it to the input
                    if self.txt_surface.get_width() < self.BOX_W-90: 
                        self.text += event.unicode
                # Re-render the text.
                
                self.txt_surface = pygame.font.Font(None, 25).render(self.text, True, pygame.Color('white'))


    def draw(self, screen):
        # Blit the input box rect and text surface onto the screen.
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))