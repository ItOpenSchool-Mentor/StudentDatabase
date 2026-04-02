# Transpose a Matrix using LC
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix :")
for row in matrix:
    print(row)
print()

# Transpose the Matrix
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)
for row in transpose:
    print(row)
print()
