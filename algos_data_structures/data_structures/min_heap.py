class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
		# declare heap property, invoke buildHeap and pass input array as argument
        self.heap = self.buildHeap(array)
	# O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array)-2) // 2
		# begin at firstParentIdx, then go down to zeroith element
		for currentIdx in reversed(range(firstParentIdx+1)):
			self.siftDown(currentIdx, len(array)-1, array)
        return array
	# O(log(n)) time | O(1) space	
    def siftDown(self, currentIdx, endIdx, heap):
        # Write your code here.
		childOneIdx = currentIdx*2+1
		# Important: If a node has no children (i.e. its a leaf node)
			# we can't sift it down
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx*2+2 if currentIdx*2+2 <= endIdx else -1
			# If there is a second child node, and that node is smaller than the first child
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			# the first child node is smaller, so that is the idx to swap
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap] < heap[currentIdx]:
				# If current node is bigger than smaller of two child nodes, swap them
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx*2+1
			else:
				# otherwise, our current node is <= both child nodes and is in correct position
				return
        
	# O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
		parentIdx = (currentIdx-1) // 2
		# If we were dealing with a maxHeap, it would be 'and heap[currentIdx] > heap[parentIdx]'
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx-1) // 2
        
    def peek(self):
        # Peak at root value of heap.
        return self.heap[0]

    def remove(self):
        # Write your code here.
		# Swap root el with last el, then pop root el from end
		self.swap(0, len(self.heap)-1, self.heap)
		valToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap)-1, self.heap)
		return valToRemove
		
    def insert(self, value):
        # Write your code here.
		self.heap.append(value)
		# siftingUp the last el of the array
		self.siftUp(len(self.heap)-1, self.heap)
	
	def swap(self, element1, element2, heap):
		heap[element1], heap[element2] = heap[element2], heap[element1]
