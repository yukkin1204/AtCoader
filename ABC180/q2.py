# さまざまな距離

import math

N = int(input())
X = list(map(int, input().split()))
md = 0
a = 0
mc = 0

for num in X:
    md += abs(num)
    a += num * num
    if abs(num) > mc:
        mc = abs(num)
ed = math.sqrt(a)

print(md)
print(ed)
print(mc)