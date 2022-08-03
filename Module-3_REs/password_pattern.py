import re

password=input("Enter Password:")
cpassword=input("Enter Confirm Password:")

password_pattern="[A-Z@#$_.]+[a-z@#$_.]+[0-9@#$_.]"

x=re.findall(password_pattern,password)

if x:
    print("Password is valid!")
    if password == cpassword:
        print("Success!")
    else:
        print("Does not match your password!")
else:
    print("Invalid Password....Try again!")
