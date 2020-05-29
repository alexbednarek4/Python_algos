# Dictionary subclass which calls a factory function to supply missing values
from collections import defaultdict
d = defaultdict(int)

d[1] = 'python'
d[2] = 'alex'
print(d[3])