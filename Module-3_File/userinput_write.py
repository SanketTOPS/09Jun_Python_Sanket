fl=open('stdata.txt','w')

"""name=input("Enter Name:")
sub=input("Enter Subject:")
city=input("Enter City:")"""

"""fl.write(f"Name:{name}")
fl.write(f"\nSubject:{sub}")
fl.write(f"\nCity:{city}")
fl.write("\n------------------\n")"""

if fl.writable():
    print("Yes...you can write anything!")
else:
    print("Error...Plz check your file mode.")
