from utils.Linked_list import Linked_list
from utils.Sequential_list import Sequential_list
from utils.Doubly_linked_list import Doubly_linked_list

list_i = Doubly_linked_list()

list_i.insert(5,1) 
list_i.insert(8,2) 
list_i.insert(10,3) 
list_i.insert(14,4) 
list_i.insert(2,5) 

print("initial Size: " + str(list_i.get_size()))

for i in range(1, list_i.get_size() + 1):
    print("Element " + str(list_i.get_element(i)))
   

list_i.insert(10,4)

print("\nnew Size: " + str(list_i.get_size()))

for i in range(1, list_i.get_size() + 1):
    print("Element " + str(list_i.get_element(i)))
   
n = 5
list_i.remove(n)

print("\nremoved position " + str(n) + ". Size: "+ str(list_i.get_size()))

for i in range(1, list_i.get_size() + 1):
    print("Element " + str(list_i.get_element(i)))


    
    
   




