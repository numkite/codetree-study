arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a >= b and a >= c:
    max = a
elif b >= c:
    max = b
else:
    max = c

print(max)