arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

print(int(a <= b and a <= c), int(a == b and b == c))