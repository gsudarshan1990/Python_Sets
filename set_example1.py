#empty set declaration
set1=set()

#when using set() we need to provide the iterable
set2=set([1,2,3,4,5,6])
set3=set('hello')
set4=set((1,2,3,4,5))

print(set1)
print(set2)
print(set3)
print(set4)

#when using curly braces we should not define the empty set
set5={'foo','bar','buzz','foo','qux'}
print(set5)
a={'q','u','u','x'}
print(a)

set6={'abbbac'}
set7=set('abbbac')
print(set7)

#set can contain the objects of different types.
x={2,2.01,'abc',(1,2,3)}
print(x)

#length of the set1
set8={'a','d','b','c'}
my_set={'cat','dog','fruit','apple'}
print('cat' in my_set)
print('orange' in my_set)

set9={'a','b','c'}
set9.add('d')
print(set9)
set10={'e','f','g','h'}
set9.update(set10)
print(set9)

#update can also send the tuple,list and string

b=[1,2,3]
set9.update(b)
c=('sonu','deepu')
set9.update(c)
print(set9)
#remove operation
set11={1, 'e', 'a', 2, 3, 'c', 'd', 'f', 'g', 'sonu', 'deepu', 'h', 'b'}
set11.remove('e')
#set11.remove('z') shows keyError as 'z' is not there in the set
set11.discard('c')
print(set11)
set11.pop()
print(set11)
set12={2, 3, 'sonu', 'a', 'f', 'd', 'h', 'deepu', 'b', 'g'}
set12.clear()
print(set12)

