# Remove Duplicates
nums = [1, 2, 2, 2, 1, 3, 3, 4, 2, 1, 4, 5]

unique = []
[unique.append(no) for no in nums if no not in unique]

print(f"Original Duplicate List : {nums}")
print(f"Unique List : {unique}")
