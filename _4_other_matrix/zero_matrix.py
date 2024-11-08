
def zero_mat(n, p):
    Z = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            row.append(0)
        Z.append(row)
    return Z

print(zero_mat(3,2))
