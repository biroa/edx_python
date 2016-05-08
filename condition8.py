string = input('give me a string')
if 'dog' in string and 'cat' not in string:
    print('Dog')
elif 'cat' in string and 'dog' not in string:
    print('Cat')
elif 'cat' in string and 'dog' in string:
    print('Dog')
else:
    print('None')

