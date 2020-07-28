# Given a target amount n and an array of distinct positive integers representing coin denominations, 
# write a function that returns the number of ways to make change for that target amount
# given the specific coin denominations
def makeChange(denoms, n):
    # For each denomination, create an array of ways from 0 to n
    ways = [0 for amount in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount-denom]
    return ways[n]

print(makeChange([2, 3, 4, 7], 7))