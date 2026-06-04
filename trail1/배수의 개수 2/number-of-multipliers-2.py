cnt = 0
i = 1

while i <= 10:
    n = int(input())
    if n % 2 != 0:
        cnt += 1
    i += 1

print(cnt)