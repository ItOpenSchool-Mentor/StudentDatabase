# Double the Even Numbers, keep ODD numbers Unchanged
nums = [1, 2, 3, 4, 5, 17, 20]
result = [no * 2 if no % 2 == 0 else no for no in nums]

print(f"Original Number List : {nums}")
print(f"Output List : {result}")
