#tuple is ordered, immutable, allows duplicates
b = ("akhilesh", 2, True)
print(b)
print(type(b))

c = ("max")
print(type(c))

c = ("max",)
print(type(c))

a =[1,2,3,4]
print(tuple(a))


#access item with index 
item = b[0]
print(item)
print(a[2])


my_tuple = ('a', 'a', 'b', 'c', 'd')
print(my_tuple.count('b'))
print(len(my_tuple))

print(my_tuple.index('b'))

print(list(my_tuple))


#slicing with tuple
print(my_tuple[1:])

#unpacking tuple
my_tuple = "max", 28, "Boston"
#or
my_tuple = ("max", 28, "Boston")
name, age, city = my_tuple
print(name, age, city)

#
my_new = (0,1,2,3,4,5)
i1,i2,*i3 = my_new
print(i1,i2,i3)

