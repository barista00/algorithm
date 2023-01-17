lst = []
cnt = 0
for i in range(9):
    num = int(input())
    lst.append(num)
print(max(lst))
print(lst.index(max(lst))+1)