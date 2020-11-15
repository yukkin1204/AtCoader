# 対称群

import itertools

N, K = map(int, input().split())
A = []
B = []
for i in range(N):
    A_i = list(map(int, input().split()))
    A.append(A_i)
for i in range(1, N):
    B.append(i)
C = list(itertools.permutations(B))
count = 0

for record in C:
    S = A[0][record[0]]
    for i in range(N - 2):
        S += A[record[i]][record[i + 1]]
    S += A[record[N - 2]][0]
    if S == K:
        count += 1

print(count)