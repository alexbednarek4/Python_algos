"""
you're given an array of integers and an integer. Write a function that moves all instances
of that integer to the end of the array and returns the array
The function should perform this in place (i.e. mutating original array)

sample input:
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2

sample output:
    [1, 3, 4, 2, 2, 2, 2, 2]
"""

def moveElementToEnd(array, toMove):
    # Write your code here.
	# Have one pointer at beginning and one at end
	# Linear time solution here due to the fact that IF we wanted to implement
	# binary search and shoot for O(logn) time, we would need a sorted array, which
	# requires an O(nlogn) operation, thus right away we know we want O(n)
	left = 0
	right = len(array) - 1
	while left < right:
		if array[right] == toMove:
			right -= 1
		if array[left] == toMove and array[right] != toMove:
			# temp = array[left]
			# array[left] = array[right]
			# array[right] = temp
			array[left], array[right] = array[right], array[left]
			
		else:
			left += 1
	return array
			