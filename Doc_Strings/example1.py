def add(a,b):
    """Addition of two integers and returns the resulting integer"""
    return a+b

help(add)
print(add.__doc__)


class Triangle:
    """
    methods: find_area()
    provides information about the area of the trianlge
    find_perimeter()
    provides information about the perimeter of the triangle
    """
    def find_area(self,base,height):
        """
        :param base: base of the triangle
        :param height: height of the triangl;e
        :return: area of the triangle
        :raises: raises the valueerror if arguments are negative
        """
        if base <0 or height <0:
            raise ValueError("value should be positive")
        else:
            return (base*height)/2

    def find_perimeter(self,side1,side2,side3):
        """

        :param side1: one of the three side of the triangle
        :param side2: second side of the triangle
        :param side3: third side of the triangle
        :return: returns the perimeter of the triangle
        :raises: raises the valueerror if the argument is negative
        """
        if side1 <0 or side2 <0 or side3 <0:
            raise ValueError
        else:
            return side1+side2+side3

help(Triangle)
t1=Triangle()
print(t1.__doc__)


class TissueSample:
    """
    Arguments:
        Patient: Provides the name of the patient
        Code: Provides the code of the patient
        Diagnosis: Provides the diagnosis for the patient
    methods:
        show_data(): Displays information related to the patient
    """
    def __init__(self,patient,code,diagnosis):
        """
        Initializes the parameter
        :param patient: name of the patient
        :param code: type of the fever
        :param diagnosis: curing method
        """
        self.patient = patient
        self.code = code
        self.diagnosis = diagnosis

    def show_data(self):
        """
        displays the data
        :return: nothing
        """
        print("========data==========")
        print("Patient name:"+self.patient)
        print("Code name:"+self.code)
        print("Diagnosis name:"+self.diagnosis)

help(TissueSample)

#Documenting the functions

def freq_data(data):
    """calculates the frequency of letters from the given data
    :param data: list of numbers
    :return: dictionary of frequency of numbers
    :raises: raise the value error if no value in data
    """
    if not data:
        raise ValueError("List is empty")

    freq={}
    for element in data:
        if element not in freq:
            freq[element]=1
        else:
            freq[element]+=1

    return freq

help(freq_data)