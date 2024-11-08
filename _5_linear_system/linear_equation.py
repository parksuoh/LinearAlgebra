X = [[3, 1, 2], [2, 6, -1], [4, 0, -1]]
Y = [5, 1, 3]

x0 = X[0]
x1 = X[1]
x2 = X[2]

y0 = Y[0]
y1 = Y[1]
y2 = Y[2]

print("원본 행렬")
print(x0, y0)
print(x1, y1)
print(x2, y2)

tmp = 1/x0[0]
x0 = [ element * tmp for element in x0 ]
y0 = y0 * tmp

print("1행 x 1/3")
print(x0, y0)
print(x1, y1)
print(x2, y2)


x0_tmp = [ element * -x1[0] for element in x0 ]
y0_tmp = y0 * -x1[0]
print(x0_tmp, y0_tmp)

for i in range(0, len(x0)):
    x1[i] = x0_tmp[i] + x1[i]
y1 = y0_tmp + y1

print("1행 x -2 + 2행")
print(x0, y0)
print(x1, y1)
print(x2, y2)



x0_tmp = [ element * -x2[0] for element in x0 ]
y0_tmp = y0 * -x2[0]
print(x0_tmp, y0_tmp)

for i in range(0, len(x0)):
    x2[i] = x0_tmp[i] + x2[i]
y2 = y0_tmp + y2

print("1행 x -4 + 3행")
print(x0, y0)
print(x1, y1)
print(x2, y2)


tmp = 1/x1[1]
x1 = [ element * tmp for element in x1 ]
y1 = y1 * tmp

print("2행 x 3/16")
print(x0, y0)
print(x1, y1)
print(x2, y2)



x1_tmp = [ element * -x2[1] for element in x1 ]
y1_tmp = y1 * -x2[1]
print(x1_tmp, y1_tmp)

for i in range(0, len(x1)):
    x2[i] = x1_tmp[i] + x2[i]
y2 = y1_tmp + y2

print("2행 x 4/3 + 3행")
print(x0, y0)
print(x1, y1)
print(x2, y2)


tmp = 1/x2[2]
x2 = [ element * tmp for element in x2 ]
y2 = y2 * tmp

print("3행 x -(4/51)")
print(x0, y0)
print(x1, y1)
print(x2, y2)

x1_tmp = [ element * -x0[1] for element in x1 ]
y1_tmp = y1 * -x0[1]
print(x1_tmp, y1_tmp)

for i in range(0, len(x1)):
    x0[i] = x1_tmp[i] + x0[i]
y0 = y1_tmp + y0

print("2행 x -(1/3) + 1행")
print(x0, y0)
print(x1, y1)
print(x2, y2)


x2_tmp = [ element * -x1[2] for element in x2 ]
y2_tmp = y2 * -x1[2]
print(x2_tmp, y2_tmp)

for i in range(0, len(x2)):
    x1[i] = x2_tmp[i] + x1[i]
y1 = y2_tmp + y1

print("3행 x (7/16) + 2행")
print(x0, y0)
print(x1, y1)
print(x2, y2)


x2_tmp = [ element * -x0[2] for element in x2 ]
y2_tmp = y2 * -x0[2]
print(x2_tmp, y2_tmp)

for i in range(0, len(x2)):
    x0[i] = x2_tmp[i] + x0[i]
y0 = y2_tmp + y0

print("3행 x (0.8) + 1행")
print(x0, y0)
print(x1, y1)
print(x2, y2)

sol = [y0, y1, y2]
print(sol)
