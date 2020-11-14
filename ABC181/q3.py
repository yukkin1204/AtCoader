# 同一直線上に並ぶか

N = int(input())
P = []
flag = False

for i in range(N):
    P_i = list(map(int, input().split()))
    P.append(P_i)

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            a, b = P[j][0] - P[i][0], P[j][1] - P[i][1]
            c, d = P[k][0] - P[i][0], P[k][1] - P[i][1]
            # 傾きが同じなら一直線上に並ぶ (ただし分母0対策として、分母を払っている)
            if a * d == b * c:
                flag = True
                break
        if flag:
            break
    if flag:
        break    

if flag:
    print("Yes")
else:
    print("No")