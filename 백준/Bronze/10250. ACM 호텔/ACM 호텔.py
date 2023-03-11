T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())

    th = 1
    while True:
        if n - h <= 0:
            break
        else:
            n -= h
            th += 1
    
    if th >= 10: # 호수가 10넘어가면 1층 10호면 110호가 나와야하기 때문에 2가지 출력결과를 대비해야됨
        print(f'{n}{th}')
    else:
        print(f'{n}0{th}') # 호수가 10이 넘지않으면 중간에 0을 넣어줘야함