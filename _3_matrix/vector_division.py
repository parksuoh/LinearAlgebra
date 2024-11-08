u = [6, 5, 9]
v = [2, 2, -3]

n = len(u)
w = []

for i in range(0, n):
    val = u[i] / v[i]
    w.append(val)

print(w)