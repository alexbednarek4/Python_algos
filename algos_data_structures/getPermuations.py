# Given number of rounds to be played (rounds), return all permutations of possible rounds played
# Input: 2
# Output: [[r, r], [r, p], [r, s], [p, p], [p, r], [p, s], [s, s], [s, r], [s, p]]


def getPermutations(array):

    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations


def permutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        # We want to put all numbers that come after our current position, in our current position
        for j in range(i, len(array)):
            # Starts at j == 1
            swap(array, i, j)
            permutationsHelper(i+1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

print(getPermutations(['a', 'l', 'e', 'x']))