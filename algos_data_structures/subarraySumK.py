"""
Given an array of integers and an integer (k), determine total number of continuous subarrays
whose sum is equal to k.

Ex: Arr = [1, 1, 1], k = 2
Output: 2
"""
def subArraySum(nums, k):
    # Keep track of sum
    # Utilize hashmap, initialize with 0 because the runningSum starts at 0
    runningSum = 0
    count = 0
    hashmap = {0:1}

    # We want to create a running sum starting from the zeroith element
    # If there are two numbers that have a difference of k, we know that there is a continuous array 
        # between those two indexes
    for num in nums:
        runningSum += num
        if runningSum - k in hashmap:
            count += hashmap[runningSum - k]
        if runningSum in hashmap:
            hashmap[runningSum] += 1
        else:
            hashmap[runningSum] = 1
    return count

print(subArraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))