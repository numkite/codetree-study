arr = input().split()
a = int(arr[0])
b = int(arr[1])

if a < b:
    f = 1
else:
    f = 0

if a == b:
    r = 1
else:
    r = 0

print(f, r)