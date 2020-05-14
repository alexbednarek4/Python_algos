# Binary Search Tree class
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
	#Average: O(logn) time | O(1) space
	#Worst: O(n) time | O(1) space
    def insert(self, value):
		currNode = self
		while True:
			if value < currNode.value:
				if currNode.left is None:
					currNode.left = BST(value)
					break
				else:
					currNode = currNode.left
			else:
				if currNode.right is None:
					currNode.right = BST(value)
					break
				else:
					currNode = currNode.right
    	return self
	#Average: O(logn) time | O(1) space
	#Worst: O(n) time | O(1) space
    def contains(self, value):
        # Write your code here.
		currNode = self
		while currNode is not None:
			if value < currNode.value:
				currNode = currNode.left
			elif value > currNode.value:
				currNode = currNode.right
			else:
				return True
		return False
	#Average: O(logn) time | O(1) space
	#Worst: O(n) time | O(1) space
    def remove(self, value, parentNode = None):
		# Want to keep track of parent node bc we must reassign the child node of the parent of the node we are removing
		currNode = self
		while currNode is not None:
			if value < currNode.value:
				parentNode = currNode
				currNode = currNode.left
			elif value > currNode.value:
				parentNode = currNode
				currNode = currNode.right
			else:
				if currNode.left is not None and currNode.right is not None:
					currNode.value = currNode.right.getMinValue()
					#currNode.value = smallest value of right subtree
					currNode.right.remove(currNode.value, currNode)
				# We're going to come back to the root node case
				elif parentNode is None:
					if currNode.left is not None:
						currNode.value = currNode.left.value
						currNode.right = currNode.left.right
						currNode.left = currNode.left.left
					elif currNode.right is not None:
						currNode.value = currNode.right.value
						currNode.left = currNode.right.left
						currNode.right = currNode.right.right
					# Last edge case, imagine we want to move the root node that has no parent and no children
					else:
						# this is a single node tree, do nothing
						pass
				elif parentNode.left == currNode:
					parentNode.left = currNode.left if currNode.left is not None else currNode.right
				elif parentNode.right == currNode:
					parentNode.right = currNode.right if currNode.left is not None else currNode.right
				break
		return self
	def getMinValue(self):
		currNode = self
		while currNode.left is not None:
			currNode = currNode.left
		return currNode.value
        