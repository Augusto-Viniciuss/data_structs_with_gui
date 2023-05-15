from .Node import Node

class Queue:
    def __init__(self):
        self.begin = None
        self.end = None
        self.qtd_elements = 0
        
    def is_empty(self):
        if self.qtd_elements == 0:
            return True
        else:
            return False
    
    def get_size(self):
        return self.qtd_elements

    def get_begin_element(self):
        if not self.is_empty():
            return self.begin.get_value()
        else:
            return None
    
    def insert(self, value):
        if self.is_empty():
            aux_node = Node(value)
            self.begin = self.end = aux_node
        else:
            aux_node = Node(value)
            self.end.set_next_node(aux_node)
            self.end = aux_node
        
        self.qtd_elements += 1
            
        return True
            
    def remove(self):
        if not self.is_empty():
            self.begin = self.begin.get_next_node()
            self.qtd_elements -= 1
            
            return True
        else:
            return False
        
    def listelements(self, position):
        if self.qtd_elements==0:
            return False
        else:
            aux = self.begin
            for x in range(position):
                aux = aux.get_next_node()
            return aux.get_value()
