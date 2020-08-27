"""
This is another ZeroDivisionError Example

"""

list_=[2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,464,56,7,3,43,23]

num_list =[]

for num in list_:
    try:
        if 3%num == 0:
            num_list.append(num)
    except ZeroDivisionError:
        print('Zero Division Error')

print(num_list)