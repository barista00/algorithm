N = int(input())

lst = []
for _ in range(N):
    stick = int(input())
    lst.append(stick)

cnt = 1
master = lst[-1]
for i in reversed(range(N)):
    if lst[i] > master:
        cnt += 1
        master = lst[i]
print(cnt)