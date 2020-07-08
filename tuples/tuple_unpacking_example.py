"""
This is the example of the tuple unpacking
"""

tuple2 = (1,2,3.3, [1,3,4],(11,89,3),{1,2},{"a":1,"b":2})

a,b,c,d,e,f,g = tuple2
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#Advanced tuple unpacking

a,*middle,b = tuple2

*head, _ =tuple2

_,*tail =tuple2
print(*middle)
print(*head)
print(*tail)
