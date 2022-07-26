class usersignup: #super
    fnm="Sanket"
    lnm="Chauhan"
    unm="sanket2020"
    pas="tops?123"
    def createuser(self):
        print("Firstname:",self.fnm)
        print("Lastname:",self.lnm)
        print("Username:",self.unm)
        print("Password:",self.pas)


class userlogin(usersignup): #sub
    def usersignin(self):
        print("Username:",self.unm)
        print("Password:",self.pas)


userlog=userlogin()
userlog.createuser()
userlog.usersignin()