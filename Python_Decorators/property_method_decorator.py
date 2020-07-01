class User:
    def __init__(self, name, age, display_name):
        self.name = name
        self.age = age
        self._display_name = display_name

    @property
    def display_name(self):
        return self._display_name

u1=User("abc",29,"rahul")
print(u1.display_name)
