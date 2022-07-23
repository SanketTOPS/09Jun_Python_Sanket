#myset={'A','B','C','D','E'}

#print(myset)

#print(len(myset))

"""if "A" in myset:
    print("Yes...")
else:
    print("Noo")"""

#myset.add("F")
#myset.update(["G","H","A","B","C"])
#myset.remove("F")
#myset.pop()
#print(myset)

# -------------------------------------- #

myset={'A','B','C','D','E',"S"}
newset={'P','Q','R','S',"A","C"}

#x=myset.union(newset)
x=myset.intersection(newset)
print(x)