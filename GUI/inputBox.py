import pygame

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('lightskyblue3')
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
            self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # If the user pressed Return, clear the input box and print the input.
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    # If the user pressed Backspace, remove the last character from the input.
                    self.text = self.text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    self.active = False
                else:
                    # If the user typed a character, add it to the input.
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = pygame.font.Font(None, 32).render(self.text, True, self.color)

    def draw(self, screen):
        # Blit the input box rect and text surface onto the screen.
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))