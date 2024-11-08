u = [7, 3, 9]
v = [2, 5, 7]

n = len(u)
w = []

for i in range(0, n):
    val = u[i] - v[i]
    w.append(val)

print(w)