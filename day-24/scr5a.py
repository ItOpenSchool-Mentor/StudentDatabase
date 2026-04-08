# Transpose matrix
matrix = [[1, 2, 3],
          [4, 5, 6]
          ]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
print(transpose)