"""
This is the third example of exception

"""

blog_posts = [{'Photos':3, 'Likes' :21, 'Comments':2},{'Likes':13, 'comments':2 ,'shares':1}, {'photos':5, 'Likes':33, 'comments':8, 'shares':3},
              {'comments':4,'shares':2}, {'photos':3 , 'Likes':19, 'comments':3}]

total_likes = 0
for post in blog_posts:
    try:
        total_likes = total_likes+post['Likes']
    except KeyError:
        print('Key is not found')

print(total_likes)

