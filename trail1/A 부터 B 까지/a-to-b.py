n = input().split()
a = int(n[0])
b = int(n[1])

while a <= b:
    if a % 2 == 0:
        print(a, end = ' ')
        a += 3
    else:
        print(a, end = ' ')
        a *= 2