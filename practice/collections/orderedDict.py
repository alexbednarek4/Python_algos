# OrderedDict is a dictionary subclass which remembers the order in which the entries were added.
from collections import OrderedDict
d = OrderedDict()
d[1] = 'a'
d[2] = 'l'
d[3] = 'e'
d[4] = 'x'
print(d)
print(d.keys())
d[1] = 'A'
print(d)