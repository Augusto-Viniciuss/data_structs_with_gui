from .Node import Node

class Doubly_linked_list:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.qtd_elements = 0
        
    def is_empty(self):
        if self.qtd_elements == 0:
            return True
        else:
            return False
        
    def get_size(self):
        return self.qtd_elements
    
    def get_element(self, position):
        if self.is_empty() or position <= 0 or position > self.qtd_elements:
            return None
        else:
            if position > (self.qtd_elements / 2):
                aux_node = self.last_node
                
                for i in range(self.qtd_elements, (position - 1)):
                    aux_node = aux_node.get_previous_node()
                
                return aux_node.get_value()
            else:
                aux_node = self.first_node
                
                for i in range(position - 1):
                    aux_node = aux_node.get_next_node()
                    
                return aux_node.get_value()
    
    def get_position(self, value):
        if self.is_empty():
            return None
        else:
            aux_node = self.first_node
            
            for i in range(self.qtd_elements):
                if aux_node.get_value() == value:
                    return i + 1
                
                aux_node = aux_node.get_next_node()
            
            return None
    
    def insert(self, value, position):
        if position <= 0 or position > (self.qtd_elements + 1):
            return False
        else:
            if position == 1:
                new_node = Node(value, self.first_node)
                if self.is_empty():
                    self.last_node = new_node
                else:
                    self.first_node.set_previous_node(new_node)
                self.first_node = new_node
            elif position == (self.qtd_elements + 1):
                new_node = Node(value)
                new_node.set_previous_node(self.last_node)
                self.last_node.set_next_node(new_node)
                self.last_node = new_node
            else:
                if position > (self.qtd_elements / 2):
                    aux_node = self.last_node

                    for i in range(self.qtd_elements, (position - 2), -1):
                        aux_node = aux_node.get_next_node()
                    
                    new_node = Node(value, aux_node.get_next_node(), aux_node)
                    new_node.get_next_node().set_previous_node(new_node)
                    aux_node.set_next_node(new_node)
                else: 
                    aux_node = self.first_node

                    for i in range(position - 2):
                        aux_node = aux_node.get_next_node()
                    
                    new_node = Node(value, aux_node.get_next_node(), aux_node)
                    new_node.get_next_node().set_previous_node(new_node)
                    aux_node.set_next_node(new_node)
                
            self.qtd_elements = self.qtd_elements + 1    
            
            return True
            
    def remove(self, position):
        if self.is_empty() or position < 0 or position > self.qtd_elements:
            return None
        else:
            if position == 1:
               removed_value = self.first_node.get_value()
               self.first_node = self.first_node.get_next_node()
               self.first_node.set_previous_node(None)
               
               self.qtd_elements = self.qtd_elements - 1
               
               return removed_value
            elif position == self.qtd_elements:
                removed_value = self.last_node.get_value()
                self.last_node = self.last_node.get_previous_node()
                self.last_node.set_next_node(None)
                
                self.qtd_elements = self.qtd_elements - 1
                
                return removed_value
            else: 
                if position > (self.qtd_elements / 2):
                    aux_node = self.last_node

                    for i in range(self.qtd_elements, (position - 2), -1):
                        aux_node = aux_node.get_next_node()
                    
                    removed_value = aux_node.get_next_node().get_value()
                    aux_node.set_next_node(aux_node.get_next_node().get_next_node())
                    aux_node.get_next_node().set_previous_node(aux_node)
                else: 
                    aux_node = self.first_node

                    for i in range(position - 2):
                        aux_node = aux_node.get_next_node()
                    
                    removed_value = aux_node.get_next_node().get_value()
                    aux_node.set_next_node(aux_node.get_next_node().get_next_node())
                    aux_node.get_next_node().set_previous_node(aux_node)

                