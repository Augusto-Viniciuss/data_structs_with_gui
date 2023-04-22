import pygame
from windowManager import WindowManager
from menu import Menu
from sequentialList import SequentialList
from linkedList import LinkedList
from doublyLinkedLIst import DoublyLinkedList

class AppManager():
    def __init__(self):
        pygame.init()
        self.running = True
        self.current_window = None

    def run_app(self):
        self.current_window = Menu()

        while self.running:
            next_window = self.current_window.show_display()
            if next_window == -1:
                self.running = False
            elif next_window == 1:
                self.current_window = Menu()
            elif next_window == 2:
                self.current_window = SequentialList()
            elif next_window == 3:
                self.current_window = LinkedList()
            elif next_window == 4:
                self.current_window = DoublyLinkedList()
