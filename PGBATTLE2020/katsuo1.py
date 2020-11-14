# 奇点と偶点

N = int(input())
countArray = [0] * N
for i in range(N - 1):
    a, b = map(int, input().split())
    countArray[a - 1] += 1
    countArray[b - 1] += 1
count = countArray.count(1)
if countArray[0] == 1:
    count -= 1
print(count)
