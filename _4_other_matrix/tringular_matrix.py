A =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def u_tri(A):
    n = len(A)
    p = len(A[0])
    utri = []

    for i in range(0, n):
        row = []
        for j in range(0, p):
            if i > j :
                row.append(0)
            else:
                row.append(A[i][j])
        utri.append(row)

    return utri

def l_tri(A):
    n = len(A)
    p = len(A[0])
    ltri = []

    for i in range(0, n):
        row = []
        for j in range(0, p):
            if i < j :
                row.append(0)
            else:
                row.append(A[i][j])
        ltri.append(row)

    return ltri

print(l_tri(A))
