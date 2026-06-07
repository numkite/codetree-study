n = input().split()
a = int(n[0])
b = int(n[1])
sum = 0
cnt = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum += i
        cnt += 1

avg = round(sum/cnt, 1)
print(sum, avg)