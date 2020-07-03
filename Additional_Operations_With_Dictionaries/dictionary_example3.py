"""
Usage of the one line if else for obtaining the values from dictionary
"""

dict1={'name':'rahul','age':29}

result1 = dict1['gender'] if 'gender' in dict1 else 'unknown'
print(result1)

result1 = dict1.get('gender','0')
print(result1)