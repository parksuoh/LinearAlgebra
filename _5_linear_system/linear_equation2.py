import copy

def solve(A ,b):

    X = copy.deepcopy(A)
    sol = copy.deepcopy(b)
    n = len(X)

    for i in range(0, n):
        print("--- i = ", i, " 번째 실행 시작 -----")
        x_row = X[i]
        y_val = sol[i]

        if x_row[i] != 0:
            tmp = 1 / x_row[i]
        else:
            tmp = 0
        
        x_row = [ element * tmp for element in x_row ]
        y_val = y_val * tmp

        X[i] = x_row
        sol[i] = y_val

        print(x_row)
        print(y_val)
        print("---- 행 나누기 완료 ----")

        for j in range(0, n):
            if i == j:
                continue
            print("--- j = ", j, " 번째 실행 시작 -----") 
            x_next = X[j]
            y_next = sol[j]

            x_tmp = [ element * -x_next[i] for element in x_row ]
            y_tmp = y_val * (-x_next[i])

            for k in range(0, len(x_row)):
                x_next[k] = x_tmp[k] + x_next[k]
            y_next = y_tmp + y_next

            X[j] = x_next
            sol[j] = y_next

            print(X)
            print(sol)
            print("--- j = ", j, " 번째 실행 종료 -----") 

        print("--- i = ", i, " 번째 실행 완료 -----")
    
    return sol

X = [[3, 1, 2], [2, 6, -1], [4, 0, -1]]
y = [5, 1, 3]
print(solve(X, y))

        