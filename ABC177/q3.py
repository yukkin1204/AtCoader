# 異なる2数の積の和

N = int(input())
A = list(map(int, input().split()))
sumA = 0
sumA2 = 0

for num in A:
    sumA += num
    sumA2 += num ** 2

t = (sumA ** 2 - sumA2) // 2
print(t % 1000000007)
