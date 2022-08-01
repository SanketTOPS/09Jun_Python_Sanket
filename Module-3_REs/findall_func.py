import re

mystr="This is Python!"

x=re.findall("is",mystr)

print(x)

if x: #true
    print("it's found..")
else:
    print("Error...Not found!")