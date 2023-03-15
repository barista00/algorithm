n, k = map(int, input().split())

prime = [True for _ in range(n+1)]
prime[0] = False
prime[1] = False

nth = 0
for i in range(2, n + 1):
    if prime[i] == True:
        cnt = 1
        while n >= i * cnt:
            if prime[i * cnt] == True:
                prime[i * cnt] = False
                nth += 1
                if nth == k:
                    print(i * cnt)
                    exit()
            cnt += 1