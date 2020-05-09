"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output

[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""
class minStack:
    #Constructor
    def __init__(self):
        self.stack = []

    # push utilizing a tuple
    def push(self, x):
        curr_min = self.getMin()
        if curr_min is None or x < curr_min: 
            curr_min = x
        self.stack.append((x, curr_min))

    # pop
    def pop(self):
        self.stack.pop()
    
    # getMin
    def getMin(self):
        if not self.stack:
            return None
        return self.stack[-1][1]

    # top
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1][0]


newStack = minStack()
newStack.push(3)
newStack.push(2)
newStack.push(4)
# newStack.push(1)
print(newStack.stack)