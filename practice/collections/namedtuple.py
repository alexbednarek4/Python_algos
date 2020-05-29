# Returns a tuple with a named value for each element in the tuple
from collections import namedtuple

a = namedtuple('courses', 'name, technology')
# s = a('data science', 'python')
# print(s)
s = a._make(['artificial intelligence', 'python'])
print(s)