T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())

    호수 = 1
    while True:
        if n - h <= 0:
            break
        else:
            n -= h
            호수 += 1
    
    if 호수 >= 10:
        print(f'{n}{호수}')
    else:
        print(f'{n}0{호수}')