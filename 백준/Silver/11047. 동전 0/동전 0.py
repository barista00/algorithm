n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)
# print(coins)
count = 0
for coin in coins:
    
    if k - coin < 0:
        continue
    else:
        while True:
            if k - coin < 0:
                break
            else:
                count += 1
                k = k - coin
print(count)