# Creating a List with Condition
marks = [35, 50, 25, 55, 63, 91, 49]
result = [f"{m} : Pass" if m >= 50 else f"{m} : Fail" for m in marks]

print(f"Marks : {marks}")
print(f"Result : {result}")
