# Optimized list to perform easy insertion and deletion
 # Used to implement a queue
from collections import deque
a = ['a', 'l', 'e', 'x']
d = deque(a)
d.appendleft('python')
print(d)
# remove 'python'
d.popleft()