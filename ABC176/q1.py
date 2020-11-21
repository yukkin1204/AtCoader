# T分で同時にX個作る

N, X, T = map(int, input().split())

if N % X == 0:
    print(N // X * T)
else:
    print((N // X + 1) * T)