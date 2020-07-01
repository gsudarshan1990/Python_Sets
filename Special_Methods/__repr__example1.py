class Shirt:
    """Class describes the details of the shirt"""
    def __init__(self, color, size, brand):
        """
        Initializes the values of the parameter
        :param color: color of the shirt
        :param size: size of the shirt
        :param brand: brand of the shirt
        """
        self.color = color
        self.size = size
        self.brand = brand

    def __str__(self):
        return f'color :{self.color}, size :{self.size}, brand:{self.brand}'

    def __repr__(self):
        return f"Shirt({self.color},{self.size},{self.brand})"

s1=Shirt("Blue","XL","Levis")
print("--str--",str(s1))
print("--repr--",repr(s1))
