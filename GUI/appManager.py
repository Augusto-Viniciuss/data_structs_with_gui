import pygame
from windowManager import WindowManager
from menu import Menu
from sequentialList import SequentialList
from linkedList import LinkedList
from doublyLinkedLIst import DoublyLinkedList
from stack import Stack_
from common_queue import Common_Queue
from tree import Tree_



class AppManager():
    def __init__(self):
        pygame.init()
        self.running = True
        self.current_window = None

    def run_app(self):
        self.current_window = Menu()

        while self.running:
            next_window = self.current_window.show_display()
            if next_window == "quit":
                self.running = False
            elif next_window == "menu":
                self.current_window = Menu()
            elif next_window == 2:
                self.current_window = SequentialList()
            elif next_window == 3:
                self.current_window = LinkedList()
            elif next_window == 4:
                self.current_window = DoublyLinkedList()
            elif next_window == 5:
                self.current_window = Stack_()
            elif next_window == 6:
                self.current_window = Common_Queue()
            elif next_window == 7:
                self.current_window = Tree_()
