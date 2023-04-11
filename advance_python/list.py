#copy
a = [1,2,3,4,5,1,1]
print(a[1:10])
print(a.count(1))
print(a.index(3))
b = a
b.append(7)
print(a,b)


#new copy

#first method
b = list(a)
b.append(8)
print(a,b)


#second method
b = a[1:4]
print(a,b)


#third method

b = a.copy()
b.append(9)
print(a,b)

#forth method

b=[i for i in a]
print(a,b)

# ###Remove
# print(f"Before a is: {a}")
# a.remove(7)
# print(f"After remove a is : {a}")
#
# #
# print(f"Before a is: {a}")
# a.pop(1)
# print(f"After remove a is : {a}")
#
# ##
# print(f"Before a is: {a}")
# a.pop()
# print(f"After remove a is : {a}")
#

###