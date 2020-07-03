"""
Merging of the two dictionaries
"""
dict1={'a':1 , 'b':0 , 'c' :3 }
dict2 ={'z':10, 'x':12 , 'y':15}

dict1.update(dict2)

dict3={**dict1, **dict2}
