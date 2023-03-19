T = int(input())
for _ in range(T):
    n = int(input())
    lst = [1, 1, 1, 2] 
    def f(n):
        if n < 5:
            return lst[n-1]
        for i in range(4, n):
            num = lst[i-2] + lst[i-3]
            lst.append(num)
        return lst[n-1]
    print(f(n))