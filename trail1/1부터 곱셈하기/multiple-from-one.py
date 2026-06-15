n = int(input())
res = 1
current = 0 

for i in range(1, 11):
    res *= i
    if res >= n:
        current = i
        break

print(current)