# 9の倍数かどうか

l = list(map(int, list(input())))
sumDigit = 0
for digit in l:
    sumDigit += digit

if sumDigit % 9 == 0:
    print("Yes")
else:
    print("No")

