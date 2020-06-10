# Almost everything in python is an object

#Create class

class User:
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
   
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1
    

#Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name}, I am {self.age} years old and my balance is {self.balance}'

#Init user object
Alex = User("Alex Bednarek", "alex@alex.io", 24)
print(Alex.greeting())
print(type(Alex))

#Init customer
James = Customer("James Johnson", 'jimmy@james.io', 25)
James.set_balance(500)
print(James.greeting())