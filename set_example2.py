set1=set(['foo','bar','bazz','foo','qux'])
print(set1)
set2=set(('foo','bar','bazz','foo','qux'))
print(set2)

s='quux'
print(set(s))
set3={'foo','bar','buzz','foo','qux'}
print(set3)

set3={'foo','bar','bazz'}
print(len(set3))

print('foo' in set3)
print('bar' in set3)

x1={'foo','bar','baz'}
x2={'baz','qux','quux'}
print(x1.union(x2))
print(x1 | x2)
x1={'foo','bar','baz'}
x1.union(('baz','qux','quux'))
print(x1)

a={1,2,3,4,5}
b={2,3,4,5,6}
c={3,4,5,6,7}
d={4,5,6,7,8}

print(a.union(b,c,d))
print(a.union([6,7,8,9,10]))
print(a | b | c | d)

x1={'foo','bar','baz'}
x2={'baz','qux','quzz'}
print(x1.intersection(x2))
print(x1 & x2)
print(x1.intersection(['baz','qux','quzz']))


a={1,2,3,4,5}
b={2,3,4,5,6}
c={3,4,5,6,7}
d={4,5,6,7,8}

print(a.intersection(b,c,d))
print(a & b & c & d)

#set difference
print(a.intersection((5,6,7,8,9,19)))
x1={'foo','bar','baz'}
x2={'baz','quz','quz'}
print(x1.difference(x2))
print(x1-x2)

a={1,2,3,30,300}
b={10,20,30,40}
c={100,200,300,400}

print(a.difference(b,c))
print(a-b-c)

#symmetric_difference
x1={'foo','bar','baz'}
x2={'baz','quz','quzz'}
print(x1.symmetric_difference(x2))
print(x1^x2)

a={1,2,3,4,5}
b={10,2,3,4,50}
c={1,50,100}

print(a^b^c)


a={1,2,3,4,5}
b={10,2,3,4,50}
c={1,50,100}

print(a^b^c)

#isdisjoint
x1={'foo','bar','baz'}
x2={'baz','qux','quxx'}
print(x1.isdisjoint(x2))

x2=x2-{'baz'}
print(x1.isdisjoint(x2))

x1={1,3,5}
x2={2,4,6}
print(x1.isdisjoint(x2))

#issubset

x1={'foo','bar','baz'}
print(x1.issubset({'foo','bar','baz','qux','quxx'}))
print("<= symbol")
print(x1<={'foo','bar','baz','qux','quxx'})

x2={'baz','qux','quux'}
print(x1.issubset(x2))
print(x1.issubset(x1))

#propersubset
print("*"*5+"proper subset"+"*"*5)
x1={'foo','bar'}
x2={'foo','bar','bazz'}
print(x1 < x2)

x1= {'foo','bar','bazz'}
x2={'foo','bar','bazz'}
print(x1<x2)


#superset
x1={'foo','bar','baz'}
x2={'foo','bar'}
print(x1.issuperset(x2))

x2={'baz','qux','quux'}
print(x1.issuperset(x2))

print("using symbol >=")
print(x1>=x2)
x1={'foo','bar','baz'}
x2={'foo','bar'}
print(x1>=x2)

#proper superset
print("====proper superset=========")
x1={'foo','bar','baz'}
x2={'foo','bar'}
print(x1 > x2)

x1={'foo','bar','baz'}
x2={'foo','bar','baz'}
print(x1>x2)
