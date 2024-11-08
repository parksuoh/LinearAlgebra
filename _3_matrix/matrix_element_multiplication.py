A = [[1, 5], [6, 4], [2, 7]]
B = [[5, -1], [1, 2], [4, 1]]

n = len(A)
p = len(A[0])

res = []

for i in range(0, n):
    row = []
    for j in range(0, p):
        val = A[i][j] * B[i][j]
        row.append(val)
    res.append(row)

print(res)