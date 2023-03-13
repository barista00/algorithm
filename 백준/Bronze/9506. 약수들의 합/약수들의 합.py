while True:
    n = int(input())
    cnt = 0
    lst = []
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            cnt = cnt + i
            lst.append(i)
            lst.append('+')
    if cnt == n:
        print(f'{n} =',*lst[:-1])
    else:
        print(f'{n} is NOT perfect.')