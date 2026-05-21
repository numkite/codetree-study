arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a <= b <= c or c <= b <= a:
    mid = b
elif a <= c <= b or b <= c <= a:
    mid = c
else:
    mid = a


print(mid)
