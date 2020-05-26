# Max Heap
    # underlying data structure is a list
    # Every node is less than or equal to its parent
    # Tree structure
    # Insert Time: O(logn)
    # Remove max time: O(logn)
    # Get Max time: O(1)

"""
A max heap always bubbles the highest value to the top, so it can be removed instantly
Public functions: push, top (peek), pop
Private functions: swap, __floatUp, __bubbleDown

Ex: i = 4
parent(i) = i/2 = 2
left(i) = i * 2 = 8
right(i) = i * 2 + 1 = 9 
"""

class MaxHeap():
    def __init__(self, items = []):
        super().__init__()
        # We start our elements at index 1 in a max heap
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)
    # Push
        # Add value to end of list
        # Float value up to proper position
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)
    
    # Pop
        # Move max to end of list
        # Delete it
        # Bubble down item at index 1 to proper position
        # Return max
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    # return value at top of heap
    def top(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
    
    def __bubbleDown(self, index):
        # Left and right children
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)