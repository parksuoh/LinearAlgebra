import copy

def transpose(A):
    n = len(A) 
    p = len(A[0]) 

    At = []

    for i in range(0, p):
        row = []
        for j in range(0, n):
            val = A[j][i]
            row.append(val)
        At.append(row)
    return At

def scalar_mul(b, A):
    n = len(A)
    p = len(A[0])

    res = []

    for i in range(0, n):
        row = []
        for j in range(0, p):
            val = b * A[i][j]
            row.append(val)
        res.append(row)
    return res

def det_rec(A):
    n = len(A)
    res = 0

    if n == 2:
        res = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return res
    
    for i in range(0, n):
        X = copy.deepcopy(A)
        X = X[1:]
        nx = len(X)

        for j in range(0, nx):
            X[j] = X[j][0:i] + X[j][i+1:]

        sign = (-1) ** (i % 2)
        sub_det = det_rec(X)
        res += sign * A[0][i] * sub_det
    
    return res

def inv(A):
    n = len(A)
    X = copy.deepcopy(A)

    C = []
    for i in range(0, n):
        row_C = []
        idx_r = list(range(0, n))
        idx_r.remove(i)
        # [1, 2]
        # [0, 2]
        # [0, 1]

        for j in range(0, n):
            idx_c = list(range(0, n))
            idx_c.remove(j)
            # [1, 2]
            # [0, 2]
            # [0, 1]
            M = []

            for k in idx_r:
                row_M = []
                for l in idx_c:
                    val = X[k][l]
                    row_M.append(val)
                M.append(row_M)
                
            Mij = det_rec(M)
            Cij = ((-1)**(i+j))*Mij
            row_C.append(Cij)
        C.append(row_C)
    
    adj = transpose(C)
    res = scalar_mul(1/det_rec(X), adj)

    return res

A = [[3, 2, 0], [-1, -3, 6], [2, 3, -5]]
print(inv(A))