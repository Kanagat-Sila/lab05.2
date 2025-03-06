import re

s = input('Input your string: ')

c = re.compile('[A-Z][a-z]+')

n = c.search(s)

if n:
    print("Found: ", n.group())

else:
    print('No match')