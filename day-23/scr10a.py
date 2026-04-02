# Using & = Bitwise AND Operator
# When used with Set, Set Intersection
# Finding Common Elements
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = list(set(a) & set(b))
d = set(a) & set(b)

print(d)
print(c)
