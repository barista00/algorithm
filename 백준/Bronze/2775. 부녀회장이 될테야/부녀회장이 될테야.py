T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    
    # n이 1이면 무조건 1 층수 상관없이
    def f(k, n):
        if n == 1:
            return 1
        if k == 0:
            return n
        return f(k-1, n) + f(k, n-1)
    print(f(k, n))