# How to find the second largest element in a BST

# Finding largest value in BST
def find_largest(root):
    current = root
    while current:
        if not current.right:
            return current.value
        current = current.right


def find_second_largest(root):
    if root is None or root.left is None and root.right is None:
        return "Tree must have at least 2 nodes"
    current = root
    while current:
        # Case: current is largest and has a left subtree
        # 2nd largest is largest in that subtree
        if current.left and not current.right:
            find_largest(current.left)
        
        # Case: current is parent of largest, and largest has no children
        # so current is 2nd largest
        if (current.right and
            not current.right.left and 
            not current.right.right):
                return current.value
        current = current.right