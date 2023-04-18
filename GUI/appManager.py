import pygame
from menu import Menu
from seqlist import Seqlist
from chainlist import ChainList
from doublechainlist import DoubleChainList

class AppManager():
    def __init__(self):
        pygame.init()
        self.running = True
        self.current_window = None

    def run_app(self):
        self.current_window = Menu()

        while self.running:
            next_window = self.current_window.show_display()
            if self.current_window.id == "menu":
                if next_window == -1:
                    self.running = False
                elif next_window == 1:
                    self.current_window = Seqlist()
                elif next_window == 2:
                    self.current_window = ChainList()
                elif next_window == 3:
                    self.current_window = DoubleChainList()
            else:
                self.current_window = Menu()