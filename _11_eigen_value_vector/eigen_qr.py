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


def norm(a):
    n = len(a)
    res = 0
    for i in range(0, n):
        res += a[i]**2
    res = res**(0.5)
    return res

def inner_product(a, b):
    n = len(a)
    res = 0
    for i in range(0, n):
        res += a[i]*b[i]
    return res


def normalize(a):
    n = len(a)
    v = []
    for i in range(0, n):
        tmp = a[i]/norm(a)
        v.append(tmp)
    return v

def qr_gram(A):
    n = len(A)
    p = len(A[0])

    At = transpose(A)
    U = []
    norm_list = []

    V = []
    Q = []
    R = []

    for i in range(0, n):
        if i == 0:
            u = At[i]
            norm_u = norm(u)
            U.append(u)
            norm_list.append(norm_u)
        else:
            a = At[i]
            dp_list = []
            for j in range(0, i):
                dp = inner_product(a, U[j])
                dp_list.append(dp)

            u = []
            for j in range(0, n):
                val = a[j]
                for k in range(0, i):
                    val -= (dp_list[k]/norm_list[k]**2)*U[k][j]
                u.append(val)
            norm_u = norm(u)
            U.append(u)
            norm_list.append(norm_u)
        
        v = normalize(u)
        V.append(v)
    
    Q = transpose(V)

    for i in range(0, n):
        r = []
        for j in range(0, n):
            if i > j:
                r.append(0)
            else:
                r_ele = inner_product(At[j], V[i])
                r.append(r_ele)
        R.append(r)

    return Q, R


def identity(n):
    I = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        I.append(row)
    return I

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

def eig_qr(A):
    n = len(A)
    E = copy.deepcopy(A)
    V = identity(n)
    for i in range(0, 30):
        Q, R = qr_gram(E)
        E = matmul(R, Q)
        V = matmul(V, Q)
    return E, V

A = [[3, 2, 1], [2, 1, 4], [1, 4, 2]]
E, V = eig_qr(A)
print(E)
print(V)