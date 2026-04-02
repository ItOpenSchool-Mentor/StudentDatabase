# Flatten a Nested List Using LC
list = [[1, 2], [3, 4, 5], [6, 7], [8, 9, 10]]
flatten_list = [item for sublist in list for item in sublist]

print(f"Original Nested List : {list}")
print(f"Flattened List       : {flatten_list}")

print("-" * 30)

result = []
for sl in list:
    for item in sl:
        result.append(item)
print(result)
