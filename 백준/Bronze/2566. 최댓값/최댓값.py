lst = [list(map(int, input().split())) for _ in range(9)]
lst2 = []
y = 0
for i in lst:
    lst2.append(max(i))
for i in lst:
    y += 1
    if max(lst2) in i:
        x = i.index(max(lst2)) + 1
        break
print(max(lst2))
print(y, x)