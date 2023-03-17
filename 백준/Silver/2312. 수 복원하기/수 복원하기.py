import math
T = int(input())
for _ in range(T):
    n = int(input())
    prime_li = [True for _ in range(n+1)]

    div = n
    result = []
    for i in range(2, n + 1):
        if prime_li[i]:
            num = 2
            cnt = 0

            while num * i <= n:
                prime_li[num * i] = False
                num += 1
            
            while div % i == 0:
                div = div // i
                cnt += 1
            if cnt != 0:
                result.append((i, cnt))
    for i in result:
        print(*i)