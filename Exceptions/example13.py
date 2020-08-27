"""
This is another example exception
"""

sport =["hockey","basketball","soccer","tennis","football","baseball"]

ppl_play = {'hokey':4 ,"soccer":10,"football":15,"tennis":8}

for x in sport:
    try:
        print(ppl_play[x])
    except KeyError:
        print('Key is not found')

