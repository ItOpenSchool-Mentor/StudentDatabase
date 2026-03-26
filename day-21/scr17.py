# Extended Multiplication Table

numbers = [] # empty list, Can hold Max of 5 values

for i in range(1, 6):
    no = input(f"Enter no {i} : ")
    if no:
        numbers.append(int(no))
    else:
        break

# Generate Multiplication Table
spaces = 7

for j in range(1, 11):
    for i in numbers:
        print(f"{i} * {j} = {i * j}", end = "")
        print(f"{" " * spaces}", end = "")
    print()

print(f"Number List : {numbers}")
print("Script Over.....")