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
        super()

    def bubble_up(self, value):
    
    def bubble_down(self, value):

    # Push
        # Add value to end of list
        # Float value up to proper position
    def push(self, value):
    
    # Pop
        # Move max to end of list
        # Delete it
        # Bubble down item at index 1 to proper position
        # Return max
    def pop():

    # return value at top of heap
    def top(self):


    
