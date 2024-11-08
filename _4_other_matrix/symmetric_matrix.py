A = [[1, 0, 2], [0, 2, 1], [2, 1, 1]]

def transpose(A):

    n = len(A) # 2
    p = len(A[0]) # 1

    At = []

    for i in range(0, p):
        row = []
        for j in range(0, n):
            val = A[j][i]
            row.append(val)
        At.append(row)
    print(At)
    print(At == A)
    return At

print(transpose(A))

def matmul(A, B):
    n = len(A) 
    p1 = len(A[0]) 
    p2 = len(B[0]) 

    res = []

    for i in range(0, n):
        row = []
        for j in range(0, p2):
            val = 0
            for k in range(0, p1):
                val += A[i][k] * B[k][j]
            row.append(val)
        res.append(row)
    return res

AA = A
for i in range(0, 9):
    AA = matmul(AA, A)
    print(i+2," 제곱 = ", AA)
    print("transpose", transpose(AA))


