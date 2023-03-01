def pi(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return pi(n-1) + pi(n-2)
n = int(input())
if n == 0:
    print(0)
else:
    print(pi(n))