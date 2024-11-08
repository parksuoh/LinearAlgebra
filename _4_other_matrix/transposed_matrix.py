A = [[1, 5], [3, 4], [6, 2]]

n = len(A) # 2
p = len(A[0]) # 1

At = []

for i in range(0, p):
    row = []
    for j in range(0, n):
        val = A[j][i]
        # 0 0
        # 1 0
        # 2 0
        row.append(val)
    At.append(row)

print(At)