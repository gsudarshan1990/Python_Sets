def append_something(name):
    """Taking the person name and printing the name of the person"""
    print('The name of the person is {}'.format(name))

new_function = append_something
append_something("john")
new_function("Peter")

print("Taking the function as the argument")
def calling_function(function):
    """Taking the function object as parameter and returning the result of the function executed which is passed as argument"""
    name="Clive"
    return function(name)

new_function3=calling_function(append_something)
print(new_function3)

print("The function with in the function there by return")

def outer_func():
    """Returns an inner function"""
    def inner_funtion(name):
        print('The name of the person is {}'.format(name))
    return inner_funtion

function1=outer_func()
function1("Mark")

#creation of the decorator


def get_text(name):
    """Decorator can be utilized"""
    return name.upper()

def outer_decorator(function):
    """This is the decorator which takes the function as the object"""
    def inner_decorator(name):
        """Place where the argument of the outer function is called"""
        return "The age of the person {} and name of the person is {}".format(29,function(name))
    return inner_decorator


new_fuction1 =outer_decorator(get_text)
print(new_fuction1("suresh"))


