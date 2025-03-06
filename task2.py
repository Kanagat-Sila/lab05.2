import re

s = input('Input your string: ')

c = re.compile('ab{2, 3}')

n = c.search(s)

if n:
    print("Found: ", n.group())

else:
    print('No match')