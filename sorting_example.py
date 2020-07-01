list_ =['Cherry', 'Apple', 'BlueBerry']
list_.sort(key = len)
print(list_)

list2  = sorted(list_, key = lambda x:len(x))
print(list2)