#Lists are collections which are ordered and changeable. Allows duplicate items, unlike a set

#
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Pears"]
#
# numbers2 = list((1, 2, 3, 4, 5))


# #Get value
# print(fruits[1])
# #Get length
# print(len(fruits))

# #Append to list
# fruits.append("Pineapple")

# #remove
# fruits.remove("Grapes")

# #Insert at position
# fruits.insert(2, "Bananas")

# #Remove by position
# fruits.pop(2)

# #reverse list
# fruits.reverse()

# #sort
# fruits.sort(reverse=True)

# Sorted returns a NEW LIST
# fruits.sorted()

# Descending sort
# fruits.sort(reverse = True)

# #Change value
# fruits[0] = "Blueberries"
# print(fruits)

# tupl3 = (10, 20)
# new_list = list(tupl3)
# print(new_list)

# # list comprehensions
# a = [m for m in range(8)]
# print(a)
# b = [i**2 for i in range(10) if i>4]
# print(b)

# delete
# x = [5, 3, 8, 6]
# del(x[0])
# print(x)

# append
# x = [5, 3, 8, 6]
# x.append(7)
# print(x)

# # Extending or combining lists
# y = [12, 14]
# x.extend(y)
# print(x)

# Remove the first instance of an item
x = [1, 3, 5, 6, 3, 5]
x.remove(3)
print(x)
