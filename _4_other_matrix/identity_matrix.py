
def identity(n):
    I = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            if i == j :
                row.append(1)
            else:
                row.append(0)
        I.append(row)
    return I

print(identity(3))
