class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeKthNode(head, k):
    # Initialize two pointers to begin at head of LL
    first = head
    second = head

    counter = 1
    while counter <= k:
        second = second.next
        counter += 1

    if second is None:
        






newLL = LinkedList()