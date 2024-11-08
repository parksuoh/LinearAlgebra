u = [1, 2, 4]
v = [7, 3, 2]

n = len(u)
w = []

for i in range(0, n):
    val = u[i] * v[i]
    w.append(val)

print(w)