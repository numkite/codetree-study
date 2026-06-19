sum = 0
cnt = 0
while True:
    n = int(input())
    if not(20 <= n < 30):
        break
    sum += n
    cnt += 1

print(f"{sum/cnt:.2f}")