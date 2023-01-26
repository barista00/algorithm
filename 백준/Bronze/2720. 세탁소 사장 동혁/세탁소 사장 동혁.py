T = int(input())
for t in range(T):
    coin = int(input()) 
    lst = []
    a = coin // 25
    b = (coin - 25 * a) // 10
    c = ((coin - 25 * a) % 10) // 5
    d = ((coin - 25 * a) % 10) % 5 
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.append(d)
    print(*lst)