num = input().split()
n = int(num[0])
a = int(num[1])
i = 1

while i <= n:
    if i % a == 0:
        print(1)
    else:
        print(0)
    i += 1