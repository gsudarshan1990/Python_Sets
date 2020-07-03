"""
Difference between == and is
"""

a =[1,2,3,4,5]
b = a
print(b)
print(a)
print("Both the values are same")
print("b==a",b == a)#prints true
print("b is a", b is a)#print true


c = list(a)
print(c)
print(a)
print('c==a:', c==a)#prints True
print('c is a:', c is a)#prints False