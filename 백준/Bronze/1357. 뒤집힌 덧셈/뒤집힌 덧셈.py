x, y = map(str, input().split())

def rev(a):
    lst = list(reversed(str(a)))
    re = lst[0]
    for i in range(1,len(lst)):
        re = re + lst[i]
    return int(re)

print(rev(rev(x)+rev(y)))