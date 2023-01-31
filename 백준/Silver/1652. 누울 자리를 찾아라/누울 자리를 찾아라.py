N = int(input())
lst = [list(input()) for _ in range(N)]
a = 0
cnt_lst = []

for i in range(N):
    for j in range(N-1):
        if lst[i][j] == 'X':
            if a == 1:
                cnt_lst.append(a)
                a = 0
        else:
            if lst[i][j] == '.' and lst[i][j+1] == '.':
                a = 1
    if a == 1:
        cnt_lst.append(a)
        a = 0

b = 0
cnt_lst2 = []
for i in range(N):
    for j in range(N-1):
        if lst[j][i] == 'X':
            if b == 1:
                cnt_lst2.append(b)
                b = 0
        else:
            if lst[j][i] == '.' and lst[j+1][i] == '.':
                b = 1
    if b == 1:
        cnt_lst2.append(b)
        b = 0

print(len(cnt_lst), len(cnt_lst2)) 