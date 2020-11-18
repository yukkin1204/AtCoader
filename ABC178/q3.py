# 0と9を含む数列の個数

N = int(input())
ans = (10 ** N - (9 ** N + 9 ** N - 8 ** N)) % 1000000007
print(ans)