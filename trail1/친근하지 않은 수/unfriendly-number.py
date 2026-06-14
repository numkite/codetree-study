n = int(input())
res = 0
for i in range(1, n+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    res += 1

print(res)