#Lists are collections which are ordered and changeable. Allows duplicate items, unlike a set

#
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Pears"]
#
# numbers2 = list((1, 2, 3, 4, 5))


#Get value
print(fruits[1])
#Get length
print(len(fruits))

#Append to list
fruits.append("Pineapple")

#remove
fruits.remove("Grapes")

#Insert at position
fruits.insert(2, "Bananas")

#Remove by position
fruits.pop(2)

#reverse list
fruits.reverse()

#sort
fruits.sort(reverse=True)

#Change value
fruits[0] = "Blueberries"
print(fruits)