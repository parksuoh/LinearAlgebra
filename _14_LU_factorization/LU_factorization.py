


def lu_decomp(A):
    n = len(A)
    p = len(A[0])

    L = [ [0]*p for i in range(0, n) ]
    U = []
    
    for i in range(0, n):
        a = A[i]
        val = 1/a[i]
        L[i][i] = 1/val
        a = [element * val for element in a]
        # 1 -1 -1
        # 0, 1, -1
        print("a ==> ",a)
        U.append(a)

        for j in range(i+1, n):
            row = A[j] 
            print("row ==> ", row)
            #0
            # 0, -2, 2
            # -1, 5, 2
            #1
            # 0, 4, 1
            a_tmp = [element * -row[i] for element in a] 
            print("a_tmp ==> ", a_tmp)
            #0
            # 0, 0, 0
            # 1, -1, -1
            #1
            # 0, -4, 4
            L[j][i] = row[i] 
            #0
            # 1 0 -> 0
            # 2 0 -> -1
            #1
            # 2 1 -> 4
            A[j] = [ a_tmp[k] + row[k] for k in range(p) ] 
            print("A[j] ==> ", A[j])
            #0
            # 1 -> 0, -2, 2
            # 2 -> 0, 4, 1
            #1
            # 2 -> 0, 0, 5
    return L, U


A = [[2 ,-2, -2], [0, -2, 2], [-1, 5, 2]]
L, U = lu_decomp(A)
print("L ==> ", L)
print("U ==> ", U)