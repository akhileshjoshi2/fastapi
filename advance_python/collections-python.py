#collections: Counter, namedtuple, ordereddict, defaultdict, deque
from collections import Counter

a = "aaaaabbbbccccddddeee"
print(Counter(a))
print(Counter(a).items())
print(Counter(a).values())
print(Counter(a).keys())

print(Counter(a).most_common(1))
print(Counter(a).most_common(1)[0][0])
print(Counter(a).most_common(2))


print(Counter(a).elements())
my_counter = Counter(a).elements()
print(list(my_counter))


from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt)
print(pt.x, pt.y)


from collections import OrderedDict
#ordered Dict remembers the order, however after Python version 7 dictionaries do remember their order



from collections import defaultdict
d = defaultdict(float)
d['a'] = 1
d['b'] = 2

print(d)
print(d['a'])
print(d['c'])


d = defaultdict(list)
print(d['a'])

d = {}
# print(d['c']) #here it will raise a error but with default dict it wont



from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)

d.appendleft(4)

print(d)
d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)
d.append(5)
d.append(7)
d.extend([1,2,3,3])
d.extendleft([9,8,7,8])
print(d)

d.rotate(2)
print(d)

d.rotate(-1)
print(d)
