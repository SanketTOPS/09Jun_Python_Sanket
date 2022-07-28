class student:
    __stid=12
    __stnm="Mitesh"

    def getdata(self):
        print("This is getdata from student.")
    
    def __getsum(self,a,b):
        print("Sum:",a+b)
    
    def answer(self):
        self.__getsum(23,54)

st=student()
st.getdata()
st.answer()