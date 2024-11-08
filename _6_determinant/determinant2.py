import copy
# 재귀함수로 determinant

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
            #  0     0  0:0      0  1:
            #  1     1  0:0      1  1:
            # X = [[-3, 6], [3, -5]]

            #  0     0  0:1      0  2:
            #  1     1  0:1      1  2:
            # X = [[-1, 6], [2, -5]]

            #  0     0  0:2      0  3:
            #  1     1  0:2      1  3:
            # X = [[-1, -3], [2, 3]]   

        sign = (-1) ** (i % 2)
        sub_det = det_rec(X)
        res += sign * A[0][i] * sub_det
    
    return res

A = [[3, 2, 0], [-1, -3, 6], [2, 3, -5]]

print(det_rec(A))
