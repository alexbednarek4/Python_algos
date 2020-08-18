# Given head of linked list, determine if there is a cycle

#? Leetcode
def detectCycle(head):

    # pointers iterating at different speeds, one visits each node, the other every other
    p1 = head
    p2 = head.next
# while they are never equal, we iterate
    while p1 != p2:
        # if we've reached the end of the linked list, its come to no avail
        if p2 == None or p2.next == None:
            return False
        # move our pointers to the next respective nodes
        p1 = p1.next
        p2 = p2.next.next

    # If we get to this point, it means p1 == p2 and there is a cycle so return True 
    return True




#? Algo Expert
def hasCycle(head):
    # Initialize pointers as head.next and head.next.next bc we don't want to start them off equal
    first = head.next
    second = head.next.next

    # iterate until pointers
    while first != second:
        first = first.next
        second = second.next.next
    
    # At this point, they are pointing to the same node.
        # move first back to head, then move pointers forward until they meet again
    first = head
    while first != second:
        first = first.next
        second = second.next.next

    return first




class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
