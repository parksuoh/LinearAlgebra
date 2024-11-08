A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def diag(A):
    n = len(A)
    D = []

    for i in range(0, n):
        row = []
        for j in range(0, n):
            if i == j:
                row.append(A[i][j])
            else:
                row.append(0)
        D.append(row)

    print(D)
    return D

def diag_ele(A):
    n = len(A)
    d = []
    for i in range(0, n):
        d.append(A[i][i])
    return d


print(diag_ele(A))

a = [1, 9, 5]

def ele2diag(a):
    n = len(A)
    D = []

    for i in range(0, n):
        row = []
        for j in range(0, n):
            if i == j:
                row.append(A[i][j])
            else:
                row.append(0)
        D.append(row)
    return D

D = ele2diag(a)

print(D)



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

AD = matmul(A, D)
DA = matmul(D, A)
print(AD)
print(DA)