n = int(input())
cnt = 0
res = n

for i in range(1, 5001):
    res //= i
    cnt += 1
    if res <= 1:
        break
print(cnt)