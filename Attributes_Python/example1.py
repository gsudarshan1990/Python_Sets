#Example of the class attribute

class Dog:
    """This is a class describing about the Dog and contains class attributes"""
    genus ="Cannibe"
    family ="Cannie"

print(Dog.genus)
print(Dog.family)

print("Example of the class and instance attributes")
#Example of class and instance attributes

class Dog:
    """This is a class describing about the Dog and contains the class and instance attributes"""
    genus ="Cannis"
    family = "Cannidae"

    def __init__(self, breed, name):
        """
        Initializing the values
        """
        self.breed = breed
        self.name = name

D1 = Dog("Alsiacian", "Jimmy")
print(D1.breed)
print(D1.name)
print(Dog.genus)
print(Dog.family)

print("Example with class , instance, classmethod decorator and static method decorator")

class Dog:
    """This describes about the class"""
    genus = 'Cannus'
    family = 'Cannidae'

    def __init__(self, breed, name):
        """
        Initializing the instance variables
        :param breed: assigning to breed
        :param name: assigning to name
        """
        self.breed = breed
        self.name = name

    @classmethod
    def tag_name(cls, tagname):
        breed = tagname['breed']
        name = tagname['name']
        return cls(breed, name)

    @staticmethod
    def can_bark():
        print("All dogs can bark")

    def bark(self):
        print('few dogs can bark')

print(Dog.genus)
print(Dog.family)
d1 = Dog('Alcesian', 'Jimmy')
t1={'breed' : 'Rajapalaym','name' : 'Jackie' }
D2=d1.tag_name(t1)
print(D2.name)
print(D2.breed)

#Private Attributes

class Dog:
    """
    This is the class which describes about the Dog
    """
    def __init__(self, breed, name):
        """
        Initializes the variables
        :param breed: assigning to breed
        :param name: assigning to name
        """
        self.breed = breed
        self.name = name
        self.__tag = f"{name} | {breed}"

d1 = Dog('Ada', 'Roweltier')
print(d1.__dict__)
print(d1._Dog__tag)

#Using of the property decorator

print("Usage of the property decorator")

class Dog:
    """
    This is the class which describes about the Dog class
    """
    def __init__(self, breed, name, nickname):
        """
        Initializing the values
        :param breed: assignig to breed
        :param name: assigning to name
        :param nickname: assigning to nickname
        """
        self.breed = breed
        self.name = name
        self._nickname = nickname

    @property
    def nickname(self):
        """
        returning the nickname
        :return:
        """
        return self._nickname

    @nickname.setter
    def nickname(self, newnickname):
        """
        Setting the nickname
        :param newnickname:
        :return:
        """
        self._nickname = newnickname

d1 = Dog('Alsacian', 'jimmy', 'B')
print(d1.nickname)
d1.nickname = 'A'
print(d1.nickname)