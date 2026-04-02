# Cartesian Product
list1 = [1, 2]
list2 = ['x', 'y', 'z']

result = [(x, y) for x in list1 for y in list2]
print(f"Ist List  : {list1}")
print(f"IInd List : {list2}")
print(f"Cartesian Product : {result}")

