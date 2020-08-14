"""
Given a sorted array nums, remove the duplicates in-place such that each 
element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2]

Your function should return length = 2, with the first two elements of nums 
being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums 
being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""
def removeDuplicates(nums):
    # Initialize two pointers, First and second elements
    # if same, move second pointer forward
    # if not same, move first pointer forward, then replace value at p1 with value at p2
    p1 = 0
    p2 = p1+1

    while p2 < len(nums):
        if nums[p1] == nums[p2]:
            p2+=1
        else:
            p1+=1
            nums[p1] = nums[p2]
    # Since we are returning the pointer, and the count begins at 0, return p1+1
    return p1+1


print(removeDuplicates([1, 1, 2, 2, 4, 5, 5]))