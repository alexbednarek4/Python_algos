# Stacks are Last In, First Out(LIFO)

#Key operations
    # Push, Pop, Peek, Clear

# Use wrapper class to implement a stack
class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def top(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    
    def __str__(self):
        return str(self.stack)

