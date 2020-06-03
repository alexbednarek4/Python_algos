# Given an array of n numbers and a shift value 'd', shift each element in the array by d 
# Python3 program to rotate an array by  
# d elements  
# Function to left rotate arr[] of size n by d*/ 
def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
  
# Function to left Rotate arr[] of size n by 1*/  
def leftRotatebyOne(arr, n):
    # store first element in temp 
    temp = arr[0] 
    # iterte over array
    for i in range(n-1): 
        # shift elements left by one 
        arr[i] = arr[i + 1]
        print(arr)
    arr[n-1] = temp 
          
  
# utility function to print an array */ 
def printArray(arr, size): 
    for i in range(size): 
        print("%d"% arr[i], end = ' ') 
  
   
# Driver program to test above functions */ 
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArray(arr, 7) 