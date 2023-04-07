from utils.Linked_list import Linked_list
from utils.Sequential_list import Sequential_list
from utils.Doubly_linked_list import Doubly_linked_list

lits_int = Sequential_list()

lits_int.insert(5,1) 
lits_int.insert(8,2) 
lits_int.insert(10,3) 
lits_int.insert(14,4) 
lits_int.insert(2,5) 

print("Size: " + str(lits_int.get_size()))

for i in range(1, lits_int.get_size() + 1):
    print("Element " + str(lits_int.get_element(i)))
   

print("Size: "+ str(lits_int.get_size()))

lits_int.insert(10,4)

for i in range(1, lits_int.get_size() + 1):
    print("Element " + str(lits_int.get_element(i)))
   

print("Size: " + str(lits_int.get_size()))

lits_int.remove(1)

print("Size: "+ str(lits_int.get_size()))

for i in range(1, lits_int.get_size() + 1):
    print("Element " + str(lits_int.get_element(i)))
   

print("Size: "+ str(lits_int.get_size()))


