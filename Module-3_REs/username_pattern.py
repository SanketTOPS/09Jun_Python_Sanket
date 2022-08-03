import re

#Sanket2020

username=input("Enter Username:")

usernm_pattern="^[A-Z]+[a-z]+[0-9]"

x=re.findall(usernm_pattern,username)

if x: #true
    print("Username is valid!")
else:
    print("Invalid Username!")