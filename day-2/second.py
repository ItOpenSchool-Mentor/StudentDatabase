# Defining the List
name_list = ["John", "Smith", "Alex"]

print(name_list)  
print("=" * 50)

print("Ist Element   : ", name_list[0])
print("IInd Element : ", name_list[1])
print("IIIrd Element : ", name_list[2])


# Define a Tuple

tpl1 = (1, "Apple", 3.5, "John", True, 1)
print("=" * 50)

print(tpl1)
print("Ist Element   : ", tpl1[0])
print("IInd Element   : ", tpl1[1])
print("IIIrd Element   : ", tpl1[2])
print("IVth Element   : ", tpl1[3])
print("Vth Element   : ", tpl1[4])
print("VI Element   : ", tpl1[5])


print("=" * 50)
print(name_list)
name_list[0] = "Tom"
print(name_list)


tpl1[1] = "Orange"
print(tpl1)
