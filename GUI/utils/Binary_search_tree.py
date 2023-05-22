from .Node import Node

class Binary_search_tree:
    def __init__(self):
        self.root = None
        self.empty = True

    def is_empty(self):
        return self.empty

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
        if self.is_empty:
            self.root = Node(value)
            self.empty = False
        else:
            aux_node = self.root
            
            while True:
                if value < aux_node.get_value():
                    if aux_node.get_previous_node() == None:
                        aux_node.set_previous_node = Node(value, aux_node, None)
                        break
                    else:
                        aux_node = aux_node.get_previous_node()
                elif value > aux_node.get_value():
                    if aux_node.get_next_node() == None:
                        aux_node.set_next_node = Node(value, None, aux_node)
                        break
                    else:
                        aux_node = aux_node.get_next_node()

        return True

    def show_tree(self, node = root, walking_type = "prefix"):
        if self.is_empty():
            return
        else:
            if walking_type == "prefix":
                printf(node.get_value())

            if node.get_previous_node() != None:
                self.show_tree(node.get_previous_node(), walking_type)

            if walking_type == "infix":
                print(node.get_value())

            if node.get_next_node() != None:
                self.show_tree(node.get_next_node(), walking_type)

            if walking_type == "suffix":
                print(node.get_value))
