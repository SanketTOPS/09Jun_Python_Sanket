class grandFather:
    gold=0
    house=0

    def g_getdata(self):
        self.gold=(input("Enter the gold details:"))
        self.house=(input("Enter the house details:"))

class father(grandFather):
    bal=0
    car=0

    def f_getdata(self):
        self.bal=input("Enter the bank balance:")
        self.car=input("Enter the car detail:")

class son(father):

    def all_prop(self):
        print("Gold:",self.gold)
        print("House:",self.house)
        print("Bank balance:",self.bal)
        print("Car:",self.car)

sn=son()
sn.g_getdata()
sn.f_getdata()
sn.all_prop()

