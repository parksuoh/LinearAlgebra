A = [[3, 2, 0], [-1, -3, 6], [2, 3, -5]]

n = len(A)
p = len(A[0])

detA = 0

for j in range(0, p):
    print("11 = ",A[1][:j])
    print("22 = ",A[1][j+1:])
    M = [ A[1][:j]+A[1][j+1:], A[2][:j]+A[2][j+1:] ]
    print("M = ",M)
    Mij = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    print("Mij = ",Mij)
    Cij = ((-1)**(0+j))*Mij
    print("Cij = ",Cij)
    detA += A[0][j] * Cij
    print("detA = ",detA)

