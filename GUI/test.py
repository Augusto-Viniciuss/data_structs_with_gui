from utils.Stack import Stack

common_queue = Stack()



common_queue.push(1)
common_queue.push(2)
common_queue.push(3)
randommm = common_queue.get_size()


for i in range(randommm):
    print(common_queue.listelements(i))

