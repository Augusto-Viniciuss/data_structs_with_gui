from utils.Binary_search_tree import Binary_search_tree

tree = Binary_search_tree()


tree.insert(30)
tree.insert(20)
tree.insert(10)
tree.insert(40)
tree.insert(60)

return_f = tree.search_element(30)
print("tentando achar a raiz: " + str(return_f))
return_f = tree.search_element(40)
print("tentando achar um nó maior: " + str(return_f))
return_f = tree.search_element(20)
print("tentando achar um nó menor: " + str(return_f)+ "\n")

array_x = tree.get_walkin_array("prefix")
print("prefix:")     
print(array_x)
array_x = tree.get_walkin_array("infix")
print("infix:")  
print(array_x)
array_x = tree.get_walkin_array("suffix")
print("suffix:")  
print(array_x)

#o 60 está sendo printado dentro da funcao ".get_walking_array"
