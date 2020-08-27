"""
This is another example of exception
"""

di =[{"Puppies":17, 'kittens':9,'Birds':23,'Fish':90,'hamsters':49},{'Puppies':23,'Birds':29,'Fish':20,'Mice':20,'snakes':7},
     {'Fish':203,'hamsters':93,'snakes':25,'kittens':89},{'Birds':20,'Puppies':90,'Snakes':21,'Fish':10,'kittens':67}
     ]

total_puppies  =0

for dict1 in di:
    try:
        total_puppies+=dict1['Puppies']
    except KeyError:
        print('Key not found on the dictionary')

print(total_puppies)
