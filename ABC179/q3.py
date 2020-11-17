# A*B+C=N

N = int(input())
i = 1
count = 0

while i * i < N:
    for j in range(i, N):
        if i * j < N:
            if i == j:
                count += 1
            else:
                count += 2
        else:
            break
    i += 1

print(count)