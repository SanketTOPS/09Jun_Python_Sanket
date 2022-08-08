import re

class createaccount :
    fname = ""
    lname = ""
    username = ""
    password = ""
    cpassword = ""
    vusername = ""
    vpassword = ""
    
    def signup(self) :
        print("Sign up")
        self.fname = input("enter your first name : ")
        self.lname = input("enter your last name : ")
        self.username = input("enter your usename : ")
        self.vusername=re.findall('^[A-Z]+[a-z0-9]',self.username)
        if self.vusername:
            print("Username confirm")
        else:
            print("Check your username")

        self.password = input("enter your password : ")
        self.vpassword=re.findall('[A-Za-z0-9_@#$/*&!%]{6,8}',self.password)
        if self.vpassword:
            self.cpassword = input("enter confirm password :")
            if self.password == self.cpassword:
                print("password confirm")
            else:
                print("password does not match!")
        else:
            print("password invalid!")
        
    def login(self):
        print("Log in")
        self.lusername=input("enter your username: ")
        if self.username == self.lusername:
            print("username confirm")
        else:
            print("Invalid username")

        self.lpassword = input("enter your password : ")
        if self.password == self.lpassword:
            print("password confirm")
        else:
            print("Invalid password")
            
c=createaccount()

c.signup()
c.login()
