class student:
    stid=12
    stnm='Ashok'

    def printdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

# Calling via object
"""st=student()
st.printdata()
st.stid=34
st.stnm="Nirav"
st.printdata()"""


# Calling via instance
student().printdata()
student().stid=67
student().stnm="Sanket"
student().printdata()