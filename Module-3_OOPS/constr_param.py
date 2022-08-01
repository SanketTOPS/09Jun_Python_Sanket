class student:
    def __init__(self,id,name):
        print("ID:",id)
        print("Name:",name)
    
    def getsum(self,a,b):
        print("Sum:",a+b)


stid=input("Enter ID:")
stnm=input("Enter Name:")

st=student(stid,stnm)
st.getsum(43,65)
