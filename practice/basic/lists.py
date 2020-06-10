#Lists are collections which are ordered and changeable. Allows duplicate items, unlike a set
import statistics

"""
Map, Filter, Reduce in Python

"""

# Convert to list where degrees are in fahrenheight
# temps = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokyo', 27), ('New York', 28), ('London', 22), ('Beijing', 32)]

# c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)
# # Map converter function to list of data
# print(list(map(c_to_f, temps)))


# Filter function: Used to select certain data from list, tuple or other collection of data
 # Find all data above average

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Reverse the list!!!!!!!
print(data[::-1])


# avg = statistics.mean(data)
# print(avg)

# print(list(filter(lambda x: x > avg, data)))
# print(list(filter(lambda x: x < avg, data)))
# # Remove missing data
# countries = ['', 'Argentina', '', 'Brazil', 'Chile', '', 'Colombia', '', 'Ecuador', '', '', 'Venezuela']
# print(list(filter(None, countries))) # Prints non-false values





#
# numbers = [1, 2, 3, 4, 5]
# fruits = ["Apples", "Oranges", "Grapes", "Pears"]
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
# x = [1, 3, 5, 6, 3, 5]
# x.remove(3)
# print(x)


