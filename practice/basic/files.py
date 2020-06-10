# Open a file
my_file = open('myfile.txt', 'w')

#Get info
print('Name: ', my_file.name)
print('Is Closed: ', my_file.closed)
print('Opening mode: ', my_file.mode)

#Write to file
my_file.write('I love Python')
my_file.write(' and JS')
my_file.close()
print(my_file.closed)

#Append to file
my_file = open('myfile.txt', 'a')
my_file.write(' and Golang')
my_file.close()

#Read from file
my_file = open('myfile.txt', 'r+')
text = my_file.read(100)
print(text)

