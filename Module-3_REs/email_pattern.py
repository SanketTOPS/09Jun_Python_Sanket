import re

email=input("Enter your Email:")

#sanket2020@gmail.com
email_pattern="^[a-z0-9_]+@+[a-z]+[\.]+[a-z]{2,4}$"

x=re.findall(email_pattern,email)

if x:
    print("Valid Email!")
else:
    print("Error...Invalid Email.")
