# ジグザグウォークの最大値

N = int(input())
l = list(map(int, input().split()))
s, start, maxSum, maxTotalSum = 0, 0, 0, 0

for num in l:
    s += num 
    if s > maxSum:
        maxSum = s
    t = start + maxSum
    if t > maxTotalSum:
        maxTotalSum = t
    start += s 

print(maxTotalSum)