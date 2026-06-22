n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.
max_cnt = 0
selected = []

def is_overlap(idx1, idx2):
    if (x1[idx1] <= x2[idx2] and x1[idx1] >= x1[idx2] or (x1[idx2] <= x2[idx1] and x1[idx2] >= x1[idx1])):
        return True
    return False

def find_max(idx):
    global max_cnt

    if idx == n:
        max_cnt = max(max_cnt, len(selected))
        return
    
    can_select = True
    for sel_idx in selected:
        if is_overlap(idx, sel_idx):
            can_select = False
            break
    
    if can_select:
        selected.append(idx)
        find_max(idx + 1)
        selected.pop()

    find_max(idx + 1)

find_max(0)

print(max_cnt)