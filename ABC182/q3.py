# 何文字除けば3の倍数になるか

l = list(map(int, list(input())))
m = list(map(lambda n: n % 3, l))
N = len(l)
sum = 0

for num in m:
    sum += num
sum = sum % 3

if sum == 0:
    print(0)
elif sum in m:
    if len(l) >= 2:
        print(1)
    else:
        print(-1)
else:
    if len(l) >= 3:
        print(2)
    else:
        print(-1)

