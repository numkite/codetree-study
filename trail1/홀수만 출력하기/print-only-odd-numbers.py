n = int(input())
i = 1

while i <= n:
    a = int(input())
    if a % 2 != 0 and a % 3 == 0:
        print(a)
    i += 1