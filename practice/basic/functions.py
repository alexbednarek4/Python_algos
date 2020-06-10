#Functions
def sayHello(name = 'Joe'):
    print(f'Hello {name}')
#if we run with an argument, we get the argument name
sayHello('Alex') #prints Hello Alex
#if we run without an argument, the default name parameter is used
sayHello() #prints Hello Joe

# Return values
def getSum(num1, num2):
    total = num1+num2
    return total

num = getSum(2, 4)
print(num)

#A lambda function is a small anonymous function
#A lambda function can take any number of arguments, but can only have one expression, similar to JS arrow functions
 
getSum = lambda num1, num2 : num1 + num2
print(getSum(10, 10))