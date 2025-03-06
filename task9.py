import re

def insert_spaces(text):
    return re.sub(r'(?<!^)([A-Z])', r' \1', text)

s = input()
print(insert_spaces(s))
