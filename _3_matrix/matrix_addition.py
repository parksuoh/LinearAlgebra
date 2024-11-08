A = [[2, 7], [3, 4], [6, 1]]
B = [[1, 4], [4, -1], [2, 5]]

n = len(A)
p = len(A[0])

res = []

for i in range(0, n):
    row = []
    for j in range(0, p):
        val = A[i][j] + B[i][j]
        row.append(val)
    res.append(row)

print(res)