import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('akhilesh', 32)


def encode_complex(z):
    if isinstance(z, User):
        # just the key of the class name is important, the value can be arbitrary.
        return {z.__class__.__name__: True, "name":z.name, "age":z.age}
    else:
        raise TypeError(f"Object of type '{z.__class__.__name__}' is not JSON serializable")


zjson = json.dumps(user, default=encode_complex)
# zJSON = json.dumps(user, default=encode_complex)
print(zjson)