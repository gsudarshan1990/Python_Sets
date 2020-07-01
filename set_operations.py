#Union and Intersection of 2 set
color={'Red','Yellow','blue','Orange'}
Fruit={'Orange','Apple','Grape','Banana'}
print(color.union(Fruit))
print("Using Operator |: ",color | Fruit)
print(color.intersection(Fruit))
print("Using Operator &",color & Fruit)

#Union and Intersection of more than two set
set1={'a','b','c','d'}
set2={'c','d','e','f'}
set3={'e','f','g','h'}
print(set1.union(set2,set3))
print(set1 | set2 | set3)


set1={'a','b','c','d'}
set2={'b','c','d','e'}
set3={'c','d','e','f'}
print(set1.intersection(set2,set3))
print(set1 & set2 & set3)

#difference
print(color-Fruit)
print(color.difference(Fruit))

set1={'a','b','c','d','e','f'}
set2={'c','d','e'}
set3={'c','d','e','f'}

print(set1.difference(set2,set3))
print(set1 - set2 - set3)

#symmetric difference
print(color ^ Fruit)
print(color.symmetric_difference(Fruit))

#subset and superset
x={1,2}
y={1,2,3,4,5}
print(x.issubset(y))
print(y.issuperset(x))