# Dictionary subclass for counting hashable objects
from collections import Counter

a = [1, 2, 1, 2, 1, 2, 3, 3, 4, 5, 6, 2, 1, 2]
count = Counter(a)
print(count)
# print(list(count.elements()))
print(count.most_common())
sub = {2:1, 6:1}
print(count.subtract(sub))
print(count.most_common())