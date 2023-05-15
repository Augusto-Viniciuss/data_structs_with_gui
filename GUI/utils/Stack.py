from .Node import Node

class Stack:
    def __init__(self, ):
        self.top = None
        self.qtd_elements = 0
        
    def is_empty(self):
        if self.qtd_elements == 0:
            return True
        else:
            return False
                
    def get_size(self):
        return self.qtd_elements
        
    def get_top(self):
        if not self.is_empty():
            return self.top.get_value()
        else:
            return None
        
    def push(self, value):
        if self.is_empty():
            self.top = Node(value)
        else:
            aux_node = Node(value, self.top)
            self.top = aux_node
            
        self.qtd_elements += 1
        
        return True
            
    def pop(self):
        if self.is_empty():
            return False
        else:
            self.top = self.top.get_next_node()
            self.qtd_elements -= 1
            
            return True
        

    def listelements(self, position):
        if self.qtd_elements==0:
            return False
        else:
            aux = self.top
            for x in range(position):
                aux = aux.get_next_node()
            return aux.get_value()