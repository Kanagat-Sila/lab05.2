import re

s = input('Input your string: ')

c = re.compile('[a-z]+_[a-z]+')

n = c.search(s)

if n:
    print("Found: ", n.group())

else:
    print('No match')