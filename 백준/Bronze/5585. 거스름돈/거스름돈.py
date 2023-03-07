N = int(input())
cos = 1000 - N
coin = [500, 100, 50, 10, 5, 1]
cnt = 0
how_many = 0
while True:
    if cos == 0:
        break
    if cos - coin[cnt] < 0:
        cnt += 1
        continue
    else:
        cos = cos - coin[cnt]
        how_many += 1
print(how_many)