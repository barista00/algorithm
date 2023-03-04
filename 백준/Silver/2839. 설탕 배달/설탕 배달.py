N = int(input())
cnt = 0
def sugar(N):
    global cnt
    if N < 3:
        cnt = -1
        return
    if (N - 3) % 5 == 0:
        cnt += 1
        cnt = cnt + ((N-3) // 5)
    else:
        cnt += 1
        sugar(N - 3)

if N % 5 == 0:
    print(N // 5)
else:
    sugar(N)
    print(cnt)