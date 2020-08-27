"""
This is another example of exception

"""

countries =[['spain','France','Greece','Portugal','Romania','Germany'],['USA','MEXICO','Canada'],['Japan','China','Korea','Vietnam','Combodia'],['Argentina','Chile','Brazil','Ecuador','Uruguay','Venezula'],['Australia'],['Zimbabwe','Morocco','Kenya','Ethiopia','SouthAfrica'],['Antartica']]

count =[]

for list1 in countries:
    try:
        count.append(list1[2])
    except IndexError:
        print('List out of bound')

print(count)