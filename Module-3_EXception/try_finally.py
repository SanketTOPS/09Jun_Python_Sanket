try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",a+b)
except Exception as error:
    print(error)
finally:
    print("This is Exception handing in Python!")

"""else:
    print("This is Exception handing in Python!")"""