# Reverse or Invert BST

def invert(root):
    if not root:
        return None
    # Switch child nodes
    temp = root.left
    root.left = root.right
    root.right = temp

    invert(root.left)
    invert(root.right)

    return root
