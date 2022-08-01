import re

mystr="This is Python! 56654"

#x=re.findall("[A-Z]",mystr)
#x=re.findall("[a-z]",mystr)
#x=re.findall("[0-9]",mystr)
#x=re.findall("[A-Za-z]",mystr)
#x=re.findall("[A-Za-z0-9]",mystr)
#x=re.findall("^This",mystr)
#x=re.findall("^[A-Z]",mystr)
#x=re.findall("[^A-Z]",mystr)
#x=re.findall("54$",mystr)
#x=re.findall("\w",mystr)
#x=re.findall("\W",mystr)
#x=re.findall(r"\bThis",mystr)
#x=re.findall("\B54",mystr)
#x=re.findall("\AThis",mystr)
#x=re.findall("54\Z",mystr)
#x=re.findall("\d",mystr)
#x=re.findall("\D",mystr)
#x=re.findall("This|That",mystr)
x=re.findall("Py..on",mystr)
print(x)

