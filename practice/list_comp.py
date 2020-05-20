import random

# get values within a range

under_10 = [x for x in range(10)]
print('under_10: ' + str(under_10))

# Get squared values

squares = [x**2 for x in under_10]
print('squares: ', str(squares))

# Get odd nums using mod
odds = [x for x in range(10) if x%2 == 1]
print('odds:', str(odds))

# get multiples of 10
ten_x = [x * 10 for x in range(10)]
print('ten_x: ', str(ten_x))

# Get all nums from a string
s = 'I love 2 go t0 the store 7 times a w3ek.'
nums = [x for x in s if x.isnumeric()]
print('nums: ' + ''.join(nums))

# Get index of a list item
names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
idx = [k for k, v in enumerate(names) if v == 'Anu']
print('index = ' + str(idx[0]))

# Delete an item from a list
letters = [x for x in 'ABCDEF']
random.shuffle(letters)
letas = [a for a in letters if a != 'C']
print(letters, letas)

