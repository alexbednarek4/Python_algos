def threeNumSum(array):
    
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        # Declare pointers for each iteration
        left = 1
        right = len(array)-1
        while left < right:
            currSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left+=1
			elif currentSum > targetSum:
				right-=1
				
    return triplets

print(threeNumSum([]))