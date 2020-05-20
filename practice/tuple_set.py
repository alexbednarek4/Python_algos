#A tuple is a collection which is ordered and unchangeable. Allows duplicates
# Faster than lists
# Sequence type (all functions that we used on lists will work on tuples)

#Create tuple
# fruits = ("Apples", "Pineapples", "Blueberries")

# #If you only have one value in the tuple, leave a trailing comma
# fruits2 = ("Apples")
# # print(fruits2, type(fruits2))

# #get value
# # print(fruits[1])

# #Can't change value
# # fruits[0] = "Grapes"

# # Sorting a tuple -> this returns a new list of sorted elements
# z = ('Kevin', 'Alex', 'Claire', 'Rod')
# print(sorted(z))

# x = ()
# x = (1, 2, 3)
# x = 1, 2, 3
# x = 2,
# print(x, type(x))

# # tuples are immutable, BUT member objects can be mutable
# y = ([1, 2], 3)
# del(y[0][1])
# print(y)
# # concatenating tuples
# y += (4,)
# print(y)


# Sets
    # Fast access vs lists
        # Due to values being hashed
    # Math Set ops (union, intersection)
# x = {3, 5, 3, 5}
# print(x)

# y = set()
# print(y)

# list1 = [2, 3, 4]
# z = set(list1)
# print(z)
# z.add(7)
# print(z)

"""
Mathematical set operations
    intersection (AND): set1 & set2
    union (OR): set1 | set2
    symmetric difference (XOR): set1 ^ set2 difference (in set1 but not set2): set1 - set2
    subset (set2 constains set1): set1 <= set2
    superset (set1 constains set2): set1 >= set2
"""
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 - s2)
print(s1 <= s2)
print(s1 >= s2)

# # A set is a collection which is unordered and unindexed. No duplicates
# fruit_set = {'Apples', 'Mangoes', 'Pineapples'}
# print(fruit_set)

# #check if element in a set
# print('Apples' in fruit_set)

# #add to set
# fruit_set.add("Grapes")
# fruit_set.add('Apples')
# print(fruit_set)
# #remove from set
# fruit_set.remove("Grapes")

# #clear fruit set
# # fruit_set.clear()

# # #delete
# # del(fruit_set)
# # print(fruit_set)

