#unordered, mutable, non duplicate
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)

print(my_set)
my_set.remove(2)
print(my_set)
my_set.discard(3)
print(my_set)
my_set.add(2)
my_set.clear()

my_set.add(1)
print(my_set.pop())
print(my_set)

#union, intersection, subset, etc check yourself