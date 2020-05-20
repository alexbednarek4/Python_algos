# First In, First Out (FIFO)

# Queue using Python Deque
    # A deque is a double ended queue
    # we can use append and popleft methods on a deque

from collections import deque
# my_queue = deque()
# my_queue.append(3)
# my_queue.append(6)
# my_queue.append(9)
# my_queue.append(12)
# print(my_queue)
# print(my_queue.popleft())

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()

    def get_size(self):
        return len(self.queue)

q = Queue()
q.enqueue(3)
q.enqueue(6)
q.enqueue(9)
q.enqueue(12)
print(q.queue)
print(q.get_size())
print(q.dequeue())
print(q.get_size())
