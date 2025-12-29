x = 10 * 100
y =  50 * 20

print("x = ", x)
print("y = ", y)
print("x == y ", x == y)   # True  (values same)
print("x is y", x is y)    #  True (objects same)
print("=" * 70)

a = 10
x = a * 100
y = 50 * 20
print("a = ", a)
print("x = ", x)
print("y = ", y)

print("x is y", x is y)   # False (objects different)
print("=" * 70)
##
##a = 10
##x = a * 100
##y = 50 * a * 2
##print(x is y) # False (objects different)
