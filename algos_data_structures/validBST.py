# Given a binary search tree, return boolean that says if the tree is balanced or not.
def validateBST(tree):
    # Invoke helper method
    # Args: tree, minValue, maxValue
    # Traverse tree, while left val is less than parent,
    # and right val is greater than or equal to parent, return true
    return validateHelper(tree, float("-inf"), float("inf"))


def validateHelper(tree, minVal, maxVal):
    
    if tree is None:
        return True
    # False if current node is less than minValue and current node is greater than or equal to maxValue
    print(tree.value)
    if tree.value < minVal or tree.value >= maxVal:
        return False
    # climb back up the tree after going all the way to the left
        # This variable will hold a boolean
    leftIsValid = validateHelper(tree.left, minVal, tree.value)
    # Return true if both leftIsValid and value returned from validateHelper on right subtree return TRUE
    return leftIsValid and validateHelper(tree.right, tree.value, maxVal)


class binarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = binarySearchTree(10)
root.left = binarySearchTree(5)
root.left.left = binarySearchTree(2)
root.left.right = binarySearchTree(5)
root.left.left.left = binarySearchTree(1)
root.right = binarySearchTree(15)
root.right.left = binarySearchTree(13)
root.right.left.right = binarySearchTree(12)
root.right.right = binarySearchTree(22)

print(validateBST(root))
