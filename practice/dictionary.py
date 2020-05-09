#Dictionary collection of unordered, muteable, indexed. No duplicate members
 
#creation
person = {
    'first_name': 'Alex',
    'last_name': 'Bednarek',
    'age': 24
}
# print(person, type(person))

# #Use constructor
# person2 = dict(first_name = 'Al', last_name= 'Guy')
# print(person2)

#get value
# print(person['first_name'])
# print(person.get('last_name'))

#Add key:value
person['phone'] = '555-555-5555'

#get dictionary keys
# print(person.keys())

#get dictionary items
# print(person.items())

#Copy dict, similar to spread operator, getting all values of objects
person2 = person.copy()
person2['city'] = 'NYC'
print(person2)

#these dictionaries are not pointing to the same thing
print(person != person2)

#remove item
del(person['age'])
person.pop('phone')
print(person)

#Clear
#person.clear()

#list of dicts
people = [
    {
        'name': 'Martha',
        'age': 30
    },
    {
        'name': 'Kevin',
        'age': 20
    },
]
#Dictionaries do not have dot notation like in JS. Must use bracket notation (safer anyways)
print(people[0]['name'])
