# 何文字変更で部分文字列になるか

S = list(input())
T = list(input())
s = len(S)
t = len(T)
n = s - t
maxCount = 0

for i in range(n + 1):
    count = 0
    for j in range(t):
        if S[i + j] == T[j]:
            count += 1
    if count > maxCount:
        maxCount = count

print(t - maxCount)