import re

def split_at_uppercase(text):
    words = re.split(r'(?=[A-Z])', text) 
    return [word for word in words if word] 

s = input("Enter your string: ")
print("Split words:", split_at_uppercase(s))
