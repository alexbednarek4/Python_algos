
#    # O(n) time | O(n) space

# def maxSubsetSumNoAdjacent(array):
# 	if not len(array):
# 		return 0
# 	elif len(array) == 1:
# 		return array[0]
# 	# make copy of entire input array
#     maxSums = array[:]
# 	# value at index 1 will be the greater of the first two indices
# 	maxSums[1] = max(array[0], array[1])
# 	# iterate over array starting at index 2, until end of array
# 		# at each index, take either the previous maxSum or i-2 + current
# 	for i in range(2, len(array)):
# 		maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
# 	return maxSums[-1]

 # O(n) time | O(1) space

def maxSubsetSumNoAdjacent(array):
	if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]
	#
    second = array[0]
	first = max(array[0], array[1])
	# iterate over array starting at index 2, until end of array
		# at each index, take either the previous maxSum or i-2 + current
	for i in range(2, len(array)):
		currentMax = max(first, second + array[i])
		second = first
		first = currentMax
	return first