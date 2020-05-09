# For loops used for looping over iterables
people = ['John', 'Paul', 'Sara', 'Susan']

# for person in people:
#     print(person)

# #Break 
# for person in people:
#     if person == 'Sara':
#         break
#     print(person)

#Continue
# for person in people:
#     if person == 'Sara':
#         print(f"Found {person}")
#         continue
#     print(person)

#Range
for i in range(len(people)):
    print(f"Person at element {i} is {people[i]}")

#While
count = 1
while count <= 10:
    print(count)
    count+=1