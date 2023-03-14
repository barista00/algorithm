import math

T = int(input())
for _ in range(T):
    n = int(input())
    prime = [True for _ in range(n+1)]
    prime[0] = False
    prime[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if prime[i] == True:
            multi = 2
            while n >= multi * i:
                prime[i * multi] = False
                multi += 1
    lst = []
    for i in range(1, n+1):
        if prime[i]:
            lst.append(i)
    lst2 = []
    gap = 10000
    result = 1
    for i in lst:
        for j in lst:
            if i + j == n:
                if i <= j:
                    if gap > j - i:
                        gap = j - i
                        result = i, j
    print(*result)