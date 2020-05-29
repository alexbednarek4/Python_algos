# Dictionary like class for creating single view of multiple mappings
# Essentially returns a list of several other dictionaries
from collections import ChainMap
a = {1: 'alex', 2: 'python'}
b = {3: 'ML', 4: 'AI'}
a1 = ChainMap(a, b)
print(a1)