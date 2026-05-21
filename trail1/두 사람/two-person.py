a = input().split()
a_age = int(a[0])
a_sex = a[1]

b = input().split()
b_age = int(b[0])
b_sex = b[1]

print(int((a_age >= 19 and a_sex == 'M') or (b_age >= 19 and b_sex == 'M')))