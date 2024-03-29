from .Node import Node

class Binary_search_tree:
    def __init__(self):
        self.root = None
        self.aux_count = 0
        self.walking_values = [None] * 15 

    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False

    def search_element(self, value):
        if self.is_empty():
            return False
        else:
            aux_node = self.root

            while aux_node != None:
                if aux_node.get_value() > value:
                    aux_node = aux_node.get_previous_node()
                elif aux_node.get_value() < value:
                    aux_node = aux_node.get_next_node()
                elif aux_node.get_value() == value:
                    return True

            return False

    def insert(self, value):
        if self.is_empty():
            self.root = Node(value)
        else:
            aux_node = self.root
            
            while True:
                if value < aux_node.get_value():
                    if aux_node.get_previous_node() == None:
                        aux_node.set_previous_node(Node(value))
                        break
                    else:
                        aux_node = aux_node.get_previous_node()
                elif value > aux_node.get_value():
                    if aux_node.get_next_node() == None:
                        aux_node.set_next_node(Node(value))
                        break
                    else:
                        aux_node = aux_node.get_next_node()
                elif value == aux_node.get_value():
                    return False

        return True

    def get_walkin_array(self, walking_type = "prefix"):
        self.aux_count = 0
        self.walking(self.root, walking_type)
        return self.walking_values

    def walking(self, node = None, walking_type = "prefix"):
        if self.is_empty():
            return
        else:
            if walking_type == "prefix":
                self.walking_values[self.aux_count] = node.get_value()
                self.aux_count += 1

            if node.get_previous_node() != None:
                self.walking(node.get_previous_node(), walking_type)

            if walking_type == "infix":
                self.walking_values[self.aux_count] = node.get_value()
                self.aux_count += 1

            if node.get_next_node() != None:
                self.walking(node.get_next_node(), walking_type)

            if walking_type == "suffix":
                self.walking_values[self.aux_count] = node.get_value()
                self.aux_count += 1
