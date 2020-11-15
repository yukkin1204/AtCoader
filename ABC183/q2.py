# 反射(一直線上の問題)

Sx, Sy, Gx, Gy = map(int, input().split())
Gy = -1 * Gy
m = (Gy - Sy) / (Gx - Sx)

print(Sx - Sy / m)
