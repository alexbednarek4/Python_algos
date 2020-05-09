#A tuple is a collection which is ordered and unchangeable. Allows duplicates

#Create tuple
fruits = ("Apples", "Pineapples", "Blueberries")

#If you only have one value in the tuple, leave a trailing comma
fruits2 = ("Apples")
# print(fruits2, type(fruits2))

#get value
# print(fruits[1])

#Can't change value
# fruits[0] = "Grapes"
# A set is a collection which is unordered and unindexed. No duplicates
fruit_set = {'Apples', 'Mangoes', 'Pineapples'}
print(fruit_set)

#check if element in a set
print('Apples' in fruit_set)

#add to set
fruit_set.add("Grapes")
fruit_set.add('Apples')
print(fruit_set)
#remove from set
fruit_set.remove("Grapes")

#clear fruit set
# fruit_set.clear()

# #delete
# del(fruit_set)
# print(fruit_set)