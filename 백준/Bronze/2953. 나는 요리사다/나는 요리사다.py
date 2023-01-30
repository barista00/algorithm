lst = []
for i in range(1,6):
    N = list(map(int, input().split()))
    lst.append((i, sum(N)))
lst2 = sorted(lst, key=lambda x:x[1])
print(*lst2[-1])