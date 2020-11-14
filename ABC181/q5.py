# ペアの身長の差の合計の最小値

import bisect

N, M = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
W = list(map(int, input().split()))
W.append(float('inf'))
W.append(-float('inf'))
W.sort()

D_L, D_R = [0], [0]
sum_L, sum_R = 0, 0
for i in range(0, N - 1, 2):
    sum_L += H[i + 1] - H[i]
    D_L.append(sum_L)
for i in range(N - 2, -1, -2):
    sum_R += H[i + 1] - H[i]
    D_R.append(sum_R)

ans = float('inf')
for i in range(0, N, 2):
    j = bisect.bisect_left(W, H[i])
    d = min(H[i] - W[j - 1], W[j] - H[i])
    t = D_L[i // 2] + D_R[(N - i - 1) // 2] + d
    if t < ans:
        ans = t

print(ans)