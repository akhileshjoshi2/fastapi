a = {"name": "akhilesh", "city": "almora"}
print(a)
a.pop("name")
print(a)

mydict2 = dict(name="Marry", age=27, city="Boston")
print(mydict2)
del mydict2['name']
print(mydict2)
mydict2.pop('age')
print(mydict2)

mydict2 = dict(name="Marry", age=27, city="Boston")
mydict2.popitem()
print(mydict2)

#copy
print("\n\n")
a = {"name": "akhilesh", "city": "almora"}
b = a
print(a,b)
b["city"] = "kashmir"
print(a,b)
print("\n")
c = a.copy()
c["city"] = "nagpur"
print(a,c)

print("\n")
d = dict(a)

d["city"] = "rajathan"
print(a,d)

#merge
mydict2 = dict(name="Marry", age=27, city="Boston", email = "a@gmail")
a = {"name": "akhilesh", "city": "almora", "age": 22}
a.update(mydict2)
print(a)