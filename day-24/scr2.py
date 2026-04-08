# Unzipping - Reverse of zip
pairs = [('Aman', 90), ('Riya', 85)]
print(*pairs)

# Unzipping
names, marks = zip(*pairs)

print(names)
print(marks)
