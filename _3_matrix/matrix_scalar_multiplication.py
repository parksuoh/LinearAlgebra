A = [[2, 7], [3, 4], [6, 1]]
b = 2

n = len(A)
p = len(A[0])

res = []

for i in range(0, n):
    row = []
    for j in range(0, p):
        val = b * A[i][j]
        row.append(val)
    res.append(row)

print(res)