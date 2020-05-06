def smallestDifference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    indexOne = 0
    indexTwo = 0
    
    #declare and initialize smallest and current variables
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while indexOne < len(arr1) and indexTwo < len(arr2):
        firstNum = arr1[indexOne]
        secondNum = arr2[indexTwo]
        # if firstNumber is less than second, we close the gap by incrementing first pointer
        if firstNum < secondNum:
            current = secondNum - firstNum
            indexOne += 1
        # if secondNumber is less than first, we close the gap by incrementing second pointer
        elif secondNum < firstNum:
            current = firstNum - secondNum
            indexTwo += 1
        else:
            return [firstNum, secondNum]
        
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]

    return smallestPair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))