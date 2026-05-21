a = input().split()
b = input().split()

a_m = int(a[0])
a_e = int(a[1])
b_m = int(b[0])
b_e = int(b[1])

print(int(a_m > b_m and a_e > b_e))