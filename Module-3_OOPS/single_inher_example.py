class usersignup: #super
    fnm=""
    lnm=""
    unm=""
    pas=""
    def createuser(self):
        self.fnm=input("Enter Firstname:")
        self.lnm=input("Enter Lastname:")
        self.unm=input("Enter Username:")
        self.pas=input("Enter Password:")


class userlogin(usersignup): #sub
    def usersignin(self):
        print("Username:",self.unm)
        print("Password:",self.pas)


userlog=userlogin()
userlog.createuser()
userlog.usersignin()