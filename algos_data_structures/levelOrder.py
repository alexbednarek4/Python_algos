def levelOrder(root):
    # Base case
    if not root:
        return []
    # Declare return array
    result = []
    # Declare queue
    q = []
    q.append(root)
        
    while len(q) > 0:
        currentLevel = []
        # Iterate over current queue length
            # The key is that each iteration, the queue length pertains to the level
        for node in range(len(q)):
            # grab first node in queue
            current = q.pop(0)
            # push value into current level array
            currentLevel.append(current.val)
            # check if this node has left 
            if current.left != None:
                q.append(current.left)
            # check if this node has right
            if current.right != None:
                q.append(current.right)
        # after each level, push currentLevel array into result array
        result.append(currentLevel)       
    return result