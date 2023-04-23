MAX_SIZE = 100

class Sequential_list:
    def __init__(self):
        self.list = []
        self.qtd_elements = 0
    
    def is_empty(self):
        if self.qtd_elements == 0:
            return True
        else:
            return False
    
    def is_full(self):
        if self.qtd_elements == MAX_SIZE:
            return True
        else:
            return False    

    def get_size(self):
        return self.qtd_elements
    
    def get_element(self, position):
        if self.is_empty() or position <= 0 or position > self.qtd_elements:
            return None
        else:
            return self.list[position - 1]
        
    def get_position(self, value):
        if self.is_empty():
            return None
        else:
            for i in range(self.qtd_elements):
                if value == self.list[i]:
                    return i + 1
                
            return None

    #def get_position(self, value, offset):
     #   if self.is_empty() or offset > self.qtd_elements:
      # else:
       #     for i in range((offset - 1), self.qtd_elements):
        #        if value == self.list[i]:
           #         return i + 1
         #       
          #  return None
    
    def insert(self, value, position):
        if position <= 0 or position > (self.qtd_elements + 1) or self.is_full():
            return False
        else:
            if position == (self.qtd_elements + 1):
                self.list.append(value);
            else:
                self.list.append(self.list[self.qtd_elements - 1])
                
                for i in range((self.qtd_elements - 1), (position - 1), -1):
                    self.list[i] = self.list[i - 1]
                    
                self.list[position - 1] = value
                
            self.qtd_elements = self.qtd_elements + 1
            
            return True
    
    def remove(self, position):
        if self.is_empty() or position <= 0 or position > self.qtd_elements:
            return None
        else:
            self.qtd_elements = self.qtd_elements - 1
            
            return self.list.pop(position - 1)
            
                
        
        