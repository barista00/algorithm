n, m = map(str, input().split())
lst = list(n)
lst2 = list(m)
plus = 0
while lst:
    for i in lst2:
        plus += int(lst[-1]) * int(i)
    lst.pop()
print(plus)