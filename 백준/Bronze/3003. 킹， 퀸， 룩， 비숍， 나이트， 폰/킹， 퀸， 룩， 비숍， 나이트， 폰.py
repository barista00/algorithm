k, q, l, b, n, p = map(int, input().split())

def kq(x):
    return 1 - x

def lbn(x):
    return 2 - x

def pa(x):
    return 8 - x
print(kq(k), kq(q), lbn(l), lbn(b), lbn(n), pa(p))