"""
Can be surrounded by either single or double quotes

"""
name = "Alex"
age = 24

#Concatenation
# print("Hello, my name is "+ name + "and I am " + str(age) + " years old!")



#Arguments by position
# print("My name is {name} and I am {age}".format(name=name, age=age))

#F-Strings (3.6+)
# print(f"Hello, my name is {name} and I am {age}")

#String methods
s ='hello world'
#Capitalize first letter
print(s.capitalize()) #Hello world

#Make all uppercase
print(s.upper())

#Make all lowercase
print(s.lower())

#Swap case
print(s.swapcase())

#Length
print(len(s))

#Replace
print(s.replace('world', 'errbody'))
 
#count
sub = 'h'
print(s.count(sub))

#Starts with
print(s.startswith('hello'))

#ends with
print(s.endswith('d'))

#Split into a list
print(s.split())

#Find position
print(s.find('r'))

#Is all alphanumeric
print(s.isalnum())

#is alphabetic
print(s.isalpha())

#is numeric
print(s.isnumeric())
