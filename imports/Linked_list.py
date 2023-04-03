import Node

class Linked_list:
    def __init__(self):
        self.first_node = None
        self.qtd_elements = 0
        
    def is_empty(self):
        if self.qtd_elements == 0:
            return True
        else:
            return False
        
    def get_size(self):
        return self.qtd_elements
    
    def get_element(self, position):
        if self.is_empty() or position < 0 or position > self.qtd_elements:
            return None
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
        if position < 0 or position > (self.qtd_elements + 1):
            return False
        else:
            if position == 1:
                new_node = Node(value, self.first_node)
                self.first_node = new_node
            else:
                aux_node = self.first_node

                for i in range(position - 2):
                    aux_node = aux_node.get_next_node()
                
                new_node = Node(value, aux_node.get_next_node())
                aux_node.set_next_node(new_node)
                
            self.qtd_elements = self.qtd_elements + 1
            
            return True
            
    def remove(self, position):
        if self.is_empty() or position < 0 or position > self.qtd_elements:
            return None
        else:
            aux_node = self.first_node
            
            for i in range(position - 1):
                aux_node = aux_node.get_next_node()
                
            removed_value = aux_node.get_next_node().get_value()
            aux_node.set_next_node(aux_node._get_next_node().get_next_node())
            
            self.qtd_elements = self.qtd_elements - 1
            
            return removed_value

                