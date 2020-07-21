def RPS(rounds):
    rps = ['r', 'p', 's']
    permutations = []
    helper('', rps, rounds, permutations)
    return permutations

def helper(game, rps, rounds, permutations):
    length = len(rps)
    if rounds == 0:
        permutations.append(game)
    else:
        for hand in range(length):
            helper(game + rps[hand], rps, rounds-1, permutations) 

print(RPS(3))