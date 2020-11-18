# 和がSになる数の組

from math import factorial

S = int(input())
count = 0

for i in range(1, S // 3 + 1):
    # 重複組合せ (○がS-3i個と仕切りがi-1個)
    count += factorial(S - 2 * i - 1) // (factorial(S - 3 * i) * factorial(i - 1))

print(count % 1000000007)