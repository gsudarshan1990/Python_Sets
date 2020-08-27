"""
This is another example of exception

"""

full_list = ['ab','cde','fgh','i','jkml','nop','qr','s','tv','wxy','z']

attempt = []

for element in full_list:
    try:
        attempt.append(element[1])
    except IndexError:
        print('Index out of range')

print(attempt)