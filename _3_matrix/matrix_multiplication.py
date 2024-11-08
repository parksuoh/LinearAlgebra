A = [[2, 7], [3, 4], [5, 2]]
B = [[3, -3, 5], [-1, 2, -1]]

n = len(A) #2 i
p1 = len(A[0]) #1 k
p2 = len(B[0]) #2 j

res = []

for i in range(0, n):
    row = []
    for j in range(0, p2):
        val = 0
        for k in range(0, p1):
            val += A[i][k] * B[k][j]
            # A[0][0] * B[0][0]
            # A[0][1] * B[1][0]

            # A[0][0] * B[0][1]
            # A[0][1] * B[1][1]

            # A[0][0] * B[0][2]
            # A[0][1] * B[1][2]
        row.append(val)
    res.append(row)

print(res)