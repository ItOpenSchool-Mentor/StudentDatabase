# zip function
# 1. Python built-in
# 2. Combines multiples into Pairs
# 3. zip stops at Shortest List
lst1 = [1, 2]
lst2 = ["apple", "orange", "banana"]
res = zip(lst1, lst2)
print(res, type(res))
for v1, v2 in res:
    print(v1, v2)

