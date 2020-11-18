# ２数の積の最大値

a, b, c, d = map(int, input().split())
ans = max(a * c, a * d, b * c, b * d)
print(ans)