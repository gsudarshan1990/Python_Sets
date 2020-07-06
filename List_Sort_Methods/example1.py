"""
Usage of the sort functions for the list
"""

vowels=['o','a','i','u','e']
vowels.sort(reverse = True)
print(vowels)


takesecond = lambda x:x[1]
random_list_tuple =[(1,2),(9,7),(10,15),(12,6),(3,10),(15,4)]
random_list_tuple.sort(key=takesecond)
print(random_list_tuple)
