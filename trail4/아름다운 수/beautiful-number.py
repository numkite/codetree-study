n = int(input())

# Please write your code here.
ans = 0

def count_beauti_nums(length):
    global ans

    if length == n:
        ans += 1
        return

    if length > n:
        return

    for i in range(1, 5):
        count_beauti_nums(length + i)

count_beauti_nums(0)

print(ans)