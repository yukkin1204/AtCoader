# 最も多くの数を割り切る整数

N = int(input())
l = list(map(int, input().split()))
maxCount = 0
maxNumber = 1

for i in range(2, 1001):
    count = 0
    for j in range(N):
        if l[j] % i == 0:
            count += 1
    if count > maxCount:
        maxCount = count
        maxNumber = i

print(maxNumber)

