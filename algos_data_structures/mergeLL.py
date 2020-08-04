# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize list to return
        head = ListNode(0)
        pointer = head
        
        # Loop: We don't want to iterate for really niche edge cases
        # This is an easy way to continuously loop until we don't need to 
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                pointer.next = l2
                break
            elif l2 is None:
                pointer.next = l1
                break
            else:
                smallerVal = float('-inf')
                if l1.val < l2.val:
                    smallerVal = l1.val
                    l1 = l1.next
                else:
                    smallerVal = l2.val
                    l2 = l2.next
                    
            # Make new node using smallerval
                newNode = ListNode(smallerVal)
                pointer.next = newNode
                pointer = pointer.next
        return head.next
                    