a = input().split()
a_occur = a[0]
a_temp = int(a[1])

b = input().split()
b_occur = b[0]
b_temp = int(b[1])

c = input().split()
c_occur = c[0]
c_temp = int(c[1])

cnt = 0

if a_occur == 'Y' and a_temp >= 37:
    cnt += 1
if b_occur == 'Y' and b_temp >= 37:
    cnt += 1
if c_occur == 'Y' and c_temp >= 37:
    cnt += 1

if cnt >= 2:
    print("E")
else:
    print("N")