import copy

def zero_mat(n, p):
    Z = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            row.append(0)
        Z.append(row)
    return Z

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


def sign(a):
    res = 1
    if a < 0:
        res = -1
    return res


def v_add(u, v):
    n = len(u)
    w = []

    for i in range(0, n):
        val = u[i] + v[i]
        w.append(val)
    return w


def householder(v):
    n = len(v)
    outer_mat = outer_product(v, v)
    inner_val = inner_product(v, v)
    V = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            val = (2/inner_val) * outer_mat[i][j]
            row.append(val)
        V.append(row)
    H = subtract(identity(n), V)
    return H

def inner_product(a, b):
    n = len(a)
    res = 0
    for i in range(0, n):
        res += a[i]*b[i]
    return res

def outer_product(a, b):
    res = []
    n1 = len(a)
    n2 = len(b)
    for i in range(0, n1):
        row = []
        for j in range(0, n2):
            val = a[i]*a[j]
            row.append(val)
        res.append(row)
    return res

def subtract(A, B):
    n = len(A)
    p = len(A[0])
    res = []

    for i in range(0, n):
        row = []
        for j in range(0, p):
            val = A[i][j] - B[i][j]
            row.append(val)
        res.append(row)
    return res


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

def qr_householder(A):
    n = len(A)
    p = len(A[0])

    H_list = []

    for i in range(0, p):
        if i == 0:
            A1 = copy.deepcopy(A)
            exA = A1
        elif i < p-1:
            Ai = []
            for j in range(1, len(exA)):
                row = []
                for k in range(1, len(exA[0])):
                    row.append(HA[j][k])
                Ai.append(row)
            exA = Ai
        elif i == p-1:
            Ap = []
            for j in range(1, len(HA)):
                Ap.append(HA[j][1])
            exA = Ap

        # 열 추출
        if i < p-1:
            a = transpose(exA)[0]
        else:
            a = exA
        nm = norm(a)

        # e 생성
        e = [1]
        for j in range(0, len(a)-1):
            e.append(0)

        # v 생성
        tmp_e = []
        for j in range(0, len(e)):
            val = sign(a[0])*nm*e[j]
            tmp_e.append(val)
        v = v_add(a, tmp_e)

        # H 생성
        H = householder(v)

        # H*A
        if i == p-1:
            HA = []
            for j in range(0, len(H)):
                val = 0
                for k in range(0, len(H[0])):
                    val += H[j][k]*exA[k]
                HA.append(val)
        else:
            HA = matmul(H, exA)

        H_list.append(H)

        if i > 0:
            tmp_H = identity(len(A))
            for j in range(i, len(A)):
                for k in range(i, len(A)):
                    tmp_H[j][k] = H_list[-1][j-i][k-i]
            H_list[-1] = tmp_H
        
        Q = copy.deepcopy(H_list[0])
        for j in range(0, len(H_list)-1):
            Q = matmul(Q, H_list[j+1])
        
        R = copy.deepcopy(H_list[-1])
        for j in range(1, len(H_list)):
            R = matmul(R, H_list[-(j+1)])
        R = matmul(R, A)

        return Q, R




