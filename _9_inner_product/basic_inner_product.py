a = [1, 2, 3]
b = [4, 5, 6]

def inner_product(a, b):
    n = len(a)
    res = 0
    for i in range(0, n):
        res += a[i]*b[i]
    return res

print(inner_product(a, b))