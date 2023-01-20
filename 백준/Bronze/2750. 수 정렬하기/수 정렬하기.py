T = int(input())
lst = []
for t in range(1,1+T):
    num = int(input())
    lst.append(num)
lst.sort()
for i in lst:
    print(i)