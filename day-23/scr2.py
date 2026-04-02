# Extract Digits from a String
data = "a123b45c678d9ef#"
result = [int(dig) for dig in data if dig.isdigit()]

print(f"String : {data}")
print(f"Number List : {result}")
