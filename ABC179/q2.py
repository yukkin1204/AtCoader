# 3連続ゾロ目

N = int(input())
D = []
for i in range(N):
    D_i = list(map(int, input().split()))
    D.append(D_i)
flag = False

for i in range(N - 2):
    if D[i][0] == D[i][1] and D[i + 1][0] == D[i + 1][1] and D[i + 2][0] == D[i + 2][1]:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")