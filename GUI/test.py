from utils.Binary_search_tree import Binary_search_tree

tree = Binary_search_tree()

tree.insert(30)
tree.insert(20)
tree.insert(10)
tree.insert(5)
tree.insert(40)
tree.insert(60)

return_f = tree.search_element(100)

print(return_f)

tree.get_walkin_array("suffix")
