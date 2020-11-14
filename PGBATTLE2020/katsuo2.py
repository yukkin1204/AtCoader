# 和がSとなるN個の整数の組

def f(n, s):
    if n == 1:
        if n == N or s >= outputNums[N - n - 1]:
            outputNums[N - n] = s
            print(" ".join(map(str, outputNums)))
    else:
        for l in range(1, s // n + 1):
            if n == N or l >= outputNums[N - n - 1]:
                outputNums[N - n] = l
                f(n - 1, s - l)

N, S = map(int, input().split())
outputNums = [0] * N
f(N, S)
