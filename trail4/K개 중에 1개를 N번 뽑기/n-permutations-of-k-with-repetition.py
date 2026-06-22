K, N = map(int, input().split())

# Please write your code here.
selected  = []

def find_seq(cnt):
    if cnt == N:
        print(*selected)
        return

    for i in range(1, K+1):
        selected.append(i)
        find_seq(cnt + 1)
        selected.pop()

find_seq(0)