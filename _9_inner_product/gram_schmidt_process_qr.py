A = [[1, 0, 1], [0, 1, 1], [1, 2, 0]]

n = len(A)
p = len(A[0])

a1 = []
a2 = []
a3 = []


for i in range(0, n):
    a1.append(A[i][0])
    a2.append(A[i][1])
    a3.append(A[i][2])

# u1
u1 = a1

# norm u1
norm_u1 = 0
for i in range(0, len(u1)):
    norm_u1 += u1[i]**2
norm_u1 = norm_u1**(0.5)

# u2
dp21 = 0
for i in range(0, len(u1)):
    tmp = a2[i]*u1[i]
    dp21 += tmp

u2 = []
for i in range(0, n):
    tmp = a2[i] - (dp21/norm_u1**2)*u1[i]
    u2.append(tmp)

# norm u2
norm_u2 = 0
for i in range(0, n):
    norm_u2 += u2[i]**2
norm_u2 = norm_u2**(0.5)

# u3
dp31 = 0
for i in range(0, n):
    tmp = a3[i]*u1[i]
    dp31 += tmp

dp32 = 0
for i in range(0, n):
    tmp = a3[i]*u2[i]
    dp32 += tmp

u3 = []
for i in range(0, n):
    tmp = a3[i] - (dp31/norm_u1**2)*u1[i] - (dp32/norm_u2**2)*u2[i]
    u3.append(tmp)

# norm u3
norm_u3 = 0
for i in range(0, n):
    norm_u3 += u3[i]**2
norm_u3 = norm_u3**(0.5)

# v
v1 = []
v2 = []
v3 = []
for i in range(0, n):
    tmp1 = u1[i]/norm_u1
    tmp2 = u2[i]/norm_u2
    tmp3 = u3[i]/norm_u3
    v1.append(tmp1)
    v2.append(tmp2)
    v3.append(tmp3)


Q = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, n ):
    Q[i][0] = v1[i]
    Q[i][1] = v2[i]
    Q[i][2] = v3[i]

print(Q)

# R
R = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, n):
    R[0][0] += a1[i]*v1[i]
    R[0][1] += a2[i]*v1[i]
    R[0][2] += a3[i]*v1[i]
    R[1][1] += a2[i]*v2[i]
    R[1][2] += a3[i]*v2[i]
    R[2][2] += a3[i]*v3[i]

print(R)

