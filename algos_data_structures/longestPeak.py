def longestPeak(array):
    # Write your code here.
	# Keep track of current peak, greater than both adjacent els
	# Here we are keeping track of longest peak length
	longestPeakLength = 0
	i = 1
	# Begin traversing array
	while i < len(array) - 1:
		# At each element, check for a peak
		isPeak = array[i-1] < array[i] and array[i] > array[i+1]
		# if not a peak, move to next element
		if not isPeak:
			i+=1
			continue
		# if there is a peak, we begin expanding to left and right
			# we expanded until we ran out of bounds OR we are not strictly decreasing
		leftIdx = i-2
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx+1]:
			leftIdx-=1
		
		rightIdx = i+2
		while rightIdx <len(array) and array[rightIdx] < array[rightIdx - 1]:
			rightIdx+=1
			
		currentPeakLength = rightIdx - leftIdx - 1
		longestPeakLength = max(longestPeakLength, currentPeakLength)
		i = rightIdx
		
	return longestPeakLength
		
    