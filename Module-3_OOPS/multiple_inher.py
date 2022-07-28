class nirav:
    nid=0
    nsub=""

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")

class ashok:
    aid=0
    asub=""

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")
    
class prasiddh:
    pid=0
    psub=""

    def p_getdata(self):
        self.pid=input("Enter Prasiddh's ID:")
        self.psub=input("Enter Prasiddh's Subject:")

class tops(nirav,ashok,prasiddh):
    def printdata(self):
        print("----------Nirav Data----------")
        print("NIrav's ID:",self.nid)
        print("NIrav's Subject:",self.nsub)
        print("----------Ashok Data----------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("----------Prasiddh Data----------")
        print("Prasiddh's ID:",self.pid)
        print("Prasiddh's Subject:",self.psub)
    
tp=tops()
tp.n_getdata()
tp.a_getdata()
tp.p_getdata()

tp.printdata()


