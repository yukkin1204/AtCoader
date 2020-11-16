# 約数の列挙

import math

N = int(input())
l = []
i = 1

while i * i <= N:
    if N % i == 0:
        print(i)
        if i * i < N:
            l.append(N // i)
    i += 1

for num in reversed(l):
    print(num)